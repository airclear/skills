---
name: conductor-implement
description: Executes the tasks defined in a Conductor track's plan. Use when the user wants to start or continue implementing a feature or bug fix. This skill manages the task lifecycle, adheres to the project's workflow, and synchronizes project documentation upon completion.
metadata:
  version: "0.3.1"
---

# Conductor Implement

## Overview

This skill is the "engine" of the Conductor framework. It takes the approved `plan.md` and works through it task-by-task, ensuring that every piece of code is tested, documented, and committed according to the project's standards.

## When to Use

- When a user says "Start implementing," "Do the next task," or "Continue working on track X."
- After a track has been initialized and planned.

## Workflow

1.  **Track Selection:** Identify the track to implement from the Tracks Registry. **Confirm selection using `ask_user`.**
2.  **Context Loading:** Load the track's spec and plan, and the project's workflow.
3.  **Task Execution:** Loop through tasks in the plan. **Defer to the project's `workflow.md`** as the single source of truth for implementation, testing, and committing.
4.  **Completion & Sync:** Once all tasks are done, synchronize the project-level documentation (`product.md`, `tech-stack.md`) with the new changes after user approval.
5.  **Track Cleanup:** Offer choices to **Review, Archive, Delete, or Skip** the completed track.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find Conductor artifacts.
- **Implementation Protocol:** [references/implementation-protocol.md](references/implementation-protocol.md) - The logic for track selection and execution.
- **Synchronization Protocol:** [references/synchronization.md](references/synchronization.md) - How to update project context after completion.

## Mandatory Constraints

- **Workflow is Law:** The `workflow.md` file in the project is the single source of truth for how tasks are implemented.
- **Interactive Validation:** Every human-in-the-loop interaction or confirmation mentioned in the workflow MUST use the `ask_user` tool.
- **Confirmation for Sync:** NEVER update `product.md`, `tech-stack.md`, or `product-guidelines.md` without explicit user approval of a proposed diff.
- **Success Validation:** Validate every tool call. Halt on failure.
