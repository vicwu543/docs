---
title: 为什么 Streamlit 限制嵌套 st.columns？
slug: /knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns
---

# 为什么 Streamlit 限制嵌套 `st.columns`？

从版本 1.46.0 开始，Streamlit 移除了对嵌套列、扩展器、弹出窗口和聊天消息容器的显式限制。为了遵循最佳设计实践并在所有屏幕尺寸上保持良好的外观，不要过度使用嵌套布局。

从版本 1.18.0 到 1.45.0，Streamlit 允许在其他 `st.columns` 内嵌套 [`st.columns`](/develop/api-reference/layout/st.columns)，但有以下限制：

- 在应用的主要区域中，列可以嵌套最多一个级别。
- 在侧边栏中，列不能被嵌套。

这些限制是为了使 Streamlit 应用在所有设备尺寸上看起来很好。嵌套列多次通常会导致糟糕的用户界面。您可能能够在一个屏幕尺寸上使其看起来不错，但一旦不同屏幕上的用户查看该应用，他们就会有糟糕的体验。某些列会很小，其他列会太长，复杂的布局看起来会很不合适。Streamlit 尽力自动调整元素的大小，以在各种设备上看起来不错，无需开发人员的任何帮助。但对于具有多个级别嵌套的复杂布局，这是不可能的。
