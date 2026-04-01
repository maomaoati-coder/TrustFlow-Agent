# 🛡️ TrustFlow-Agent

> **Enterprise-Grade Trusted AI Agent with Audit-First Architecture**
> 
> *Verified on Android/Termux & Edge Devices*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Build: Passing](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/YourUsername/TrustFlow-Agent)
[![Device: Termux Verified](https://img.shields.io/badge/Device-Termux%20Verified-blue.svg)](https://github.com/YourUsername/TrustFlow-Agent)

---

## 🌟 Overview / 项目概述

**TrustFlow-Agent** is a lightweight, high-reliability AI Agent framework designed to solve the "Black Box" problem in LLM decision-making. 

Unlike traditional agents, TrustFlow implements a **Strict Verification Gate** at every step, ensuring that tool outputs are audited before the next action. This makes it ideal for financial, medical, or critical system automation.

**TrustFlow-Agent** 是一个轻量级、高可靠的 AI Agent 框架，旨在解决大模型决策中的“黑盒”和“幻觉”问题。通过内置的**验证网关**，确保每一步操作在进入下一步之前都经过严格审计。

---

## 🚀 Key Features / 核心特性

- **🛡️ Hallucination Guard:** Mandatory validation nodes to intercept `Error/Failed` outputs. (内置防幻觉守卫)
- **📱 Edge-Native:** Optimized and verified on **Termux (Android)**. Perfect for private, offline agents. (边缘设备原生支持)
- **📝 Traceable Audit:** Automatically logs every decision point for human review. (全链路决策审计)
- **⚡ Zero Bloat:** Pure Python implementation with minimal dependencies. (极简架构，零冗余)

---

## 🏗️ Architecture / 技术架构

```mermaid
graph TD
    User[User Input] --> Plan[Planner Node]
    Plan --> Exec[Tool Execution]
    Exec --> Gate{Verification Gate}
    Gate -- "Invalid/Error" --> Plan
    Gate -- "Verified" --> Audit[Audit Trail & Output]
    Audit --> End((Success))

graph TD
    User[User Input] --> Plan[Planner Node]
    Plan --> Exec[Tool Execution]
    Exec --> Gate{Verification Gate}
    Gate -- "Invalid" --> Plan
    Gate -- "Verified" --> Audit[Audit Trail & Output]
    Audit --> Success((Success))

How to Run Tests:
# Install dependencies
pip install pytest

# Run the test suite
pytest test_trust.py

Verified Output:
platform android -- Python 3.13.x, pytest-9.x.x
rootdir: /data/data/com.termux/files/home
collected 2 items

test_trust.py ..                                [100%]

================== 2 passed in 0.01s ==================

🛠️ Installation / 安装

git clone [https://github.com/maomaoati-coder/TrustFlow-Agent.git](https://github.com/maomaoati-coder/TrustFlow-Agent.git)
cd TrustFlow-Agent
pip install -r requirements.txt

🗺️ Roadmap / 路线图
​[x] Core Verification Logic (Pure Python)
​[ ] LangGraph State Machine Integration
​[ ] Mobile-First Low-Code UI (Coming Soon!)
​[ ] Local LLM Support (Ollama/Llama.cpp integration)

​🤝 Contributing / 贡献
​Contributions are welcome! If you find a bug or have a feature request, please open an issue.
​欢迎提交 Issue 或 Pull Request。让我们一起构建更可信的 AI 生态！

​📄 License
​MIT License. See LICENSE for details.


