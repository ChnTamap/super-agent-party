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
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage,ResultMessage, TextBlock
from py.get_setting import load_settings

from typing import AsyncIterator

async def claude_code_async(prompt) -> str | AsyncIterator[str]:
    """返回 str（报错）或 AsyncIterator[str]（正常流式输出）。"""
    # 1. 环境变量检查
    for key in ("ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL", "ANTHROPIC_MODEL"):
        if key not in os.environ:
            return f"Error: {key} environment variable not set. Please check your shell configuration files (.zshrc, .bash_profile, etc.)"

    # 2. 工作目录检查
    settings = await load_settings()
    cwd = settings.get("CLISettings", {}).get("cc_path")
    if not cwd or not cwd.strip():
        return "No working directory is set, please set the working directory first!"

    # 3. 正常场景：返回异步生成器
    async def _stream() -> AsyncIterator[str]:
        options = ClaudeAgentOptions(
            cwd=cwd,
            permission_mode='acceptEdits',
            continue_conversation=True,
            env={
                'ANTHROPIC_API_KEY': os.environ['ANTHROPIC_API_KEY'],
                'ANTHROPIC_BASE_URL': os.environ['ANTHROPIC_BASE_URL'],
                'ANTHROPIC_MODEL': os.environ['ANTHROPIC_MODEL'],
            }
        )
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        yield block.text

    return _stream()

claude_info = """Claude Code，Anthropic 官方的 Claude CLI
  工具。这是一个交互式命令行工具，专门帮助用户完成软件工程任务。

  可以协助您：
  - 编写、调试和重构代码
  - 搜索和分析文件内容
  - 运行构建和测试
  - 管理 Git 操作
  - 代码审查和优化
  - 以及其他编程相关的任务

  运行在您的本地环境中，可以访问文件系统并使用各种工具来帮助您完成工作。
"""

claude_code_tool = {
    "type": "function",
    "function": {
        "name": "claude_code_async",
        "description": f"你可以和控制CLI的智能体Claude Code进行交互。{claude_info}",
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