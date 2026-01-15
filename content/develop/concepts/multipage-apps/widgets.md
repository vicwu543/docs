---
title: 在多页应用中使用部件
slug: /develop/concepts/multipage-apps/widgets
description: 了解部件在多页 Streamlit 应用中的行为，包括部件状态管理、ID 和跨页面交互。
keywords: 多页部件, 部件状态, 部件 ID, 跨页面部件, 部件行为, 状态管理, 多页交互, 部件持久性
---

# 在多页应用中使用部件

当您在 Streamlit 应用中创建一个部件时，Streamlit 会生成一个部件 ID 并使用它使您的部件有状态。随着用户交互，您的应用重新运行，Streamlit 通过将其值关联到其 ID 来跟踪部件的值。特别是，部件的 ID 取决于创建它的页面。如果您在两个不同页面上定义相同的部件，那么当您切换页面时，部件将重置为其默认值。

本指南解释了三种策略来处理此行为，如果您希望部件在所有页面上保持有状态。如果您不希望部件出现在所有页面上，但希望在离开其页面（然后返回）时保持有状态，则可以使用选项 2 和 3。有关这些策略的详细信息，请参见[了解部件行为](/develop/concepts/architecture/widget-behavior)。

## 选项 1（首选）：在您的入口点文件中执行您的部件命令

当您使用 `st.Page` 和 `st.navigation` 定义多页应用时，您的入口点文件成为页面周围公共元素的框架。当您在入口点文件中执行部件命令时，Streamlit 将部件关联到您的入口点文件而不是特定页面。由于您的入口点文件在每次应用重新运行时都会执行，入口点文件中的任何部件将在用户在页面间切换时保持有状态。

如果您使用 `pages/` 目录定义应用，此方法不起作用。

以下示例在侧边栏中包含一个选择框和滑块，它们在所有页面上渲染并保持有状态。每个部件都有一个分配的键，以便您可以通过会话状态在页面内访问它们的值。

**目录结构：**

```
your-repository/
├── page_1.py
├── page_2.py
└── streamlit_app.py
```

**`streamlit_app.py`：**

```python
import streamlit as st

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])

st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")

pg.run()
```

## 选项 2：在会话状态中将您的部件值保存到虚拟键中

如果您希望离开部件并返回到它同时保持其值，或者如果您希望在多个页面上使用相同的部件，请使用 `st.session_state` 中的单独键来独立于部件保存值。在此示例中，临时键与部件一起使用。临时键使用下划线前缀。因此，`"_my_key"` 用作部件键，但数据被复制到 `"my_key"` 以在页面间保留它。

```python
import streamlit as st

def store_value():
    # 将值复制到永久键
    st.session_state["my_key"] = st.session_state["_my_key"]

# 将保存的值复制到临时键
st.session_state["_my_key"] = st.session_state["my_key"]
st.number_input("Number of filters", key="_my_key", on_change=store_value)
```

如果这被功能化以与多个部件一起工作，它可能看起来像这样：

```python
import streamlit as st

def store_value(key):
    st.session_state[key] = st.session_state["_"+key]
def load_value(key):
    st.session_state["_"+key] = st.session_state[key]

load_value("my_key")
st.number_input("Number of filters", key="_my_key", on_change=store_value, args=["my_key"])
```

## 选项 3：中断部件清理过程

当 Streamlit 到达应用运行结束时，它将删除任何未渲染部件的数据。这包括任何未关联到当前页面的部件的数据。但是，如果您在应用运行中重新保存键值对，Streamlit 将不会将键值对关联到任何部件，直到您再次使用该键执行部件命令。

因此，如果您在每个页面顶部有以下代码，具有键 `"my_key"` 的任何部件将在其渲染（或不渲染）的地方保留其值。或者，如果您使用 `st.navigation` 和 `st.Page`，您可以在执行页面之前在入口点文件中包含此内容一次。

```python
if "my_key" in st.session_state:
    st.session_state.my_key = st.session_state.my_key
```
