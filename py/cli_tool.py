import anyio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock


async def claude_code_async(prompt, cwd):
    # With options
    options = ClaudeAgentOptions(
        cwd=cwd,
        permission_mode='acceptEdits'
    )

    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)