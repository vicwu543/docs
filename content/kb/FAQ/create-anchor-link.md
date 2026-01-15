---
title: 如何创建锚链接？
slug: /knowledge-base/using-streamlit/create-anchor-link
---

# 如何创建锚链接？

## 概述

您想过创建锚点，以便您的应用用户可以通过在 URL 中指定 `#anchor` 来直接导航到特定部分吗？如果是这样，让我们了解一下如何做。

## 解决方案

锚点会自动添加到标题文本中。

例如，如果您通过以下 [st.header()](/develop/api-reference/text/st.header) 命令定义标题文本：

```python
st.header("Section 1")
```

然后您可以使用以下命令创建指向此标题的链接：

```python
st.markdown("[Section 1](#section-1)")
```

## 示例

- 演示应用：[https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/](https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/)
- GitHub 仓库：[https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py](https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py)
