---
name: design-direction
description: Help people who cannot describe a website's appearance choose through real whole-site references, record what they like, and turn that choice into page structure and a buildable design brief. Use for ambiguous aesthetic requests, reference mixing, overall layout decisions, or reducing generic AI-looking design. Preserve a settled direction for precise edits.
license: Apache-2.0
---

# Design Direction

Make preferences visible and decisions traceable: content and tasks → suitable real references → recognizable alternatives → a recorded choice → implementation → evidence-based review. Speak the user's language, not design jargon. Methods adapted from Impeccable are credited in [NOTICE.md](NOTICE.md).

## Route by the actual request

- **Uncertain direction:** read [direction-workflow.md](references/direction-workflow.md). Start from known purpose, content and visitor tasks; ask only what materially changes the result.
- **Clear reference or delegated choice:** extract the binding choices and proceed within scope. Do not manufacture another approval round.
- **Existing page needs polish or less AI-looking design:** inspect the incumbent, then read [review.md](references/review.md). Do not restart identity selection for a local fix.
- **Asked to build:** continue from the selected direction into implementation. Planning alone is incomplete for a build request; a direction-only request does not authorize building or publishing.

## Classify each page by visitor success

Borrow Impeccable's surface distinction, not an industry taxonomy:

| Mode | Visitor succeeds when… | Design consequence |
| --- | --- | --- |
| `read` | They find and understand information | Readable text, indexes, search where needed, navigation and inner pages |
| `operate` | They complete a task | Predictable controls, useful density, visible states and recovery |
| `persuade` | They can evaluate an offer and act | Real evidence, clear sequence and an appropriate primary action |
| `experience` | They explore the work itself | Artifacts lead, discoverable navigation, usable exploration |

A website can mix modes. A personal homepage may introduce work, its archive support discovery, and its article page support reading. Do not turn all three into posters. Expressive sites and dense tools are both legitimate; match expression to the task and explicit preference.

## Use the case library honestly

Read [catalog-guide.md](references/catalog-guide.md) before adding records or making evidence claims. The portable [catalog](references/catalog.json) contains historical seeds, not a fully reviewed gallery.

If Python 3 is available, the bundled script validates and screens records without network access:

```sh
python3 <skill-dir>/scripts/catalog.py validate
python3 <skill-dir>/scripts/catalog.py shortlist --mode read --content articles
```

Default selection requires whole-site evidence. `--include-partial` explicitly allows partially inspected candidates and labels their missing evidence; text-only candidates remain excluded. Empty output is a coverage gap, not permission to invent a reference or silently lower the evidence bar. Without Python, apply the same rules manually.

Screen by tasks, content, assets and constraints before choosing for visual variety. The script's ordering is a transparent retrieval heuristic, not a beauty or usability score. Review current pages when tools permit. Historical observations are not fresh inspection; a text crawl cannot establish visual quality.

## Turn the selection into an implementation contract

Follow the brief and preference receipt in [direction-workflow.md](references/direction-workflow.md). Record the selected structure, exact reference aspects, rejected aspects, homepage and inner-page order, mobile behavior and acceptance checks. Label assistant assumptions separately from user choices.

Preserve factual product context and existing design systems. Missing `DESIGN.md` does not imply no identity exists. Use existing project documents rather than creating competing authorities. Keep page decisions in `DESIGN-BRIEF.md` or the existing page brief; record reusable tokens in `DESIGN.md` after verifying the implementation. These are development documents, not copy for the site's visitors.

Reference images show source evidence; wireframes and generated concepts show proposals and must be labeled accordingly. Never present a generated picture as a screenshot of a real site. Do not copy reference branding, assets or exact site compositions as a default. Describe the principle being transferred and the adaptation to this content.

## Verify the selected direction survived

Use [review.md](references/review.md) after implementation or when asked for review. Inspect the whole page, a key inner page, mobile layout and core task; check loading/error/empty/focus states when relevant. First judge content, hierarchy and selection fidelity, then reconcile any mechanical findings. A clean detector report is not proof of good design.

Fix material issues within scope, recheck affected views, and report remaining limits. A user who chose vivid color must not receive monochrome minimalism as an automatic anti-slop correction. Do not keep restyling after acceptance criteria hold.

Impeccable is optional. The integration notes in `review.md` explain when its commands help; this skill does not install it, activate hooks, invoke remote catalogs or require image generation automatically.
