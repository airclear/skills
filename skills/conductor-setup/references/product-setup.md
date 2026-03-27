# Product and Tech Stack Setup Protocol

## General Questioning Guidelines

- **Mode Selection:** Each section offers Interactive/Autogenerate mode via `ask_user`. The user chooses how they want to proceed.
- **Question Batching:** Batch up to 4 questions in a single `ask_user` tool call to streamline the process.
- **Question Types:** Categorize as **Additive** (`multiSelect: true` - select all that apply) or **Exclusive Choice** (`multiSelect: false` - singular commitment).
- **Suggested Answers:** For each question, generate 3 high-quality suggested answers with both `label` and `description` fields.
- **Brownfield Awareness:** For existing projects, formulate questions that are specifically aware of the analyzed codebase. Do not ask generic questions if the answer is already in the files.
- **User Confirmation:** Each drafted document MUST be embedded into a confirmation `ask_user` call so the user can Approve or Suggest changes before writing.

### ask_user Tool Usage

When constructing `ask_user` calls:
- **header:** Very short label (max 16 chars).
- **type:** "choice", "text", or "yesno".
- **multiSelect:** `true` for additive questions, `false` for exclusive choice.
- **options:** Each option has `label` and `description`. Do NOT include an "Autogenerate" option within interactive questions (it is handled at mode selection level).
- **placeholder:** Provide a placeholder for "text" type questions.

---

## 1. Generate Product Guide (`product.md`)

### Step 1: Introduce the Section
Announce that you will now help the user create the `product.md`.

### Step 2: Determine Mode
Use the `ask_user` tool to let the user choose their preferred workflow:
- **header:** "Product"
- **question:** "How would you like to define the product details? Whether you prefer a quick start or a deep dive, both paths lead to a high-quality product guide!"
- **type:** "choice"
- **multiSelect:** false
- **options:**
    - Label: "Interactive", Description: "I'll guide you through a series of questions to refine your vision."
    - Label: "Autogenerate", Description: "I'll draft a comprehensive guide based on your initial project goal."

### Step 3: Gather Information (Conditional)
- **If user chose "Autogenerate":** Skip this step and proceed to Step 4.
- **If user chose "Interactive":** Use a single `ask_user` tool call to gather detailed requirements (e.g., target users, goals, features).
    - **CRITICAL:** Batch up to 4 questions in this single tool call.
    - **BROWNFIELD PROJECTS:** Formulate questions that are specifically aware of the analyzed codebase.
    - **SUGGESTIONS:** For each question, generate 3 high-quality suggested answers.
    - **Formulation:** Each question object has `header` (max 16 chars), `type: "choice"`, `multiSelect` (true/false), and `options` (each with `label` and `description`).
    - Wait for the user's response, then proceed.

### Step 4: Draft the Document
- **Autogenerate:** Use best judgment to expand on the initial project goal and infer missing details to create a comprehensive document.
- **Interactive:** Use the specific answers provided. The source of truth is **only the user's selected answer(s)**. Expand on these choices to create a polished output.

### Step 5: User Confirmation Loop
Use the `ask_user` tool to request confirmation. **Embed the drafted content directly into the `question` field** so the user can review it in context:
- **header:** "Review Draft"
- **question:**
    ```
    Please review the drafted Product Guide below. What would you like to do next?

    ---

    <Insert Drafted product.md Content Here>
    ```
- **type:** "choice"
- **multiSelect:** false
- **options:**
    - Label: "Approve", Description: "The guide looks good, proceed to the next step."
    - Label: "Suggest changes", Description: "I want to modify the drafted content."

### Step 6: Write File
Once approved, append the generated content to the existing `conductor/product.md` file, preserving the `# Initial Concept` section.

### Step 7: Continue
Immediately proceed to Product Guidelines.

---

## 2. Generate Product Guidelines (`product-guidelines.md`)

### Step 1: Introduce the Section
Announce that you will now help the user create the `product-guidelines.md`.

### Step 2: Determine Mode
Use the `ask_user` tool to let the user choose their preferred workflow:
- **header:** "Product"
- **question:** "How would you like to define the product guidelines? You can hand-pick the style or let me generate a standard set."
- **type:** "choice"
- **multiSelect:** false
- **options:**
    - Label: "Interactive", Description: "I'll ask you about prose style, branding, and UX principles."
    - Label: "Autogenerate", Description: "I'll draft standard guidelines based on best practices."

### Step 3: Gather Information (Conditional)
- **If user chose "Autogenerate":** Skip this step and proceed to Step 4.
- **If user chose "Interactive":** Use a single `ask_user` tool call to gather detailed preferences (e.g., prose style, brand messaging, visual identity).
    - **CRITICAL:** Batch up to 4 questions in this single tool call.
    - **BROWNFIELD PROJECTS:** Analyze current docs/code to suggest guidelines matching the established style.
    - **Formulation:** Each question object has `header` (max 16 chars), `type: "choice"`, `multiSelect` (true/false), and `options` (each with `label` and `description`).
    - Wait for the user's response, then proceed.

### Step 4: Draft the Document
- **Autogenerate:** Use best judgment to infer standard, high-quality guidelines suitable for the project type.
- **Interactive:** Use the specific answers provided. The source of truth is **only the user's selected answer(s)**. Expand to create a polished output.

### Step 5: User Confirmation Loop
Embed the drafted content in the `ask_user` confirmation call:
- **header:** "Review Draft"
- **question:**
    ```
    Please review the drafted Product Guidelines below. What would you like to do next?

    ---

    <Insert Drafted product-guidelines.md Content Here>
    ```
- **type:** "choice"
- **multiSelect:** false
- **options:**
    - Label: "Approve", Description: "The guidelines look good, proceed to the next step."
    - Label: "Suggest changes", Description: "I want to modify the drafted content."

### Step 6: Write File
Once approved, write the generated content to `conductor/product-guidelines.md`.

### Step 7: Continue
Immediately proceed to Tech Stack.

---

## 3. Generate Tech Stack (`tech-stack.md`)

### Step 1: Introduce the Section
Announce that you will now help define the technology stack.

### Step 2: Determine Mode

**FOR GREENFIELD PROJECTS:** Use the `ask_user` tool to choose the workflow:
- **header:** "Tech Stack"
- **question:** "How would you like to define the technology stack? I can recommend a proven stack for your goal or you can hand-pick each component."
- **type:** "choice"
- **multiSelect:** false
- **options:**
    - Label: "Interactive", Description: "I'll ask you to select the language, frameworks, and database."
    - Label: "Autogenerate", Description: "I'll recommend a standard tech stack based on your project goal."

**FOR BROWNFIELD PROJECTS:**
- **CRITICAL WARNING:** Your goal is to document the project's *existing* tech stack, not to propose changes.
- **State the Inferred Stack:** Based on the code analysis, state the technology stack you have inferred in the chat.
- **Request Confirmation:** After stating the detected stack, ask the user for confirmation:
    - **header:** "Tech Stack"
    - **question:** "Is the inferred tech stack (listed above) correct?"
    - **type:** "yesno"
- **Handle Disagreement:** If the user disputes the suggestion, immediately call `ask_user` with `type: "text"` to allow the user to provide the correct technology stack manually.

### Step 3: Gather Information (Greenfield Interactive Only)
- **If user chose "Interactive":** Use a single `ask_user` tool call to gather detailed preferences.
    - **CRITICAL:** Batch up to 4 questions, separating concerns (e.g., Languages, Backend Frameworks, Frontend Frameworks, Database).
    - **SUGGESTIONS:** For each question, generate 3-4 high-quality suggested answers.
    - **Formulation:** Each question object has `header` (max 16 chars), `type: "choice"`, `multiSelect: true` (to allow hybrid stacks), and `options` (each with `label` and `description`).
    - **Label Guidance:** Use the `label` field to explain *why* or *where* a technology fits (e.g., "TypeScript - Ideal for Angular UI").
    - Wait for the user's response, then proceed.

### Step 4: Draft the Document
- **Autogenerate:** Use best judgment to infer a standard, high-quality stack suitable for the project goal.
- **Interactive or corrected Brownfield:** Use the specific answers provided. The source of truth is **only the user's selected answer(s)**.

### Step 5: User Confirmation Loop
Embed the drafted content in the `ask_user` confirmation call:
- **header:** "Review Draft"
- **question:**
    ```
    Please review the drafted Tech Stack below. What would you like to do next?

    ---

    <Insert Drafted tech-stack.md Content Here>
    ```
- **type:** "choice"
- **multiSelect:** false
- **options:**
    - Label: "Approve", Description: "The tech stack looks good, proceed to the next step."
    - Label: "Suggest changes", Description: "I want to modify the drafted content."

### Step 6: Write File
Once approved, write the generated content to `conductor/tech-stack.md`.

### Step 7: Continue
Immediately proceed to Configuration (Code Styleguides).
