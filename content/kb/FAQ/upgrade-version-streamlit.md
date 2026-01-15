---
title: 如何升级到最新版本的 Streamlit？
slug: /knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit
---

# 如何升级到最新版本的 Streamlit？

我们建议升级到最新的官方 Streamlit 版本，以便您可以访问最新的尖端功能。如果您还没有安装 Streamlit，请阅读我们的[安装指南](/get-started/installation)。它可以帮助您设置虚拟环境，并指导您在 Windows、macOS 和 Linux 上安装 Streamlit。无论您使用哪个包管理工具和操作系统，我们建议在虚拟环境中运行本页上的命令。

如果您之前已安装 Streamlit 并想升级到最新版本，以下是根据您的依赖管理器如何操作的方法。

## Pipenv

Streamlit 官方支持的 macOS 和 Linux 环境管理器是 [Pipenv](https://pypi.org/project/pipenv/)。

1. 导航到包含您的 Pipenv 环境的项目文件夹：

```bash
cd myproject
```

2. 激活该环境，升级 Streamlit，并验证您拥有最新版本：

```bash
pipenv shell
pip install --upgrade streamlit
streamlit version
```

或者，如果您想使用易于复现的环境，每次安装或更新软件包时将 `pip` 替换为 `pipenv`：

```bash
pipenv update streamlit
pipenv run streamlit version
```

## Conda

1. 激活安装了 Streamlit 的 conda 环境：

```bash
conda activate $ENVIRONMENT_NAME
```

请确保将 `$ENVIRONMENT_NAME` ☝️ 替换为您的 conda 环境的名称！

2. 在活跃的 conda 环境中更新 Streamlit 并验证您拥有最新版本：

```bash
conda update -c conda-forge streamlit -y
streamlit version
```

## Poetry

为了使用 [Poetry](https://python-poetry.org/) 获取最新版本的 Streamlit 并验证您拥有最新版本，请运行：

```bash
poetry update streamlit
streamlit version
```
