---
name: bmad-sync
description: Maintenance skill for synchronizing BMad framework source files from the project root (references/) to aggregate skills (bmad-core, bmad-bmm, bmad-tea). Use when a new BMad version is released or when source files need to be refreshed.
metadata:
  version: "1.0"
  author: airclear
---

# BMad Synchronization Skill

You are a maintenance specialist for the BMad Agent Skills Library. Your goal is to ensure all aggregate BMad skills reflect the latest source version from the root `references/` directory.

## 🛠 Synchronization Protocol

When asked to "sync bmad" or "upgrade bmad skills", follow these steps:

### 1. Version Detection
Identify the source directory in the root `references/bmad-[version]/`.
- **Current Target Version:** (Check directory name, e.g., `6.0.4`)

### 2. Module Mapping & Sync
Execute a clean sync (wipe `assets/source/` first) for each module:

- **bmad-core:**
  - Sync `_config/` -> `skills/bmad-core/assets/source/_config/`
  - Sync `core/` -> `skills/bmad-core/assets/source/core/`
- **bmad-bmm:**
  - Sync `_config/` -> `skills/bmad-bmm/assets/source/_config/`
  - Sync `bmm/` -> `skills/bmad-bmm/assets/source/bmm/`
- **bmad-tea:**
  - Sync `_config/` -> `skills/bmad-tea/assets/source/_config/`
  - Sync `tea/` -> `skills/bmad-tea/assets/source/tea/`

### 3. Metadata Update
For each synchronized skill, update its `SKILL.md` YAML frontmatter:
- Set `metadata.version` to the detected BMad version.
- (Optional) Append a changelog entry to `CLAUDE.md` if present.

### 4. Validation
After syncing, verify that `module-help.csv` exists in each skill's `assets/source/` and conforms to the Agent Skills specification using `skills-ref validate` if available.

## 🚀 Execution Commands (Example)
```bash
# Clean and Sync Core
rm -rf skills/bmad-core/assets/source/*
mkdir -p skills/bmad-core/assets/source/_config skills/bmad-core/assets/source/core
cp -rv references/bmad-6.0.4/_config/* skills/bmad-core/assets/source/_config/
cp -rv references/bmad-6.0.4/core/* skills/bmad-core/assets/source/core/
```

## 📂 Reference
Detailed sync instructions can be found in [Sync Protocol](references/sync-protocol.md).
