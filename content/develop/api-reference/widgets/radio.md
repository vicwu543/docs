---
title: st.radio
slug: /develop/api-reference/widgets/st.radio
description: st.radio 显示单选按钮小部件。
keywords: st.radio, radio button, radio, single selection, radio group, option selection, exclusive selection, radio widget
---

<Autofunction function="streamlit.radio" />

<br />

小部件可以使用 `label_visibility` 参数自定义如何隐藏其标签。如果为"hidden"，标签不会显示，但在小部件上方仍有空白空间（相当于 `label=""`）。如果为"collapsed"，则标签和空间都会被移除。默认值为"visible"。单选按钮也可以使用 `disabled` 参数禁用，并使用 `horizontal` 参数水平定向：

```python
import streamlit as st

# 将小部件的初始值存储在会话状态中
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("禁用单选小部件", key="disabled")
    st.checkbox("水平定向单选选项", key="horizontal")

with col2:
    st.radio(
        "设置标签可见性 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
```

<Cloud name="doc-radio1" height="300px" />

### Featured videos

查看我们关于如何使用 Streamlit 核心功能之一的视频：单选按钮！🔘

<YouTube videoId="CVHIMGVAzwA" />

在下面的视频中，我们将更进一步，学习如何组合[按钮](/develop/api-reference/widgets/st.button)、[复选框](/develop/api-reference/widgets/st.checkbox)和单选按钮！

<YouTube videoId="EnXJBsCIl_A" />
