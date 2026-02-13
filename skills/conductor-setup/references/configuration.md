# Configuration Protocol

## 1. Select Code Style Guides
- List templates from `assets/templates/code_styleguides/`.
- **Greenfield:** Recommend based on Tech Stack.
- **Brownfield:** State inferred selection and ask for confirmation.
- **Action:** `mkdir -p conductor/code_styleguides` and copy selected `.md` files.

## 2. Select Workflow (`workflow.md`)
- Copy `assets/templates/workflow.md` to `conductor/workflow.md`.
- **Customization Options:**
    - Test coverage percentage (Default: 80%).
    - Commit frequency (Task vs Phase).
    - Task summary storage (Git Notes vs Commit Message).
- Update `conductor/workflow.md` based on responses.

## 3. Finalization
- Create `conductor/index.md` as the project context index.
- Summarize all actions taken.
