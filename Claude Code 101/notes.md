# Notes

## The Agentic Loop

- Gather context
- Take action
- Verify results

## The Explore → Plan → Code → Commit Workflow

- Use plan mode
- Review with a Subagent
- Use the /commit-push-pr skill
- Session Linking with --from-pr

When Claude creates a PR through gh pr create, the session gets linked to that PR automatically. If you need to come back to it later — maybe to address review comments or fix a failing build — run:

```bash
claude --from-pr <PR_NUMBER>
```

This picks up right where you left off.

## Subagents

Built-in subagents:
- General purpose (multi-step)
- Explore 
- Plan (used in plan mode)

## Skills

- .claude/skills (personal)
- project/.claude/skills (project)

## MCP

Use `claude mcp add`

- stdio MCPs for local processes

- Local: current project for me
- User: ~/.claude.json
- Project: project/.mcp.json

## Hooks

- Deterministic
- Always run
- settings.json
- Config
  - Event
  - Matcher (optional)
  - Command that runs
- Examples
  - UserPromptSubmit: 
    - after submitting a prompt
    - before claude processes it
  - PreToolUse
    - before a tool call
  - PostToolUse
    - after a tool call
  - Notification
    - when claude sends a notification
  - Stop
    - when claude finishes responding

```json
{
    "PostToolUse": [
        {
            "matcher": "Edit|MultiEdit|Write",
            "hooks": [
                {
                    "type": "command",
                    "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/auto-format.sh",
                    "timeout": 20
                }
            ]
        }
    ]
}
```
