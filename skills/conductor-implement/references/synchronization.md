# Documentation Synchronization & Track Cleanup Protocol

## 1. Synchronization Trigger

**PROTOCOL: Update project-level documentation based on the completed track.**

This protocol MUST only be executed when a track has reached a `[x]` status in the tracks file. DO NOT execute this protocol for any other track status changes.

---

## 2. Synchronization Process

1.  **Announce Synchronization:** Announce that you are now synchronizing the project-level documentation with the completed track's specifications.

2.  **Load Track Specification:** Read the track's **Specification**.

3.  **Load Project Documents:**
    -   Resolve and read:
        -   **Product Definition**
        -   **Tech Stack**
        -   **Product Guidelines**

4.  **Analyze and Update:**
    a.  **Analyze Specification:** Carefully analyze the **Specification** to identify any new features, changes in functionality, or updates to the technology stack.

    b.  **Update Product Definition:**
        i. **Condition for Update:** Based on your analysis, you MUST determine if the completed feature or bug fix significantly impacts the description of the product itself.
        ii. **Propose and Confirm Changes:** If an update is needed:
            -   **Ask for Approval:** Use the `ask_user` tool to request confirmation. You MUST embed the proposed updates (in a diff format) directly into the `question` field so the user can review them in context.
                - **questions:**
                    - **header:** "Product"
                    - **question:** "Please review the proposed updates to the Product Definition below. Do you approve?\n\n---\n\n<Insert Proposed product.md Updates/Diff Here>"
                    - **type:** "yesno"
        iii. **Action:** Only after receiving explicit user confirmation, perform the file edits to update the **Product Definition** file. Keep a record of whether this file was changed.

    c.  **Update Tech Stack:**
        i. **Condition for Update:** Similarly, you MUST determine if significant changes in the technology stack are detected as a result of the completed track.
        ii. **Propose and Confirm Changes:** If an update is needed:
            -   **Ask for Approval:** Use the `ask_user` tool to request confirmation. You MUST embed the proposed updates (in a diff format) directly into the `question` field so the user can review them in context.
                - **questions:**
                    - **header:** "Tech Stack"
                    - **question:** "Please review the proposed updates to the Tech Stack below. Do you approve?\n\n---\n\n<Insert Proposed tech-stack.md Updates/Diff Here>"
                    - **type:** "yesno"
        iii. **Action:** Only after receiving explicit user confirmation, perform the file edits to update the **Tech Stack** file. Keep a record of whether this file was changed.

    d.  **Update Product Guidelines (Strictly Controlled):**
        i. **CRITICAL WARNING:** This file defines the core identity and communication style of the product. It should be modified with extreme caution and ONLY in cases of significant strategic shifts, such as a product rebrand or a fundamental change in user engagement philosophy. Routine feature updates or bug fixes should NOT trigger changes to this file.
        ii. **Condition for Update:** You may ONLY propose an update to this file if the track's **Specification** explicitly describes a change that directly impacts branding, voice, tone, or other core product guidelines.
        iii. **Propose and Confirm Changes:** If the conditions are met:
            -   **Ask for Approval:** Use the `ask_user` tool to request confirmation. You MUST embed the proposed changes (in a diff format) directly into the `question` field, including a clear warning.
                - **questions:**
                    - **header:** "Product"
                    - **question:** "WARNING: This is a sensitive action as it impacts core product guidelines. Please review the proposed changes below. Do you approve these critical changes?\n\n---\n\n<Insert Proposed product-guidelines.md Updates/Diff Here>"
                    - **type:** "yesno"
        iv. **Action:** Only after receiving explicit user confirmation, perform the file edits. Keep a record of whether this file was changed.

5.  **Final Report:** Announce the completion of the synchronization process and provide a summary of the actions taken.
    - **Construct the Message:** Based on the records of which files were changed, construct a summary message.
    - **Commit Changes:**
        - If any files were changed (**Product Definition**, **Tech Stack**, or **Product Guidelines**), you MUST stage them and commit them.
        - **Commit Message:** `docs(conductor): Synchronize docs for track '<track_description>'`
    - **Example (if Product Definition was changed, but others were not):**
        > "Documentation synchronization is complete.
        > - **Changes made to Product Definition:** The user-facing description of the product was updated to include the new feature.
        > - **No changes needed for Tech Stack:** The technology stack was not affected.
        > - **No changes needed for Product Guidelines:** Core product guidelines remain unchanged."
    - **Example (if no files were changed):**
        > "Documentation synchronization is complete. No updates were necessary for project documents based on the completed track."

---

## 3. Track Cleanup

**PROTOCOL: Offer to archive or delete the completed track.**

This protocol MUST only be executed after the current track has been successfully implemented and the **Synchronization** step is complete.

1.  **Ask for User Choice:** Immediately call the `ask_user` tool to prompt the user (do not repeat the question in the chat):
    - **questions:**
        - **header:** "Track Cleanup"
        - **question:** "Track '<track_description>' is now complete. What would you like to do?"
        - **type:** "choice"
        - **multiSelect:** false
        - **options:**
            - Label: "Review", Description: "Run the review command to verify changes before finalizing."
            - Label: "Archive", Description: "Move the track's folder to `conductor/archive/` and remove it from the tracks file."
            - Label: "Delete", Description: "Permanently delete the track's folder and remove it from the tracks file."
            - Label: "Skip", Description: "Do nothing and leave it in the tracks file."

2.  **Handle User Response:**

    *   **If user chooses "Review":**
        *   Announce: "Please run `/conductor:review` to verify your changes. You will be able to archive or delete the track after the review."

    *   **If user chooses "Archive":**
        i.   **Create Archive Directory:** Check for the existence of `conductor/archive/`. If it does not exist, create it.
        ii.  **Archive Track Folder:** Move the track's folder from its current location (resolved via the **Tracks Directory**) to `conductor/archive/<track_id>`.
        iii. **Remove from Tracks File:** Read the content of the **Tracks Registry** file, remove the entire section for the completed track (the part that starts with `---` and contains the track description), and write the modified content back to the file.
        iv.  **Commit Changes:** Stage the **Tracks Registry** file and `conductor/archive/`. Commit with the message `chore(conductor): Archive track '<track_description>'`.
        v.   **Announce Success:** Announce: "Track '<track_description>' has been successfully archived."

    *   **If user chooses "Delete":**
        i. **CRITICAL WARNING:** Before proceeding, immediately call the `ask_user` tool to ask for final confirmation (do not repeat the warning in the chat):
            - **questions:**
                - **header:** "Confirm"
                - **question:** "WARNING: This will permanently delete the track folder and all its contents. This action cannot be undone. Are you sure?"
                - **type:** "yesno"
        ii. **Handle Confirmation:**
            - **If 'yes':**
                a. **Delete Track Folder:** Resolve the **Tracks Directory** and permanently delete the track's folder from `<Tracks Directory>/<track_id>`.
                b. **Remove from Tracks File:** Read the content of the **Tracks Registry** file, remove the entire section for the completed track, and write the modified content back to the file.
                c. **Commit Changes:** Stage the **Tracks Registry** file and the deletion of the track directory. Commit with the message `chore(conductor): Delete track '<track_description>'`.
                d. **Announce Success:** Announce: "Track '<track_description>' has been permanently deleted."
            - **If 'no':**
                a. **Announce Cancellation:** Announce: "Deletion cancelled. The track has not been changed."

    *   **If user chooses "Skip":**
        *   Announce: "Okay, the completed track will remain in your tracks file for now."
