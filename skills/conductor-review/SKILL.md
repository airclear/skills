---
name: conductor-review
description: Acts as a Principal Software Engineer and Code Review Architect to review completed or in-progress work against project standards, style guides, and the implementation plan. Use when the user wants a quality check on their code or before finalizing a track.
metadata:
  version: "0.4.1"
---

# Conductor Review

## Overview

This skill provides a meticulous, first-principles code review from the perspective of a Principal Software Engineer. It compares implementation diffs against the "Law" (Code Style Guides), the "Identity" (Product Guidelines), and the "Mission" (Spec and Plan). It identifies critical bugs, safety risks, security issues, and architectural deviations with structured, severity-ranked reporting.

## When to Use

- When a user says "Review my changes," "Is this track ready?", or "Run a code review."
- Before archiving or deleting a completed track.

## Workflow

1.  **Setup Check:** Verify the Conductor environment is properly set up before proceeding.
2.  **Scope Selection:** Identify the track or changes to review using user arguments or auto-detection. **Confirm selection using `ask_user`.**
3.  **Context Loading:** Retrieve guidelines, style guides, and the track's plan. **CRITICAL: Check and load all style guides in `conductor/code_styleguides/`.**
4.  **Smart Chunking Analysis:** Load and analyze changes with volume-aware strategy. **For large changes (> 300 lines), use Iterative Review Mode** after user confirmation.
5.  **Deep Verification:** Perform Intent Verification, Style Compliance, Correctness & Safety (including security scan), and automated Testing.
6.  **Structured Reporting:** Generate a Review Report with Summary, Verification Checks, and severity-ranked Findings with diff-based suggestions.
7.  **Review Decision:** Determine recommendation and offer choices to **Apply Fixes, Manual Fix, or Complete Track.**
8.  **Commit Review Changes:** Commit review fixes, update `plan.md` with Review Fixes phase, and record commit SHAs.
9.  **Track Cleanup:** Offer choices to **Archive, Delete (with confirmation), or Skip** the reviewed track.

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find Conductor artifacts.
- **Review Protocol:** [references/review-protocol.md](references/review-protocol.md) - The logic for scope identification, smart chunking, deep analysis, report generation, commit tracking, and track cleanup.

## Mandatory Constraints

- **Style is Law:** Violations of `conductor/code_styleguides/*.md` are HIGH severity.
- **Iterative Review Confirmation:** You MUST use `ask_user` before starting a large (> 300 lines) review.
- **Automated Verification:** ALWAYS attempt to run existing tests to verify correctness.
- **Plan Integrity:** If fixes are applied, the `plan.md` MUST be updated to record the review-related tasks and commits.
- **Tool Call Validation:** Validate every tool call. Halt on failure.
