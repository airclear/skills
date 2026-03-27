#!/usr/bin/env bash
# Create a date-based git tag and publish a GitHub release
#
# Usage:
#   release.sh                  # Auto-generate tag from today's date
#   release.sh 2026-03-27       # Use specified date as tag
#   release.sh 2026-03-27 v2    # Use date + suffix to avoid collisions
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

# --- Parse arguments ---
TAG_DATE="${1:-$(date +%Y-%m-%d)}"
TAG_SUFFIX="${2:-}"

# Validate date format
if ! date -j -f "%Y-%m-%d" "$TAG_DATE" &>/dev/null 2>&1; then
  echo "Error: Invalid date format '$TAG_DATE'. Expected YYYY-MM-DD." >&2
  exit 1
fi

# Build tag name
TAG_NAME="${TAG_DATE}${TAG_SUFFIX:+-$TAG_SUFFIX}"

# --- Pre-flight checks ---
if ! command -v gh &>/dev/null; then
  echo "Error: 'gh' CLI is not installed." >&2
  exit 1
fi

if ! gh auth status &>/dev/null 2>&1; then
  echo "Error: Not authenticated with GitHub CLI. Run 'gh auth login'." >&2
  exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
  echo "Error: Working tree has uncommitted changes. Commit or stash first." >&2
  exit 1
fi

# Check if tag already exists
if git rev-parse "$TAG_NAME" &>/dev/null; then
  echo "Error: Tag '$TAG_NAME' already exists (points to $(git rev-parse --short "$TAG_NAME"))." >&2
  echo "       Use a suffix to create a new tag, e.g.: $0 $TAG_DATE v2" >&2
  exit 1
fi

# Check if remote is up-to-date
BRANCH=$(git rev-parse --abbrev-ref HEAD)
git fetch origin "$BRANCH" --quiet 2>/dev/null || true
LOCAL_SHA=$(git rev-parse HEAD)
REMOTE_SHA=$(git rev-parse "origin/$BRANCH" 2>/dev/null || echo "")
if [ -n "$REMOTE_SHA" ] && [ "$LOCAL_SHA" != "$REMOTE_SHA" ]; then
  echo "Error: Local branch is out of sync with origin/$BRANCH." >&2
  echo "       Run 'git push' first." >&2
  exit 1
fi

# --- Generate release notes from recent commits ---
PREV_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
if [ -n "$PREV_TAG" ]; then
  CHANGELOG=$(git log "$PREV_TAG"..HEAD --pretty=format:"- %s (%h)" --no-merges)
else
  CHANGELOG=$(git log HEAD --pretty=format:"- %s (%h)" --no-merges -10)
fi

if [ -z "$CHANGELOG" ]; then
  CHANGELOG="- No changes since last tag"
fi

RELEASE_BODY=$(cat <<EOF
## Changes

${CHANGELOG}

---
*Released on $(date +%Y-%m-%d)*
EOF
)

# --- Create tag and push ---
echo "Tag:    $TAG_NAME"
echo "Branch: $BRANCH"
echo "Commit: $(git rev-parse --short HEAD)"
echo ""
echo "--- Release Notes ---"
echo "$RELEASE_BODY"
echo ""

read -rp "Proceed with release? [y/N] " confirm
if [[ "$confirm" != [yY] ]]; then
  echo "Aborted."
  exit 0
fi

# Create and push tag
git tag -a "$TAG_NAME" -m "Release $TAG_NAME"
git push origin "$TAG_NAME"

# Create GitHub release
echo "Creating GitHub release..."
gh release create "$TAG_NAME" \
  --title "Release $TAG_NAME" \
  --notes "$RELEASE_BODY" \
  --target "$BRANCH"

echo ""
echo "Done! Release published: https://github.com/$(gh repo view --json nameWithOwner -q .nameWithOwner)/releases/tag/$TAG_NAME"
