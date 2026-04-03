# Project Workflow

## Guiding Principles

1. **The Plan is the Source of Truth:** All work must be tracked in `plan.md`
2. **The Tech Stack is Deliberate:** Changes to the tech stack must be documented in `tech-stack.md` *before* implementation
3. **Test-Driven Development:** Write unit tests before implementing functionality
4. **High Code Coverage:** Aim for >80% code coverage for all modules
5. **Non-Interactive & CI-Aware:** Prefer non-interactive commands; use `CI=true` for watch-mode tools

## Task Workflow

All tasks follow this lifecycle:

1. **Select Task** — choose next available task from `plan.md`
2. **Mark In Progress** — change `[ ]` to `[~]` in `plan.md`
3. **Red Phase** — write failing tests first; confirm they fail
4. **Green Phase** — implement minimum code to pass tests
5. **Update Release Artifacts** — if DB/config changes, update `docs/release-artifacts/`
6. **Refactor** — improve clarity without changing behavior
7. **Verify Coverage** — target >80% for new code
8. **Commit** — conventional commit message
9. **Attach Git Note** — summarize task in `git notes`
10. **Update Plan** — mark `[x]` with commit SHA

## Quality Gates

Before marking any task complete:

- [ ] All tests pass
- [ ] Code coverage >80%
- [ ] Follows code style guidelines (`conductor/code_styleguides/`)
- [ ] No linting / static analysis errors
- [ ] Release artifacts updated if applicable
- [ ] No security vulnerabilities introduced

## Commit Guidelines

```
<type>(<scope>): <description>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Definition of Done

1. All code implemented to specification
2. Unit tests written and passing
3. Code coverage meets requirements
4. Documentation complete (if applicable)
5. Changes committed with proper message
6. Git note with task summary attached
