# Design rationale

This is an independently written evolution of the workflow popularized by
[Adam Lyttle's ASO screenshot skill](https://github.com/adamlyttleapps/claude-skill-aso-appstore-screenshots).
It retains benefit discovery and screenshot pairing while replacing the fixed
rendering template. Upstream uses MIT; its notice is included in `NOTICE`.

## What we retain

- Read the app before writing promises. Screens, data contracts and flags inform
  which outcomes exist and how to demonstrate them.
- Inspect captures honestly and request specific retakes instead of filling the
  campaign with sparse or irrelevant screens.
- Pair each benefit with visible evidence and persist decisions for resumption.
- Export exact dimensions; do not give the user raw model outputs as upload files.

## What changes

| Upstream convention | This package's decision | Reason |
| --- | --- | --- |
| Same phone position/size, top type, fixed uppercase hierarchy | Shared visual grammar plus an intentional composition matrix | Cohesion does not require repetition |
| Every headline starts with an isolated action verb | Outcome-first, idiomatic localized copy | Languages and brands need different emphasis |
| One saturated solid background; avoid light backgrounds/gradients | Learn palette, materials and contrast from the app | The references include successful-looking light, dark, saturated and softly lit treatments |
| Three variants for each frame | Distinct concepts only while a choice is open | Approved directions need precise execution, not repeated speculative spending |
| Named Gemini tool and Claude-only memory | Available image tools and project-local manifest | The workflow should travel between capable agents |
| Narrow iPhone crop assumptions | Placement-specific ratio and background adaptation | iPad, headers and search need different compositions |
| Fixed default resolution treated as current | Explicit target, current source verification and validation | Upload slots and accepted sizes evolve |

## Lessons from visual review

[visual-benchmarks.md](visual-benchmarks.md) records the inspected portfolio
sample and supplied campaign references. Their value includes expressive
typography, photography/casting, content selection, coherent materials and
layered scenes. Benefit discovery and a layout matrix alone don't produce that
finish. The production workflow therefore compares representative finished
frames against actual reference images before extending the direction.

Review of an earlier local-news trial exposed the gap: bold headings, true UI,
different phone leans and enlarged cards could pass the old checklist while
the images still looked assembled and generic. The new criteria separate the
visual idea, typography, image quality and spatial integration from factual
correctness. This is a retrospective diagnosis, not evidence that a subsequent
campaign has already improved.

The references also contradict universal aesthetic bans. Repeated upright
devices can create calm; grain, gradients and 3D can establish identity; useful
secondary text can coexist with one dominant message. The hidden-headline and
competitor-swap checks are diagnostic aids, not automatic rejection rules.
User constraints still take precedence over these stylistic choices.

Polish driving-school production exposed practical failure modes: excessive
whitespace after removing a wordmark, identical phone leans, generic repeated
layouts, too little card/type separation, raw outputs in the wrong dimensions,
contact sheets mixed into upload archives, tiny focal art after safe-area
overcorrection, and a tall image pasted onto iPad side bars. Each is addressed
as a transferable decision criterion, not a mandatory blue-road aesthetic.

## Intentional limits

This is a production skill, not an ASO ranking predictor or automatic App Review
certifier. It does not claim that reference artwork converts well without data.
It does not bundle third-party artwork, private captures, fonts, device renders
or a paid provider dependency. Its local tools validate file invariants; visual
and factual review still require looking at the result.

The bundle is suitable for publication, but creating it does not authorize
publishing a repository, uploading assets or changing a live store listing.
