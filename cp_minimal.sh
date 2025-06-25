#!/bin/bash

ALFOLIO_DIR="../al-folio"
TARGET_DIR="."

declare -a ITEMS=(
  "_config.yml"
  "index.md"
  "_layouts"
  "_includes"
  "_sass"
  "_data"
  "assets"
  "_posts"
  "_pages"
  "_projects"
  "_news"
  "_bibliography"
  "cv.md"
  "publications.md"
)

for item in "${ITEMS[@]}"; do
  SRC="$ALFOLIO_DIR/$item"
  DEST="$TARGET_DIR/$item"

  if [ -e "$SRC" ]; then
    if [ -d "$SRC" ]; then
      cp -r "$SRC" "$DEST"
    else
      cp "$SRC" "$DEST"
    fi
    echo "Copied: $item"
  else
    echo "Skipped (not found): $item"
  fi
done
