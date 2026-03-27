#!/usr/bin/env bash
# Link all skill directories to .claude/skills/
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_SRC="$PROJECT_ROOT/skills"
SKILLS_DST="$PROJECT_ROOT/.claude/skills"

# Create target directory
mkdir -p "$SKILLS_DST"

linked=0
skipped=0

for dir in "$SKILLS_SRC"/*/; do
  name="$(basename "$dir")"
  target="$SKILLS_DST/$name"

  if [ -L "$target" ]; then
    # Update existing symlink
    ln -sfn "$dir" "$target"
    echo "Updated: $name"
    ((linked++))
  elif [ -d "$target" ]; then
    echo "Skipped (real dir exists): $name"
    ((skipped++))
  else
    ln -s "$dir" "$target"
    echo "Linked:  $name"
    ((linked++))
  fi
done

echo ""
echo "Done: $linked linked, $skipped skipped → $SKILLS_DST"
