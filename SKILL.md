---
name: app-store-screenshot-studio
description: Analyze an app and create or improve art-directed App Store screenshot sets with evidence-based benefit copy, varied cohesive compositions, faithful app UI, and validated exports. Also adapt approved artwork for iPad, product page headers, or search results.
---

# App Store Screenshot Studio

Build a campaign around what this app actually helps people do. Give it an
authored visual identity: a recognizable world, expressive type, selected
product content and deliberately composed relationships between them.
Treat conversion as a hypothesis to test, not a result proved by visual polish.

## Resume and scope

Look for the task's brief, approved images and campaign manifest before repeating
discovery. Keep state in the user's project, not a particular agent's private
memory. Reuse decisions unless the user or the app has materially changed them.
Preserve unrelated files and follow local project instructions.

Establish the audience, locale, requested assets, upload slot, available captures
and references from context. Ask only about unresolved choices that affect the
result. If the user says to wait for visual references, prepare the brief and
capture plan, then wait before generating. Do not make speculative alternatives.

Treat follow-up feedback as a scoped change to the accumulated brief, not a
replacement for it. Record what changes, what remains required, and what was
actually rejected. A supplied logo may refine palette without requesting logo
motifs; a font complaint does not reject the entire composition. A new set still
needs the full art-direction and sequence review. Do not collapse the workflow
to the newest constraint or add a universal design ban after one failed render.

Keep a compact manifest; [campaign.example.json](examples/campaign.example.json)
is a structural example, not facts or a style preset. Store source evidence,
capture pairings, copy, layout decisions, versions, approved paths, dimensions,
tool and prompt paths. Distinguish proposed, approved and exported states.

Image generation is required for new campaign artwork and visual revisions.
Before rendering, discover the host's image-generation tool and read the
generation/access workflow in [production.md](references/production.md). If no
usable generator is available, ask for secure local API configuration and pause
artwork production. Never ask for an API key in chat or silently substitute a
Pillow, SVG, HTML/CSS or canvas-built campaign. Discovery and capture work can
continue while access is pending.

## 1. Discover benefits from the product

Read [discovery.md](references/discovery.md) for a new campaign or revised copy.
Trace actual actions through screens, features, contracts, flags, onboarding,
paywalls and store metadata. Separate implemented behavior, demo data, disabled
features and plans. Code is evidence of a feature, not of demand or superiority.

Build an evidence table: audience -> problem -> outcome -> source -> visual
proof. Rank outcomes by relevance, specificity, distinctiveness and visible
proof. Lead with the clearest reason this audience would install the app. Give
each later image one distinct job. Choose the count to fit the story.

Write concise localized headlines about the user's gain. Strong verbs help
when natural; uppercase, an isolated verb, English syntax and fixed line counts
are not requirements. Never invent ratings, reviews, awards, adoption, revenue,
savings or performance claims. Obtain real evidence or omit the claim.

Present the proposed story and important uncertainties together. An approved
brief or existing user authorization is enough to continue; do not create a
separate approval ceremony for each phase.

## 2. Pair each promise with a useful capture

Inspect pixels, not filenames. Prefer active, representative states where the
benefit is visible; an intentional empty state can be appropriate when it is the
feature. Mark captures ready, usable with a named limitation, or retake.
Capture through available tools when authorized, following the project's data
environment rules. If capture tools are unavailable, give a precise capture list.

Each promise needs visual proof. Do not fake an absent feature or a native iPad
screen by asking an image model to invent it. Use authorized demo data and
consistent identities. Apply requested name/school substitutions in both screen
and enlarged cards. Never expose private data or credentials in a prompt.

## 3. Art-direct the series before generating

Read [art-direction.md](references/art-direction.md). For a new direction or
quality complaint, also read [visual-benchmarks.md](references/visual-benchmarks.md)
and inspect the actual reference images. A page's title or text summary is not
visual inspection. State any inaccessible references rather than claiming review.

Extract how the references achieve their effects, then choose a visual world
that extends this app's identity. Plan typography, image selection, scale,
occlusion, material and light together. Richness, restraint and repeated layouts
can all work; none is a quality guarantee. Preserve the distinction between
product evidence and expressive art. Do not copy another app's claims or assets.

Record a concise direction and a sequence matrix: each frame's message, visual
idea, focal source, type treatment, spatial relationships and role next to its
neighbors. A phone angle or a background color is not a visual idea. A gallery
of headings, phones and unrelated floating cards needs further art direction.

Honor explicit constraints such as a phone in every frame, no wordmark, or a
specific palette. Do not turn those into defaults for every future app. Do not
inherit an example's mascot or force breakouts into every image.

If direction is open, sketch a small number of genuinely different concepts
before polishing. Choose using the app, references and user feedback; do not
require a new approval step. Before a full new set, render the opening frame and
one meaningfully different frame to intended finish. Compare them with the
chosen references at the same display size using [review.md](references/review.md).
Fix the visible craft gap before expanding the series.
Do not expand a rejected direction by changing only its font or palette. Inspect
whether the new render has a product-specific visual relationship, not merely
a new decorative motif. Apply the background test in art-direction.md and record
the visible result before rendering further frames.
For an approved direction or narrow revision, preserve the work and change only what was requested.

## 4. Produce faithful artwork

Read [production.md](references/production.md) for generation, secure access
and edits. Use an actual image-generation/editing call to produce each new
creative or visual revision, honoring explicit model choices. Generate the
intended composition, not a token decorative asset added to a procedural poster.
Record the tool/model, prompt and returned artifact paths, never credentials.
An unavailable or failed generator leaves production pending, not complete.

Separate creative environment from product evidence. Reuse real screen pixels
with deterministic compositing where permitted; generate around them. If a tool
redraws UI, compare every headline, focal label, time, number, name and control
with the source. “Preserve exactly” in a prompt is not a pixel lock. Restore from
the source through supported editing tools or retake instead of silently shipping
corrupt UI. Follow the host's image editing rules.

Use a prompt contract: asset/ratio; reference roles; exact copy; visual idea;
spatial relationships, type and light; unchanged elements; changes; avoid list.
A rejected variant must not become the next style reference. A spacing
correction changes spacing, not the
whole design. Removing a wordmark should reclaim its space. Keep phone and type
large enough to work at listing thumbnail size.

## 5. Adapt the composition, then export

Read [formats-and-export.md](references/formats-and-export.md). Verify current
Apple specifications against the actual upload slot or user-provided accepted
sizes. Preview-video dimensions are not screenshot dimensions.

For a new ratio, recompose or outpaint the environment edge to edge. Do not
stretch hardware, crop away a headline, paste a narrow poster onto side bars,
mirror UI into margins, or replace a phone with a tablet without instruction.
If explicitly asked to keep an iPhone on an iPad-sized canvas, honor that art
direction and identify the depicted device accurately in the manifest. Pixel
validation does not prove device representation or App Review acceptance.

Header and search artwork need crop-aware layouts. Use current Apple templates
and preview crops. Keep meaning and readability in the focal area. Do not shrink
the entire design into illegibility to satisfy a guide; recompose the focal story.
Never burn template guides into deliverables.

Use [asset_tool.py](scripts/asset_tool.py) for deterministic export and checks.
It does not generate art, outpaint, assess copy or certify Apple acceptance.
It refuses substantial aspect changes without an explicit crop box. Return to
composition if cropping would remove important content. Deliver exact-size
opaque RGB files in sRGB.

## 6. Review the campaign and deliver

Read [review.md](references/review.md). Inspect full-size images, a small preview,
and all images side by side. Check factual copy, UI fidelity, hierarchy,
text/phone separation, intentional edges and the sequence's rhythm. Compare
typography, imagery and spatial finish against the actual visual benchmark,
not just a checklist. Revise weak frames before delivery. Passing file checks
or describing a design as premium is not evidence of visual quality.

Export one selected file per requested image and slot. Keep rejects, source
captures, contact sheets and metadata outside upload folders. Deliver a clean
folder built from an explicit validated file list, not a directory crawl. Do not
create a ZIP unless the user explicitly requests one. Update the manifest and
regenerate previews from final paths after revisions. Link the ready folder/files
and preview; report target sizes and material limitations. Do not publish a
repository or upload to a store unless requested.

See [design-rationale.md](references/design-rationale.md) for design decisions
and [NOTICE](NOTICE) for upstream attribution.
