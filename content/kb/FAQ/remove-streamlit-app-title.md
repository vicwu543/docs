---
title: 如何从应用标题中删除"· Streamlit"？
slug: /knowledge-base/using-streamlit/remove-streamlit-app-title
---

# 如何从应用标题中删除"· Streamlit"？

使用 [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) 分配页面标题不会在该标题后附加"· Streamlit"。例如：

```python
import streamlit as st

st.set_page_config(
   page_title="Ex-stream-ly Cool App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)
```
