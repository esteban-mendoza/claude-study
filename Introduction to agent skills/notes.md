# Skills

- Folders, scripts and resources

## Purpose

- standards
  - commit message formats
  - brand guidelines
- specialized knowledge that applies to specific tasks

## Priority

1. Enterprise — managed settings, highest priority
2. Personal — your home directory (~/.claude/skills)
3. Project — the .claude/skills directory inside a repository
4. Plugins — installed plugins, lowest priority

## Format

- name: required. Max 64 characters
- description: required. Max 1024 characters
- license: optional
- compatibility: Max 500 characters. Indicates environment requirements (intended product, system packages, network access, etc.).
- metadata: dict
- allowed-tools: space-separated string of pre-approved tools the skill may use (experimental)

## Multi-file skills

- Progressive disclosure:
  - Keep SKILL.md short and focused.
    - Under 500 lines.
    - Link to supporting files
  - Use other files as needed
    - assets folder
    - references folder
    - scripts folder

- Use scripts. They don't load into context

## Skills vs. other features

- CLAUDE.md loads into every conversation
  - Project wide standards
  - Constraints
  - Framework preferences and coding style
- Skills load on demand.
  - Task-specific expertise
  - Knowledge that's only relevant sometimes
  - Expertise applies throughout a conversation
- Subagents run in a separate context
  - Delegate a task to a separate execution context
  - Different tool access than the main conversation
- Hooks fire on events
  - Operations that should run on every file save
  - Validations before/after specific tool calls
  - Automated side effects
- MCP servers provide external tools

## Sharing skills

- Version control
  - project/.claude/skills
- Plugins
  - plugin-project/skills
- Enterprise
  - `managed-settings.json`
- Subagents don't automatically see skills
  - Only custom subagents use skills
    - Add **skills** metadata field
    - Use `/agents` creator

## Troubleshooting

- Use [agent skills verifier](https://github.com/agent-ecosystem/skill-validator#what-it-checks)
- Multi-skills. Check for conflicts with other skills
- Make sure enterprise skills do not conflict with personal skills
- Clear the cache: 
    ```bash
    rm ~/.claude/plugins/cache
    ````
  
  - Then restart Claude
- If a skill uses external tools, add that into the description