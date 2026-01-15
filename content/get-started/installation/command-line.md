---
title: 使用命令行安装 Streamlit
slug: /get-started/installation/command-line
description: 使用命令行工具安装 Streamlit 的逐步指南，并构建您的第一个 Hello World 应用。
keywords: 命令行安装, pip 安装 streamlit, venv, 虚拟环境, 命令行设置, pip 安装, 终端安装
---

# 使用命令行安装 Streamlit

本页面将引导您使用 `venv` 创建环境并使用 `pip` 安装 Streamlit。这些是我们推荐的工具，但如果您熟悉其他工具，也可以使用您喜欢的工具。最后，您将构建一个简单的"Hello world"应用并运行它。如果您更喜欢使用图形界面来管理您的 Python 环境，请查看如何 [使用 Anaconda 发行版安装 Streamlit](/get-started/installation/anaconda-distribution)。

## 先决条件

与任何编程工具一样，为了安装 Streamlit，您首先需要确保您的计算机已正确设置。更具体地说，您需要：

1. **Python**

   我们支持 [版本 3.9 到 3.13](https://www.python.org/downloads/)。

1. **Python 环境管理器** (推荐)

   环境管理器在项目之间创建虚拟环境，以隔离 Python 包的安装。

   我们推荐使用虚拟环境，因为安装或升级 Python 包可能会对另一个包产生意外影响。有关 Python 环境的详细介绍，请查看
   [Python 虚拟环境：入门指南](https://realpython.com/python-virtual-environments-a-primer/)。

   对于本指南，我们将使用 `venv`，它随 Python 一起提供。

1. **Python 包管理器**

   包管理器处理安装每个 Python 包，包括 Streamlit。

   对于本指南，我们将使用 `pip`，它随 Python 一起提供。

1. **仅在 macOS 上：Xcode 命令行工具**

   使用 [这些说明](https://mac.install.guide/commandlinetools/4.html) 下载 Xcode 命令行工具，以便包管理器安装 Streamlit 的一些依赖项。

1. **代码编辑器**

   我们最喜欢的编辑器是 [VS Code](https://code.visualstudio.com/download)，我们在所有教程中都使用它。

## 使用 `venv` 创建环境

1. 打开终端并导航到您的项目文件夹。

   ```bash
   cd myproject
   ```

2. 在终端中，输入：

   ```bash
   python -m venv .venv
   ```

3. 您的项目中将出现一个名为".venv"的文件夹。此目录是您的虚拟环境及其依赖项安装的位置。

## 激活您的环境

4. 在终端中，根据您的操作系统，使用以下命令之一激活您的环境。

   ```bash
   # Windows 命令提示符
   .venv\Scripts\activate.bat

   # Windows PowerShell
   .venv\Scripts\Activate.ps1

   # macOS 和 Linux
   source .venv/bin/activate
   ```

5. 激活后，您将在提示符前的括号中看到您的环境名称。"(.venv)"

## 在您的环境中安装 Streamlit

6. 在激活环境的终端中，输入：

   ```bash
   pip install streamlit
   ```

7. 通过启动 Streamlit Hello 示例应用程序来测试安装是否成功：

   ```bash
   streamlit hello
   ```

   如果这不起作用，请使用完整命令：

   ```bash
   python -m streamlit hello
   ```

8. Streamlit 的 Hello 应用程序应该在您的网页浏览器的新标签页中出现！
   <Cloud name="doc-mpa-hello" height="700px" />
9. 完成后关闭您的终端。

## 创建"Hello World"应用程序并运行它

10. 在您的项目文件夹中创建一个名为 `app.py` 的文件。

```python
import streamlit as st

st.write("Hello world")
```

11. 每当您想使用您的新环境时，首先需要转到您的项目文件夹（其中包含 `.venv` 目录）并运行激活它的命令：

```bash
# Windows 命令提示符
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS 和 Linux
source .venv/bin/activate
```

12. 激活后，您将在终端提示符开头的括号中看到您的环境名称。"(.venv)"

13. 运行您的 Streamlit 应用程序。

```bash
streamlit run app.py
```

如果这不起作用，请使用完整命令：

```bash
python -m streamlit run app.py
```

14. 要停止 Streamlit 服务器，请在终端中按 `Ctrl+C`。

15. 当您完成使用此环境时，通过输入以下内容返回到正常 shell：

```bash
deactivate
```

## 下一步是什么？

阅读我们的 [基本概念](/get-started/fundamentals/main-concepts) 来了解 Streamlit 的数据流模型。