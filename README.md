# Claude Study

## CORE

1. [x] Claude Code 101            → breadth: CLAUDE.md, plan mode, context mgmt, code review
2. [ ] Claude Code in Action      → depth: hooks + SDK, custom commands, controlling context
3. [ ] Introduction to subagents  → Domain 1 (27%) depth + context isolation
4. [ ] Introduction to agent skills → Domain 3 skill frontmatter + "which feature when"
5. [ ] Building with the API      → (in progress) Domains 2, 4

## OPTIONAL

6. [ ] Claude Platform 101        → agent loop explained, managed agents (SDK loop concepts)

## Still left for self-study

1. **MCP structured error responses** — isError, errorCategory, isRetryable, retryable vs. non-retryable
2. **Message Batches API** — 50% savings, 24-hr window, custom_id, no multi-turn tools, SLA math
3. **Domain 4 judgment patterns** — explicit criteria vs. vague instructions, false-positive reduction, multi-pass/independent review architectures
4. **Domain 5 reliability** — lost-in-the-middle, escalation calibration (policy gaps, not sentiment/confidence), error propagation, information provenance (claim-source mappings, conflict annotation, temporal data), confidence calibration (stratified sampling, accuracy segmentation)
5. **Agent SDK loop anti-patterns** — verify Platform 101's "agent loop" lesson covers stop_reason mechanics and why iteration caps / NL parsing are anti-patterns; if not, hit the SDK docs
