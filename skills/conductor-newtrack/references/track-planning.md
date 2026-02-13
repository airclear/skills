# Track Planning Protocol

## 1. Initialization
- **Project Context:** Read Product Definition, Tech Stack, and Workflow using the Resolution Protocol.
- **Track Description:** Get from user if not provided.
- **Infer Type:** Determine if it's a "Feature" or "Other" (Bug, Chore, etc.).

## 2. Interactive Specification (`spec.md`)
- **Sequential Questions:** Ask 3-5 (Feature) or 2-3 (Other) context-aware questions.
- **Question Types:** Additive (Select all that apply) or Exclusive Choice.
- **Drafting:** Include Overview, Functional/Non-Functional Requirements, Acceptance Criteria, and Out of Scope.
- **Confirmation:** Get user approval before proceeding.

## 3. Interactive Plan (`plan.md`)
- **Generation:** Create a hierarchical list of Phases, Tasks, and Sub-tasks.
- **Workflow Compliance:** Adhere to `workflow.md` (e.g., TDD tasks).
- **Status Markers:** Use `[ ]` for all items.
- **Phase Completion:** Append: `- [ ] Task: Conductor - User Manual Verification '<Phase Name>' (Protocol in workflow.md)` to each phase.
- **Confirmation:** Get user approval.

## 4. Artifact Creation
1. **Duplicate Check:** Verify the track name doesn't already exist in the Tracks Directory.
2. **Generate ID:** `shortname_YYYYMMDD`.
3. **Directory:** Create `conductor/tracks/<track_id>/`.
4. **Metadata:** Create `metadata.json` with current timestamp and status "new".
5. **Write Files:** `spec.md`, `plan.md`, and `index.md`.
6. **Registry Update:** Append the new track section to `conductor/tracks.md`.
7. **Commit:** `git add conductor/tracks.md` and commit with `chore(conductor): Add new track '<description>'`.
