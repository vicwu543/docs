---
title: 运行你的 Streamlit 应用
slug: /develop/concepts/architecture/run-your-app
description: 了解如何在本地运行 Streamlit 应用、设置参数、配置环境变量和理解开发和生产的执行模型。
keywords: streamlit run, 应用执行, 本地开发, 环境变量, 命令行参数, 应用启动, 开发服务器, 生产部署
---

# 运行你的 Streamlit 应用

使用 Streamlit 很简单。首先你在普通的 Python 脚本中加入一些 Streamlit 命令，然后运行它。我们根据你的用例列出了几种运行脚本的方法。

## 使用 streamlit run

一旦你创建了脚本，比如 `your_script.py`，最简单的运行方法是使用 `streamlit run`：

```bash
streamlit run your_script.py
```

如上所示运行脚本后，本地 Streamlit 服务器将启动，你的应用将在你的默认 Web 浏览器中的新选项卡中打开。

### 将参数传递给你的脚本

当向脚本传递一些自定义参数时，必须在两个破折号之后传递它们。否则参数会被解释为 Streamlit 本身的参数：

```bash
streamlit run your_script.py [-- script args]
```

### 将 URL 传递给 streamlit run

你也可以将 URL 传递给 `streamlit run`！当你的脚本托管在远程位置（如 GitHub Gist）时，这很有用。例如：

```bash
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

## 作为 Python 模块运行 Streamlit

运行 Streamlit 的另一种方式是将其作为 Python 模块运行。这在配置 IDE（如 PyCharm）以使用 Streamlit 时很有用：

```bash
# 运行
python -m streamlit run your_script.py
```

```bash
# 等价于：
streamlit run your_script.py
```
