# Pattern Library

**This file defines the reusable visual patterns used by the diagram skill.**  
The color palette defines *how things look*.  
This pattern library defines *how ideas should be structured visually*.

Use these patterns to turn user intent into diagrams that feel editorial, calm, and article-ready.

---

## Core Principle

A good diagram should not merely display information.  
It should make a claim obvious.

Choose a pattern based on the **argument** the diagram is making:

- Is this showing a sequence?
- A comparison?
- A system boundary?
- A loop?
- A branching decision?
- A layered architecture?
- A group overlap?
- A quantitative contrast?

The wrong pattern makes the content feel busy even when the styling is correct.

---

## Pattern Selection Rules

Choose the pattern that best matches the user's explanatory intent.

| User Intent | Preferred Pattern |
|-------------|-------------------|
| Explain a sequence of steps | Linear Workflow |
| Show retries, iteration, refinement | Feedback Loop Workflow |
| Show decisions or branching logic | Decision Tree / Branch Workflow |
| Compare before/after or old/new | Split Comparison |
| Show components inside systems | Grouped Architecture |
| Show layered stack or hierarchy | Layered Stack |
| Show interactions across actors or systems | Swimlane Sequence |
| Show shared responsibility or overlap | Venn / Overlap |
| Show performance or metric comparison | Editorial Chart |
| Show one central concept with supporting ideas | Hub-and-Spoke |
| Show multiple workers operating in parallel | Parallel Fan-out / Fan-in |

### Pattern Priority Rule

When multiple patterns seem possible:
1. Prefer the pattern with the **clearest reading order**
2. Prefer the pattern with the **fewest crossing lines**
3. Prefer the pattern that supports the **main claim in one glance**
4. Prefer **comparison** over complicated topology when the core message is contrast
5. Prefer **grouped architecture** over workflow when containment matters more than time

---

## Universal Composition Rules

These rules apply to all patterns.

### 1. One dominant idea per diagram
A diagram should explain one main point.  
Secondary details should support that point, not compete with it.

### 2. Reading order must be obvious
The viewer should know where to start and where to look next within 3 seconds.

Default reading directions:
- left to right for workflows and comparisons
- top to bottom for stacks and hierarchies
- outer to inner for containment diagrams

### 3. Keep hierarchy shallow
Prefer at most:
- 1 title level
- 1 section/group level
- 1 node level
- optional annotation level

Avoid deeply nested visual structures.

### 4. Use whitespace as structure
Spacing should separate groups before boxes do.

### 5. Use containers sparingly
Do not put every label in a box.  
Use free-floating text when the relationship is already clear.

### 6. Reduce visual grammar before adding color
First solve layout, grouping, and connector logic.  
Then add semantic color.

---

## Pattern 1: Linear Workflow

### Use When
- the process is mostly sequential
- each step leads to the next
- the key message is procedural flow

### Typical Examples
- prompt -> retrieve -> reason -> answer
- gather context -> take action -> verify -> done
- ingest -> index -> retrieve -> generate

### Visual Structure
- one row or one column of nodes
- evenly spaced
- consistent connector style
- optional small labels over arrows

### Layout Rules
- use 3 to 7 major steps
- equal or near-equal spacing between nodes
- keep the main path straight
- avoid side branches unless critical

### Node Rules
- start node may use Start/Trigger
- processing steps may use AI/LLM or Primary/Neutral
- end node may use End/Success

### Connector Rules
- primary flow only
- use optional arrow labels only when they clarify transformation

### Anti-Patterns
- too many side annotations
- mixing architecture grouping into a simple flow
- long paragraphs inside nodes

---

## Pattern 2: Feedback Loop Workflow

### Use When
- the process involves retry, refinement, evaluation, or iteration
- the key message is that work loops until success criteria are met

### Typical Examples
- generate -> evaluate -> revise
- gather context -> act -> verify -> retry
- agent loop with human steering

### Visual Structure
- one main forward path
- one loop-back connector
- optional external interrupt or override

### Layout Rules
- keep the main path straight
- route the loop outside the main path
- use curved or gently orthogonal return connectors
- avoid multiple loops unless explicitly necessary

### Connector Semantics
- forward path = solid
- retry loop = feedback connector
- human interrupt = dashed warm-colored connector

### Anti-Patterns
- multiple overlapping loopbacks
- loop connector passing through nodes
- showing every internal retry as a separate visible step

---

## Pattern 3: Branch Workflow / Decision Tree

### Use When
- a choice meaningfully changes the path
- the diagram needs to show approval, routing, or gating

### Typical Examples
- policy check -> allow / deny
- retrieve enough context? yes / no
- task type -> choose specialized agent

### Visual Structure
- one incoming path
- one decision node
- 2 to 4 outgoing branches
- branches should be visually balanced

### Layout Rules
- branches should fan out clearly
- label branches directly near the divergence
- rejoin later only if the paths truly converge

### Node Rules
- decision nodes should be visually distinct
- do not use decision styling for generic steps

### Connector Rules
- branch labels should be short: yes / no / low confidence / use tool
- keep branches separated with whitespace

### Anti-Patterns
- more than 4 branches from one decision
- unlabeled branch semantics
- arbitrary diamonds everywhere

---

## Pattern 4: Parallel Fan-out / Fan-in

### Use When
- one task splits into multiple concurrent workers
- multiple results are aggregated into one outcome

### Typical Examples
- planner -> multiple subagents -> synthesizer
- query -> parallel retrieval sources -> ranker
- dispatcher -> workers -> reducer

### Visual Structure
- one source node
- 2 to 5 parallel branches
- one merge or synthesis node

### Layout Rules
- distribute branches evenly
- keep branch node sizes consistent
- use a clear convergence point
- align parallel workers on one row or column

### Semantic Rules
- worker nodes often use AI/LLM or Secondary / Context depending on role
- merge node often uses Tertiary / Control

### Anti-Patterns
- uneven branch spacing
- showing too many workers
- converging lines crossing each other

---

## Pattern 5: Split Comparison

### Use When
- the point is contrast between two states or approaches
- before/after or without/with AI is the main message

### Typical Examples
- before AI vs with AI
- prompt engineering vs context engineering
- baseline vs improved system

### Visual Structure
- two or three large side-by-side panels
- mirrored or comparable composition
- minimal connectors across panels

### Layout Rules
- panels should have equal visual weight
- use repeated labels where comparison benefits from symmetry
- keep color differences restrained
- use structure, not saturation, to show difference

### Title Rules
- title should state the comparison claim, not just the categories

### Anti-Patterns
- unrelated layouts in each panel
- overusing arrows between panels
- too much text explaining what the eye should already see

---

## Pattern 6: Grouped Architecture

### Use When
- the main point is system boundaries, modules, resources, or containment
- components belong to subsystems more than they happen in time

### Typical Examples
- agent config + virtual machine
- application + tools + storage + runtime
- sandbox boundaries and policy layers

### Visual Structure
- large outer groups or panels
- smaller nodes inside groups
- connectors between components or between groups
- optional annotation callouts

### Layout Rules
- place grouped systems first
- place internal nodes second
- connect after layout is stable
- use orthogonal connectors by default

### Grouping Rules
- use containers to indicate ownership or environment
- use softer grouping for conceptual regions
- keep nesting shallow

### Anti-Patterns
- excessive nesting
- using workflow arrows when simple adjacency is enough
- putting every sentence inside a container

---

## Pattern 7: Layered Stack

### Use When
- the diagram explains hierarchy, dependency, or abstraction layers
- the order is vertical, not procedural

### Typical Examples
- model layer / orchestration layer / tool layer
- UI / services / storage
- policy / execution / filesystem

### Visual Structure
- stacked horizontal bands or cards
- optional small dependencies between layers
- labels aligned consistently

### Layout Rules
- use top-to-bottom hierarchy
- keep layers horizontally aligned
- do not overconnect adjacent layers unless needed

### Anti-Patterns
- turning a stack into a workflow
- too many internal arrows
- inconsistent widths without semantic reason

---

## Pattern 8: Swimlane Sequence

### Use When
- multiple actors or systems interact over time
- timing/order matters across participants

### Typical Examples
- user / agent / tool / verifier
- planner / worker / reviewer / executor
- browser / model / sandbox / file system

### Visual Structure
- vertical or horizontal lanes for actors
- time direction is consistent
- messages cross lanes

### Layout Rules
- 2 to 5 lanes only
- lane titles should be visually quiet but clear
- events inside lanes should align to a timeline
- message lines should be short and readable

### When to Avoid
- when the true message is system architecture, not interaction order
- when a simple workflow would suffice

### Anti-Patterns
- too many lanes
- too many tiny message steps
- unaligned timing rows

---

## Pattern 9: Hub-and-Spoke

### Use When
- one central entity connects to several supporting concepts
- the point is central coordination, not sequence

### Typical Examples
- a central model using tools
- one orchestrator with multiple capabilities
- one concept with several implications

### Visual Structure
- one central dominant node
- 3 to 6 surrounding nodes
- minimal connector complexity

### Layout Rules
- center node should be visibly primary
- surrounding nodes should be balanced around it
- preserve symmetry where possible

### Anti-Patterns
- using hub-and-spoke for actual sequential workflows
- too many spokes
- unequal visual weight making the composition drift

---

## Pattern 10: Venn / Overlap

### Use When
- the message is shared responsibility, convergence, or blended ownership
- overlap itself is the idea

### Typical Examples
- product / design / engineering overlap
- multiple disciplines converging under AI
- overlapping capability zones

### Visual Structure
- 2 or 3 overlapping soft shapes
- labels placed in or near each region
- center overlap may carry emphasis if meaningful

### Layout Rules
- keep shapes large and simple
- use transparency lightly
- avoid dense annotations

### Anti-Patterns
- more than 3 overlapping groups
- forcing workflow semantics into overlap shapes
- too much text in intersections

---

## Pattern 11: Editorial Chart

### Use When
- the main claim is numerical comparison
- precise values matter less than the contrast/trend

### Typical Examples
- baseline vs improved retrieval
- error rate comparisons
- task success rate by method

### Chart Types Allowed
- bar chart
- column chart
- simple grouped bar chart
- very restrained line chart

### Chart Rules
- no dashboard styling
- no saturated palettes
- no heavy legends when direct labels are possible
- gridlines should be faint
- use 2 to 4 series max
- values should be easy to read without clutter

### Preferred Styling
- warm neutral background
- bars in neutral + 1–2 semantic accents
- large title
- direct value labels where helpful

### Anti-Patterns
- pie charts
- rainbow series
- dense axes and ticks
- multi-metric chart junk

---

## Pattern 12: Callout Annotation

### Use When
- one supporting fact or note clarifies a main diagram
- the annotation is helpful but not central to the structure

### Typical Examples
- “contents of skill directories live in the file system”
- “human can interrupt, steer, or add context”
- “policy layer enforces sandbox restrictions”

### Visual Structure
- small callout box outside the main flow
- one connector pointing to the referenced region
- minimal text

### Layout Rules
- keep callouts outside major flow regions
- use them to explain, not replace, structure
- 1 to 3 callouts per diagram is usually enough

### Anti-Patterns
- too many callouts
- callouts becoming the dominant content
- crossing callout connectors over main structure

---

## Pattern Combination Rules

Patterns can be combined, but only when one pattern is clearly primary.

### Good Combinations
- Grouped Architecture + Callout Annotation
- Linear Workflow + Feedback Loop
- Split Comparison + Simple Workflow
- Parallel Fan-out / Fan-in + Grouped Architecture
- Swimlane Sequence + Callout Annotation

### Risky Combinations
- Split Comparison + Swimlane + Architecture
- Venn + Workflow
- Layered Stack + Branch Tree + Fan-out all together

### Combination Rule
If combining patterns increases cognitive load more than it increases explanatory value, split into two diagrams instead.

---

## Density Guidelines

### Simple
- 3–5 nodes
- 1 primary pattern
- almost no annotations

### Medium
- 6–12 nodes
- 1 primary pattern
- 1 secondary pattern allowed
- 1–3 callouts

### Dense
- 12–20 nodes
- only when architecture or sequence genuinely requires it
- strong grouping required
- must preserve obvious reading order

### Hard Limit Guidance
A single editorial diagram should usually avoid:
- more than 20 visible nodes
- more than 4 semantic colors
- more than 3 nested group levels
- more than 2 visible loopbacks
- more than 5 parallel branches

---

## Node Content Rules

### Labels
- keep labels short
- prefer nouns or verb phrases
- avoid full-sentence labels inside nodes

### Good Examples
- Gather context
- Verify results
- Retrieved docs
- Policy layer
- Remote MCP server

### Weak Examples
- This stage is where the system gathers context from different sources
- Use the tool when it is appropriate and then maybe verify output

### Evidence Blocks
Only include concrete evidence blocks when they meaningfully improve precision:
- code snippet
- file tree
- API response
- schema excerpt

---

## Connector Grammar

Use connectors consistently to preserve meaning.

| Connector Style | Meaning |
|-----------------|---------|
| Solid | primary path |
| Dashed | optional, inferred, soft relationship, human-overridable |
| Curved return | feedback loop |
| Orthogonal | architecture/system interaction |
| Straight | simple step progression |
| No arrowhead | grouping, alignment, weak association |

### Connector Rules
- do not let connectors do layout work
- layout first, connect second
- minimize crossings
- label connectors only when the transformation is important

---

## Choosing Between Workflow and Architecture

This is the most common mistake.

Choose **Workflow** when:
- time/order is the main message
- the viewer should understand what happens next

Choose **Architecture** when:
- containment/boundary is the main message
- the viewer should understand what belongs where

Choose **Swimlane** when:
- interaction order across actors matters

Choose **Comparison** when:
- the core message is “this structure changed”

---

## Visual Review Checklist

Before finalizing, verify:

### Argument
- Can the main point be understood in one sentence?
- Does the chosen pattern support that point?

### Reading Order
- Is the start obvious?
- Is the main path visually dominant?
- Are groups clear before the viewer reads labels?

### Density
- Are there too many nodes?
- Are there too many accents?
- Can any labels become free text instead of boxes?

### Connectors
- Any crossings that can be removed?
- Any loopbacks that can be simplified?
- Are dashed lines used sparingly?

### Balance
- Does the composition feel centered and stable?
- Is whitespace distributed intentionally?
- Is there one focal point rather than many?

---

## Pattern Fallback Rules

When the structure is ambiguous:

1. default to **Linear Workflow** for process-like user input
2. default to **Grouped Architecture** for system/component descriptions
3. default to **Split Comparison** for before/after content
4. default to **Callout Annotation** rather than adding extra nodes
5. split into multiple diagrams rather than forcing a hybrid

---

## Output Planning Template

Before rendering, the system should internally identify:

- **main claim**
- **primary pattern**
- **secondary pattern** if any
- **reading direction**
- **main flow**
- **semantic node types**
- **groups/panels**
- **required annotations**
- **evidence artifacts** if needed

Example:

- main claim: Agent skills extend model capability through a runtime environment
- primary pattern: Grouped Architecture
- secondary pattern: Callout Annotation
- reading direction: left to right
- main flow: configuration -> runtime execution
- groups: agent configuration, virtual machine, remote servers
- annotations: skill directories live in filesystem

---

## Non-Goals

Do not use this pattern library to create:
- dense UML-style enterprise diagrams
- BPMN-heavy process charts
- dashboard-like product graphics
- decorative posters with no explanatory structure
- deeply technical notation unless the user explicitly asks for it