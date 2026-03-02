# Upgrade Protocol

## 1. Map .toml to Protocols

Each Conductor `.toml` file in the project's root `references/conductor-X.Y.Z/commands/conductor/` corresponds to one or more Skill protocols:


- **setup.toml:** 
  - [Project Discovery] -> `references/project-discovery.md`
  - [Product Setup] -> `references/product-setup.md`
  - [Configuration] -> `references/configuration.md`
  - [Track Generation] -> `references/track-generation.md`
- **newTrack.toml:**
  - [Track Planning] -> `references/track-planning.md`
- **implement.toml:**
  - [Implementation Logic] -> `references/implementation-protocol.md`
  - [Synchronization Logic] -> `references/synchronization.md`
- **revert.toml:**
  - [Revert Logic] -> `references/revert-protocol.md`
- **review.toml:**
  - [Review Logic] -> `references/review-protocol.md`
- **status.toml:**
  - [Status Logic] -> `references/status-protocol.md`

### Alignment Checklist:
- Does the `.toml` include new `ask_user` questions (like batching or choices)? Update the protocol.
- Does the `.toml` include new Git commands or file parsing logic? Update the protocol.
- Does the `.toml` include new constraints (like "flash" model preference)? Update the protocol.

## 2. Template Synchronization

For `conductor-setup`, ensure that:
- `references/conductor-X.Y.Z/templates/workflow.md` is copied to `assets/templates/workflow.md`.
- `references/conductor-X.Y.Z/templates/code_styleguides/*.md` is copied to `assets/templates/code_styleguides/*.md`.

The source of these files is always the latest `conductor-X.Y.Z` directory found in the project's root `references/` folder.

## 3. Metadata and Changelog

For **each** `conductor-*` skill:
- Update the frontmatter:
  ```yaml
  metadata:
    version: "X.Y.Z"
  ```
- Append a dated entry to `CLAUDE.md` explaining the major version changes.
