# Implementation Protocol

## 1. Track Selection
- **Registry Check:** Read and parse `conductor/tracks.md`.
- **Match Track:**
    - If user provided a name: Find exact or unique match.
    - If no name: Select the first track NOT marked as `[x] Completed`.
- **Status Update:** Change track status to `[~] In Progress` in the Tracks Registry.

## 2. Execution Loop
- **Load Context:** Read Track Spec, Plan, and Project Workflow using the Resolution Protocol.
- **Iterate Tasks:** Loop through each task in `plan.md`.
- **Workflow Deferral:** For each task, execute the "Task Workflow" defined in `conductor/workflow.md`. This is the single source of truth for implementation, testing, and committing.

## 3. Finalization
- **Completion Update:** Change track status to `[x] Completed` in the Tracks Registry.
- **Commit:** `git add conductor/tracks.md` and commit with `chore(conductor): Mark track '<description>' as complete`.

## 4. Track Cleanup (Optional)
Offer the user options after implementation:
- **Review:** Run `/conductor:review`.
- **Archive:** Move folder to `conductor/archive/` and remove from registry.
- **Delete:** Irreversibly delete the track folder (requires confirmation).
- **Skip:** Do nothing.
