import anyio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock
from py.get_setting import load_settings

async def claude_code_async(prompt):
    settings = await load_settings()
    CLISettings= settings["CLISettings"]
    cwd = CLISettings["cc_path"]
    if cwd is None or cwd.strip() == "":
        return "No working directory is set, please set the working directory first!"
    # With options
    options = ClaudeAgentOptions(
        cwd=cwd,
        permission_mode='acceptEdits',
        continue_conversation=True,
    )
    buffer = []
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)
                    buffer.append(block.text)
    return "\n\n".join(buffer)

claude_code_tool = {
    "type": "function",
    "function": {
        "name": "claude_code_async",
        "description": "你可以和控制CLI的智能体Claude Code进行交互，他可以帮你控制本地文件系统、例如增删查改本地文件，也可以生成代码文件并执行和返回结果。当用户提出一些需要和本地文件系统交互的需求时，你可以使用这个工具来满足用户需求。",
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "你想让Claude Code执行的指令，例如：请帮我创建一个文件，文件名为test.txt，文件内容为hello world",
                }
            },
            "required": ["prompt"],
        },
    },
}