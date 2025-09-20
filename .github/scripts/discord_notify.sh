#!/usr/bin/env bash
set -euo pipefail

# Simple helper to post a message to Discord webhook. Two modes:
#   push - build message for a push event (expects GITHUB_* env vars)
#   pr_merged - build message for a merged PR (expects PR_* and MERGED_BY env vars)

mode=${1:-}
if [ -z "$mode" ]; then
  echo "Usage: $0 <push|pr_merged>" >&2
  exit 2
fi

if [ -z "${WEBHOOK:-}" ]; then
  echo "WEBHOOK env missing" >&2
  exit 2
fi

build_push_message() {
  ref=${GITHUB_REF#refs/heads/}
  commit_url="${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/commit/${GITHUB_SHA}"
  lines=(
    "**Update** in ${GITHUB_REPOSITORY}"
    "Branch: '${ref}'"
    "Pusher: ${GITHUB_ACTOR}"
    "Commit: <${commit_url}>"
  )
  content=""
  for l in "${lines[@]}"; do
    if [ -z "$content" ]; then
      content="$l"
    else
      content="$content\n$l"
    fi
  done
  printf '%s' "$content"
}

build_pr_message() {
  pr_url="${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/pull/${PR_NUMBER}"
  lines=(
    "**PR merged** in ${GITHUB_REPOSITORY}"
    "Title: ${PR_TITLE}"
    "Number: ${PR_NUMBER}"
    "Author: ${PR_USER}"
    "Merged by: ${MERGED_BY}"
    "${pr_url}"
  )
  content=""
  for l in "${lines[@]}"; do
    if [ -z "$content" ]; then
      content="$l"
    else
      content="$content\n$l"
    fi
  done
  printf '%s' "$content"
}

if [ "$mode" = "push" ]; then
  content=$(build_push_message)
elif [ "$mode" = "pr_merged" ]; then
  content=$(build_pr_message)
else
  echo "Unknown mode: $mode" >&2
  exit 2
fi

# Use python to safely JSON-encode the content
json=$(python -c "import json,sys; print(json.dumps({'content': sys.argv[1]}))" "$content")
curl -s -H "Content-Type: application/json" -d "$json" "$WEBHOOK"
