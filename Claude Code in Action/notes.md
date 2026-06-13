# Claude Code in Action

## Hooks

Defined in
- Global: ~/.claude/settings.json
- Project: project/.claude/settings.json
- Project (not committed): project/settings.local.json

Write by hand or using `/hooks`.

### Security Best Practices

Key practices for secure hooks:

1. Validate and sanitize inputs
2. Always quote shell variables - `"$VAR"` not `$VAR`
3. Block path traversal - Check for .. in file paths
4. Use absolute paths - Specify full paths for scripts
5. Skip sensitive files - Avoid .env, .git/, keys, etc.
