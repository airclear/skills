# BMad Framework to Agent Skills Conversion Plan

This document outlines the strategy for converting the BMad (v6.0.4) framework into the Agent Skills format, ensuring source integrity while optimizing for developer experience and context efficiency.

## 1. Core Philosophy
*   **Domain Aggregation:** Instead of atomic skills per workflow, group by major BMad modules (`core`, `bmm`, `tea`) to reduce fragment management.
*   **Zero-Modification Source:** Treat BMad source files as read-only. Copy entire module directories into `assets/` to preserve internal relative paths and logic.
*   **Dynamic Orchestration:** Use `SKILL.md` as a high-level router that instructs the agent to "self-discover" capabilities via `module-help.csv`.

## 2. Proposed Skill Structure

### bmad-core
*   **Purpose:** Basic elicitation, brainstorming, help routing, and master agent definitions.
*   **Source Root:** `references/bmad-6.0.4/core/` and `_config/`.
*   **Mapping:** 
    *   `skills/bmad-core/assets/source/core/`
    *   `skills/bmad-core/assets/source/_config/`

### bmad-bmm
*   **Purpose:** 30+ SDLC Workflows (Analysis, Planning, Solutioning, Implementation).
*   **Source Root:** `references/bmad-6.0.4/bmm/`.
*   **Mapping:** 
    *   `skills/bmad-bmm/assets/source/bmm/`

### bmad-tea
*   **Purpose:** Test Architecture, tiered knowledge loading, and specialized QA agents.
*   **Source Root:** `references/bmad-6.0.4/tea/`.
*   **Mapping:** 
    *   `skills/bmad-tea/assets/source/tea/`

## 3. Implementation Specification

### 3.1 SKILL.md Template (The "Router" Pattern)
Every BMad-based skill will follow this logic in its `SKILL.md`:
1.  **Identity:** Define the module's role (e.g., "Product Management & Development Specialist").
2.  **Discovery Protocol:** Instruct the agent to read `assets/source/[module]/module-help.csv` upon activation to map available workflows to user intent.
3.  **Execution Protocol:** Provide instructions on how to interpret BMad artifacts (.xml, .md) and how to assume roles defined in `agents/`.

### 3.2 Assets Organization
```text
skills/bmad-bmm/
├── SKILL.md
├── assets/
│   └── source/             <-- Direct copy from references/bmad-6.0.4/
│       ├── bmm/
│       │   ├── module-help.csv
│       │   ├── agents/
│       │   └── workflows/
│       └── _config/        <-- Shared config needed for execution
```

## 4. Maintenance & Upgrade Path

### 4.1 Sync Automation
A dedicated maintenance skill (or script) will handle version upgrades:
*   **Trigger:** New version detected in `references/bmad-x.y.z/`.
*   **Action:** 
    1. Update version metadata in `skills/bmad-*/SKILL.md`.
    2. Wipe and re-copy the `assets/source/` folders.
    3. Validate against the Agent Skills Spec.

### 4.2 Handling Redundancy
While copying `_config/` into multiple skills creates disk redundancy, it ensures each skill is **self-contained** and functional in any Agent environment (IDE, CLI, Cloud) without assuming the presence of other skills or a specific global directory structure.

## 5. Next Steps
1.  [ ] Prototype `bmad-core` as the first aggregate skill.
2.  [ ] Define the "Discovery Protocol" prompt in `SKILL.md` to ensure agents can find workflows.
3.  [ ] Test orchestration efficiency: Does the agent successfully find a BMM workflow within the aggregate skill?
