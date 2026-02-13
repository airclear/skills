# Revert Protocol (Git-Aware)

## 1. Target Selection (Interactive)
1.  **Direct Target:** If the user provided a target (e.g., track ID), confirm it.
2.  **Guided Selection (Menu):**
    - Scan all `plan.md` files for "In Progress" (`[~]`) items.
    - If none, show the 5 most recently completed (`[x]`) Tasks/Phases.
    - Present a hierarchical menu and get user's choice.

## 2. Git Reconciliation
1.  **Identify Implementation Commits:** Find the SHAs recorded in `plan.md` for the selected target.
2.  **Handle Missing SHAs:** If a SHA is not in Git, search the log for similar commit messages.
3.  **Identify Plan-Update Commits:** Find the `conductor(plan):` commits that happened after each implementation commit.
4.  **Track Creation Commit:** If reverting an entire track, find the commit that added it to `tracks.md`.
5.  **Analyze List:** Check for merge commits or complexities.

## 3. Execution Plan Confirmation
1.  **Summarize:** Present the target and the list of SHAs to be reverted in reverse order.
2.  **Final Go/No-Go:** Ask: "Do you want to proceed? (yes/no)".

## 4. Execution
1.  **Revert:** Run `git revert --no-edit <sha>` starting from the most recent.
2.  **Conflicts:** If conflicts occur, halt and ask for manual resolution.
3.  **Plan Synchronization:** Verify and manually edit the `plan.md` or `tracks.md` files to ensure their state matches the revert. Commit the plan correction.
4.  **Announce:** Confirm completion and plan synchronization.
