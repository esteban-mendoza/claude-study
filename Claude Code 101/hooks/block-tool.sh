#!/bin/bash
# PreToolUse hook: Block dangerous bash commands
# Exit 2 = block (stderr feeds back to Claude). Exit 0 = allow

COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -qE 'rm\s+(-[a-zA-Z]*f[a-zA-Z]*\s+|.*-rf\s+)(/|\.|~)'; then
    echo "Blocked: destructive rm command" >&2
    exit 2
fi

if echo "$COMMAND" | grep -qE 'git\s+push\s+.*--force[^-]'; then
    echo "Blocked: force push - use --force-with-lease instead" >&2
    exit 2
fi

exit 0