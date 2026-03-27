# Implementation Protocol

## 1. Setup Check

**PROTOCOL: Verify that the Conductor environment is properly set up.**

1.  **Verify Core Context:** Using the **Universal File Resolution Protocol**, resolve and verify the existence of:
    -   **Product Definition**
    -   **Tech Stack**
    -   **Workflow**

2.  **Handle Failure:** If ANY of these are missing (or their resolved paths do not exist), announce: "Conductor is not set up. Please run `/conductor:setup`." and HALT.

---

## 2. Track Selection

**PROTOCOL: Identify and select the track to be implemented.**

1.  **Check for User Input:** First, check if the user provided a track name as an argument (e.g., `/conductor:implement <track_description>`).

2.  **Locate and Parse Tracks Registry:**
    -   Resolve the **Tracks Registry**.
    -   Read and parse this file. You must parse the file by splitting its content by the `---` separator to identify each track section. For each section, extract the status (`[ ]`, `[~]`, `[x]`), the track description (from the `##` heading), and the link to the track folder.
    -   **CRITICAL:** If no track sections are found after parsing, announce: "The tracks file is empty or malformed. No tracks to implement." and halt.

3.  **Select Track:**
    -   **If a track name was provided:**
        1.  Perform an exact, case-insensitive match for the provided name against the track descriptions you parsed.
        2.  If a unique match is found, immediately call the `ask_user` tool to confirm the selection (do not repeat the question in the chat):
            - **questions:**
                - **header:** "Confirm"
                - **question:** "I found track '<track_description>'. Is this correct?"
                - **type:** "yesno"
        3.  If no match is found, or if the match is ambiguous, immediately call the `ask_user` tool to inform the user and request the correct track name (do not repeat the question in the chat):
            - **questions:**
                - **header:** "Clarify"
                - **question:** "I couldn't find a unique track matching the name you provided. Did you mean '<next_available_track>'? Or please type the exact track name."
                - **type:** "text"
    -   **If no track name was provided (or if the previous step failed):**
        1.  **Identify Next Track:** Find the first track in the parsed tracks file that is NOT marked as `[x]` Completed.
        2.  **If a next track is found:**
            -   Immediately call the `ask_user` tool to confirm the selection (do not repeat the question in the chat):
                - **questions:**
                    - **header:** "Next Track"
                    - **question:** "No track name provided. Would you like to proceed with the next incomplete track: '<track_description>'?"
                    - **type:** "yesno"
            -   If confirmed, proceed with this track. Otherwise, immediately call the `ask_user` tool to request the correct track name (do not repeat the question in the chat):
                - **questions:**
                    - **header:** "Clarify"
                    - **question:** "Please type the exact name of the track you would like to implement."
                    - **type:** "text"
        3.  **If no incomplete tracks are found:**
            -   Announce: "No incomplete tracks found in the tracks file. All tasks are completed!"
            -   Halt the process and await further user instructions.

4.  **Handle No Selection:** If no track is selected, inform the user and await further instructions.

---

## 3. Track Implementation

**PROTOCOL: Execute the selected track.**

1.  **Announce Action:** Announce which track you are beginning to implement.

2.  **Update Status to 'In Progress':**
    -   Before beginning any work, you MUST update the status of the selected track in the **Tracks Registry** file.
    -   This requires finding the specific heading for the track (e.g., `## [ ] Track: <Description>`) and replacing it with the updated status (e.g., `## [~] Track: <Description>`) in the **Tracks Registry** file you identified earlier.

3.  **Load Track Context:**
    a. **Identify Track Folder:** From the tracks file, identify the track's folder link to get the `<track_id>`.
    b. **Read Files:**
        -   **Track Context:** Using the **Universal File Resolution Protocol**, resolve and read the **Specification** and **Implementation Plan** for the selected track.
        -   **Workflow:** Resolve **Workflow** (via the **Universal File Resolution Protocol** using the project's index file).
    c. **Error Handling:** If you fail to read any of these files, you MUST stop and inform the user of the error.

4.  **Execute Tasks and Update Track Plan:**
    a. **Announce:** State that you will now execute the tasks from the track's **Implementation Plan** by following the procedures in the **Workflow**.
    b. **Iterate Through Tasks:** You MUST now loop through each task in the track's **Implementation Plan** one by one.
    c. **For Each Task, You MUST:**
        i. **Defer to Workflow:** The **Workflow** file is the **single source of truth** for the entire task lifecycle. You MUST now read and execute the procedures defined in the "Task Workflow" section of the **Workflow** file you have in your context. Follow its steps for implementation, testing, and committing precisely.
           - **CRITICAL:** Every human-in-the-loop interaction, confirmation, or request for feedback mentioned in the **Workflow** (e.g., manual verification plans or guidance on persistent failures) MUST be conducted using the `ask_user` tool.

5.  **Finalize Track:**
    -   After all tasks in the track's local **Implementation Plan** are completed, you MUST update the track's status in the **Tracks Registry**.
    -   This requires finding the specific heading for the track (e.g., `## [~] Track: <Description>`) and replacing it with the completed status (e.g., `## [x] Track: <Description>`).
    -   **Commit Changes:** Stage the **Tracks Registry** file and commit with the message `chore(conductor): Mark track '<track_description>' as complete`.
    -   Announce that the track is fully complete and the tracks file has been updated.
