---
name: conductor-newtrack
description: Initiates a new unit of work (Track) in a Conductor-managed project. Use when the user wants to start a new feature, fix a bug, or perform maintenance. This skill guides the user through interactive specification building and detailed implementation planning.
metadata:
  version: "0.3.1"
---

# Conductor New Track

## Overview

This skill facilitates the "Plan before you build" philosophy. It ensures that every task starts with clear requirements (`spec.md`) and a structured, actionable execution path (`plan.md`) that respects the project's established workflow.

## When to Use

- When a user says "Start a new feature," "Fix a bug," or "I have a new task."
- Before any implementation code is written.

## Workflow

1.  **Context Check:** Verify Conductor is set up and load project context.
2.  **Interactive Spec:** Ask targeted questions to define success. **Batch up to 4 related questions in a single tool call.**
3.  **Plan Generation:** Create a phased to-do list based on the spec and the project's `workflow.md`. **Inject Phase Completion Tasks** if defined in the workflow.
4.  **Artifact Scaffolding:** Create the track directory and initialize index, metadata, spec, and plan files. **Ensure unique short names** and create an `index.md`.
5.  **Registry Registration:** Add the track to the project's `tracks.md` and commit the changes.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find and verify Conductor artifacts.
- **Track Planning Protocol:** [references/track-planning.md](references/track-planning.md) - The interactive process for generating specs and plans.

## Mandatory Constraints

- **Batch Questioning:** Streamline the process by batching up to 4 questions in a single `ask_user` tool call.
- **Workflow Alignment:** Plans MUST include TDD tasks (Write Tests -> Implement) and Phase Completion meta-tasks if required by the project workflow.
- **Unique IDs:** Verify that the track's short name is unique before generating the full ID.
- **Git Hygiene:** Every new track creation MUST conclude with a commit of the `tracks.md` file.
