---
name: conductor-status
description: Provides a comprehensive status overview of the Conductor project. Use when the user wants to know the current progress, active tasks, next steps, or overall health of the project tracks and plans.
metadata:
  version: "0.4.1"
---

# Conductor Status

## Overview

This skill acts as a project dashboard. It aggregates information from the project's Tracks Registry and individual Implementation Plans to provide a unified view of what's done, what's currently being worked on, and what's coming up next.

## When to Use

- When a user asks "What's the status?", "How are we doing?", or "Show me the project progress."
- To identify current blockers or the next actionable task.

## Workflow

1.  **Setup Check (Section 1.1):** Using the Universal File Resolution Protocol, resolve and verify the existence of the Tracks Registry, Product Definition, Tech Stack, and Workflow. If ANY file is missing, halt immediately and announce that Conductor is not set up.
2.  **Read Project Plan (Section 2.1):** Read the Tracks Registry and each track's Implementation Plan. Support both `- [ ] **Track:` (new) and `## [ ] Track:` (legacy) parsing formats.
3.  **Parse and Summarize (Section 2.2):** Parse content to identify statuses (COMPLETED, IN PROGRESS, PENDING). Count total phases and tasks.
4.  **Present Status Overview (Section 2.3):** Generate a structured report including Current Date/Time, Project Status, Current Phase and Task, Next Action Needed, Blockers, Phases (total), Tasks (total), and Progress (tasks_completed/tasks_total, percentage).

## Implementation Details

Refer to the following protocols for detailed procedural instructions:

- **Resolution Protocol:** [references/resolution-protocol.md](references/resolution-protocol.md) - How to find and verify Conductor artifacts.
- **Status Protocol:** [references/status-protocol.md](references/status-protocol.md) - The logic for setup verification, parsing plans, and generating the status report.

## Mandatory Constraints

- **Accurate Metrics:** Percentages MUST be based on actual task counts in the `plan.md` files.
- **Legacy Support:** Correctly parse both the new (`- [ ] **Track:`) and old (`## [ ] Track:`) track registry formats.
- **Clear Identification:** Explicitly state which track, phase, and task is currently "In Progress".
