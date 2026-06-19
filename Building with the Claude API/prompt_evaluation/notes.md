# Prompt evaluation

- Prompt engineering
  - Best practices to improve prompts
- Prompt evaluation
  - Testing to measure how well prompts work

## Ways of testing

- Test prompt once
- Test a few times
- Run an evaluation pipeline

## Evaluation workflow

1. Draft a prompt
2. Create an eval dataset
3. Feed through claude
4. Feed through grader
5. Change prompt and repeat

## Graders

Approaches:
- Code based
- Model based
  - The key insight is asking for strengths, weaknesses, and reasoning alongside the score
  - Without this context, models tend to default to middling scores around 6.
- Human based

Criteria
- Format
- Valid syntax
- Task following

Workflow
- Validate format
- 