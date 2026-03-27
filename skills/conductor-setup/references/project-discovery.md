# Project Discovery Protocol

## 1. Detect Project Maturity

Classify the project as "Brownfield" (Existing) or "Greenfield" (New) based on these indicators:

### Brownfield Indicators
- **Dependency manifests:** Check for `package.json`, `pom.xml`, `requirements.txt`, `go.mod`, `Cargo.toml`.
- **Source code directories:** Check for `src/`, `app/`, `lib/`, `bin/` containing code files.
- **Git status check:** If a `.git` directory exists, execute `git status --porcelain`. Ignore changes within the `conductor/` directory. If there are *other* uncommitted changes, it may be Brownfield.
- **Classification rule:** If ANY of the primary indicators (manifests or source code directories) are found, classify as **Brownfield**.

### Greenfield Condition
Classify as **Greenfield** ONLY if:
1. NONE of the "Brownfield Indicators" are found.
2. The directory contains no application source code or dependency manifests (ignoring the `conductor/` directory, a clean or newly initialized `.git` folder, and a `README.md`).

## 2. Resume Fast-Forward Check

- If the **Target Section** (from the Project Audit) is anything other than "Section 2.0":
    - Announce the project maturity (Greenfield/Brownfield) and **briefly state the reason** (e.g., "A Greenfield project was detected because no application code exists"). Then announce the target section.
    - **IMMEDIATELY JUMP** to the Target Section. Do not execute the rest of this protocol.
- If the Target Section is "Section 2.0", proceed to step 3.

## 3. Execute Workflow based on Maturity

### 3A. Brownfield Project Initialization Protocol

1.  **Announce Detection:** Inform the user that an existing project has been detected and **briefly state the specific indicator found** (e.g., "because I found a `package.json` file"). Be concise.

2.  **Git Warning:** If the `git status --porcelain` check indicated uncommitted changes (excluding `conductor/` directory), inform the user: "WARNING: You have uncommitted changes in your Git repository. Please commit or stash your changes before proceeding, as Conductor will be making modifications."

3.  **Pre-analysis Confirmation:**
    - **Request Permission:** Inform the user that a brownfield (existing) project has been detected.
    - **Ask for Permission:** Request permission for a read-only scan using the `ask_user` tool:
        - **header:** "Permission"
        - **question:** "A brownfield (existing) project has been detected. May I perform a read-only scan to analyze the project?"
        - **type:** "yesno"
    - **Handle Denial:** If permission is denied, halt the process and await further user instructions.

4.  **Code Analysis:**
    - **Announce Action:** Inform the user that you will now perform a code analysis.
    - **Prioritize README:** Begin by analyzing the `README.md` file, if it exists.
    - **Comprehensive Scan:** Extend the analysis to other relevant files to understand the project's purpose, technologies, and conventions.

5.  **File Size and Relevance Triage:**
    - **Respect Ignore Files:** Before scanning, check for `.geminiignore` and `.gitignore`. If either exists, use their combined patterns to exclude files and directories. `.geminiignore` patterns take precedence over `.gitignore` if there are conflicts.
    - **Efficiently List Relevant Files:** Use `git ls-files --exclude-standard -co | xargs -n 1 dirname | sort -u` to list relevant directories. If Git is not used, construct a `find` command that reads the ignore files and prunes the corresponding paths.
    - **Fallback to Manual Ignores:** ONLY if neither `.geminiignore` nor `.gitignore` exist, fall back to manually ignoring common directories (e.g., `node_modules`, `.m2`, `build`, `dist`, `bin`, `target`, `.git`, `.idea`, `.vscode`).
    - **Prioritize Key Files:** Focus analysis on high-value, low-size files first (manifest files like `package.json`, `pom.xml`, etc.).
    - **Handle Large Files:** For any single file over 1MB, read only the first and last 20 lines using `head` and `tail`.

6.  **Extract and Infer Project Context:**
    - **Strict File Access:** Do NOT ask for more files. Base analysis SOLELY on provided snippets and directory structure.
    - **Extract Tech Stack:** Identify Programming Language, Frameworks (frontend and backend), and Database Drivers from manifest files.
    - **Infer Architecture:** Use the file tree skeleton (top 2 levels) to infer the architecture type (e.g., Monorepo, Microservices, MVC).
    - **Infer Project Goal:** Summarize the project's goal in one sentence based on `README.md` header or `package.json` description.

7.  **Continue:** Upon completing the brownfield initialization protocol, proceed to Generate Product Guide.

### 3B. Greenfield Project Initialization Protocol

1.  **Announce Detection:** Inform the user that a new project will be initialized, briefly noting that no existing application code or dependencies were found.

2.  **Initialize Git:** If a `.git` directory does not exist, execute `git init` and report that a new Git repository has been initialized.

3.  **Inquire about Project Goal:** Ask the user using the `ask_user` tool:
    - **header:** "Project Goal"
    - **type:** "text"
    - **question:** "What do you want to build?"
    - **placeholder:** "e.g., A mobile app for tracking expenses"
    - **CRITICAL:** Do NOT execute any tool calls until the user has provided a response.

4.  **Initial Setup:**
    - Execute `mkdir -p conductor`.
    - Write the user's response into `conductor/product.md` under a header named `# Initial Concept`.

5.  **Continue:** Immediately proceed to Generate Product Guide.
