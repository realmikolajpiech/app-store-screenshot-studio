# Placement-aware production and exact exports

## Verify the slot first

Use the user's current App Store Connect accepted sizes, or check Apple's current
documentation. Names and required slots change. Do not describe these convenient
examples as an exhaustive list or infer required uploads from an old default.

| Placement | Useful exact size (width x height) | Important distinction |
| --- | --- | --- |
| iPhone, Dynamic Island medium | 1206 x 2622 | Other accepted sizes exist |
| iPhone, Dynamic Island large | 1320 x 2868 | 1290 x 2796 is also listed |
| iPad 13-inch portrait | 2064 x 2752 | 2048 x 2732 is also listed |
| iPad 13-inch landscape | 2752 x 2064 | 2732 x 2048 is also listed |
| Product page header | 3840 x 1646 | Wide composition and crop-aware focal area |
| Search results | 3840 x 2560 | 3:2; documented range starts at 1920 x 1280 |
| Universal header/search image | 5244 x 2950 | PNG; use the current universal template |

Examples verified on 2026-11-01. The scripts accept explicit sizes and do not
hardcode Apple's acceptance rules. Reverify at production time if possible.
If offline, use user-provided sizes and say that current requirements were not
independently checked. Do not silently change their requested placement.

Primary sources:

- [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications)
- [Creative assets specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications)
- [Asset best practices and current templates](https://developer.apple.com/app-store/asset-best-practices/)

Screenshots are still images. App previews are videos with different dimensions
and requirements. This package exports stills only. No alpha is allowed by these
Apple specifications. RGB/sRGB is the package's delivery convention. Technical
validation of a file is distinct from acceptance of the depicted device, app
content, metadata or claims in App Review.

## Adaptation without damage

Do not squeeze a narrow poster into 3:4. Fit the art direction to the new canvas:
continuous background geometry and shadows, intentional use of width, readable
headline, proportionate device and undistorted real UI. Background props can
bleed through the actual outer edge; they must not terminate at an interior
vertical boundary. A solid “matching” margin still fails this visual requirement.

For a small rounding difference, the export script makes a negligible center
crop (at most 0.5% aspect mismatch). A larger mismatch is rejected. Supply an
explicit reviewed crop box only if losing that area is intended. Otherwise
recompose/outpaint first. The export script deliberately has no contain/padding
or stretch mode.

For headers/search, obtain the current template for that ratio. Test its likely
crop at realistic display size. The goal is a large understandable focal story,
not a tiny full poster surrounded by decoration. Prefer moving groups, revising
line breaks, changing hierarchy or making a placement-specific composition over
uniformly shrinking everything. Save guides as QA files, never upload artwork.

## Tool commands

Python 3.9+ and Pillow 10+ are needed only for local helpers. Paths below assume
the current directory is this skill folder; replace them with absolute skill
paths when working in a project. Input art must already have the intended ratio.

```bash
python3 scripts/asset_tool.py export --input render.png --output upload/01.png --size 2064x2752
python3 scripts/asset_tool.py validate --size 2064x2752 upload/01.png upload/02.png
python3 scripts/asset_tool.py contact-sheet --output review/series.jpg --columns 6 upload/01.png upload/02.png
python3 scripts/asset_tool.py deliver --output delivery/ipad --size 2064x2752 upload/01.png upload/02.png
```

File commands refuse existing outputs unless `--force` is supplied. `deliver`
always requires a new folder and never overwrites an existing directory. Export
normalizes orientation, converts tagged input to sRGB, removes metadata, and
creates an opaque RGB PNG. Transparent input requires an explicit `--matte`
color. This flattens pixels; it never creates side margins. Invalid color
profiles cause a clear error instead of being silently mislabeled.

For an intentional crop, `--crop-box LEFT,TOP,RIGHT,BOTTOM` uses coordinates in
the orientation-normalized source. The resulting box must already have the
target ratio within the small rounding tolerance. Review content before export.

Contact sheets are previews and can contain margins or labels. Upload assets
cannot. Deliver validates explicit files for size, encoding, count and unique
basenames; it does not inspect words, corners, UI fidelity, crop safety or the
art direction. Keep its report and the campaign manifest outside the delivery
folder. The handoff is a folder, not an archive. Create a ZIP only if explicitly
requested by the user, using ordinary archive tools after validation.
