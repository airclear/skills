# Revert Protocol (Git-Aware)

## 0. Setup Check

**PROTOCOL: Verify that the Conductor environment is properly set up.**

1.  **Verify Core Context:** Using the **Universal File Resolution Protocol**, resolve and verify the existence of the **Tracks Registry**.
2.  **Verify Track Exists:** Check if the **Tracks Registry** is not empty.
3.  **Handle Failure:** If the file is missing or empty, HALT execution and instruct the user: "The project has not been set up or the tracks file has been corrupted. Please run `/conductor:setup` to set up the plan, or restore the tracks file."

---

## Phase 1: Interactive Target Selection & Confirmation

**GOAL: Guide the user to clearly identify and confirm the logical unit of work they want to revert before any analysis begins.**

1.  **Initiate Revert Process:** Determine the user's target.

2.  **Check for a User-Provided Target:** Check if the user provided a specific target as an argument (e.g., `/conductor:revert track <track_id>`).
    -   **IF a target is provided:** Proceed directly to **Path A (Direct Confirmation)**.
    -   **IF NO target is provided:** Proceed to **Path B (Guided Selection Menu)**. This is the default behavior.

3.  **Interaction Paths:**

    -   **PATH A: Direct Confirmation**
        1.  Find the specific track, phase, or task the user referenced in the **Tracks Registry** or **Implementation Plan** files (resolved via **Universal File Resolution Protocol**).
        2.  Confirm the selection with the user:
            -   "You asked to revert the [Track/Phase/Task]: '[Description]'. Is this correct?"
        3.  If confirmed, establish this as the `target_intent` and proceed to Phase 2. If denied, ask clarifying questions:
            -   "I'm sorry, I misunderstood. Please describe the Track, Phase, or Task you would like to revert."

    -   **PATH B: Guided Selection Menu**
        1.  **Identify Revert Candidates:**
            -   **Scan All Plans:** Read the **Tracks Registry** and every track's **Implementation Plan** (resolved via **Universal File Resolution Protocol** using the track's index file).
            -   **Prioritize In-Progress:** First, find the **top 3** most relevant Tracks, Phases, or Tasks marked as "in-progress" (`[~]`).
            -   **Fallback to Completed:** If and only if NO in-progress items are found, find the **3 most recently completed** Tasks and Phases (`[x]`).
        2.  **Present a Unified Hierarchical Menu:** Present the results to the user as a choice menu.
            -   **CRITICAL:** Limit the menu to a maximum of **4 items**. Group by Track if possible.
            -   **Example Option:** `"[Task] Update user model"` with description `"Track: track_20251208_user_profile"`.
            -   **Note:** An "Other" option is automatically added by the tool.
        3.  **Process User's Choice:**
            -   If the user selects a specific item, set this as the `target_intent` and proceed to Phase 2.
            -   If the user selects "Other", engage in dialogue to find the correct target. Once identified, loop back to Path A for final confirmation.

4.  **Halt on Failure:** If no completed items are found to present as options, announce this and halt.

---

## Phase 2: Git Reconciliation & Verification

**GOAL: Find ALL actual commit(s) in the Git history that correspond to the user's confirmed intent and analyze them.**

1.  **Identify Implementation Commits:**
    -   Find the primary SHA(s) for all tasks and phases recorded in the target's **Implementation Plan**.

2.  **Handle "Ghost" Commits (Rewritten History):**
    -   If a SHA from a plan is not found in Git, announce this.
    -   Search the Git log for a commit with a highly similar message.
    -   Ask the user to confirm it as the replacement. If not confirmed, halt.

3.  **Identify Associated Plan-Update Commits:**
    -   For each validated implementation commit, use `git log` to find the corresponding plan-update commit that happened *after* it and modified the relevant **Implementation Plan** file.

4.  **Identify the Track Creation Commit (Track Revert Only):**
    -   **IF** the user's intent is to revert an entire track, perform this additional step.
    -   **Method:** Use `git log -- <path_to_tracks_registry>` and search for the commit that first introduced the track entry.
        -   Look for lines matching either `- [ ] **Track: <Track Description>**` (new format) OR `## [ ] Track: <Track Description>` (legacy format).
    -   Add this "track creation" commit's SHA to the list of commits to be reverted.

5.  **Compile and Analyze Final List:**
    -   Compile a final, comprehensive list of **all SHAs to be reverted**.
    -   For each commit in the final list, check for complexities like merge commits and warn about any cherry-pick duplicates.

---

## Phase 3: Final Execution Plan Confirmation

**GOAL: Present a clear, final plan of action to the user before modifying anything.**

1.  **Summarize Findings:** Present a summary of the investigation and the exact actions to be taken.
    > "I have analyzed your request. Here is the plan:"
    > -   **Target:** Revert Task '[Task Description]'.
    > -   **Commits to Revert:** 2
    >     -   `<sha_code_commit>` ('feat: Add user profile')
    >     -   `<sha_plan_commit>` ('conductor(plan): Mark task complete')
    > -   **Action:** Run `git revert` on these commits in reverse order.

2.  **Final Go/No-Go:** Ask for final confirmation with two options:
    -   **Approve:** Proceed with the revert actions.
    -   **Revise:** Change the revert plan.

3.  **Process User Choice:**
    -   If "Approve", proceed to Phase 4.
    -   If "Revise", ask the user to describe the changes needed for the revert plan and loop back.

---

## Phase 4: Execution & Verification

**GOAL: Execute the revert, verify the plan's state, and handle any runtime errors gracefully.**

1.  **Execute Reverts:** Run `git revert --no-edit <sha>` for each commit in the final list, starting from the **most recent** and working **backward** (reverse chronological order).
2.  **Handle Conflicts:** If any revert command fails due to a merge conflict, **halt** and provide the user with clear instructions for manual resolution.
3.  **Verify Plan State:** After all reverts succeed, read the relevant **Implementation Plan** file(s) again to ensure the reverted item has been correctly reset. If not, perform a file edit to fix it and commit the correction.
4.  **Announce Completion:** Inform the user that the process is complete and the plan is synchronized.
