# App Store Screenshot Studio

**Status: experimental alpha.** The workflow and export helpers are usable,
but visual results are not yet consistent across apps or revision rounds.
Recent trials exposed drift toward generic imagery and loss of composition
quality after font/palette feedback. The review instructions address these
failures; their effectiveness still needs further real-world evaluation.
Automated tests verify file handling, not visual quality.

App-grounded copy. An authored visual world. A purposeful screenshot sequence.

An agent skill for turning real product capabilities and captures into polished
App Store artwork. It starts with codebase analysis and benefit discovery, then
plans the whole series before rendering individual images.

Inspired by [Adam Lyttle's ASO screenshot workflow](https://github.com/adamlyttleapps/claude-skill-aso-appstore-screenshots),
with a new art-direction and delivery system. MIT licensed; attribution in
[NOTICE](NOTICE). No upstream scripts, third-party reference images or proprietary
app captures are bundled.

## What it does differently

- Maps each promise to actual product evidence and a capture that proves it.
- Derives a visual grammar from the app and your references instead of forcing
  every product into one saturated, top-headline, centered-phone template.
- Studies actual reference images for typography, content selection, spatial
  relationships, materials and light. Includes written breakdowns of contrasting
  campaigns in [visual-benchmarks.md](references/visual-benchmarks.md).
- Designs the whole sequence, then compares a finished opener and a contrasting
  frame with the selected references before expanding it. Intentional repetition
  and visual richness are both available; neither is a universal template.
- Makes narrow revisions: more breathing room stays a spacing edit; removing a
  logo reclaims space; wider formats get continuous backgrounds, not side bars.
- Covers iPhone/iPad screenshots and static header/search creatives, with current
  slot verification and exact-size opaque exports.
- Requires image generation for artwork. Uses the host's built-in image tool
  first; otherwise asks you to configure a provider securely on your machine.
- Keeps resumable project-local decisions, prompts, versions and final paths.

Visual review includes the quality of type, imagery and integration, separate
from UI truth and export validation. The skill aims for persuasive design.
It does not promise conversion uplift or App Review approval. Only real tests
can establish conversion outcomes.

## Install

Clone the repository into your agent's skill directory (use a new destination):

```bash
git clone https://github.com/realmikolajpiech/app-store-screenshot-studio.git ~/.codex/skills/app-store-screenshot-studio
```

If that folder already exists, preserve your local changes before updating it.

Put this folder, including `SKILL.md`, in your agent's skill directory:

- Codex: `~/.codex/skills/app-store-screenshot-studio/`
- Claude Code: `~/.claude/skills/app-store-screenshot-studio/`
- Other skill-capable agents: use their supported skill location or load
  `SKILL.md` directly. Tool access and automatic discovery vary by host.

No specific provider or MCP server is required. New artwork and visual revisions
require a working image-generation tool or API. Without one, the agent asks you
to configure your chosen provider locally and pauses artwork production; it does
not substitute a scripted poster. Never paste API keys into chat. Use the host's
secret store or a locally configured environment variable. Credentials do not
belong in prompts, logs, manifests or this repository. Analysis, copy, planning
and file-only operations on approved artwork can proceed without generation.

## Use

```text
Use $app-store-screenshot-studio. Analyze this app and prepare six screenshots
in Polish, primarily for students. Keep the app's visual identity, a phone in
every frame and large headlines. Vary the layouts. Wait for my references
before generating images.
```

```text
Adapt our approved screenshot set to iPad 2064x2752. Keep the iPhones and extend
the backgrounds seamlessly across the full canvas. Preserve the UI and copy.
```

```text
The search creative is approved. Increase the gap between the headline and
phone/card without making them smaller. Export at the accepted target size.
```

You get a brief, evidence-to-capture pairings, series composition plan, selected
artwork, a clean folder of validated upload files and a separate contact sheet.
No ZIP is created unless you explicitly request one.
Unsupported tools or missing captures are reported as remaining work, not as
rendered results. Publishing/uploading is a separate user action.

## Local helpers

Use Python 3.9+ and install `requirements.txt` in your normal environment or a
virtual environment. Only Pillow is required for the image/file helpers:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/asset_tool.py --help
```

Commands: `export`, `validate`, `contact-sheet`, `deliver`. See
[formats-and-export.md](references/formats-and-export.md) for examples, color
handling and intentional cropping. The helper refuses large ratio mismatches,
does not stretch or add side bars, and never claims its checks replace review.
It does not generate images or require network access.

## Tests and limits

```bash
python3 -m unittest discover -s tests -v
```

The tests exercise file invariants and real CLI behavior. For agent behavior,
[evals/scenarios.md](evals/scenarios.md) provides realistic forward-test tasks
and observable success criteria. These scenarios are a manual evaluation suite,
not claimed automated visual benchmarks. Read
[design-rationale.md](references/design-rationale.md) for the reasoning behind
the workflow and [review.md](references/review.md) for visual QA.

Reference examples, product screenshots and generated campaign assets keep their
own rights. This package's MIT license does not grant rights to external artwork.
