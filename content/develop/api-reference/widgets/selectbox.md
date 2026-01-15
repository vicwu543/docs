---
title: st.selectbox
slug: /develop/api-reference/widgets/st.selectbox
description: st.selectbox 显示下拉选择小部件。
keywords: selectbox, widget, dropdown, selection, input, interactive
---

<Autofunction function="streamlit.selectbox" />

<br />

选择小部件可以使用 `label_visibility` 参数自定义如何隐藏其标签。如果为"hidden"，标签不会显示，但在小部件上方仍有空白空间（相当于 `label=""`）。如果为"collapsed"，则标签和空间都会被移除。默认值为"visible"。选择小部件也可以使用 `disabled` 参数禁用：

```python
import streamlit as st

# 将小部件的初始值存储在会话状态中
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("禁用选择框小部件", key="disabled")
    st.radio(
        "设置选择框标签可见性 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "您希望如何被联系？",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
```

<Cloud name="doc-selectbox1" height="300px" />
