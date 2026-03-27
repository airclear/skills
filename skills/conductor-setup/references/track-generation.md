# Initial Track Generation Protocol

## Pre-Requisite (Cleanup)
If resuming from a previous interrupted setup, check if `conductor/tracks/` exists but is incomplete. If so, **delete** the entire `conductor/tracks/` directory before proceeding.

---

## 1. Generate Product Requirements (Greenfield only)

### Step 1: Transition to Requirements
Announce that the initial project setup is complete. State that you will now define high-level product requirements (user stories, functional/non-functional requirements).

### Step 2: Analyze Context
Read and analyze `conductor/product.md` to understand the project's core concept.

### Step 3: Determine Mode
Use the `ask_user` tool to let the user choose:
- **header:** "Product Reqs"
- **question:** "How would you like to define the product requirements? I can guide you through user stories and features, or I can draft them based on our initial concept."
- **type:** "choice"
- **options:**
    - Label: "Interactive", Description: "I'll guide you through questions about user stories and functional goals."
    - Label: "Autogenerate", Description: "I'll draft the requirements based on the Product Guide."

### Step 4: Gather Information (Conditional)
- **If "Autogenerate":** Skip to Step 5.
- **If "Interactive":** Use a single `ask_user` tool call to gather requirements.
    - **CRITICAL:** Batch up to 4 questions (User Stories, Key Features, Constraints, Non-functional Requirements).
    - **SUGGESTIONS:** Generate 3 high-quality suggested answers per question based on the project goal.
    - **Formulation:** Use "choice" type, `multiSelect: true` for additive answers. Each question has `header` (max 16 chars), `question`, and `options` (each with `label` and `description`).
    - Do NOT include an "Autogenerate" option within the interactive questions.
    - Wait for user response, then proceed.

### Step 5: Draft Requirements
Generate a draft of product requirements. Source of truth is **only the user's selected answer(s)**.

### Step 6: User Confirmation Loop
Briefly state that the requirements draft is ready. Embed the drafted requirements into the `ask_user` confirmation call:
- **header:** "Review"
- **question:** "Please review the drafted Product Requirements below. What would you like to do next?\n\n---\n\n<Insert Drafted Requirements Here>"
- **type:** "choice"
- **multiSelect:** false
- **options:**
    - Label: "Approve", Description: "The requirements look good, proceed to the next step."
    - Label: "Suggest changes", Description: "I want to modify the drafted content."

### Step 7: Continue
Once approved, retain requirements in context and proceed to Track Proposal.

---

## 2. Propose Initial Track

### Step 1: State Goal
Announce that you will propose an initial track. Briefly explain what a "track" is.

### Step 2: Generate Track Title
Analyze project context (`product.md`, `tech-stack.md`) and (for greenfield) the requirements.
- **Greenfield:** Focus on MVP core (e.g., "Build core tip calculator functionality").
- **Brownfield:** Focus on maintenance or targeted enhancements (e.g., "Implement user authentication flow").

### Step 3: Confirm Proposal
Use `ask_user`:
- **header:** "Confirm Track"
- **type:** "choice"
- **multiSelect:** false
- **question:** "To get the project started, I suggest the following track: '<Track Title>'. Do you want to proceed with this track?"
- **options:**
    - Label: "Yes", Description: "Proceed with '<Track Title>'."
    - Label: "Suggest changes", Description: "I want to define a different track."

### Step 4: Handle Response
- **If "Yes":** Use the suggested title as the track description.
- **If "Suggest changes":** Immediately call `ask_user` with `type: "text"`, `question: "Please enter the description for the initial track:"`, `placeholder: "e.g., Setup CI/CD pipeline"`.
- Proceed to artifact creation with the determined track description.

---

## 3. Convert Track into Artifacts

### Step 1: Announce
Announce that you will now create the artifacts for this track.

### Step 2: Initialize Tracks File
Create `conductor/tracks.md`:
```markdown
# Project Tracks

This file tracks all major tracks for the project. Each track has its own detailed plan in its respective folder.

---

- [ ] **Track: <Track Description>**
  *Link: [./<Tracks Directory Name>/<track_id>/](./<Tracks Directory Name>/<track_id>/)*
```
Replace `<Tracks Directory Name>` with the actual tracks folder resolved via the protocol.

### Step 3: Generate Track-Specific Spec and Plan
- **spec.md:** Detailed specification for the track.
- **plan.md:** Phased implementation plan.
    - **CRITICAL:** Task structure must adhere to `conductor/workflow.md` (e.g., TDD: "Write Tests" sub-task followed by "Implement Feature" sub-task).
    - **CRITICAL:** Include status markers `[ ]` for EVERY task and sub-task:
        - Parent Task: `- [ ] Task: ...`
        - Sub-task: `    - [ ] ...`
    - **CRITICAL: Inject Phase Completion Tasks.** Read `conductor/workflow.md` to check if a "Phase Completion Verification and Checkpointing Protocol" is defined. If so, append a final meta-task to each Phase: `- [ ] Task: Conductor - User Manual Verification '<Phase Name>' (Protocol in workflow.md)`.

### Step 4: Create Track Directory and Files
1. **Generate Track ID:** Create a unique ID using format `shortname_YYYYMMDD`. Use this ID consistently.
2. **Create Directory:** Resolve the Tracks Directory via Universal File Resolution Protocol and create `<Tracks Directory>/<track_id>/`.
3. **Create `metadata.json`:**
    ```json
    {
      "track_id": "<track_id>",
      "type": "feature",
      "status": "new",
      "created_at": "YYYY-MM-DDTHH:MM:SSZ",
      "updated_at": "YYYY-MM-DDTHH:MM:SSZ",
      "description": "<Initial user description>"
    }
    ```
    Populate with actual values and current timestamp.
4. **Write `spec.md` and `plan.md`** in the track directory.
5. **Write `index.md`:**
    ```markdown
    # Track <track_id> Context

    - [Specification](./spec.md)
    - [Implementation Plan](./plan.md)
    - [Metadata](./metadata.json)
    ```
    If patching a missing index from Audit, use the existing folder's track_id.

### Step 5: Exit Plan Mode
Call `exit_plan_mode` with the path: `<Tracks Directory>/<track_id>/index.md`.

### Step 6: Announce Progress
Announce that the track has been created.

---

## 4. Final Announcement

1. **Announce Completion:** State that project setup and initial track generation are complete.
2. **Save Conductor Files:** Add and commit all files with message `conductor(setup): Add conductor setup files`.
3. **Next Steps:** Inform the user they can begin work with `/conductor:implement`.
