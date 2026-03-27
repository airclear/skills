---
name: conductor-setup
description: Scaffolds the project and sets up the Conductor environment for Context-Driven Development. Use when starting a new project or initializing the Conductor workflow in an existing (brownfield) project. This skill guides the user through project discovery, product definition, tech stack configuration, and initial track planning.
metadata:
  version: "0.4.1"
---

# Conductor Setup

## Overview

This skill transforms a standard repository into a **Conductor-managed project**. It establishes the "Source of Truth" by creating structured documentation for the product vision, technical standards, and development workflows.

## Workflow Overview

The setup process runs entirely within **Plan Mode** and follows these sequential phases:

1.  **Pre-Initialization Overview (Section 1.1):** Present a high-level overview of the setup steps to the user.
2.  **Project Audit (Section 1.2):** Check for existing Conductor artifacts and determine the resume point using a priority table.
3.  **Project Discovery (Section 2.0):** Determine if the project is New (Greenfield) or Existing (Brownfield). Resume from the audit target if applicable.
4.  **Product Documentation (Sections 2.1-2.3):** Collaborative creation of `product.md`, `product-guidelines.md`, and `tech-stack.md` with Interactive/Autogenerate mode selection.
5.  **Configuration (Sections 2.4-2.5):** Selection of code style guides and customization of `workflow.md` with Default/Customize options.
6.  **Finalization (Section 2.6):** Generate `conductor/index.md` and summarize all actions.
7.  **Track Generation (Sections 3.1-3.3):** Collect product requirements (Greenfield only), propose and create the first Track with `spec.md`, `plan.md`, `metadata.json`, and `index.md`.
8.  **Final Announcement (Section 3.4):** Commit all files and inform the user of next steps.

## State Management

Setup progress is tracked via **Project Audit** (Section 1.2). Instead of a state file, the agent checks for existing Conductor artifacts and uses a priority table to determine the resume point:

| Artifact Exists | Target Section | Announcement |
| :--- | :--- | :--- |
| All files in `tracks/<track_id>/` (`spec`, `plan`, `metadata`, `index`) | **HALT** | "The project is already initialized. Use `/conductor:newTrack` or `/conductor:implement`." |
| `index.md` (top-level) | **Section 3.0** | "Resuming setup: Scaffolding is complete. Next: generate the first track." |
| `workflow.md` | **Section 2.6** | "Resuming setup: Workflow is defined. Next: generate project index." |
| `code_styleguides/` | **Section 2.5** | "Resuming setup: Guides/Tech Stack configured. Next: define project workflow." |
| `tech-stack.md` | **Section 2.4** | "Resuming setup: Tech Stack defined. Next: select Code Styleguides." |
| `product-guidelines.md` | **Section 2.3** | "Resuming setup: Guidelines are complete. Next: define the Technology Stack." |
| `product.md` | **Section 2.2** | "Resuming setup: Product Guide is complete. Next: create Product Guidelines." |
| (None) | **Section 2.0** | (None) |

After determining the target section, the agent MUST proceed to Section 2.0 to establish Greenfield/Brownfield context before jumping to the target.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

### 1. Initialization and Resolution
- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find Conductor artifacts.
- **Project Discovery:** [references/project-discovery.md](references/project-discovery.md) - Brownfield vs Greenfield detection with improved indicators and git status checking.

### 2. Product Documentation
- **Product and Tech Stack:** [references/product-setup.md](references/product-setup.md) - Interactive/Autogenerate mode selection, question batching, and user confirmation loops.

### 3. Standards and Workflow
- **Configuration:** [references/configuration.md](references/configuration.md) - Code style guide selection via shell commands, workflow customization, and index generation.

### 4. Planning the First Track
- **Track Generation:** [references/track-generation.md](references/track-generation.md) - Product requirements collection, track proposal, artifact creation, and phase completion tasks.

## Mandatory Constraints

- **Plan Mode Execution:** The entire setup process runs within Plan Mode. The agent MUST call `enter_plan_mode` at the start. All file operations MUST use relative paths starting with `conductor/` (e.g., `conductor/product.md`). Do NOT use absolute paths. Redirection operators (`>`, `>>`) are NOT allowed in `run_shell_command` calls while in Plan Mode.
- **Self-Correction:** If a tool call fails (e.g., due to a policy restriction or path error), the agent MUST attempt to intelligently self-correct by reviewing the error message. If the failure is unrecoverable after a self-correction attempt, halt immediately and await user instructions.
- **Relative Paths:** In Plan Mode, all file write and replace operations MUST use relative paths starting with `conductor/`. Absolute paths will be blocked by Plan Mode security policies.
- **TDD Integration:** When generating `plan.md`, you MUST adhere to the TDD principles defined in `workflow.md` (Red/Green/Refactor tasks).
- **Universal File Resolution:** ALWAYS use the protocol in `references/resolution-protocol.md` to find or verify files.
- **Git Hygiene:** Setup concludes with a commit of all `conductor/` files.

## Assets

Templates used during setup are located in `assets/templates/`:
- `workflow.md`: The base development workflow.
- `code_styleguides/`: Language-specific style guides (Python, TypeScript, Go, etc.).

Policies for Plan Mode file access are located in `assets/policies/`:
- `conductor.toml`: Defines Plan Mode permissions for writing Conductor files and running authorized shell commands.
