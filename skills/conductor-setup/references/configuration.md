# Configuration Protocol

## 1. Select Code Style Guides

### Step 1: Initiate Dialogue
Announce that the initial scaffolding is complete and you now need the user's input to select the project's guides from the locally available templates.

### Step 2: List Available Guides
List the available style guides by using the `run_shell_command` tool to execute `ls <templates_path>/code_styleguides/`.

**CRITICAL:** You MUST use `run_shell_command` for this step. Do NOT use the `list_directory` tool, as the templates directory may reside outside of the allowed workspace and the call will fail.

### Step 3: Select Guides based on Project Type

**FOR GREENFIELD PROJECTS:**
1.  **Recommendation:** Based on the Tech Stack defined in the previous step, recommend the most appropriate style guide(s) and explain why.
2.  **Determine Mode:** Use the `ask_user` tool:
    - **header:** "Code Style Guide"
    - **question:** "How would you like to proceed with the code style guides?"
    - **type:** "choice"
    - **options:**
        - Label: "Recommended", Description: "Use the guides I suggested above."
        - Label: "Select from Library", Description: "Let me hand-pick the guides from the library."
3.  **If user chose "Select from Library":**
    - **Batching Strategy:** Split the list of available guides into groups of 3-4 items.
    - Announce "I'll present the available guides in groups. Please select all that apply." Then, immediately call the `ask_user` tool with the batched questions.
    - **Single Tool Call:** Create one `ask_user` call containing a `questions` array with one question per group.
    - **Constraint Handling:** If the final group has only 1 item, add a second option labeled "None" to satisfy the minimum 2 options requirement.
    - **Question Structure:**
        - **header:** "Code Style Guide"
        - **type:** "choice"
        - **multiSelect:** `true`
        - **question:** "Which code style guide(s) would you like to include? (Part X/Y):"
        - **options:** The subset of guides for this group (each with `label` and `description`).

**FOR BROWNFIELD PROJECTS:**
1.  **Announce Selection:** Inform the user: "Based on the inferred tech stack, I will copy the following code style guides: <list of inferred guides>."
2.  **Determine Mode:** Use the `ask_user` tool:
    - **header:** "Code Style Guide"
    - **question:** "I've identified these guides for your project. Would you like to proceed or add more?"
    - **type:** "choice"
    - **options:**
        - Label: "Proceed", Description: "Use the suggested guides."
        - Label: "Add More", Description: "Select additional guides from the library."
3.  **If user chose "Add More":**
    - Announce "I'll present the additional guides. Please select all that apply." Then, immediately call the `ask_user` tool.
    - Use a single `ask_user` tool call. Dynamically split the available guides into batches of 4 options max. Create one `multiSelect: true` question for each batch.

### Step 4: Copy Selected Guides
Construct and execute a command to create the directory and copy all selected files. For example:
```
mkdir -p conductor/code_styleguides && cp <templates_path>/code_styleguides/python.md <templates_path>/code_styleguides/javascript.md conductor/code_styleguides/
```

---

## 2. Select Workflow (`workflow.md`)

### Step 1: Copy Initial Workflow
Copy the workflow template to `conductor/workflow.md`.

### Step 2: Determine Mode
Use the `ask_user` tool to let the user choose their preferred workflow:
- **header:** "Workflow"
- **question:** "Do you want to use the default workflow or customize it? The default includes >80% test coverage and per-task commits."
- **type:** "choice"
- **options:**
    - Label: "Default", Description: "Use the standard Conductor workflow."
    - Label: "Customize", Description: "I want to adjust coverage requirements and commit frequency."

### Step 3: Gather Information (Conditional)

**If user chose "Default":** Skip this step and proceed to Step 4.

**If user chose "Customize":**

a. **Initial Batch:** Use a single `ask_user` tool call to gather primary customizations:
    - **Coverage question:**
        - **header:** "Coverage"
        - **question:** "The default required test code coverage is >80%. What is your preferred percentage?"
        - **type:** "text"
        - **placeholder:** "e.g., 90"
    - **Commits question:**
        - **header:** "Commits"
        - **question:** "Should I commit changes after each task or after each phase?"
        - **type:** "choice"
        - **options:**
            - Label: "Per Task", Description: "Commit after every completed task"
            - Label: "Per Phase", Description: "Commit only after an entire phase is complete"
    - **Summaries question:**
        - **header:** "Summaries"
        - **question:** "Where should I record task summaries?"
        - **type:** "choice"
        - **options:**
            - Label: "Git Notes", Description: "Store summaries in Git notes metadata"
            - Label: "Commit Messages", Description: "Include summaries in the commit message body"

b. **Final Tweak (Second Batch):** Once the first batch is answered, use a second `ask_user` tool call to show the result and allow additional tweaks:
    - **header:** "Workflow"
    - **type:** "text"
    - **question:**
        ```
        Based on your answers, I will configure the workflow with:
        - Test Coverage: <User Answer 1>%
        - Commit Frequency: <User Answer 2>
        - Summary Storage: <User Answer 3>

        Is there anything else you'd like to change or add to the workflow? (Leave blank to finish or type your additional requirements).
        ```

### Step 4: Update Workflow File
Update `conductor/workflow.md` based on all user answers from both steps.

---

## 3. Finalization

### Step 1: Generate Index File
Create `conductor/index.md` with the following content:

```markdown
# Project Context

## Definition
- [Product Definition](./product.md)
- [Product Guidelines](./product-guidelines.md)
- [Tech Stack](./tech-stack.md)

## Workflow
- [Workflow](./workflow.md)
- [Code Style Guides](./code_styleguides/)

## Management
- [Tracks Registry](./tracks.md)
- [Tracks Directory](./tracks/)
```

Announce: "Created `conductor/index.md` to serve as the project context index."

### Step 2: Summarize Actions
Present a summary of all actions taken during the initial setup, including:
- The guide files that were copied.
- The workflow file that was copied.

### Step 3: Transition to Track Generation
Announce that the initial setup is complete and you will now proceed to define the first track for the project.
