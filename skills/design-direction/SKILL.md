---
name: design-direction
description: Help users who cannot describe their preferred website appearance choose a design direction through concrete references and plain-language comparisons, then turn preferences into a usable page and visual brief. Use for ambiguous aesthetic requests, reference mixing, overall website layout, or requests to reduce generic AI-looking design. Do not force a discovery flow for precise edits or an already settled design.
---

# Design Direction

Help the user express preferences by recognizing examples rather than requiring design vocabulary. Use their language. Treat aesthetic choices as decisions about their actual content and visitors.

## Establish what the site must do

Use the current brief and project context first. If necessary, ask one compact question about purpose, main content, and the visitor's most important action. Do not start with a long questionnaire about colors and fonts. Respect existing brands, selected references and explicit instructions.

If the user delegates design choices, make a justified choice and proceed. Do not create an approval gate merely because a direction has not been named. If they are actively choosing between options, wait for that choice before committing to a dependent design.

## Offer concrete, contrasting directions

For an uncertain user, read [the seed catalog](references/catalog.json) and shortlist about three meaningfully different directions that can support the content. The catalog is a starting point, not an exhaustive set of permitted styles. Search beyond it when suitable tools are available and the brief needs other directions.

Explain each direction with an everyday name, a real reference, its page organization, what the visitor sees first, and one tradeoff. Contrast layout, density or reading path, not merely different palettes applied to the same template.

Prefer actual full-page and inner-page views, with mobile views where available. Inspect current sites if browsing is available; historical observations are not fresh verification. With no visual access, provide clickable references, label the limitation, and restrict claims to supported content structure. Never claim to have seen a design from a text crawl alone. Never substitute invented screenshots for source evidence.

Ask for recognition rather than expert specification: “Which feels closest? You can like A's layout and B's colors, or reject all of them.” If every option misses, ask what feels wrong and change the direction of the search. Avoid cycling indefinitely through the same visual family.

## Translate preferences into decisions

Record what the user likes and dislikes at the component level: layout, typography, color, imagery, density, motion. Explain how borrowed elements fit together. Copy neither branding nor source assets without appropriate permission. A favorite hero alone is insufficient evidence for an entire site's architecture.

Turn vague adjectives into testable alternatives. “Premium” can mean restrained hierarchy, rich imagery, or strong editorial composition; it is not a command to use beige and serif fonts. “Cool” need not mean WebGL. A user-requested gradient, card grid or playful motion is legitimate when it supports the brief.

## Deliver a buildable brief

Scale the detail to the project. When producing a durable brief, use `DESIGN-BRIEF.md` in the requested project and include:

- Audience, content inventory, primary task and constraints.
- Navigation and the order and purpose of sections on the homepage and at least one relevant inner page; a simple wireframe when useful.
- Typography roles with appropriate language coverage, semantic color roles, spacing, content width and image treatment. Choose values for the actual project, not a fixed universal palette.
- Reference URLs or IDs, exactly what to borrow, what to avoid, and why.
- Mobile reflow and navigation; loading, empty, error and focus states where applicable; motion with reduced-motion behavior.
- A short acceptance checklist tied to real tasks, plus any unresolved assumptions.

Before building, ask whether the plan would remain identical if the subject and content changed. If so, reconsider the parts that should respond to the brief. Preserve existing design-system choices that work. Do not add visual novelty just to differ.

## Review generic defaults in context

Use this review when requested to reduce an AI-looking design, or when checking the implemented direction. For an existing site, start with its content, chosen style and task paths; do not restart preference discovery unless the direction itself is unresolved. These are contextual warning signs, not evidence that AI authored a page:

- A stock sequence of oversized hero, three feature cards, metrics, testimonials and CTA: require a content or visitor-task reason for each section. Remove unsupported sections; never invent numbers or testimonials to fill them.
- Equal cards for unequal content: check whether articles, projects or data need a list, index or table. Keep cards when grouping and comparison justify them.
- Competing gradients, glows, glass and motion: identify which effects support the chosen identity, hierarchy or feedback. Reduce competition without banning a palette or technique.
- Oversized headings, excessive spacing or faint text: inspect real content lengths and mobile layouts before changing type scale, width, spacing or contrast.
- Interchangeable copy and structure: replace generic claims with actual content and a useful organization specific to the brief. Do not fabricate subject matter.
- A polished hero with weak inner pages or broken states: prioritize the visitor's core path and consistency across pages over more hero decoration.

Report only the most consequential findings, usually three to five, with location, observed evidence, user impact and a concrete correction. Separate preference disagreements from usability defects. Without visual access, mark visual findings unverified. Do not invent a numerical AI-likeness score. Preserve explicit user preferences and established design systems; avoid converging every project on monochrome minimalism. After corrections, revisit the same views and tasks, checking both usability and fidelity to the selected direction.

## Continue within the requested scope

If the user requested a website, implement the brief with the tools available; if they requested only direction, deliver the brief. Additional design skills are optional, not prerequisites. Do not install tools, publish a site, or change unrelated configuration merely because this skill is used.

After implementation, compare actual screenshots and task paths against the brief where the environment permits. Check the page beyond the hero: content density, navigation, inner pages, readable contrast, responsive overflow, keyboard focus and meaningful interactions. Report verified behavior separately from unchecked items. Make a focused correction based on evidence rather than replacing the visual direction by default.
