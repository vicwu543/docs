---
title: 如何安装不在 PyPI/Conda 上但可在 GitHub 上获得的包
slug: /knowledge-base/dependencies/install-package-not-pypi-conda-available-github
---

# 如何安装不在 PyPI/Conda 上但可在 GitHub 上获得的包

## 概述

您是否尝试将应用部署到[Streamlit Community Cloud](/deploy/streamlit-community-cloud)，但不知道如何在 requirements 文件中指定[Python 依赖项](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies)，而该依赖项在公共 GitHub 仓库上可用，但不在 PyPI 或 Conda 等任何包索引上？如果是这样，请继续阅读以了解如何操作！

假设您想从 GitHub 安装 `SomePackage` 及其 Python 依赖项，GitHub 是流行的版本控制系统 (VCS) Git 的托管服务。假设 `SomePackage` 可在以下 URL 获取：`https://github.com/SomePackage.git`。

pip（通过 `requirements.txt`）[支持](https://pip.pypa.io/en/stable/topics/vcs-support/)从 GitHub 安装。此支持需要一个可用的工作可执行文件（对于 Git）。它通过 URL 前缀使用：`git+`。

## 指定 GitHub 网址

要安装 `SomePackage`，请在 `requirements.txt` 文件中包含以下内容：

```bash
git+https://github.com/SomePackage#egg=SomePackage
```

您甚至可以指定 "git ref"，例如分支名称、提交哈希或标签名称，如下面的示例所示。

## 指定 Git 分支名称

通过在 `requirements.txt` 中指定分支名称（如 `main`、`master`、`develop` 等）来安装 `SomePackage`：

```bash
git+https://github.com/SomePackage.git@main#egg=SomePackage
```

## 指定提交哈希

通过在 `requirements.txt` 中指定提交哈希来安装 `SomePackage`：

```bash
git+https://github.com/SomePackage.git@eb40b4ff6f7c5c1e4366cgfg0671291bge918#egg=SomePackage
```

## 指定标签

通过在 `requirements.txt` 中指定标签来安装 `SomePackage`：

```bash
git+https://github.com/SomePackage.git@v1.1.0#egg=SomePackage
```

## 限制

目前**不可能**使用 URI 形式从私有 GitHub 仓库安装私有包：

```bash
git+https://{token}@github.com/user/project.git@{version}
```

其中 `version` 是标签、分支或提交。`token` 是具有只读权限的个人访问令牌。Streamlit Community Cloud 仅支持从公共 GitHub 仓库安装公共包。
