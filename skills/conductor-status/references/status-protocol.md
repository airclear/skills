# Status Overview Protocol

## 1. Context Verification
- Use the **Resolution Protocol** to verify the existence of:
    - Tracks Registry
    - Product Definition
    - Tech Stack
    - Workflow

## 2. Information Retrieval
1.  **Read Tracks Registry:** Resolve and read `conductor/tracks.md`.
2.  **Identify Tracks:** Parse the registry for all registered tracks (new format `- [ ] **Track:` or legacy `## [ ] Track:`).
3.  **Read Individual Plans:** For each track, resolve and read its `plan.md` via the track's `index.md`.

## 3. Analysis and Summarization
1.  **Parse Plans:**
    - Count total phases and tasks across all tracks.
    - Identify status of each task (Completed `[x]`, In Progress `[~]`, Pending `[ ]`).
2.  **Generate Report:**
    - **Timestamp:** Current date/time.
    - **Overall Status:** On Track, Behind Schedule, or Blocked.
    - **Active Work:** Identify the specific phase and task currently marked as `[~]`.
    - **Next Step:** Identify the next `[ ]` task.
    - **Metrics:** `tasks_completed / tasks_total (percentage%)`.
    - **Blockers:** List any items explicitly marked as blockers.

## 4. Presentation
Present the summary to the user in a clear, structured Markdown format.
