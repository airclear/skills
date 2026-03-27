---
name: conductor-revert
description: Reverts logical units of work (Tracks, Phases, or Tasks) by analyzing git history and synchronizing the Conductor plans. Use when a user wants to undo specific changes and ensure the project's documentation reflects the rolled-back state.
metadata:
  version: "0.4.1"
---

# Conductor Revert

## Overview

This skill is a Git-aware assistant. Unlike a standard `git revert`, it understands the relationship between implementation commits and the Conductor documentation. It ensures that when code is reverted, the corresponding `plan.md` and `tracks.md` files are also reset to their previous states.

It is designed to handle common non-linear Git histories, such as rewritten commits (from rebase/squash) and merge commits, with robust "Ghost" commit detection and plan-update commit association.

## When to Use

- When a user says "Undo that task," "Revert the last phase," or "I want to delete this track and its changes."
- To cleanly roll back a feature that isn't working as expected.

## Workflow

The revert process follows 4 phases:

### Phase 1: Interactive Target Selection & Confirmation

Two interaction paths:

- **Path A (Direct Confirmation):** When the user provides a specific target (e.g., track ID). Confirm the selection and proceed.
- **Path B (Guided Selection Menu):** When no target is provided. Scan all plans for in-progress items (top 3), or fallback to the 3 most recently completed items. Present a **unified hierarchical menu** with a max of 4 choices plus an automatically-added "Other" option.

### Phase 2: Git Reconciliation & Verification

Map the logical Conductor item to specific Git commit SHAs:

- **Implementation Commits** - primary SHAs from `plan.md`.
- **Ghost Commits** - if a SHA is missing, search for similar commit messages.
- **Plan-Update Commits** - `conductor(plan):` commits after each implementation commit.
- **Track Creation Commit** - only for full Track reverts; supports both new and legacy Track Registry formats.

### Phase 3: Final Execution Plan Confirmation

Present a detailed summary of the revert plan including target, commit count, and each commit with its message. Offer Approve/Revise choice.

### Phase 4: Execution & Verification

Execute reverts in **reverse chronological order**, handle conflicts, verify plan state, and announce completion.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find Conductor artifacts.
- **Revert Protocol:** [references/revert-protocol.md](references/revert-protocol.md) - The logic for mapping Conductor items to Git history and executing reverts.

## Mandatory Constraints

- **Double Confirmation:** Always confirm the target selection AND the final execution plan before running `git revert`.
- **Reverse Order:** Reverts MUST be performed in reverse chronological order.
- **Plan Sync:** The final step MUST be verifying that `plan.md` or `tracks.md` reflects the reverted state.
- **Tool Call Validation:** Every tool call must be validated for success. If any fails, halt immediately and await instructions.
