# Introduction to subagents

Custom subagents .claude/agents/<name>.md

Markdown with YAML frontmatter:
- name
- description
- tools
- model: haiku, sonnet, opus, *inherit*
- color

`/agents` to create new agent

Tips:
- Use the word 'proactively' to the description if you want Claude to suggest using it more commonly

## Effective subagents

- Tail the description so the main agent knows what is the correct input for and return of the subagent. 
- Use output formats in the system prompt
- Subagents must report obstacles
- Tail `tools` access

## Using subagents

- When exploration is separate from execution.
  - **Does intermediate work matter?**
- Patterns: 
  - research and investigation
  - tasks needing custom instructions
    - applying custom system prompts
    - code review
  - Truly independent
  - Return rich outputs (not hiding any important details)
- Antipatterns:
  - Expert claims
  - Multi-step pipelines (each step depends on previous steps)
  - Test runners