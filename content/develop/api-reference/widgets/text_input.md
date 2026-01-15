---
title: st.text_input
slug: /develop/api-reference/widgets/st.text_input
description: st.text_input 显示单行文本输入小部件。
keywords: st.text_input, text input, single-line text, text field, input field, string input, text widget, input widget
---

<Autofunction function="streamlit.text_input" />

<br />

文本输入小部件可以使用 `label_visibility` 参数自定义如何隐藏其标签。如果为"hidden"，标签不会显示，但在小部件上方仍有空白空间（相当于 `label=""`）。如果为"collapsed"，则标签和空间都会被移除。默认值为"visible"。文本输入小部件也可以使用 `disabled` 参数禁用，并可以使用 `placeholder` 参数在文本输入为空时显示可选占位符文本：

```python
import streamlit as st

# 将小部件的初始值存储在会话状态中
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("禁用文本输入小部件", key="disabled")
    st.radio(
        "设置文本输入标签可见性 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "其他文本输入小部件的占位符",
        "这是一个占位符",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "输入一些文本 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("您输入了：", text_input)
```

<Cloud name="doc-text-input1" height="400px" />
