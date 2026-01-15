---
title: 使用会话状态时窗口小部件每秒输入更新一次
slug: /knowledge-base/using-streamlit/widget-updating-session-state
---

# 使用会话状态时窗口小部件每秒输入更新一次

## 概述

您正在使用[会话状态](/develop/api-reference/caching-and-state/st.session_state)在您的应用中存储页面交互。当用户与应用中的小部件交互时（例如点击按钮），您期望您的应用更新其小部件状态并反映新值。但是，您会注意到它没有。相反，用户必须与小部件交互两次（例如，点击按钮两次）才能使应用显示正确的值。您现在做什么？🤔 让我们在下面的部分中走过解决方案。

## 解决方案

使用会话状态更新脚本中的小部件或值时，您需要使用分配给小部件的唯一键，**而不是**您分配小部件的变量。在下面的示例代码块中，分配给滑块小部件的唯一*键*是 `slider`，而小部件分配到的*变量*是 `slide_val`。

让我们在一个示例中看到这个。假设您希望用户点击一个重置滑块的按钮。

要使滑块的值在按钮点击时更新，您需要使用[回调函数](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state)与 [`st.button`](/develop/api-reference/widgets/st.button) 的 `on_click` 参数：

```python
# 按钮的回调函数将 1 添加到
# 滑块值最多 10
def plus_one():
    if st.session_state["slider"] < 10:
        st.session_state.slider += 1
    else:
        pass
    return

# 创建按钮时，分配您的回调的名称
# 函数到 on_click 参数
add_one = st.button("Add one to the slider", on_click=plus_one, key="add_one")

# 创建滑块
slide_val = st.slider("Pick a number", 0, 10, key="slider")
```

## 相关资源

- [缓存 Sqlite DB 连接导致页面渲染出现故障](https://discuss.streamlit.io/t/caching-sqlite-db-connection-resulting-in-glitchy-rendering-of-the-page/19017)
- [链接到选项框的选择全部复选框](https://discuss.streamlit.io/t/select-all-checkbox-that-is-linked-to-selectbox-of-options/18521)
