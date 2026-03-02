---
name: conductor-review
description: Acts as a Principal Software Engineer to review completed or in-progress work against project standards, tech stack choices, and the implementation plan. Use when the user wants a quality check on their code or before finalizing a track.
metadata:
  version: "0.3.1"
---

# Conductor Review

## Overview

This skill provides a meticulous, first-principles code review. It compares implementation diffs against the "Law" (Style Guides), the "Identity" (Product Guidelines), and the "Mission" (Spec and Plan). It identifies critical bugs, safety risks, and architectural deviations.

## When to Use

- When a user says "Review my changes," "Is this track ready?", or "Run a code review."
- Before archiving or deleting a completed track.

## Workflow

1.  **Scope Selection:** Identify the track or changes to review. **Confirm selection using `ask_user`.**
2.  **Context Loading:** Retrieve guidelines, style guides, and the track's plan. **Load all style guides in `conductor/code_styleguides/`.**
3.  **Meticulous Analysis (Smart Chunking):** Perform a deep dive into the diff. **For large changes (> 300 lines), use Iterative Review Mode** after user confirmation.
4.  **Automated Testing:** Run the project's test suite and report results.
5.  **Reporting:** Generate a structured Review Report with severity-ranked findings.
6.  **Decision Phase:** Offer choices to **Apply Fixes, Manual Fix, or Complete Track.**
7.  **Commit & Track:** Automatically commit review fixes and **update the `plan.md`** to record review tasks and SHAs.
8.  **Track Cleanup:** Offer choices to **Archive, Delete, or Skip** the reviewed track.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find Conductor artifacts.
- **Review Protocol:** [references/review-protocol.md](references/review-protocol.md) - The logic for deep analysis, report generation, and automated fixing.

## Mandatory Constraints

- **Style is Law:** Violations of `conductor/code_styleguides/*.md` are HIGH severity.
- **Iterative Review Confirmation:** You MUST use `ask_user` before starting a large (> 300 lines) review.
- **Automated Verification:** ALWAYS attempt to run existing tests to verify correctness.
- **Plan Integrity:** If fixes are applied, the `plan.md` MUST be updated to record the review-related tasks and commits.
