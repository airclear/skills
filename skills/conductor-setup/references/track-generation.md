# Initial Track Generation Protocol

## 1. Generate Product Requirements (Greenfield only)
- Ask up to 5 questions (User stories, Functional requirements).
- Gather information for subsequent generation.

## 2. Propose Initial Track
- Analyze project context and requirements.
- Generate a single track title (e.g., MVP feature).
- Get user approval.

## 3. Convert Track into Artifacts
1. **Initialize `conductor/tracks.md`**:
    ```markdown
    # Project Tracks
    ---
    - [ ] **Track: <Description>**
      *Link: [./tracks/<track_id>/](./tracks/<track_id>/)*
    ```
2. **Generate Spec and Plan**:
    - `spec.md`: Detailed specification.
    - `plan.md`: Phased plan following `workflow.md` (e.g., TDD tasks).
    - **Meta-tasks:** Inject phase completion verification tasks if defined in workflow.
3. **Create Directory Structure**:
    - `conductor/tracks/<track_id>/`
    - `metadata.json`, `spec.md`, `plan.md`, `index.md`.
4. **Commit and Finish**:
    - `git add conductor/`
    - `git commit -m "conductor(setup): Add conductor setup files"`
