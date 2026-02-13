# Documentation Synchronization Protocol

## 1. Trigger
Execute ONLY when a track is marked `[x]` in the Tracks Registry.

## 2. Analysis
- Read the completed track's **Specification**.
- Analyze for new features, tech changes, or branding shifts.

## 3. Update Cycle
- **Product Definition:** Propose changes if the product's high-level description is impacted.
- **Tech Stack:** Propose changes if new technologies or architectural shifts occurred.
- **Product Guidelines (Strict):** ONLY propose changes for major strategic shifts (rebranding, etc.). WARN the user.

## 4. Confirmation and Commit
- Present proposed changes as diffs.
- ONLY apply edits after explicit user confirmation.
- **Commit:** `docs(conductor): Synchronize docs for track '<description>'`.
