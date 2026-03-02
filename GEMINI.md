# GEMINI Project Context: SefWorks Skills

This repository is a modular **AI Agent Skills Library** designed for use with Gemini CLI and other Agent-based workflows. It follows the [Agent Skills Specification](./spec/Agent%20Skills%20Spec.md) and incorporates the **BMad Method** and **Conductor** frameworks.

## 📁 Directory Overview

- **`skills/`**: The core of the repository. Contains individual skill modules.
    - **`conductor-*/`**: Skills for project management, implementation, and lifecycle (Setup, NewTrack, Implement, Status, Review, Revert, Upgrade).
    - **`bmad-brainstorming-coach/`**: A creative skill for innovation and brainstorming.
- **`spec/`**: Contains the **Agent Skills Spec**, defining the required directory structure (`SKILL.md`, `references/`, `assets/`, `scripts/`) and frontmatter format.
- **`references/`**: Source materials and framework versions.
    - **`conductor-0.3.1/`**: The reference implementation for Conductor commands.
    - **`bmad-6.0.4/`**: The reference implementation for BMad workflows.
- **`docs/`**: General project documentation.
- **`dist/`**: Reserved for build outputs or packaged skills.

## 🛠️ Key Technologies & Frameworks

- **Conductor (v0.3.1)**: A spec-driven development framework for managing project context and implementation tracks.
- **BMad Method (v6.0.4)**: An AI-driven development workflow framework.
- **Agent Skills Spec**: A standardized format for portable AI instructions.

## 📖 Usage & Development Conventions

### Skill Structure
Every skill MUST have a `SKILL.md` with valid YAML frontmatter:
```yaml
---
name: skill-name
description: Clear intent-based description.
metadata:
  version: "X.Y.Z"
---
```
Optional subdirectories:
- `references/`: 精简的协议文档 (Surgical logic).
- `assets/`: 静态模板 (Byte-for-byte copies from framework sources).

### Upgrading Conductor Skills
When a new version of Conductor is released in the root `references/` folder, use the **Surgical Update** process:
1.  **Sync Assets**: Copy `workflow.md` and `code_styleguides/` from the new reference to skill `assets/`.
2.  **Align Protocols**: Read the `.toml` prompts in the reference and manually update the protocol `.md` files in the skill's `references/`.
3.  **Update SKILL.md**: Reflect new workflows or constraints in the main skill instructions.
4.  **Version Bump**: Update `metadata.version` and the `CLAUDE.md` changelog.

### Mandatory Constraints
- **Universal File Resolution Protocol**: Always use the defined protocol (found in `conductor-setup/references/resolution-protocol.md`) to locate project artifacts like `product.md` or `plan.md`.
- **TDD Requirement**: The Conductor workflow strictly enforces Test-Driven Development (Red/Green/Refactor).
- **Git Hygiene**: Changes to project tracks and plans must be committed with specific prefixes (e.g., `chore(conductor)`, `fix(conductor)`, `docs(conductor)`).

## 📝 Common Commands (Conceptual)
These are commands typically used by the Agent when a skill is activated:
- `/conductor:setup`: Scaffolding a new/existing project.
- `/conductor:newTrack <desc>`: Planning a new feature.
- `/conductor:implement`: Executing the next task in the plan.
- `/conductor:status`: Viewing project health.
- `/conductor:review`: Performing a code review.
- `/conductor:revert`: Undoing a track/phase/task.
