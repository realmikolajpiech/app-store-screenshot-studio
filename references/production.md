# Production and precise revisions

## Required generation workflow

New campaign artwork and visual revisions must use image generation/editing.
This includes restrained, typography-led directions: generation is a production
requirement, not a reason to add ornament. Do not replace the creative with
programmatically drawn phones, gradients and cards in Pillow, SVG, HTML/CSS or
canvas. Scripts may support faithful UI insertion, exact typography where
permitted, export, color conversion, validation and contact sheets; they must
not become an alternative campaign renderer.

1. Discover the host's built-in image tool first (for example, Codex's available
   image-generation tool). Use it without requesting an API key when available.
   Honor an explicitly requested provider/model and the host's editing rules.
2. If no usable host tool exists, check for an already configured, authorized
   image provider without exposing credentials. A text-only model is insufficient.
3. If neither route works, explain that generation is required and ask which
   provider the user will configure locally, for example Gemini image generation,
   xAI's image offering or OpenAI GPT Image. Read that provider's current official
   documentation before specifying model IDs, endpoints or setup instructions;
   do not hardcode a supposedly latest model. Explain relevant API billing before
   initiating a newly selected paid service.
4. Keep artwork production pending until access works. Continue useful analysis,
   copy and captures; do not deliver a procedural substitute as finished art.

Generate the planned composition using actual captures and visual references
with explicit roles. Inspect returned artifacts before expanding the series.
A successful tool call alone is not evidence of adequate visual quality.

## Secure API setup

Ask the user to configure access, never to paste a key into chat. Prefer the
host/provider's secret store or credential manager. Otherwise use a provider's
documented environment variable, configured locally by the user and inherited
by the execution environment. Give instructions with placeholders only. Do not
have the agent type a real key into a shell command or ask the user to run a
command that prints it. Do not change global configuration without authorization.

Read credentials at runtime only for the selected provider's authentication.
Check presence as a boolean and verify access with a minimal request; report
only success or a sanitized error. Do not print environment dumps, request
headers, raw debug traces or response objects that might echo authentication.
Never put keys in prompts, image metadata, manifests, source files, command-line
arguments, URLs, logs, commits or public artifacts. A local configuration file,
if required by the host, must remain outside the deliverable/repository and have
restricted access. If a key is accidentally disclosed, do not repeat it; advise
revocation and replacement through the provider's console.

Separate environment, hardware, real screen pixels and live type when supported.
Generate around product evidence and composite deterministically where allowed.
A model that redraws the whole scene can also alter small labels; “keep exactly”
does not guarantee preservation. Compare and restore through supported tools.

File-only operations on approved art (dimensions, color conversion, validation,
contact sheets) do not need another generation call. A wider canvas that exposes
missing environment needs image-based outpainting or regenerated composition.

## Build the picture, then finish it

For a new direction, work through composition, representative finished frames,
then the full series. Avoid fully rendering many variants of an unresolved idea.
The composition pass should already establish the dominant subject, headline
shape, scale and major overlaps. Useful product content belongs in this pass;
empty rectangles hide problems with actual crop and readability.

For the finished opener and contrasting frame, resolve the details that the
references make visible:

- **Type:** actual font, optical spacing, intentional emphasis, line silhouette
  and placement around the subject. Do not let browser defaults choose the look.
- **Assets:** deliberate photographic crop/casting or original illustration,
  clean cutouts, consistent material quality and enough source resolution.
- **Device and screen:** credible bezel and perspective; screen plane, corner
  mask and UI scale fit the hardware. Preserve useful UI even with dramatic crop.
- **Integration:** consistent light and color, contact shadow where surfaces
  meet, sensible occlusion, and selective depth of field that protects the proof.
  A flat graphic direction instead needs equally deliberate edges and layering.
- **Frame edges:** a purposeful continuation or crop, full canvas background,
  readable text and no unexplained seam between independently built sections.

Check at delivery scale and thumbnail scale. Compare with the relevant reference
before copying the approach across the set. If the gap is weak type or pasted
layers, fix that gap; don't add another prop or change a phone angle as a proxy.
If tools cannot achieve the intended finish, label the output as a draft and
state the specific missing work rather than silently lowering the benchmark.

## Prompt contract

```text
Asset: [placement, dimensions and ratio].
References: [1 = real capture/proof; 2 = approved style grammar;
             3 = this frame's approved version, when revising].
Message: [audience, one outcome, exact localized headline].
Visual idea: [what the subject does and how it relates to the actual product].
Composition: [focal mass, camera/crop, scale, type silhouette, spatial overlaps].
Typography: [character, emphasis, line breaks and integration with the image].
Focal UI: [actual group, names, values and controls that must survive].
Environment: [specific materials, light direction, shadows, texture and mood].
Keep: [UI, copy, identities, theme and prior approvals].
Change: [only requested differences].
Avoid: [specific failures, fake claims, unrelated decoration].
```

Use concrete choices rather than “make premium.” Mark reference roles so a tall
capture is not mistaken for the target ratio. Do not copy every instruction into
every prompt. Distinct hero alternatives are useful while direction is open;
three nearly identical variants are wasteful once a direction is approved.

## Revision contracts

| Feedback | Change | Preserve |
| --- | --- | --- |
| Text touches phone | Separate groups, measuring from the protruding card too | Approved size, copy, type and background |
| Removing name leaves hole | Rebalance into released space | Direction and message |
| All frames look the same | Reconsider focal subjects, hierarchy and sequence roles; then their geometry | Approved visual grammar and UI |
| Opening picture feels unrelated | Establish a specific relationship between subject, product and benefit | Real content and approved direction |
| Whole campaign feels generic | Compare actual type, subject, asset treatment and spatial finish with the reference. Reopen the direction if those choices are absent | Verified product facts and user constraints; don't treat a rejected look as approved |
| Feels pasted together | Match geometry/light or graphic treatment; recompose disconnected groups | Correct UI and still-approved content |
| Missing required phone | Restore device with actual UI | Benefit and still-approved motif |
| iPad background is cut off | Continue environment/props to canvas edges | Hardware proportions and focal content |
| Final feels tiny | Recompose a large focal story; examine actual crop | Legibility and preferred scale |

## Aspect adaptation contract

```text
Adapt approved artwork to [dimensions/ratio]. Extend the environment seamlessly
into the added canvas with no pasted panel or side bars. Continue [specific
road/clock/ribbon/ground] with consistent geometry, material, light and shadows.
Keep [phone, exact copy, focal UI and identities]. Do not stretch hardware, mirror
text, duplicate cards or replace phone with tablet. Rebalance only where needed.
```

Inspect the result: outpainting can still change central content. Compare copy,
names, dates, totals, percentages and selected states against evidence. Never
claim pixel-perfect preservation or native device capture without proof.

Use authorized demo identities and substitutions. Do not pass private records
or credentials to generation tools. Do not remove third-party watermarks.
Distinguish permission to use a reference from permission to publish it. Do not
add promotional URLs or attribution inside store art unless requested and allowed
by that placement.
