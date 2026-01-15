---
title: 在部署的Streamlit应用中调用Python子进程
slug: /knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app
---

# 在部署的Streamlit应用中调用Python子进程

## 问题

假设你想在部署的Streamlit应用`streamlit_app.py`中调用子进程来运行Python脚本`script.py`。例如，机器学习库[Ludwig](https://ludwig-ai.github.io/ludwig-docs/)使用命令行界面运行，或者你可能想从Python运行bash脚本或类似类型的进程。

你尝试了以下方法，但即使你在requirements文件中指定了Python依赖，仍然遇到`script.py`的依赖问题：

```python
# streamlit_app.py
import streamlit as st
import subprocess

subprocess.run(["python", "script.py"])
```

## 解决方案

当你运行上述代码块时，你将获得系统路径上的Python版本-不一定是Streamlit代码运行的虚拟环境中安装的Python可执行文件。

解决方案是使用[`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable)直接检测Python可执行文件：

```python
# streamlit_app.py
import streamlit as st
import subprocess
import sys

subprocess.run([f"{sys.executable}", "script.py"])
```

这确保了`script.py`在与Streamlit代码相同的Python可执行文件下运行-其中安装了你的[Python依赖](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies)。

### 相关链接

- https://stackoverflow.com/questions/69947867/run-portion-of-python-code-in-parallel-from-a-streamlit-app/69948545#69948545
- https://discuss.streamlit.io/t/modulenotfounderror-no-module-named-cv2-streamlit/18319/3?u=snehankekre
- https://docs.python.org/3/library/sys.html#sys.executable
