---
title: "ERROR: No matching distribution found for"
slug: /knowledge-base/dependencies/no-matching-distribution
---

# ERROR: No matching distribution found for

## 问题

在[Streamlit Community Cloud](https://streamlit.io/cloud)上部署应用时，你会收到错误 `ERROR: No matching distribution found for`。

## 解决方案

当你在 Streamlit Community Cloud 上部署应用且你的 requirements 文件中的[Python 依赖项](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies)存在以下一个或多个错误时，会发生此错误：

1. 该包是[Python 标准库](https://docs.python.org/3/py-modindex.html)的一部分。例如，如果你在 requirements 文件中包含 [`base64`](https://docs.python.org/3/library/base64.html)，你会看到 **`ERROR: No matching distribution found for base64`**，因为它是 Python 标准库的一部分。解决方案是不在 requirements 文件中包含该包。仅包含无法与标准 Python 安装一起发行的包。
2. 你的 requirements 文件中的包名拼错了。在包含包到 requirements 文件之前，仅需检查包名。
3. 该包不支持你的 Streamlit 应用运行所在的操作系统。例如，部署到 Streamlit Community Cloud 时，你看到 **`ERROR: No matching distribution found for pywin32`**。`pywin32` 模块提供了与 Python 中许多 Windows API 的访问权限。部署到 Streamlit Community Cloud 的应用在 Linux 环境中执行。因此，`pywin32` 在非 Windows 系统上（包括在 Streamlit Community Cloud 上）无法安装。解决方案是从你的 requirements 文件中排除 `pywin32`，或将你的应用部署到提供 Windows 机器的云服务上。

相关主论坛帖子：

- https://discuss.streamlit.io/t/error-no-matching-distribution-found-for-base64/15758
- https://discuss.streamlit.io/t/error-could-not-find-a-version-that-satisfies-the-requirement-pywin32-301-from-versions-none/15343/2
