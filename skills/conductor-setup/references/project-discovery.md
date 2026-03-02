# Project Discovery Protocol

## 1. Detect Project Maturity

Classify the project as "Brownfield" (Existing) or "Greenfield" (New) based on these indicators:

### Brownfield Indicators
- Existence of version control: `.git`, `.svn`, or `.hg`.
- `git status --porcelain` is not empty (dirty repo).
- Presence of dependency manifests: `package.json`, `pom.xml`, `requirements.txt`, `go.mod`.
- Presence of source code directories: `src/`, `app/`, `lib/` containing code files.

### Greenfield Condition
- Classify as **Greenfield** ONLY if NONE of the "Brownfield Indicators" are found AND the directory is empty or contains only generic documentation (e.g., `README.md`) without functional code or dependencies.

## 2. Brownfield Project Initialization Protocol

1.  **Request Permission:** Inform the user a brownfield project has been detected and ask for a read-only scan.
2.  **Code Analysis:**
    - Analyze `README.md` if it exists.
    - **Respect Ignore Files:** Combine `.geminiignore` and `.gitignore` patterns to exclude files/directories (e.g., `node_modules`).
    - **Triage:** Use `git ls-files --exclude-standard -co | xargs -n 1 dirname | sort -u` to list relevant directories. Focus on manifest files first.
    - **Handle Large Files:** For any single file >1MB, DO NOT read the entire file. Use `head` and `tail` to read only the first and last 20 lines.
3.  **Extract and Infer Context:**
    - **Strict File Access:** Base analysis SOLELY on provided snippets and directory structure.
    - **Extract Tech Stack:** Identify Language, Frameworks, Database Drivers.
    - **Infer Architecture:** Use top-level file tree skeleton to infer type (e.g., Monorepo, MVC).
    - **Infer Project Goal:** Summarize the project's goal in one sentence based on `README.md` or `package.json`.

## 3. Greenfield Project Initialization Protocol

1.  **Initialize Git:** Run `git init` if `.git` is missing.
2.  **Inquire Goal:** Ask "What do you want to build?".
3.  **Setup Directory:** Create `conductor/` and `conductor/setup_state.json` (`{"last_successful_step": ""}`).
4.  **Initial Concept:** Write user's response to `conductor/product.md` under `# Initial Concept`.
