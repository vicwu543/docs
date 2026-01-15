---
title: 安装 Streamlit
slug: /get-started/installation
description: 了解如何安装 Streamlit，包括使用 pip、conda、Anaconda Distribution、云环境和命令行工具的综合指南。
keywords: install streamlit, installation, pip install, conda install, anaconda, command line, cloud installation, setup streamlit
---

# 安装 Streamlit

有多种方式来设置您的开发环境并安装 Streamlit。
在您自己的计算机上安装 Python 后进行本地开发是最
常见的场景。

<Tip>

试试在您的浏览器中运行的 Streamlit Playground &mdash; 无需安装。
（请注意，这不是 Streamlit 的预期使用方式，因为它有许多缺点。这就是为什么它是
一个_游乐场_！）

<IconLink
    href="/get-started/installation/streamlit-playground"
    icon="arrow_forward"
    label="游乐场说明"
    cssModuleClassName="Indigo"
    cssModuleIconClassName="IconRight"
/>

</Tip>

## 经验丰富的 Python 开发者摘要

1. 要设置您的 Python 环境并测试您的安装，请执行以下终端命令：

   ```bash
   pip install streamlit
   streamlit hello
   ```

1. 跳转到我们的 [基本概念](/get-started/fundamentals/main-concepts)。

## 在您的机器上安装 Streamlit

### 选项 1：我喜欢命令行

使用 `venv` 和 `pip` 等工具在您自己的机器上安装 Streamlit。

<IconLink
    href="/get-started/installation/command-line"
    icon="arrow_forward"
    label="命令行说明"
    cssModuleClassName="Orange"
    cssModuleIconClassName="IconRight"
/>

### 选项 2：我更喜欢图形界面

使用 Anaconda Distribution 图形用户界面安装 Streamlit。如果您使用 Windows 或没有设置 Python，这也是最好的
方法。

<IconLink
    href="/get-started/installation/anaconda-distribution"
    icon="arrow_forward"
    label="Anaconda Distribution 说明"
    cssModuleClassName="Orange"
    cssModuleIconClassName="IconRight"
/>

## 在云中创建应用

### 选项 1：我想要一个免费的云环境

使用 Streamlit Community Cloud 和 GitHub Codespaces，这样您就不必费力
安装 Python 和设置环境。

<IconLink
    href="/get-started/installation/community-cloud"
    icon="arrow_forward"
    label="GitHub Codespaces 说明"
    cssModuleClassName="Orange"
    cssModuleIconClassName="IconRight"
/>

### 选项 2：我需要安全、受控且在云中的东西

使用 Snowflake 中的 Streamlit 在云中编码您的应用，同时使用基于角色的访问控制与您的
数据在一起。

<IconLink
    href="/get-started/installation/streamlit-in-snowflake"
    icon="arrow_forward"
    label="Snowflake 说明"
    cssModuleClassName="Orange"
    cssModuleIconClassName="IconRight"
/>
