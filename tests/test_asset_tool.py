"""Behavioral regression tests using generated geometric fixtures, no app data."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageCms


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "asset_tool.py"


class AssetToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def image(self, name="source.png", size=(300, 400), mode="RGB", color="blue"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        Image.new(mode, size, color).save(path)
        return path

    def cli(self, *args, ok=True):
        result = subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                                text=True, capture_output=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        self.assertNotEqual(result.returncode, 0)
        return result.stderr

    def test_exact_export_is_opaque_srgb_and_input_is_unchanged(self):
        src = self.image()
        original = src.read_bytes()
        out = self.root / "out.png"
        self.cli("export", "--input", src, "--output", out, "--size", "600x800")
        with Image.open(out) as image:
            self.assertEqual(image.size, (600, 800))
            self.assertEqual(image.mode, "RGB")
            import io
            self.assertIn("sRGB", ImageCms.getProfileDescription(
                ImageCms.ImageCmsProfile(io.BytesIO(image.info["icc_profile"]))))
            self.assertEqual(image.getpixel((300, 400)), (0, 0, 255))
        self.assertEqual(src.read_bytes(), original)

    def test_phone_to_ipad_ratio_is_rejected_instead_of_stretched_or_padded(self):
        out = self.root / "out.png"
        error = self.cli("export", "--input", self.image(size=(132, 287)),
                         "--output", out, "--size", "2064x2752", ok=False)
        self.assertIn("Recompose/outpaint", error)
        self.assertFalse(out.exists())

    def test_explicit_crop_preserves_the_selected_region(self):
        src = self.image(size=(400, 400), color="red")
        with Image.open(src) as opened:
            image = opened.copy()
        image.paste((0, 255, 0), (100, 0, 400, 400)); image.save(src)
        out = self.root / "crop.png"
        self.cli("export", "--input", src, "--output", out, "--size", "300x400",
                 "--crop-box", "100,0,400,400")
        with Image.open(out) as image:
            self.assertEqual(image.getpixel((0, 0)), (0, 255, 0))

    def test_bad_crop_is_rejected(self):
        self.cli("export", "--input", self.image(), "--output", self.root / "bad.png",
                 "--size", "300x400", "--crop-box", "0,0,900,900", ok=False)

    def test_transparency_needs_a_matte_and_is_flattened(self):
        src = self.image(mode="RGBA", color=(255, 0, 0, 0))
        out = self.root / "out.png"
        self.cli("export", "--input", src, "--output", out, "--size", "300x400", ok=False)
        self.cli("export", "--input", src, "--output", out, "--size", "300x400",
                 "--matte", "#123456")
        with Image.open(out) as image:
            self.assertEqual(image.mode, "RGB")
            self.assertEqual(image.getpixel((0, 0)), (18, 52, 86))

    def test_existing_output_and_source_overwrite_are_refused(self):
        src = self.image(); out = self.image("existing.png")
        before = out.read_bytes()
        self.cli("export", "--input", src, "--output", out, "--size", "300x400", ok=False)
        self.assertEqual(before, out.read_bytes())
        self.cli("export", "--input", src, "--output", src, "--size", "300x400",
                 "--force", ok=False)

    def test_validation_rejects_alpha_wrong_size_and_wrong_encoding(self):
        alpha = self.image("alpha.png", mode="RGBA", color=(1, 2, 3, 255))
        error = self.cli("validate", "--size", "300x400", alpha, ok=False)
        self.assertIn("opaque RGB", error)
        src = self.image()
        self.cli("validate", "--size", "400x300", src, ok=False)
        disguised = self.root / "disguised.jpg"; disguised.write_bytes(src.read_bytes())
        self.cli("validate", "--size", "300x400", disguised, ok=False)

    def test_delivery_has_only_explicit_assets_not_neighboring_preview(self):
        one = self.image("upload/01.png"); two = self.image("upload/02.png")
        self.image("upload/contact-sheet.jpg", size=(900, 300))
        out = self.root / "delivery"
        self.cli("deliver", "--output", out, "--size", "300x400", one, two)
        self.assertEqual(sorted(p.name for p in out.iterdir()), ["01.png", "02.png"])
        self.assertEqual((out / "01.png").read_bytes(), one.read_bytes())
        self.assertFalse(list(self.root.rglob('*.zip')))

    def test_delivery_duplicate_basename_is_rejected_before_output(self):
        one = self.image("a/01.png"); two = self.image("b/01.png")
        out = self.root / "delivery"
        error = self.cli("deliver", "--output", out, "--size", "300x400", one, two, ok=False)
        self.assertIn("basenames", error)
        self.assertFalse(out.exists())

    def test_delivery_never_overwrites_existing_folder(self):
        out = self.root / "delivery"
        out.mkdir()
        existing = out / "keep.txt"
        existing.write_text("existing work")
        error = self.cli("deliver", "--output", out, "--size", "300x400", self.image(), ok=False)
        self.assertIn("already exists", error)
        self.assertEqual(existing.read_text(), "existing work")

    def test_truncated_file_fails_validation_without_a_traceback(self):
        src = self.image()
        src.write_bytes(src.read_bytes()[:80])
        error = self.cli("validate", "--size", "300x400", src, ok=False)
        self.assertIn("error:", error)
        self.assertNotIn("Traceback", error)

    def test_contact_sheet_uses_current_explicit_selection(self):
        red = self.image("red.png", color="red"); blue = self.image("blue.png")
        out = self.root / "sheet.png"
        result = self.cli("contact-sheet", "--output", out, "--columns", "2",
                          "--cell-width", "30", "--cell-height", "40", blue, red)
        self.assertFalse(result["upload_asset"])
        with Image.open(out) as image:
            self.assertEqual(image.getpixel((31, 64)), (0, 0, 255))
            self.assertEqual(image.getpixel((77, 64)), (255, 0, 0))

    def test_corrupt_color_profile_is_not_silently_retagged(self):
        src = self.root / "bad-profile.png"
        Image.new("RGB", (300, 400)).save(src, icc_profile=b"invalid")
        out = self.root / "out.png"
        self.cli("export", "--input", src, "--output", out, "--size", "300x400", ok=False)
        self.assertFalse(out.exists())

    def test_empty_or_invalid_dimensions_fail(self):
        self.cli("validate", "--size", "0x400", self.image(), ok=False)
        self.cli("validate", "--size", "300x400", ok=False)


if __name__ == "__main__":
    unittest.main()
