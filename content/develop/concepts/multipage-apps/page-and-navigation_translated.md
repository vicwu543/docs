---
title: 使用 st.Page 和 st.navigation 定义多页应用
slug: /develop/concepts/multipage-apps/page-and-navigation
description: 了解如何使用最灵活和首选的方法来定义多页应用。
keywords: 多页, st.Page, st.navigation, 页面, 路由, 导航, 应用结构
---

# 使用 `st.Page` 和 `st.navigation` 定义多页应用

`st.Page` 和 `st.navigation` 是定义多页应用的首选命令。使用这些命令，您可以灵活地组织项目文件并自定义导航菜单。只需使用 `st.Page` 初始化 `StreamlitPage` 对象，然后在入口点文件中（即您传递给 `streamlit run` 的文件）将这些 `StreamlitPage` 对象传递给 `st.navigation`。

此页面假设您了解概述中介绍的[页面术语](/develop/concepts/multipage-apps/overview#page-terminology)。

## 应用结构

使用 `st.navigation` 时，您的入口点文件充当页面路由器。每个页面都是从入口点文件执行的脚本。您可以从 Python 文件或函数定义页面。如果您在入口点文件中包含元素或部件，它们将成为页面之间的公共元素。在这种情况下，您可以将入口点文件想象成每个页面的画框。

您每个应用运行只能调用一次 `st.navigation`，并且必须从入口点文件调用。当用户在导航中选择页面（或通过像 `st.switch_page` 这样的命令路由）时，`st.navigation` 返回选定的页面。您必须使用 `.run()` 方法手动执行该页面。以下示例是一个两页应用，其中每个页面由 Python 文件定义。

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
pg.run()
```

## 定义页面

`st.Page` 让您定义页面。第一个也是唯一必需的参数定义您的页面源，它可以是 Python 文件或函数。使用 Python 文件时，您的页面可以在子目录（或上级目录）中。页面文件的路径必须始终相对于入口点文件。一旦创建页面对象，将它们传递给 `st.navigation` 以将它们注册为应用中的页面。

如果您不定义页面标题或 URL 路径名，Streamlit 将从文件或函数名推断它们，如多页应用[概述](/develop/concepts/multipage-apps/overview#automatic-page-labels-and-urls)中所述。但是，`st.Page` 让您手动配置它们。在 `st.Page` 中，Streamlit 使用 `title` 设置页面标签和标题。此外，Streamlit 使用 `icon` 设置页面图标和 favicon。如果您想要不同的页面标题和标签，或不同的页面图标和 favicon，您可以使用 `st.set_page_config` 更改页面标题和/或 favicon。只需在入口点文件或页面脚本中调用 `st.set_page_config`。您可以多次调用 `st.set_page_config` 来累加配置页面。在入口点文件中使用 `st.set_page_config` 来声明默认配置，并在页面脚本中调用它来覆盖该默认值。

以下示例使用 `st.set_page_config` 在页面间一致地设置页面标题和 favicon。每个页面将在导航菜单中拥有自己的标签和图标，但浏览器标签页将在所有页面上显示一致的标题和 favicon。

**目录结构：**

```
your-repository/
├── create.py
├── delete.py
└── streamlit_app.py
```

**`streamlit_app.py`：**

```python
import streamlit as st

create_page = st.Page("create.py", title="Create entry", icon=":material/add_circle:")
delete_page = st.Page("delete.py", title="Delete entry", icon=":material/delete:")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
```

<div style={{ maxWidth: '564px', margin: 'auto' }}>
<Image src="/images/mpa-v2-use-set-page-config.jpg" frame />
</div>

## 自定义导航

您可以使用 `st.navigation` 中的 `position` 参数在侧边栏或应用顶部显示导航菜单。如果您想将页面分组到部分中，`st.navigation` 让您在侧边栏导航中插入标题，或在顶部导航中插入下拉组。或者，您可以禁用默认导航部件并使用 `st.page_link` 构建自定义导航菜单。

此外，您可以动态更改传递给 `st.navigation` 的页面。但是，只有 `st.navigation` 返回的页面接受 `.run()` 方法。如果用户输入带有路径名的 URL，而该路径名未关联到 `st.navigation` 中的页面（首次运行），Streamlit 将抛出"页面未找到"错误并将他们重定向到默认页面。

### 添加部分标题

自定义导航菜单的最简单方法是在 `st.navigation` 中组织页面。您可以排序或分组页面，以及删除您不想让用户访问的任何页面。这是处理用户权限的便捷方式。但是，您不能在导航中隐藏页面同时保持通过直接 URL 访问。如果您需要隐藏页面同时保持可访问性，您需要隐藏默认导航菜单并使用像 `st.page_link` 这样的命令构建导航菜单。

以下示例创建两个菜单状态。当用户开始新会话时，他们未登录。在这种情况下，唯一可用的页面是登录页面。如果用户尝试通过 URL 访问另一个页面，它将创建新会话，Streamlit 将不识别页面。用户将被转移到登录页面。但是，用户登录后，他们将看到带有三个部分的导航菜单，并被定向到仪表板作为应用的默认页面（即主页）。

**目录结构：**

```
your-repository/
├── reports
│   ├── alerts.py
│   ├── bugs.py
│   └── dashboard.py
├── tools
│   ├── history.py
│   └── search.py
└── streamlit_app.py
```

**`streamlit_app.py`：**

```python
import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="System alerts", icon=":material/notification_important:"
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
```

<div style={{ maxWidth: '564px', margin: 'auto' }}>
<Image src="/images/mpa-v2-page-sections.jpg" frame />
</div>

### 动态更改可用页面

您可以通过更新 `st.navigation` 中的页面列表来更改用户可用的页面。这是处理基于角色或基于用户的某些页面访问的便捷方式。有关更多信息，请查看我们的教程，[创建动态导航菜单](/develop/tutorials/multipage/dynamic-navigation)。

### 构建自定义导航菜单

如果您想要对导航菜单进行更多控制，您可以隐藏默认导航并构建自己的导航。您可以通过在 `st.navigation` 命令中包含 `position="hidden"` 来隐藏默认导航。如果您希望页面对用户可用而不显示在导航菜单中，您必须使用此方法。如果页面未包含在 `st.navigation` 中，用户无法路由到该页面。这适用于通过 URL 的导航以及像 `st.switch_page` 和 `st.page_link` 这样的命令。