---
name: drawio-skill-nothing-design
description: This skill should be used when the user explicitly says "Nothing style", "Nothing design", "/nothing-design", or directly asks to use/apply the Nothing design system. NEVER trigger automatically for generic UI or design tasks. It provides guidance and templates for generating diagrams using the minimalist, industrial aesthetic of the Nothing design language.
license: MIT
---

# Nothing Design System (Minimalist & Industrial)

## Overview

Generate `.drawio` XML files and export to PNG/SVG/PDF/JPG locally using the native draw.io desktop app CLI.

**Supported formats:** PNG, SVG, PDF, JPG — no browser automation needed.

PNG, SVG, and PDF exports support `--embed-diagram` (`-e`) — the exported file contains the full diagram XML, so opening it in draw.io recovers the editable diagram. Use double extensions (`name.drawio.png`) to signal embedded XML.

## When to Use

**Explicit triggers:** user says "diagram", "visualize", "flowchart", "draw", "architecture diagram", "process flow", "ER diagram", "UML", "sequence diagram", "class diagram", "neural network", "model architecture"

**Proactive triggers:**
- Explaining a system with 3+ interacting components
- Describing a multi-step process or decision tree
- Comparing architectures or approaches side by side

**Skip when:** a simple list or table suffices, or user is in a quick Q&A flow

## Prerequisites

The draw.io desktop app must be installed and the CLI accessible:

```bash
# macOS (Homebrew — recommended)
brew install --cask drawio
draw.io --version

# macOS (full path if not in PATH)
/Applications/draw.io.app/Contents/MacOS/draw.io --version

# Windows
"C:\Program Files\draw.io\draw.io.exe" --version

# Linux
draw.io --version
```

Install draw.io desktop if missing:
- macOS: `brew install --cask drawio` or download from https://github.com/jgraph/drawio-desktop/releases
- Windows: download installer from https://github.com/jgraph/drawio-desktop/releases
- Linux: download `.deb`/`.rpm` from https://github.com/jgraph/drawio-desktop/releases

## Workflow

Before starting the workflow, assess whether the user's request is specific enough. If key details are missing, ask 1-3 focused questions:
- **Diagram type** — which preset? (ERD, UML, Sequence, Architecture, ML/DL, Flowchart, or general)
- **Output format** — PNG (default), SVG, PDF, or JPG?
- **Scope/fidelity** — how many components? Any specific technologies or labels?

Skip clarification if the request already specifies these details or is clearly simple (e.g., "draw a flowchart of X").

1. **Check deps** — verify `draw.io --version` succeeds; note platform for correct CLI path
2. **Plan** — identify shapes, relationships, layout (LR or TB), group by tier/layer
3. **Generate** — write `.drawio` XML file to disk (output dir same as user's working dir)
4. **Export draft** — run CLI to produce PNG for preview
5. **Self-check** — use the agent's built-in vision capability to read the exported PNG, catch obvious issues, auto-fix before showing user (requires a vision-enabled model such as Claude Sonnet/Opus)
6. **Review loop** — show image to user, collect feedback, apply targeted XML edits, re-export, repeat until approved
7. **Final export** — export approved version to all requested formats, report file paths

### Step 5: Self-Check

After exporting the draft PNG, use the agent's vision capability (e.g., Claude's image input) to read the image and check for these issues before showing the user. If the agent does not support vision, skip self-check and show the PNG directly:

| Check | What to look for | Auto-fix action |
|-------|-----------------|-----------------|
| Overlapping shapes | Two or more shapes stacked on top of each other | Shift shapes apart by ≥200px |
| Clipped labels | Text cut off at shape boundaries | Increase shape width/height to fit label |
| Missing connections | Arrows that don't visually connect to shapes | Verify `source`/`target` ids match existing cells |
| Off-canvas shapes | Shapes at negative coordinates or far from the main group | Move to positive coordinates near the cluster |
| Edge-shape overlap | An edge/arrow visually crosses through an unrelated shape | Add waypoints (`<Array as="points">`) to route around the shape, or increase spacing between shapes |
| Stacked edges | Multiple edges overlap each other on the same path | Distribute entry/exit points across the shape perimeter (use different exitX/entryX values) |

- Max **2 self-check rounds** — if issues remain after 2 fixes, show the user anyway
- Re-export after each fix and re-read the new PNG

### Step 6: Review Loop

After self-check, show the exported image and ask the user for feedback.

**Targeted edit rules** — for each type of feedback, apply the minimal XML change:

| User request | XML edit action |
|-------------|----------------|
| Change color of X | Find `mxCell` by `value` matching X, update `fillColor`/`strokeColor` in `style` |
| Add a new node | Append a new `mxCell` vertex with next available `id`, position near related nodes |
| Remove a node | Delete the `mxCell` vertex and any edges with matching `source`/`target` |
| Move shape X | Update `x`/`y` in the `mxGeometry` of the matching `mxCell` |
| Resize shape X | Update `width`/`height` in the `mxGeometry` of the matching `mxCell` |
| Add arrow from A to B | Append a new `mxCell` edge with `source`/`target` matching A and B ids |
| Change label text | Update the `value` attribute of the matching `mxCell` |
| Change layout direction | **Full regeneration** — rebuild XML with new orientation |

**Rules:**
- For single-element changes: edit existing XML in place — preserves layout tuning from prior iterations
- For layout-wide changes (e.g., swap LR↔TB, "start over"): regenerate full XML
- Overwrite the same `{name}.png` each iteration — do not create `v1`, `v2`, `v3` files
- After applying edits, re-export and show the updated image
- Loop continues until user says approved / done / LGTM
- **Safety valve:** after 5 iteration rounds, suggest the user open the `.drawio` file in draw.io desktop for fine-grained adjustments

### Step 7: Final Export

Once the user approves:
- Export to all requested formats (PNG, SVG, PDF, JPG) — default to PNG if not specified
- Report file paths for both the `.drawio` source file and exported image(s)
- **Auto-launch:** offer to open the `.drawio` file in draw.io desktop for fine-tuning — `open diagram.drawio` (macOS), `xdg-open` (Linux), `start` (Windows)
- Confirm files are saved and ready to use

## Draw.io XML Structure

### File skeleton

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Page-1">
    <mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- user shapes start at id="2" -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Rules:**
- `id="0"` and `id="1"` are required root cells — never omit them
- User shapes start at `id="2"` and increment sequentially
- All shapes have `parent="1"` (unless inside a container — then use container's id)
- All text uses `html=1` in style for proper rendering
- **Never use `--` inside XML comments** — it's illegal per XML spec and causes parse errors
- Escape special characters in attribute values: `&amp;`, `&lt;`, `&gt;`, `&quot;`
- **Multi-line text in labels:** use `&#xa;` for line breaks inside `value` attributes (not literal `\n`). Example: `value="Line 1&#xa;Line 2"`

### Shape types (vertex)

| Style keyword | Use for |
|--------------|---------|
| `rounded=0` | plain rectangle (default) |
| `rounded=1` | rounded rectangle — services, modules |
| `ellipse;` | circles/ovals — start/end, databases |
| `rhombus;` | diamond — decision points |
| `shape=mxgraph.aws4.resourceIcon;` | AWS icons |
| `shape=cylinder3;` | cylinder — databases |
| `swimlane;` | group/container with title bar |

### Required properties

```xml
<!-- Rectangle / rounded box -->
<mxCell id="2" value="Label" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="60" as="geometry" />
</mxCell>

<!-- Cylinder (database) -->
<mxCell id="3" value="DB" style="shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
  <mxGeometry x="350" y="100" width="120" height="80" as="geometry" />
</mxCell>

<!-- Diamond (decision) -->
<mxCell id="4" value="Check?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
  <mxGeometry x="100" y="220" width="160" height="80" as="geometry" />
</mxCell>
```

### Containers and groups

For architecture diagrams with nested elements, use draw.io's parent-child containment — do **not** just place shapes on top of larger shapes.

| Type | Style | When to use |
|------|-------|-------------|
| **Group** (invisible) | `group;pointerEvents=0;` | No visual border needed, container has no connections |
| **Swimlane** (titled) | `swimlane;startSize=30;` | Container needs a visible title bar, or container itself has connections |
| **Custom container** | Add `container=1;pointerEvents=0;` to any shape | Any shape acting as a container without its own connections |

**Key rules:**
- Add `pointerEvents=0;` to container styles that should not capture connections between children
- Children set `parent="containerId"` and use coordinates **relative to the container**

```xml
<!-- Swimlane container -->
<mxCell id="svc1" value="User Service" style="swimlane;startSize=30;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
<!-- Child inside container — coordinates relative to parent -->
<mxCell id="api1" value="REST API" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="svc1">
  <mxGeometry x="20" y="40" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="db1" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;" vertex="1" parent="svc1">
  <mxGeometry x="160" y="40" width="120" height="60" as="geometry"/>
</mxCell>
```

### Connector (edge)

**CRITICAL:** Every edge `mxCell` must contain a `<mxGeometry relative="1" as="geometry" />` child element. Self-closing edge cells (`<mxCell ... edge="1" ... />`) are **invalid** and will not render. Always use the expanded form.

```xml
<!-- Directed arrow — always include rounded, orthogonalLoop, jettySize for clean routing -->
<mxCell id="10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="2" target="3">
  <mxGeometry relative="1" as="geometry" />
</mxCell>

<!-- Arrow with label + explicit entry/exit points to control direction -->
<mxCell id="11" value="HTTP/REST" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="2" target="4">
  <mxGeometry relative="1" as="geometry" />
</mxCell>

<!-- Arrow with waypoints — use when edge must route around other shapes -->
<mxCell id="12" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="3" target="5">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="500" y="50" />
    </Array>
  </mxGeometry>
</mxCell>
```

**Edge style rules:**
- **Animated connectors:** add `flowAnimation=1;` to any edge style to show a moving dot animation along the arrow. Works in SVG export and draw.io desktop — ideal for data-flow and pipeline diagrams. Example: `style="edgeStyle=orthogonalEdgeStyle;flowAnimation=1;rounded=1;..."`
- **Always** include `rounded=1;orthogonalLoop=1;jettySize=auto` — these enable smart routing that avoids overlaps
- **Label Background:** always add `labelBackgroundColor=#FFFFFF;` to edges with labels to prevent the connection line from crossing through the text.
- **Stroke Width:** use `strokeWidth=1.5` for standard flows and `strokeWidth=2` for primary/critical paths to create visual hierarchy.
- Pin `exitX/exitY/entryX/entryY` on every edge when a node has 2+ connections — distributes lines across the shape perimeter
- Add `<Array as="points">` waypoints when an edge must detour around an intermediate shape
- **Leave room for arrowheads:** the final straight segment between the last bend and the target shape must be ≥20px long. If too short, the arrowhead overlaps the bend and looks broken. Fix by increasing node spacing or adding explicit waypoints

### Distributing connections on a shape

When multiple edges connect to the same shape, assign different entry/exit points to prevent stacking:

| Position | exitX/entryX | exitY/entryY | Use when |
|----------|-------------|-------------|----------|
| Top center | 0.5 | 0 | connecting to node above |
| Top-left | 0.25 | 0 | 2nd connection from top |
| Top-right | 0.75 | 0 | 3rd connection from top |
| Right center | 1 | 0.5 | connecting to node on right |
| Bottom center | 0.5 | 1 | connecting to node below |
| Left center | 0 | 0.5 | connecting to node on left |

**Rule:** if a shape has N connections on one side, space them evenly (e.g., 3 connections on bottom → exitX = 0.25, 0.5, 0.75)

### Color palette (fillColor / strokeColor)

| Color name | fillColor | strokeColor | Use for |
|-----------|-----------|-------------|---------|
| Zone Gray | `#F8F9FA` | `#D5D5D5` | Background layers/swimlanes (dashed=1; arcSize=2) |
| Active Blue | `#DAE8FC` | `#6C8EBF` | Core application/service nodes (shadow=1) |
| Pure White | `#FFFFFF` | `#3788E4` | Premium card nodes (strokeWidth: 1 or 2) |
| Success Green| `#D5E8D4` | `#82B366` | Databases, validated states, storage |
| Error Red | `#F8CECC` | `#B85450` | Alerts, anomaly flows, external risks |
| Neutral Gray | `#F5F5F5` | `#B3B3B3` | External systems, legacy components |


### Industrial Premium Styles

To achieve an "industrial-grade" architectural look, apply these refined patterns:

| Feature | Style Attribute / Pattern | Effect |
|---------|---------------------------|--------|
| **Zone Background** | `fillColor=#F8F9FA;dashed=1;arcSize=2;` | Subtle, non-distracting logical grouping |
| **Zone Title** | `fontSize=18;fontStyle=1;fontColor=#333333;` | High-level navigation (place at top-left of zone) |
| **Premium Card** | `rounded=1;arcSize=12;shadow=1;fillColor=#FFFFFF;` | Modern "floating" UI feel |
| **Typography** | `value="&lt;b&gt;TITLE&lt;/b&gt;&lt;br&gt;&lt;font size=&quot;1&quot; color=&quot;#666666&quot;&gt;(Desc)&lt;/font&gt;"` | Clear information hierarchy |
| **Edge Masking** | `labelBackgroundColor=#FFFFFF;` | **Mandatory** for edge labels to prevent line-text overlap |
| **Semantic Flow** | `strokeColor=#3788E4;strokeWidth=1.5;` | Use color-coded lines (Blue: Logic, Green: Data, Red: Alert) |

### Layout tips

**Spacing — scale with complexity:**

| Diagram complexity | Nodes | Horizontal gap | Vertical gap |
|-------------------|-------|----------------|--------------|
| Simple | ≤5 | 200px | 150px |
| Medium | 6–10 | 280px | 200px |
| Complex | >10 | 350px | 250px |

**Routing corridors:** between shape rows/columns, leave an extra ~80px empty corridor where edges can route without crossing shapes. Never place a shape in a gap that edges need to traverse.

**Grid alignment:** snap all `x`, `y`, `width`, `height` values to **multiples of 10** — this ensures shapes align cleanly on draw.io's default grid and makes manual editing easier.

**General rules:**
- Plan a grid before assigning x/y coordinates — sketch node positions on paper/mentally first
- Group related nodes in the same horizontal or vertical band
- Use `swimlane` cells for logical grouping with visible borders
- Place heavily-connected "hub" nodes centrally so edges radiate outward instead of crossing
- To force straight vertical connections, pin entry/exit points explicitly on edges:
  `exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0`
- Always center-align a child node under its parent (same center x) to avoid diagonal routing
- **Event bus pattern**: place Kafka/bus nodes in the **center of the service row**, not below — services on either side can reach it with short horizontal arrows (`exitX=1` left side, `exitX=0` right side), eliminating all line crossings
- Horizontal connections (`exitX=1` or `exitX=0`) never cross vertical nodes in the same row; use them for peer-to-peer and publish connections

**Avoiding edge-shape overlap:**
- Before finalizing coordinates, trace each edge path mentally — if it must cross an unrelated shape, either move the shape or add waypoints
- For tree/hierarchical layouts: assign nodes to layers (rows), connect only between adjacent layers to minimize crossings
- For star/hub layouts: place the hub center, satellites around it — edges stay short and radial
- When an edge must span multiple rows/columns, route it along the outer corridor, not through the middle of the diagram

## Export

### Commands

```bash
# macOS — Homebrew (draw.io in PATH)
draw.io -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# macOS — full path (if not in PATH)
/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# Windows
"C:\Program Files\draw.io\draw.io.exe" -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# Linux (headless — requires xvfb-run)
xvfb-run -a draw.io -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# SVG export
draw.io -x -f svg -o diagram.svg input.drawio

# PDF export
draw.io -x -f pdf -o diagram.pdf input.drawio
```

**Key flags:**
- `-x` — export mode (required)
- `-f` — format: `png`, `svg`, `pdf`, `jpg`
- `-e` — embed diagram XML in output (PNG, SVG, PDF only) — exported file remains editable in draw.io
- `-s` — scale: `1`, `2`, `3` (2 recommended for PNG)
- `-o` — output file path (use `.drawio.png` double extension when embedding)
- `-b` — border width around diagram (default: 0, recommend 10)
- `-t` — transparent background (PNG only)
- `--page-index 0` — export specific page (default: all)

### Browser fallback (no CLI needed)

When the draw.io desktop CLI is unavailable, generate a browser-editable URL by deflate-compressing and base64-encoding the XML:

```bash
# Encode .drawio XML into a diagrams.net URL
python3 -c "
import zlib, base64, urllib.parse, sys
xml = open(sys.argv[1]).read()
compressed = zlib.compress(xml.encode('utf-8'), 9)
encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
print('https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&edit=_blank#R' + urllib.parse.quote(encoded, safe=''))
" input.drawio
```

This produces a client-side URL that opens the diagram in the browser for viewing and editing. No data is uploaded to any server — the entire diagram XML is encoded in the URL fragment (after `#`), which is never sent to the server. Useful when the user cannot install the desktop app.

### Fallback chain

When tools are unavailable, degrade gracefully:

| Scenario | Behavior |
|----------|----------|
| draw.io CLI missing, Python available | Use browser fallback (diagrams.net URL) |
| draw.io CLI missing, Python missing | Generate `.drawio` XML only; instruct user to open in draw.io desktop or diagrams.net manually |
| Vision unavailable for self-check | Skip self-check (step 5); proceed directly to showing user the exported PNG |
| Export fails (Chromium/display issues) | On Linux, retry with `xvfb-run -a`; if still failing, deliver `.drawio` XML and suggest manual export |

### Checking if draw.io is in PATH

```bash
# Try short command first
if command -v draw.io &>/dev/null; then
  DRAWIO="draw.io"
elif [ -f "/Applications/draw.io.app/Contents/MacOS/draw.io" ]; then
  DRAWIO="/Applications/draw.io.app/Contents/MacOS/draw.io"
else
  echo "draw.io not found — install from https://github.com/jgraph/drawio-desktop/releases"
fi
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Missing `id="0"` and `id="1"` root cells | Always include both at the top of `<root>` |
| Shapes not connected | `source` and `target` on edge must match existing shape `id` values |
| Export command not found on macOS | Try full path `/Applications/draw.io.app/Contents/MacOS/draw.io` |
| Linux: blank/error output headlessly | Prefix command with `xvfb-run -a` |
| PDF export fails | Ensure Chromium is available (draw.io bundles it on desktop) |
| Background color wrong in CLI export | Known CLI bug; add `--transparent` flag or set background via style |
| Overlapping shapes | Scale spacing with complexity (200–350px); leave routing corridors |
| Edges crossing through shapes | Add waypoints, distribute entry/exit points, or increase spacing |
| Special characters in `value` | Use XML entities: `&amp;` `&lt;` `&gt;` `&quot;` |
| Iteration loop never ends | After 5 rounds, suggest user open .drawio in draw.io desktop for fine-tuning |
| Self-closing edge `mxCell` | Always use expanded form with `<mxGeometry>` child — self-closing edges won't render |
| `--` inside XML comments | Illegal per XML spec — use single hyphens or rephrase |
| Arrowhead overlaps bend | Final edge segment before target must be ≥20px — increase spacing or add waypoints |
| Literal `\n` in label text | Use `&#xa;` for line breaks in `value` attributes |

## Diagram Type Presets

When the user requests a specific diagram type, apply the matching preset below for shapes, styles, and layout conventions.

### ERD (Entity-Relationship Diagram)

| Element | Style | Notes |
|---------|-------|-------|
| Table | `shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;strokeColor=#6c8ebf;fillColor=#dae8fc;` | Each table is a container |
| Row (column) | `shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontSize=12;` | Child of table, `parent=tableId` |
| PK column | Bold text: `fontStyle=1` on the row | Mark with `PK` prefix or key icon |
| FK relationship | Dashed edge: `dashed=1;endArrow=ERmandOne;startArrow=ERmandOne;` | Use ER notation arrows |
| Layout | TB, tables spaced 300px apart | Group related tables vertically |

### UML Class Diagram

| Element | Style | Notes |
|---------|-------|-------|
| Class box | `swimlane;fontStyle=1;align=center;startSize=26;html=1;` | 3-section: title / attributes / methods |
| Separator | `line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;` | Between sections |
| Inheritance | `endArrow=block;endFill=0;` | Hollow triangle arrow |
| Implementation | `endArrow=block;endFill=0;dashed=1;` | Dashed + hollow triangle |
| Composition | `endArrow=diamondThin;endFill=1;` | Filled diamond |
| Aggregation | `endArrow=diamondThin;endFill=0;` | Hollow diamond |
| Layout | TB, classes 250px apart | Interfaces above implementations |

### Sequence Diagram

| Element | Style | Notes |
|---------|-------|-------|
| Actor/Object | `shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;` | Lifeline with dashed vertical line |
| Sync message | `html=1;verticalAlign=bottom;endArrow=block;` | Solid line, filled arrowhead |
| Async message | `html=1;verticalAlign=bottom;endArrow=open;dashed=1;` | Dashed line, open arrowhead |
| Return message | `html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#999999;` | Grey dashed |
| Activation box | `shape=umlFrame;whiteSpace=wrap;` on the lifeline | Narrow rectangle on lifeline |
| Layout | LR, lifelines spaced 200px apart | Time flows top to bottom |

### Architecture Diagram (Industrial Premium)

| Element | Style | Notes |
|---------|-------|-------|
| Layer/Tier | `rounded=1;dashed=1;fillColor=#F8F9FA;strokeColor=#D5D5D5;arcSize=2;` | Use as large background boxes for layers |
| Zone Title | `text;strokeColor=none;fillColor=none;fontSize=18;fontStyle=1;` | Place inside zone at (x+20, y+10) |
| Service Card | `rounded=1;fillColor=#FFFFFF;strokeColor=#3788E4;shadow=1;arcSize=12;strokeWidth=1.5;` | The "Industrial" standard for services |
| Database | `shape=cylinder3;fillColor=#D5E8D4;strokeColor=#82B366;shadow=1;` | Solid green accent for persistence |
| Data Flow | `edgeStyle=orthogonalEdgeStyle;rounded=1;strokeWidth=2;strokeColor=#3788E4;` | Bold blue for primary flows |
| External Sys | `rounded=1;dashed=1;fillColor=#F5F5F5;strokeColor=#B3B3B3;` | Desaturated for third-party systems |

### Nothing Style (Minimalist & Industrial)

Inspired by Swiss design and industrial craft. Use when the user requests "Nothing style", "minimalist", or "monochrome industrial".

| Element | Style | Notes |
|---------|-------|-------|
| Node Card | `rounded=0;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1;shadow=0;` | Sharp edges, no shadows, flat surfaces |
| Typography | `fontFamily=Courier New;fontSize=12;fontColor=#000000;` | Monospaced technical look |
| Accent Red | `fillColor=#D71921;fontColor=#FFFFFF;` | **ONLY** for critical alerts or interrupts |
| Connectors | `endArrow=none;strokeColor=#000000;strokeWidth=1;` | Minimalist paths without bulky arrowheads |
| Background | `background=#FFFFFF;` | Pure white or OLED black (`#000000`) |

### ML / Deep Learning Model Diagram

For neural network architecture diagrams — ideal for papers targeting NeurIPS, ICML, ICLR.

| Element | Style | Notes |
|---------|-------|-------|
| Layer block | `rounded=1;whiteSpace=wrap;html=1;` + type color | Main building block |
| Input/Output | `fillColor=#d5e8d4;strokeColor=#82b366;` | Green |
| Conv / Pooling | `fillColor=#dae8fc;strokeColor=#6c8ebf;` | Blue |
| Attention / Transformer | `fillColor=#e1d5e7;strokeColor=#9673a6;` | Purple |
| RNN / LSTM / GRU | `fillColor=#fff2cc;strokeColor=#d6b656;` | Yellow |
| FC / Linear | `fillColor=#ffe6cc;strokeColor=#d79b00;` | Orange |
| Loss / Activation | `fillColor=#f8cecc;strokeColor=#b85450;` | Red/Pink |
| Skip connection | `dashed=1;endArrow=block;curved=1;` | Dashed curved arrow |
| Tensor shape label | Add shape annotation as secondary label: `value="Conv2D&#xa;(B, 64, 32, 32)"` | Use `&#xa;` for multi-line |
| Layout | TB (data flows top→bottom), layers 150px apart | Group encoder/decoder as swimlanes |

**Tensor shape convention:** annotate each layer with input/output tensor dimensions in `(B, C, H, W)` or `(B, T, D)` format. Place dimensions as the second line of the label using `&#xa;`.

### Flowchart (enhanced)

| Element | Style | Notes |
|---------|-------|-------|
| Start/End | `ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;` | Green oval |
| Process | `rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;` | Blue rectangle |
| Decision | `rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;` | Yellow diamond |
| I/O | `shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;` | Orange parallelogram |
| Subprocess | `rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;` + double border | Purple |
| Yes/No labels | `value="Yes"` / `value="No"` on decision edges | Always label decision branches |
| Layout | TB, 200px vertical gap | Decisions branch LR, merge back to center |
