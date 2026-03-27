---
name: conductor-newtrack
description: Initiates a new unit of work (Track) in a Conductor-managed project. Use when the user wants to start a new feature, fix a bug, or perform maintenance. This skill guides the user through interactive specification building and detailed implementation planning.
metadata:
  version: "0.4.1"
---

# Conductor New Track

## Overview

This skill facilitates the "Plan before you build" philosophy. It ensures that every task starts with clear requirements (`spec.md`) and a structured, actionable execution path (`plan.md`) that respects the project's established workflow. The entire track creation process runs within **Plan Mode**, providing a controlled environment for file creation and modification.

## When to Use

- When a user says "Start a new feature," "Fix a bug," or "I have a new task."
- Before any implementation code is written.

## Workflow

1.  **Setup Check:** Verify Conductor is set up and load project context (Product Definition, Tech Stack, Workflow).
2.  **Enter Plan Mode:** Call `enter_plan_mode` tool before proceeding. Get track description if not provided via args.
3.  **Interactive Spec:** Ask targeted questions to define success. **Batch up to 4 related questions** in a single `ask_user` tool call. Questions are classified as **Additive** (brainstorming/scope, `multiSelect: true`) or **Exclusive Choice** (foundational decisions, `multiSelect: false`). Draft `spec.md` and get user approval via embedded content review.
4.  **Plan Generation:** Create a phased to-do list based on the spec and the project's `workflow.md`. **Inject Phase Completion Tasks** if defined in the workflow. Draft `plan.md` and get user approval via embedded content review.
5.  **Artifact Scaffolding:** Create the track directory and initialize index, metadata, spec, and plan files. **Ensure unique short names** by checking existing tracks.
6.  **Exit Plan Mode:** Call `exit_plan_mode` tool with the path to the track's `index.md`.
7.  **Registry Registration:** Append the new track to the project's `tracks.md` in the format `- [ ] **Track: <Description>**` and commit the changes.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find and verify Conductor artifacts.
- **Track Planning Protocol:** [references/track-planning.md](references/track-planning.md) - The interactive process for generating specs and plans, including Plan Mode handling.

## Mandatory Constraints

- **Plan Mode Execution:** The entire newTrack process MUST run within Plan Mode. Enter via `enter_plan_mode` at the start and exit via `exit_plan_mode` after artifacts are created. Only `write_file`, `replace`, and authorized `run_shell_command` are permitted. All file paths MUST use `conductor/` relative paths. Redirection (`>` or `>>`) is strictly prohibited in `run_shell_command` during Plan Mode.
- **Question Classification:** Every question MUST be classified as either **Additive** (`multiSelect: true`, for brainstorming and scope definition) or **Exclusive Choice** (`multiSelect: false`, for foundational singular decisions). Each question MUST include: header (max 16 chars), type, multiSelect (for choice type), options with label and description, and placeholder (for text type).
- **Batch Questioning:** Streamline the process by batching up to 4 related questions in a single `ask_user` tool call.
- **Workflow Alignment:** Plans MUST include TDD tasks (Write Tests -> Implement) and Phase Completion meta-tasks if required by the project workflow.
- **Unique IDs:** Verify that the track's short name is unique before generating the full ID.
- **Git Hygiene:** Every new track creation MUST conclude with a commit of the `tracks.md` file.
