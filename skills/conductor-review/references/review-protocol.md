# Review Protocol (Principal Engineer Persona)

## 1. Scope Identification
- **Arguments:** Use provided `args` or auto-detect `[~] In Progress` track.
- **Confirmation:** Ensure user agrees on the review target.

## 2. Context Retrieval
- **Project Context:** Read `product-guidelines.md` and `tech-stack.md`.
- **Style Guides:** Read all `.md` files in `conductor/code_styleguides/`. Violations here are **High** severity.
- **Change Detection:**
    - Parse `plan.md` for commit SHAs.
    - Run `git diff <revision_range>`.
    - Use "Iterative Review Mode" (file-by-file) if changes > 300 lines.

## 3. Analysis and Verification
1.  **Intent:** Does it match `plan.md` and `spec.md`?
2.  **Style:** Compliance with guidelines and code styleguides.
3.  **Safety:** Bugs, race conditions, null risks, security scan (secrets, PII).
4.  **Testing:**
    - Are there new tests?
    - **Auto-Execute:** Infer and run test command (e.g., `npm test`, `pytest`). Propose up to 2 fixes for failures.

## 4. Output Findings
Format as a **Review Report** with:
- Summary
- Verification Checklist (Plan, Style, Tests)
- Findings (Critical/High/Medium/Low) with diff-based suggestions.

## 5. Decisions and Cleanup
1.  **Recommendation:** Announce if it's ready or needs fixes.
2.  **User Choice:**
    - **Apply Fixes:** Automatically apply suggestions.
    - **Manual Fix:** User edits code.
    - **Complete Track:** Proceed to cleanup.
3.  **Commit Review:**
    - If track-specific: Add "Apply review suggestions" task to `plan.md`, commit code, record SHA in plan, commit plan update.
4.  **Archive/Delete:** Offer to cleanup the track if reviewing a completed one.
