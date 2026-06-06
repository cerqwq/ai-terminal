# 💻 AI Terminal

AI终端工具，支持命令生成、脚本生成、Shell辅助。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 💻 命令生成
- 📖 命令解释
- 📝 脚本生成
- 🔄 命令转换
- 🐛 命令调试
- 🏷️ 别名建议

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_terminal import create_tools

tools = create_tools()

# 命令生成
cmd = tools.generate_command("查找所有Python文件")

# 命令解释
explanation = tools.explain_command("find . -name '*.py'")

# 脚本生成
script = tools.generate_script("批量重命名文件")

# 命令转换
converted = tools.convert_command("ls -la", "powershell")

# 命令调试
fix = tools.debug_command("python app.py", "ModuleNotFoundError")

# 别名建议
aliases = tools.suggest_alias("git status")
```

## 📁 项目结构

```
ai-terminal/
├── tools.py       # 终端工具核心
└── README.md
```

## 📄 许可证

MIT License
