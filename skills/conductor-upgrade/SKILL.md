---
name: conductor-upgrade
description: Orchestrates the upgrade of Conductor skills to a new version. It synchronizes protocols, templates, and SKILL.md logic based on the latest .toml command definitions and template files. Use when a new Conductor reference version is available.
metadata:
  version: "1.0.0"
---

# Conductor Upgrade

## Overview

This skill provides a structured method for upgrading the **Conductor Skills Suite** to a new version of the Conductor framework. It ensures that every skill's "Surgical Logic" remains aligned with the latest `.toml` command prompts and that all static templates are correctly synchronized.

## Workflow

1.  **Version Identification:** Locate the latest Conductor reference directory within the project's root `references/` folder (e.g., `references/conductor-0.3.1/`). Always use the highest version number available.

2.  **Asset Synchronization:** Directly copy/overwrite static templates from the reference to the skill assets:
    -   `conductor/templates/workflow.md` -> `assets/templates/workflow.md`
    -   `conductor/templates/code_styleguides/*.md` -> `assets/templates/code_styleguides/*.md`
3.  **Protocol Alignment:** Read the `.toml` files in the new reference to identify logic changes. Update corresponding `references/*.md` in each skill (e.g., `resolution-protocol.md`, `project-discovery.md`).
4.  **Skill Logic Update:** Update the `SKILL.md` of each affected skill to reflect new workflows, question batching, or mandatory constraints introduced in the new version.
5.  **Metadata & Docs:** Update the `metadata.version` in each `SKILL.md` and append a version notice to the changelog in each `CLAUDE.md`.

## Implementation Details

Refer to the following protocol for detailed procedural instructions:

- **Upgrade Protocol:** [references/upgrade-protocol.md](references/upgrade-protocol.md) - Mapping `.toml` logic to Skill protocols and template sync.

## Mandatory Constraints

- **Logic Alignment over Copying:** You MUST read the `.toml` command prompts and align the skill's protocol documentation manually. NEVER simply copy `.toml` prompts into Skill reference files.
- **Template Parity:** Static templates (workflow and styleguides) MUST be byte-for-byte copies of the reference version.
- **Consistency:** All `conductor-*` skills MUST be updated to the same version simultaneously to avoid cross-skill protocol drift.
- **Git Hygiene:** Every upgrade phase concludes with a commit of the modified skills.
