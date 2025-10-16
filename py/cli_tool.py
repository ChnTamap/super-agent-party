#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def get_shell_environment():
    """通过子进程获取完整的 shell 环境"""
    shell = os.environ.get('SHELL', '/bin/zsh')
    home = Path.home()
    
    # 尝试不同的配置文件
    config_commands = [
        f'source {home}/.zshrc && env',
        f'source {home}/.bash_profile && env', 
        f'source {home}/.bashrc && env',
        'env'  # 最后回退到当前环境
    ]
    
    for cmd in config_commands:
        try:
            result = subprocess.run(
                [shell, '-i', '-c', cmd],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                # 解析环境变量输出
                for line in result.stdout.splitlines():
                    if '=' in line:
                        var_name, var_value = line.split('=', 1)
                        os.environ[var_name] = var_value
                print("Successfully loaded environment from shell")
                return
        except Exception as e:
            print(f"Failed to load environment with command '{cmd}': {e}")
            continue
    
    print("Warning: Could not load shell environment, using current environment")

# 在导入 Claude SDK 之前设置环境变量
get_shell_environment()

# 现在导入 Claude SDK
import anyio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock
from py.get_setting import load_settings

async def claude_code_async(prompt):
    # Validate environment variables
    if 'ANTHROPIC_API_KEY' not in os.environ:
        return "Error: ANTHROPIC_API_KEY environment variable not set. Please check your shell configuration files (.zshrc, .bash_profile, etc.)"

    if 'ANTHROPIC_BASE_URL' not in os.environ:
        return "Error: ANTHROPIC_BASE_URL environment variable not set. Please check your shell configuration files (.zshrc, .bash_profile, etc.)"
    
    if 'ANTHROPIC_MODEL' not in os.environ:
        return "Error: ANTHROPIC_MODEL environment variable not set. Please check your shell configuration files (.zshrc, .bash_profile, etc.)"
    
    
    settings = await load_settings()
    CLISettings = settings["CLISettings"]
    cwd = CLISettings["cc_path"]
    
    if cwd is None or cwd.strip() == "":
        return "No working directory is set, please set the working directory first!"
    
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