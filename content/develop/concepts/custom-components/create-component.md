---
title: 创建组件
slug: /develop/concepts/custom-components/create
description: 从头开始创建自定义 Streamlit 组件的分步指南，包括设置、开发环境和组件结构。
keywords: create component, component development, component setup, development environment, component structure, custom component creation, build components
---

# 创建组件

<Note>

如果您只对**使用 Streamlit 组件**感兴趣，那么您可以跳过此部分并前往 [Streamlit 组件库](https://streamlit.io/components) 查找和安装社区创建的组件！

</Note>

开发人员可以编写 JavaScript 和 HTML"组件"，这些组件可以在 Streamlit 应用中渲染。Streamlit 组件可以从 Streamlit Python 脚本接收数据，也可以向其发送数据。

Streamlit 组件让您扩展基础 Streamlit 包中提供的功能。使用 Streamlit 组件为您用例所需的功能创建，然后将其包装在 Python 包中并与更广泛的 Streamlit 社区分享！

**通过 Streamlit 组件，您可以通过以下方式向应用添加新功能：**

- 创建您自己的组件，以替代现有的 Streamlit 元素和部件。
- 通过包装现有的 React.js、Vue.js 或其他 JavaScript 部件工具包创建全新的 Streamlit 元素和部件。
- 通过构建 HTML 表示并将其样式化以适应您的应用主题来渲染 Python 对象。
- 创建便捷函数来嵌入常用的网络功能，如 [GitHub gists 和 Pastebin](https://github.com/randyzwitch/streamlit-embedcode)。

查看 Streamlit 工程师 Tim Conkling 制作的这些 Streamlit 组件教程视频以开始：

## 第一部分：设置和架构

<YouTube videoId="BuD3gILJW-Q" />

## 第二部分：制作滑块部件

<YouTube videoId="QjccJl_7Jco" />