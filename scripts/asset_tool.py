#!/usr/bin/env python3
"""Deterministic image handoff tools. No generation, network or Apple certification."""

import argparse
import hashlib
import io
import json
import re
import sys
import shutil
from pathlib import Path

from PIL import Image, ImageCms, ImageDraw, ImageFont, ImageOps


TOLERANCE = 0.005  # Rounding only; not a license for substantial cropping.


def size_arg(value):
    match = re.fullmatch(r"([1-9][0-9]*)[xX]([1-9][0-9]*)", value)
    if not match:
        raise argparse.ArgumentTypeError("Use WIDTHxHEIGHT with positive integers")
    return tuple(map(int, match.groups()))


def color_arg(value):
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise argparse.ArgumentTypeError("Use #RRGGBB")
    return tuple(int(value[i:i + 2], 16) for i in (1, 3, 5))


def crop_arg(value):
    try:
        box = tuple(int(x) for x in value.split(","))
        if len(box) != 4 or not (0 <= box[0] < box[2] and 0 <= box[1] < box[3]):
            raise ValueError()
        return box
    except ValueError:
        raise argparse.ArgumentTypeError("Use LEFT,TOP,RIGHT,BOTTOM within source")


def positive(value):
    result = int(value)
    if not 1 <= result <= 10000:
        raise argparse.ArgumentTypeError("Value must be between 1 and 10000")
    return result


def destination(path, force):
    path = Path(path)
    if path.exists() and not force:
        raise ValueError("Output exists; use --force intentionally: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def ensure_distinct(output, inputs):
    if Path(output).resolve() in {Path(p).resolve() for p in inputs}:
        raise ValueError("Output must not overwrite an input")


def srgb_profile():
    return ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB"))


def load_rgb(path, matte=None):
    with Image.open(path) as opened:
        if getattr(opened, "n_frames", 1) != 1:
            raise ValueError("Animated/multiframe input is unsupported: " + str(path))
        opened.load()
        image = ImageOps.exif_transpose(opened)
        profile = opened.info.get("icc_profile")
        has_alpha = "A" in image.getbands() or "transparency" in image.info
        alpha = image.convert("RGBA").getchannel("A") if has_alpha else None
        if alpha is not None and alpha.getextrema()[0] < 255 and matte is None:
            raise ValueError("Transparent pixels require an explicit --matte #RRGGBB")
        # Drop alpha for color conversion, then composite in output sRGB space.
        if image.mode in ("RGBA", "P", "LA"):
            color = image.convert("RGB")
            if profile and image.mode == "LA":
                color = image.getchannel("L")
        else:
            color = image
        if profile:
            source = ImageCms.ImageCmsProfile(io.BytesIO(profile))
            rgb = ImageCms.profileToProfile(color, source, srgb_profile(), outputMode="RGB")
        else:
            if color.mode == "CMYK":
                raise ValueError("CMYK input requires a valid embedded color profile")
            rgb = color.convert("RGB")  # Untagged RGB is assumed sRGB.
        if alpha is not None and alpha.getextrema()[0] < 255:
            background = Image.new("RGB", rgb.size, matte)
            background.paste(rgb, mask=alpha)
            rgb = background
        return rgb.copy()


def export(args):
    ensure_distinct(args.output, [args.input])
    image = load_rgb(args.input, args.matte)
    original_size = image.size
    if args.crop_box:
        if args.crop_box[2] > image.width or args.crop_box[3] > image.height:
            raise ValueError("Crop box exceeds the source bounds")
        image = image.crop(args.crop_box)
    mismatch = abs((image.width / image.height) / (args.size[0] / args.size[1]) - 1)
    if mismatch > TOLERANCE:
        raise ValueError(
            "Aspect mismatch {:.2%}. Recompose/outpaint first or supply a reviewed "
            "--crop-box matching the target; stretching and side bars are not supported."
            .format(mismatch)
        )
    result = ImageOps.fit(image, args.size, method=Image.Resampling.LANCZOS)
    out = destination(args.output, args.force)
    if out.suffix.lower() != ".png":
        raise ValueError("Export output must use .png")
    # Use a fresh image so input EXIF, text chunks and other metadata cannot leak.
    clean = Image.new("RGB", result.size)
    clean.paste(result)
    clean.save(out, format="PNG", icc_profile=srgb_profile().tobytes())
    return {"output": str(out), "source_size": original_size,
            "size": result.size, "mode": "RGB", "crop_box": args.crop_box,
            "aspect_mismatch": mismatch, "untagged_input_assumption": "sRGB"}


def inspect(path, size):
    path = Path(path)
    # PNG verification must precede EXIF access, which may consume the decoder.
    with Image.open(path) as encoded:
        encoded.verify()
    with Image.open(path) as image:
        image.load()
        if image.format not in ("PNG", "JPEG"):
            raise ValueError("Upload files must be PNG or JPEG: " + str(path))
        if path.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            raise ValueError("Upload extension must be PNG/JPG/JPEG: " + str(path))
        expected_format = "PNG" if path.suffix.lower() == ".png" else "JPEG"
        if image.format != expected_format:
            raise ValueError("Extension does not match encoding: " + str(path))
        if image.size != size:
            raise ValueError("Wrong size {} (expected {}): {}".format(image.size, size, path))
        if image.mode != "RGB" or "transparency" in image.info:
            raise ValueError("Upload must be opaque RGB, without an alpha channel: " + str(path))
        if getattr(image, "n_frames", 1) != 1:
            raise ValueError("Upload must be a single still image: " + str(path))
        if image.getexif().get(274, 1) != 1:
            raise ValueError("Normalize EXIF orientation before upload: " + str(path))
        profile = image.info.get("icc_profile")
        if profile:
            parsed = ImageCms.ImageCmsProfile(io.BytesIO(profile))
            description = ImageCms.getProfileDescription(parsed).strip()
        else:
            description = "untagged"
    return {"file": str(path), "size": size, "mode": "RGB",
            "color_profile": description, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def validate_files(files, size):
    if not 1 <= len(files) <= 10:
        raise ValueError("Use 1 to 10 explicitly selected files for a screenshot set")
    resolved = [Path(p).resolve() for p in files]
    if len(set(resolved)) != len(resolved):
        raise ValueError("Duplicate input files")
    return [inspect(p, size) for p in files]


def contact_sheet(args):
    ensure_distinct(args.output, args.files)
    if len(args.files) > 50 or args.columns > 10:
        raise ValueError("Contact sheets support up to 50 files and 10 columns")
    if args.cell_width > 2000 or args.cell_height > 4000:
        raise ValueError("Preview cells are too large")
    columns = min(args.columns, len(args.files))
    rows = (len(args.files) + columns - 1) // columns
    gap, label = 16, 28
    size = (columns * (args.cell_width + gap) + gap,
            rows * (args.cell_height + label + gap) + gap)
    if size[0] * size[1] > 60_000_000:
        raise ValueError("Contact sheet exceeds 60 megapixels; reduce cells/columns")
    canvas = Image.new("RGB", size, "#e5e3df")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    for i, path in enumerate(args.files):
        image = load_rgb(path, (255, 255, 255))
        image.thumbnail((args.cell_width, args.cell_height), Image.Resampling.LANCZOS)
        x = gap + (i % columns) * (args.cell_width + gap)
        y = gap + (i // columns) * (args.cell_height + label + gap)
        draw.text((x, y), str(i + 1), fill="#161616", font=font)
        canvas.paste(image, (x + (args.cell_width - image.width) // 2,
                             y + label + (args.cell_height - image.height) // 2))
    out = destination(args.output, args.force)
    if out.suffix.lower() not in (".png", ".jpg", ".jpeg"):
        raise ValueError("Contact sheet output must use PNG/JPG/JPEG")
    canvas.save(out, icc_profile=srgb_profile().tobytes(), **(
        {"quality": 95, "subsampling": 0} if out.suffix.lower() != ".png" else {}))
    return {"preview": str(out), "size": size, "files": [str(p) for p in args.files],
            "upload_asset": False}


def deliver(args):
    ensure_distinct(args.output, args.files)
    reports = validate_files(args.files, args.size)
    names = [Path(p).name for p in args.files]
    if len({n.casefold() for n in names}) != len(names):
        raise ValueError("Delivery basenames must be unique (case-insensitive)")
    out = Path(args.output)
    if out.exists():
        raise ValueError("Delivery folder already exists; choose a new version: " + str(out))
    out.mkdir(parents=True)
    try:
        for path, name in zip(args.files, names):
            shutil.copyfile(path, out / name)
    except OSError:
        shutil.rmtree(out)
        raise
    return {"folder": str(out), "entries": names, "validation": reports}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("export", help="Normalize correctly composed art to exact-size RGB PNG")
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--size", type=size_arg, required=True)
    p.add_argument("--crop-box", type=crop_arg)
    p.add_argument("--matte", type=color_arg)
    p.add_argument("--force", action="store_true")
    p.set_defaults(run=export)
    p = commands.add_parser("validate", help="Check explicit files, not current Apple slot policy")
    p.add_argument("--size", type=size_arg, required=True)
    p.add_argument("files", type=Path, nargs="+")
    p.set_defaults(run=lambda a: {"files": validate_files(a.files, a.size)})
    p = commands.add_parser("contact-sheet", help="Create a separate review preview")
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--columns", type=positive, default=6)
    p.add_argument("--cell-width", type=positive, default=360)
    p.add_argument("--cell-height", type=positive, default=760)
    p.add_argument("--force", action="store_true")
    p.add_argument("files", type=Path, nargs="+")
    p.set_defaults(run=contact_sheet)
    p = commands.add_parser("deliver", help="Validate and copy selected files into a new clean folder")
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--size", type=size_arg, required=True)
    p.add_argument("files", type=Path, nargs="+")
    p.set_defaults(run=deliver)
    args = parser.parse_args()
    try:
        print(json.dumps(args.run(args), indent=2))
    except (OSError, ValueError, ImageCms.PyCMSError, Image.DecompressionBombError) as exc:
        print("error: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
