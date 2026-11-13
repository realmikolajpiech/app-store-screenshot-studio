# Contributing

Please open an issue describing the app category, intended audience, agent and
image tool, the requested outcome, and what actually happened. For visual
regressions, compare the strongest prior result with the revision and describe
the lost qualities. Include only screenshots and source material you have
permission to share; remove personal data and credentials.

Prefer small changes supported by an observed failure over broad style bans.
Preserve accumulated user constraints and test revisions as well as first runs.
Use evals/scenarios.md for manual scenarios. Do not claim conversion gains from
visual preference or claim visual quality from passing helper tests.

Run `python3 -m unittest discover -s tests -v` after helper changes.

Current priorities: consistent art direction across revisions, stronger visual
reference comparisons, faithful UI preservation, and reliable target ratios.
