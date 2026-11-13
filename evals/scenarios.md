# Manual forward-test scenarios

Use a fresh agent context with only the request, this skill and the minimum
fixtures. Evaluate the produced artifacts and actions, not whether it repeats
the wording in SKILL.md. Paid rendering or live account changes need the task's
normal authorization. These scenarios have not been claimed as executed agent
benchmarks merely because they are written here.

## 1. Discover without inventing

Request: “Make five screenshots for this meal planner in Polish.” Supply a small
repo with working planning/ingredient flows, a disabled nutrition flag and a
README mentioning future shopping delivery. Supply three captures.

Observe: promises trace to implemented flows; nutrition/delivery are not sold
as available. Copy is natural Polish; missing proof receives a concrete retake.
The app is not forced into the driving-school palette or a six-image story.

## 2. References pending

Request: “Prepare captures now. Wait for my design examples before generation.”

Observe: useful discovery/pairing proceeds, no image call occurs. When references
arrive, their geometry/hierarchy informs the plan without copying their claims.

## 3. Cohesive variety

Request: “Six frames. Phone in each. Our UI is warm cream and blue. Use the
supplied habit-game and travel campaigns as inspiration.” Supply real captures.

Observe: a matrix changes silhouettes, reading order and device leans while
keeping app identity. No borrowed mascot, ratings or country-count badge. Review
includes a contact sheet from the actual selected exports.

## 4. Narrow revision

Request: “Approved search creative: increase the gap between phone/card and type.
Keep the large text and phone.” Supply approved artwork.

Observe: only spacing changes; headline wording, scale and approved direction
survive. The nearest protruding card edge is considered. No smaller full-scene
composition is substituted for a spacing edit.

## 5. Wider canvas

Request: “iPad 2064x2752. Keep the iPhone in the art. Extend the background.”
Supply a tall campaign with a road exiting both sides.

Observe: full-bleed continuous background; no side bars, stretched phone,
mirrored words or invented tablet UI. The helper refuses a tall source before
recomposition. Exact-size RGB exports and a six-image-only folder are inspected.
No ZIP is created or offered by default.
The output is not mislabeled as a native iPad capture or guaranteed acceptance.

## 6. Missing tool

Request: “Use this skill to produce a campaign,” in an environment without image
generation. Supply app/capture access.

Observe: the agent checks for an already configured image API. If unavailable,
it asks the user to select/configure a provider through a local secret store or
environment variable, never to paste a key in chat. It completes useful discovery,
copy and captures while artwork remains pending. No Pillow/HTML/SVG campaign is
substituted, no provider account is silently created and no output is fabricated.

## 7. Header crop conflict

Request: “The text and phone are unreadably small in the final header. I liked
the larger version.” Supply current guide and both versions.

Observe: focal story is recomposed at useful scale and checked in likely preview
crops; the agent does not defend universal shrinking or claim unperformed ASC
preview verification. Target dimensions remain exact.

## 8. Factual drift and stale previews

Request: “Final review and handoff.” Supply a generated card with a changed
appointment time, correct source capture, a rejected variant and an older sheet.

Observe: discrepancy is identified and repaired via supported tools. Only the
selected corrected export enters the delivery folder; contact sheet is rebuilt from that
selection. No accidental rerender of the already approved whole campaign.

## 9. Opening frame with unrelated photography

Request: “Improve the first frame. The city photo and captions feel tacked on.
I want people to understand why they'd install this.” Supply a local news feed
capture with a populated neighborhood and two other approved store images.

Observe: the opener connects selected local content or interaction with the
benefit. It doesn't substitute another arbitrary skyline or a larger pasted
article tile for a considered composition. Copy and image work together; a
hidden-headline view is diagnostic, not an unconditional pass/fail rule. No
guessed ratings, filler captions or unrelated changes to approved frames.

## 10. Calm repetition is intentional

Request: “Use this quiet orchard campaign as the benchmark. Keep a calm rhythm.”
Supply a restrained app and a reference with several upright phones.

Observe: the agent studies scene, typography, content progression and contrast.
It may retain repeated device poses; it does not impose a rotation or color quota.
In a separate request that explicitly forbids consecutive matching leans, that
user constraint wins. Do not generalize one campaign's preference to all users.

## 11. Technically correct but visually weak

Request: “These look generic next to my references. Improve the skill's output.”
Supply actual reference images and a trial with a bold default UI font, three
phone angles, a pasted enlarged article, and an event stranded in a small footer.

Observe: the review identifies visible gaps in typography, focal content and
integration despite correct dimensions and readable copy. Corrections change
the relevant visual relationships, not just colors, angle or shadow strength.
For a new direction, the agent renders representative frames and checks them
against the references before producing the whole set. A revised prompt or
claimed quality score is not evidence of a better rendered result.

## 12. Rich visual language without copying

Request: “Keep our playful identity; aim for this illustrated, textured level.”
Supply current app assets and a rich campaign with a distinctive third-party
mascot, secondary labels and claimed adoption figures.

Observe: the agent preserves appropriate texture, illustration and layered
hierarchy rather than stripping everything to a minimal poster. It uses owned
assets or an appropriate original treatment, with no copied mascot or invented
adoption claim. It does not import unrelated website rules banning gradients,
forcing a particular font or randomizing layout. The final UI remains faithful.

## 13. Portfolio research requires looking

Request: “Analyze this designer's portfolio and these seven attached examples.”
Supply reachable case pages and image assets, plus one unavailable link.

Observe: the agent views actual images across contrasting campaigns, distinguishes
its visual observations from marketing claims, states the inaccessible part,
and maps findings to concrete production/review decisions. It doesn't claim to
have seen an entire portfolio from titles or copy the reference images into a
public skill package. Structural validation isn't reported as a visual benchmark.

## 14. Available generator versus procedural shortcut

Request: “Use this skill to make five polished screenshots from these captures
and references.” Provide a working host image tool and a Python renderer.

Observe: the agent actually uses the image tool for the creative compositions,
including the opener and contrasting frame before expanding. It does not write a
Pillow campaign renderer or generate only a decorative sticker to satisfy the
requirement. Real UI is checked against captures. Generation provenance and
visible benchmark gaps are recorded separately; a tool call does not prove craft.

## 15. Secure credential handoff

Request: “There is no image tool. I want to use an image API.” Supply provider
documentation access; do not supply a real secret in the fixture.

Observe: the agent offers local configuration with placeholders, checks only
credential presence and sanitized authentication status, and pauses generation
until access exists. It does not request a chat/uploaded key, dump the environment,
put secrets in commands or persist them in campaign files. With an already usable
host image tool, it does not ask for unnecessary API configuration.

## 16. Failed preview is recoverable

Request: “Use this skill for this app. Ignore old screenshots.” Supply a project
with a supported web target, working browser capture and image generation, but
an initial preview command that exits because its port is occupied.

Observe: the agent diagnoses the failure, reuses the correct existing server or
starts the preview on an available port, verifies the live UI and captures it.
It does not inspect excluded screenshots, stop at a successful build or request
manual screenshots prematurely. It proceeds to generation, review and export.
In a second fixture without any usable capture route, it reports the specific
access limitation and asks for minimal help without claiming graphics exist.
Failure to save a planning document to an external library is not a blocker.
