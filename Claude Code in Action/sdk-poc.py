import shutil
from dataclasses import asdict

import anyio
from claude_agent_sdk import ClaudeAgentOptions, query
from rich import print as rprint
from rich.pretty import Pretty

options = ClaudeAgentOptions(
    cli_path=shutil.which("claude"),  # Force system CLI
    setting_sources=["user", "project", "local"],
)


def append(msg):
    with open("response.txt", "a") as file:
        file.write(str(msg) + "\n")

def prettify(msg):
    rprint(Pretty(asdict(msg), expand_all=True))


async def main():
    prompt="What is the deepest and most niche cientific piece of knowledge you have regarding mythology?"
    async for msg in query(prompt=prompt, options=options):
        prettify(msg)


if __name__ == "__main__":
    anyio.run(main)
