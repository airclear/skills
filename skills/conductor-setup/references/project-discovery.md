# Project Discovery Protocol

## 1. Detect Project Maturity

Classify the project as "Brownfield" (Existing) or "Greenfield" (New) based on these indicators:

### Brownfield Indicators
- Existence of `.git`, `.svn`, or `.hg`.
- `git status --porcelain` is not empty (dirty repo).
- Presence of dependency manifests: `package.json`, `pom.xml`, `requirements.txt`, `go.mod`.
- Presence of source directories: `src/`, `app/`, `lib/` containing code.

### Greenfield Condition
- Classify as **Greenfield** ONLY if NONE of the "Brownfield Indicators" are found AND the directory is empty or contains only generic documentation (e.g., `README.md`).

## 2. Brownfield Initialization Protocol

1.  **Request Permission:** Inform the user and ask for a read-only scan (Yes/No).
2.  **Code Analysis:**
    - Analyze `README.md` if it exists.
    - **Respect Ignore Files:** Use `.geminiignore` and `.gitignore`.
    - **Triage:** Focus on manifests (`package.json`, etc.) first.
    - **Handle Large Files:** For files >1MB, read only the first and last 20 lines.
3.  **Extract Context:**
    - Identify Language, Frameworks, Database Drivers.
    - Infer Architecture (Monorepo, MVC, etc.).
    - Summarize Project Goal.

## 3. Greenfield Initialization Protocol

1.  **Initialize Git:** Run `git init` if `.git` is missing.
2.  **Inquire Goal:** Ask "What do you want to build?".
3.  **Setup Directory:** Create `conductor/` and `conductor/setup_state.json` (`{"last_successful_step": ""}`).
4.  **Initial Concept:** Write user's response to `conductor/product.md` under `# Initial Concept`.
