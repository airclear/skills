---
name: conductor-implement
description: Executes the tasks defined in a specified track's plan. Use when the user wants to start or continue implementing a feature or bug fix. This skill manages the task lifecycle, adheres to the project's workflow, synchronizes project documentation upon completion, and offers track cleanup options.
metadata:
  version: "0.4.1"
---

# Conductor Implement

## Overview

This skill is the "engine" of the Conductor framework. It takes the approved `plan.md` and works through it task-by-task, ensuring that every piece of code is tested, documented, and committed according to the project's standards. After implementation, it synchronizes project-level documentation and offers cleanup options for the completed track.

## When to Use

- When a user says "Start implementing," "Do the next task," or "Continue working on track X."
- After a track has been initialized and planned.

## Workflow

1.  **Setup Check:** Verify the Conductor environment is properly set up (Product Definition, Tech Stack, Workflow must exist).
2.  **Track Selection:** Identify the track to implement from the Tracks Registry. Parse tracks using `---` separator. Support user-provided track name with exact matching. **Confirm selection using `ask_user`.**
3.  **Context Loading:** Load the track's spec and plan, and the project's workflow.
4.  **Task Execution:** Loop through tasks in the plan. Update status markers (`[ ]` → `[~]` → `[x]`). **Defer to the project's `workflow.md`** as the single source of truth for implementation, testing, and committing.
5.  **Documentation Synchronization:** Once all tasks are done, synchronize the project-level documentation (`product.md`, `tech-stack.md`, `product-guidelines.md`) with the new changes after user approval via `ask_user` with embedded diffs.
6.  **Track Cleanup:** Offer choices to **Review, Archive, Delete, or Skip** the completed track.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find Conductor artifacts.
- **Implementation Protocol:** [references/implementation-protocol.md](references/implementation-protocol.md) - The logic for track selection and execution.
- **Synchronization Protocol:** [references/synchronization.md](references/synchronization.md) - How to update project context after completion and offer track cleanup.

## Mandatory Constraints

- **Workflow is Law:** The `workflow.md` file in the project is the single source of truth for how tasks are implemented.
- **Interactive Validation:** Every human-in-the-loop interaction or confirmation mentioned in the workflow MUST use the `ask_user` tool.
- **Confirmation for Sync:** NEVER update `product.md`, `tech-stack.md`, or `product-guidelines.md` without explicit user approval of a proposed diff. Product Guidelines updates are strictly controlled and ONLY proposed for significant strategic shifts (rebranding, core identity changes).
- **Track Cleanup:** After synchronization, always offer the user cleanup options (Review/Archive/Delete/Skip) via `ask_user`. Delete requires a second confirmation.
- **Success Validation:** Validate every tool call. Halt on failure.
