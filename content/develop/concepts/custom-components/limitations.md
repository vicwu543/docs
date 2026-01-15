---
title: 自定义组件的限制
slug: /develop/concepts/custom-components/limitations
description: 了解 Streamlit 自定义组件的限制和约束，包括 iframe 限制和与基础 Streamlit 功能的差异。
keywords: component limitations, iframe restrictions, component constraints, custom component issues, component differences, development limitations
---

# 自定义组件的限制

## Streamlit 组件与基础 Streamlit 包提供的功能有何不同？

- Streamlit 组件被封装在一个 iframe 中，这让您可以使用任何您喜欢的网络技术在 iframe 内实现任何您想要的功能。

## 使用 Streamlit 组件无法实现哪些类型的事情？

由于每个 Streamlit 组件都被挂载到其自己的沙盒 iframe 中，这意味着组件的功能存在一些限制：

- **无法与其他组件通信**：组件不能包含（或以其他方式与）其他组件通信，因此组件不能用于构建网格布局之类的结构。
- **无法修改 CSS**：组件不能修改 Streamlit 应用其余部分使用的 CSS，因此例如，您不能创建一个使应用进入暗黑模式的功能。
- **无法添加/删除元素**：组件不能向 Streamlit 应用添加或删除其他元素，因此例如，您不能创建一个移除应用菜单的功能。

## 我的组件似乎在闪烁/卡顿……如何修复？

目前，Streamlit 内部未对组件更新执行自动去抖动。组件创建者自己可以决定对其发送回 Streamlit 的更新进行速率限制。