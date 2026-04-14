# Color Palette & Brand Style

**This is the single source of truth for all colors and brand-specific styles.**  
To customize diagrams for a different visual identity, edit this file. Everything else in the skill should stay universal and semantic.

This palette is optimized for:
- warm editorial tech-blog diagrams
- low-density explanatory flowcharts
- architecture diagrams with soft grouping
- restrained comparison charts
- large-title, article-embedded visuals

It is **not** optimized for dashboards, neon UI, or high-saturation infographics.

---

## Core Style Principles

1. **Colors encode meaning, not decoration.**
2. **Most of the canvas should remain neutral.**
3. **Accent colors should be sparse and semantic.**
4. **Strokes are always darker than fills.**
5. **Typography and spacing carry more hierarchy than color.**
6. **Prefer calm, editorial contrast over vivid UI contrast.**
7. **Default to no shadows and no gradients.**

---

## Shape Colors (Semantic)

Colors encode meaning, not decoration. Each semantic purpose has a fill/stroke pair.

| Semantic Purpose | Fill | Stroke |
|------------------|------|--------|
| Primary/Neutral | #E6E2DA | #8C867F |
| Secondary / Context | #EAF4FB | #6FA8D6 |
| Tertiary / Control | #EEEAF9 | #9A90D6 |
| Start/Trigger | #F8E9E1 | #D88966 |
| End/Success | #CFE8D7 | #71AE88 |
| Warning/Reset | #F3E4DA | #C88E6A |
| Decision | #E6D7B4 | #BFA777 |
| AI/LLM | #D7E6DC | #7FB08F |
| Inactive/Disabled | #EFECE6 | #B4AEA6 |
| Error | #F8DFDA | #D96B63 |

**Rule**: Always pair a darker stroke with a lighter fill for contrast.

### Semantic Interpretation

- **Primary/Neutral**: default blocks, generic system components, standard containers
- **Secondary / Context**: files, skills, tools, docs, retrieved context, storage-like resources
- **Tertiary / Control**: routers, memory, evaluators, aggregators, orchestration, policy layers
- **Start/Trigger**: user input, prompt input, external trigger, human intervention
- **End/Success**: verified result, completed output, accepted answer, successful state
- **Warning/Reset**: retry, reset, re-entry, interrupt, caution, manual steering
- **Decision**: branch points, filters, approval logic, yes/no gates
- **AI/LLM**: model calls, agent workers, active execution stages, reasoning stages
- **Inactive/Disabled**: optional items, de-emphasized elements, unavailable or future elements
- **Error**: failures, blocked execution, invalid state, rejected result, deny path

---

## Text Colors (Hierarchy)

Use color on free-floating text to create visual hierarchy without needing extra containers.

| Level | Color | Use For |
|-------|-------|---------|
| Title | #1F1F1C | Main diagram title |
| Subtitle | #5F5A54 | Section headers, panel titles |
| Body/Detail | #4F4A44 | Labels, annotations, helper copy |
| Muted/Support | #7A756E | Secondary annotations, non-primary labels |
| On light fills | #2D2B28 | Text inside most boxes and panels |
| On dark fills | #FAF8F4 | Rare use only; avoid dark fills by default |

### Text Hierarchy Rules

- Use **Title** for the single main headline only.
- Use **Subtitle** for section names, panel labels, and major group headings.
- Use **Body/Detail** for node labels, arrows, notes, and supporting explanation.
- Use **Muted/Support** for optional captions or low-priority labels.
- Prefer free-floating text over unnecessary containers.

---

## Evidence Artifact Colors

Used for code snippets, data examples, and other concrete evidence inside technical diagrams.

| Artifact | Background | Border | Text Color |
|----------|------------|--------|------------|
| Code snippet | #EEF3F7 | #B7C9D8 | #44515C |
| JSON/data example | #EEF4EE | #B9CCBE | #46574C |
| Terminal/CLI example | #F3F1EC | #C8C1B6 | #4C4943 |
| File tree / spec excerpt | #EDF2F8 | #B8C6D8 | #506070 |

### Evidence Rules

- Evidence blocks should look quieter than primary diagram nodes.
- Use evidence artifacts only when concrete examples improve understanding.
- Do not make evidence artifacts the most visually dominant element unless the diagram is explicitly evidence-driven.

---

## Default Stroke & Line Colors

| Element | Color |
|---------|-------|
| Arrows | Use the stroke color of the source element's semantic purpose |
| Structural lines (dividers, trees, timelines) | #8C867F |
| Secondary structural lines | #9A948C |
| Marker dots (fill) | #E6E2DA |
| Marker dots (stroke) | #8C867F |
| Grouping boundary (solid) | #8C867F |
| Grouping boundary (dashed) | #B9B3AB |

### Line Rules

- Main flows inherit meaning from the source node where possible.
- Structural dividers should stay neutral.
- Do not use black lines unless the whole diagram is monochrome.
- Dashed lines indicate optionality, inferred paths, soft grouping, or human-overridable behavior.

---

## Background

| Property | Value |
|----------|-------|
| Canvas background | #F2EFE8 |
| Panel background | #FAF8F4 |
| Alternate panel background | #F6F4EE |
| Soft emphasis background | #F3F0E9 |

### Background Rules

- Keep the overall canvas warm and light.
- Avoid pure white full-canvas backgrounds unless required by export constraints.
- Panels should be only slightly lighter or cleaner than the canvas, not strongly contrasted.

---

## Container Styles

| Container Type | Fill | Stroke | Radius | Stroke Width |
|----------------|------|--------|--------|--------------|
| Outer panel | #FAF8F4 | #8C867F | 20 | 2.0 |
| Inner panel | #FAF8F4 | #8C867F | 14 | 2.0 |
| Neutral node | #E6E2DA | #8C867F | 12 | 1.8 |
| Semantic node | semantic fill | semantic stroke | 12 | 1.8 |
| Pill label | #FAF8F4 | #8C867F | 999 | 1.8 |
| Highlight callout | #EEF7E8 | #89B85A | 12 | 2.0 |
| Soft grouping region | transparent or #F6F4EE | #B9B3AB | 16 | 1.5 dashed |
| Inactive placeholder | #EFECE6 | #B4AEA6 | 12 | 1.6 |

### Container Rules

- Prefer rounded rectangles over sharp-cornered boxes.
- Use pills for small categorical labels or compact component tags.
- Use soft grouping regions to imply relationship without adding visual clutter.
- Avoid nested containers deeper than 3 levels.
- Most diagrams should have 1 outer grouping level and 0–2 inner grouping levels.

---

## Connector Styles

| Connector Type | Color | Width | Pattern | Arrow | Use For |
|----------------|-------|-------|---------|-------|---------|
| Primary flow | #7A756E | 1.8 | solid | open, size 14 | Main process path |
| Optional flow | #9A948C | 1.6 | dashed | open, size 14 | Optional / inferred path |
| Feedback loop | #8E8982 | 1.8 | solid | open, size 14 | Retry / iterative loop |
| Human override | #D88966 | 1.8 | dashed | open, size 14 | Human interrupt / steering |
| Context link | #7FB08F | 1.8 | solid | open, size 14 | Context injection / supporting flow |
| Error path | #D96B63 | 1.8 | solid or dashed | open, size 14 | Failure / blocked path |

**Arrow rule**: All connectors use `endArrow=open;endSize=14;` — this is the single most recognizable visual element of Anthropic blog diagrams. Open chevron arrowheads (not filled triangles) give the diagrams their editorial, publication-quality look. Never use filled/block arrowheads.

### Connector Rules

- Prefer **orthogonal connectors** in architecture diagrams.
- Prefer **straight or lightly orthogonal connectors** in workflow diagrams.
- Use **curved connectors** mainly for feedback loops.
- Use dashed connectors sparingly; too many make the diagram feel uncertain.
- Main flow should be visually obvious within 3 seconds of viewing.

---

## Geometry Tokens

| Token | Value |
|-------|-------|
| Small radius | 10 |
| Medium radius | 14 |
| Large radius | 20 |
| Pill radius | 999 |
| Default stroke width | 1.8 |
| Panel stroke width | 2.0 |
| Dashed pattern | 6 6 |
| Small arrow size | 10 |
| Default arrow size | 12 |

### Geometry Rules

- Keep radii consistent across the diagram.
- Prefer a single radius family per diagram.
- Avoid mixing very thick and very thin strokes.
- Use panel strokes slightly heavier than internal strokes.

---

## Typography & Spacing

| Token | Value |
|-------|-------|
| Title size | 30–42 |
| Section title size | 18–24 |
| Body label size | 12–16 |
| Caption size | 11–13 |
| Title weight | 700–800 |
| Section weight | 600–700 |
| Body weight | 400–500 |
| Outer canvas padding | 48 |
| Section gap | 28 |
| Internal box padding | 12–18 |
| Grid step | 8 |
| Default node gap | 20–28 |
| Large panel gap | 32–48 |

### Typography Rules

- The title should be large and editorial, not UI-like.
- Do not overuse bold inside nodes.
- Prefer short labels over wrapped paragraphs.
- In diagrams, spacing should do more work than font variation.

---

## Semantic Mapping Rules

Use this mapping when converting user intent into styled nodes.

- Use **AI/LLM** for model calls, agent workers, reasoning stages, execution stages.
- Use **Secondary / Context** for files, documents, tools, skills, retrieved context, and system resources.
- Use **Tertiary / Control** for routers, memory, evaluators, aggregators, controllers, and orchestration logic.
- Use **Start/Trigger** for prompts, users, interrupts, external systems, and manual input.
- Use **End/Success** for verified outputs, final answers, completed jobs, and accepted results.
- Use **Warning/Reset** for retry paths, resets, re-entry points, and caution states.
- Use **Decision** only for branch points, gates, approvals, filters, and yes/no logic.
- Use **Inactive/Disabled** for placeholders, disabled features, optional future nodes, and de-emphasized elements.
- Use **Error** for blocked execution, denied action, invalid state, failed validation, and hard stops.

---

## Diagram-Type Defaults

### Workflow Diagram
- Background: canvas background
- Nodes: AI/LLM, Start/Trigger, End/Success, Decision as needed
- Connectors: primary flow + optional feedback loop
- Layout: clean linear or gently branching
- Preferred emphasis: flow clarity

### Architecture Diagram
- Background: canvas background with panel grouping
- Nodes: Primary/Neutral + Secondary / Context + Tertiary / Control
- Connectors: orthogonal
- Layout: grouped systems and interfaces
- Preferred emphasis: containment and interaction

### Comparison Diagram
- Background: two or more large neutral panels
- Nodes: soft semantic fills
- Connectors: minimal
- Layout: mirrored or side-by-side
- Preferred emphasis: contrast in structure, not color

### Chart Diagram
- Background: warm neutral
- Bars/series: use neutral + 1–2 restrained accents
- Gridlines: very light neutral stroke
- Preferred emphasis: direct value comparison, low clutter

### Editorial Poster Diagram
- Large title, sparse elements, oversized whitespace
- Minimal arrows
- Strong compositional balance
- One dominant idea only

---

## Non-Goals

Avoid these unless the user explicitly requests them:
- saturated brand colors
- drop shadows
- glossy UI treatments
- gradients
- icon-heavy decoration
- dense legends
- more than 4 semantic accent colors in one diagram
- dashboard aesthetics

---

## Fallback Rules

If semantic meaning is unclear:
1. default to **Primary/Neutral**
2. use **Secondary / Context** for passive information objects
3. use **AI/LLM** for active computational steps
4. use **Tertiary / Control** for routing or memory-like logic
5. use **Start/Trigger** only when something truly initiates flow

If too many colors are present:
- collapse low-priority semantics into **Primary/Neutral**
- keep only the 2–3 most meaningful accent categories

If a diagram feels too busy:
- remove containers before removing spacing
- reduce connector count before reducing color
- demote secondary labels to muted text