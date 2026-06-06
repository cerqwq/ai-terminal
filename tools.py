"""
AI Terminal - AI终端工具
支持命令生成、脚本生成、Shell辅助
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AITerminalTools:
    """
    AI终端工具
    支持：命令、脚本、Shell
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_command(self, description: str, shell: str = "bash") -> str:
        """生成命令"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{shell}命令：

描述：{description}

只返回命令："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        return response.choices[0].message.content

    def explain_command(self, command: str) -> str:
        """解释命令"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请详细解释以下命令：

{command}

要求：
1. 整体功能
2. 每个参数
3. 使用场景"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def generate_script(self, task: str, shell: str = "bash") -> str:
        """生成脚本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{shell}脚本：

任务：{task}

要求：
1. 完整可运行
2. 错误处理
3. 注释说明
4. 使用说明"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def convert_command(self, command: str, target_shell: str) -> str:
        """转换命令"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下命令转换为{target_shell}格式：

{command}

只返回转换后的命令："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        return response.choices[0].message.content

    def debug_command(self, command: str, error: str) -> str:
        """调试命令"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请帮助调试以下命令：

命令：{command}
错误：{error}

请提供：
1. 错误原因
2. 解决方案
3. 修正后的命令"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def suggest_alias(self, command: str) -> Dict:
        """建议别名"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为以下命令建议简短别名：

{command}

请返回JSON格式：
{{
    "aliases": [
        {{"name": "别名", "command": "完整命令", "description": "说明"}}
    ]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"aliases": content}

    def generate_completion(self, tool_name: str, shell: str = "bash") -> str:
        """生成自动补全脚本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{tool_name}生成{shell}自动补全脚本：

要求：
1. 命令补全
2. 选项补全
3. 参数补全"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AITerminalTools:
    """创建终端工具"""
    return AITerminalTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Terminal Tools")
    print()

    # 测试
    cmd = tools.generate_command("查找当前目录下所有Python文件")
    print(f"Command: {cmd}")
