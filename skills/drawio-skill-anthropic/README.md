# anthropic-diagram

[中文](./README_CN.md) | English

A Claude Code skill that generates editorial-style diagrams in the visual language of [Anthropic's technical blog](https://claude.com/blog/product-management-on-the-ai-exponential) — calm, warm, and publication-ready — as `.drawio` files.

---

## Samples

![agent-loop-event-system](../images/anthropic-diagram/agent-loop-event-system.drawio.png)

## What it does

Give Claude a description of any process, system, or concept. The skill will:

1. Analyze the request and identify the right visual pattern
2. Write out a `DiagramSpec` — a structured plan before touching XML
3. Generate complete, styled draw.io XML
4. Save it as a `.drawio` file and open it automatically

**Output format**: `.drawio` files (editable in [draw.io](https://www.drawio.com/) / diagrams.net), with optional PNG/SVG export.

---

## Visual style

The Anthropic blog diagram style is defined by a few key principles:

- **Warm canvas** — background `#F2EFE8`, not pure white
- **Colors encode meaning, not decoration** — each semantic role (AI node, user input, error state, decision, etc.) has a dedicated fill/stroke pair
- **Open chevron arrowheads** (`endArrow=open;endSize=14`) — the single most recognizable element; never filled triangles
- **Orthogonal connectors with soft rounded corners** — clean, structured, never diagonal
- **Outer border frame** — every diagram is wrapped in a thin rounded rectangle, giving it a poster-like finish
- **Large editorial title** — bold, dark, horizontally centered
- **No shadows, no gradients, no saturated colors** — restrained contrast, typography and spacing do the hierarchy work

---

## Diagram patterns

The skill selects from 12 patterns based on what argument the diagram needs to make:

| Pattern | Use When |
|---------|----------|
| **Linear Workflow** | Sequential steps, one thing leads to the next |
| **Feedback Loop Workflow** | Retry, iteration, evaluation loops |
| **Branch Workflow / Decision Tree** | Branching logic, routing, approval gates |
| **Parallel Fan-out / Fan-in** | Concurrent workers, aggregation |
| **Split Comparison** | Before/after, two approaches side-by-side |
| **Grouped Architecture** | System boundaries, components, containment |
| **Layered Stack** | Hierarchy, abstraction layers, dependencies |
| **Swimlane Sequence** | Multiple actors interacting over time |
| **Hub-and-Spoke** | One central concept with supporting ideas |
| **Venn / Overlap** | Shared ownership, converging domains |
| **Editorial Chart** | Numerical comparison, metric contrast |
| **Callout Annotation** | Supporting notes that clarify a main diagram |

Patterns can be combined (e.g., Grouped Architecture + Callout Annotation), but one must always be primary.

---

## Semantic color system

Colors are assigned by semantic role, not aesthetics. The mapping is consistent across all diagrams:

| Role | Fill | Stroke |
|------|------|--------|
| Primary / Neutral | `#E6E2DA` | `#8C867F` |
| Secondary / Context (files, tools, docs) | `#EAF4FB` | `#6FA8D6` |
| Tertiary / Control (routers, memory, orchestration) | `#EEEAF9` | `#9A90D6` |
| Start / Trigger (user input, external trigger) | `#F8E9E1` | `#D88966` |
| End / Success | `#CFE8D7` | `#71AE88` |
| Warning / Reset (retry, interrupt) | `#F3E4DA` | `#C88E6A` |
| Decision (branch, gate, approval) | `#E6D7B4` | `#BFA777` |
| AI / LLM (model calls, agent workers) | `#D7E6DC` | `#7FB08F` |
| Inactive / Disabled | `#EFECE6` | `#B4AEA6` |
| Error | `#F8DFDA` | `#D96B63` |

This means a reader can infer structural roles at a glance without reading labels first.

---

## How to install

This skill is designed for [Claude Code](https://github.com/anthropics/claude-code). To install:

1. Copy the `skill.md` file and the `references/` directory into your Claude Code skills folder (typically `~/.claude/skills/anthropic-diagram/` or a project-level `.claude/skills/anthropic-diagram/`).
2. Claude Code will automatically detect and load the skill.

> **Prerequisite**: [draw.io Desktop](https://www.drawio.com/) must be installed if you want files to open automatically after generation.

---

## How to use

Just describe what you want to visualize in natural language. The skill triggers automatically on requests like:

- "Draw a diagram of the agent loop"
- "Create a flowchart showing how RAG retrieval works"
- "Visualize the before/after of context engineering"
- "Make an architecture diagram for this system"
- "画一张流程图，展示 agent 的工作原理"

No special syntax required. The skill works in both English and Chinese — diagram labels will match the language you use.

### Example prompts

```
Draw a diagram showing how an LLM agent uses tools: the model receives a user prompt,
decides whether to call a tool, executes the tool, then uses the result to generate a response.
```

```
Create a comparison diagram: on the left, a naive RAG pipeline;
on the right, a context-engineered version with reranking and query expansion.
```

```
画一张架构图，展示 multi-agent 系统中 planner、worker 和 verifier 的关系。
```

### PNG/SVG export

After a `.drawio` file is generated, you can export it:

```bash
# PNG export (Windows, draw.io Desktop installed)
"C:\Program Files\draw.io\draw.io.exe" -x -f png -e -b 20 -o output.png input.drawio

# SVG export
"C:\Program Files\draw.io\draw.io.exe" -x -f svg -e -b 20 -o output.svg input.drawio
```

---

## File structure

```
anthropic-diagram/
├── skill.md                      # Main skill prompt (workflow, XML templates, quality checklist)
├── references/
│   ├── color-palette.md          # Single source of truth for all colors, typography, geometry tokens
│   └── pattern-library.md        # 12 diagram patterns with layout rules and anti-patterns
└── README.md                     # This file
```

**`skill.md`** — the skill entry point. Defines the five-step workflow, all XML style strings, layout rules, and a pre-flight quality checklist.

**`references/color-palette.md`** — the brand style reference. Contains every color token, semantic mapping rule, container spec, connector spec, and typography scale. Edit this file to adapt the skill to a different visual identity without touching the workflow logic.

**`references/pattern-library.md`** — the structural reference. Defines when to use each pattern, layout rules per pattern, anti-patterns to avoid, and combination rules. Also contains density guidelines (simple / medium / dense) and a visual review checklist.

---


## Design philosophy

> A good diagram should not merely display information. It should make a claim obvious.

The skill is built around three ideas:

1. **Pattern before pixels** — choose the right structural pattern first; styling follows
2. **Semantic color** — every color decision encodes meaning, so color becomes information
3. **Restraint as quality signal** — no shadows, no gradients, no decoration; calm and sparse feels more credible than busy

These principles are what distinguish editorial technical diagrams (intended to explain ideas in articles) from UI dashboards or enterprise architecture tools.

---

## License

MIT
