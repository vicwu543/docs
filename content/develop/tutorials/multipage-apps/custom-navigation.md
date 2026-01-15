---
title: 使用 `st.page_link` 构建自定义导航菜单
slug: /develop/tutorials/multipage/st.page_link-nav
description: 了解如何在多页面 Streamlit 应用中使用 st.page_link 构建自定义导航菜单，实现具有高亮效果和简洁设计的动态导航。
keywords: custom navigation, st.page_link, multipage navigation, navigation menu, dynamic navigation, page links, custom menu, navigation design
---

# 使用 `st.page_link` 构建自定义导航菜单

Streamlit 让您可以使用 `st.page_link` 构建自定义导航菜单和元素。在 Streamlit 1.31.0 版本中引入的 `st.page_link` 可以链接到多页面应用中的其他页面或外部网站。当链接到应用中的另一个页面时，`st.page_link` 会显示高亮效果以指示当前页面。结合 [`client.showSidebarNavigation`](/develop/concepts/configuration#client) 配置选项，您可以在应用中构建简洁、动态的导航。

## 前提条件

在开发环境中创建一个新的工作目录。我们将此目录称为 `your-repository`。

## 摘要

在这个示例中，我们将为一个多页面应用构建一个动态导航菜单，该菜单根据当前用户的职责而变化。我们抽象了用户名和凭据的使用，以简化示例。相反，我们将在应用的主页上使用一个选择框来切换角色。会话状态将在页面之间传递此选择。应用将有一个主页（`app.py`），它充当抽象的登录页面。还有三个额外的页面，根据当前角色，这些页面将被隐藏或可访问。文件结构如下：

```
your-repository/
├── .streamlit/
│   └── config.toml
├── pages/
│   ├── admin.py
│   ├── super-admin.py
│   └── user.py
├── menu.py
└── app.py
```

这是我们即将构建的效果：

<Cloud name="doc-custom-navigation" height="400px" />

## 构建示例

### 隐藏默认侧边栏导航

创建自定义导航菜单时，您需要使用 `client.showSidebarNavigation` 隐藏默认的侧边栏导航。在工作目录中添加以下 `.streamlit/config.toml` 文件：

```toml
[client]
showSidebarNavigation = false
```

### 创建菜单函数

您可以为不同页面编写不同的菜单逻辑，也可以创建一个可在多个页面上调用的单一菜单函数。在此示例中，我们将在所有页面上使用相同的菜单逻辑，包括在用户未登录时重定向到主页。我们将构建一些辅助函数来完成此操作。

- `menu_with_redirect()` 检查用户是否已登录，然后重定向到主页或渲染菜单。
- `menu()` 将根据用户是否已登录调用正确的辅助函数来渲染菜单。
- `authenticated_menu()` 将根据已验证用户的角色显示菜单。
- `unauthenticated_menu()` 将为未验证用户提供菜单。

我们将在主页上调用 `menu()`，并在其他页面上调用 `menu_with_redirect()`。`st.session_state.role` 将存储当前选定的角色。如果此值不存在或设置为 `None`，则用户未登录。否则，它将以字符串形式保存用户的角色："user"、"admin" 或 "super-admin"。

将以下 `menu.py` 文件添加到您的工作目录。(我们将在下面更详细地描述这些函数。)

```python
import streamlit as st


def authenticated_menu():
    # 为已验证用户显示导航菜单
    st.sidebar.page_link("app.py", label="切换账户")
    st.sidebar.page_link("pages/user.py", label="您的资料")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="管理用户")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="管理管理员权限",
            disabled=st.session_state.role != "super-admin",
        )


def unauthenticated_menu():
    # 为未验证用户显示导航菜单
    st.sidebar.page_link("app.py", label="登录")


def menu():
    # 确定用户是否已登录，然后显示正确的导航菜单
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # 如果用户未登录，将其重定向到主页，否则继续渲染导航菜单
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
```

让我们更仔细地看看 `authenticated_menu()`。当调用此函数时，`st.session_state.role` 存在且具有非 `None` 的值。

```python
def authenticated_menu():
    # 为已验证用户显示导航菜单
```

导航菜单中的前两个页面对所有用户都可用。由于我们知道调用此函数时用户已登录，因此我们将为主页使用标签"切换账户"。(如果您不使用 `label` 参数，页面名称将从文件名派生，就像使用默认侧边栏导航一样。)

```python
    st.sidebar.page_link("app.py", label="切换账户")
    st.sidebar.page_link("pages/user.py", label="您的资料")
```

我们只想向管理员显示接下来的两个页面。此外，我们选择禁用(但不隐藏)超级管理员页面，当管理员不是超级管理员时。我们使用 `disabled` 参数来实现这一点。(当角色不是"super-admin"时，`disabled=True`。)

```
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="管理用户")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="管理管理员权限",
            disabled=st.session_state.role != "super-admin",
        )
```

就是这样！`unauthenticated_menu()` 只显示一个链接到应用主页的链接，标签为"登录"。`menu()` 简单检查 `st.session_state.role` 以在两个菜单渲染函数之间切换。最后，`menu_with_redirect()` 扩展 `menu()` 以在用户未登录时将其重定向到 `app.py`。

<Tip>

如果要在页面标签中包含表情符号，可以使用 `icon` 参数。无需在文件名或 `label` 参数中包含表情符号。

</Tip>

### 创建应用的主文件

主 `app.py` 文件将充当伪登录页面。用户可以从 `st.selectbox` 小部件中选择一个角色。一些逻辑将把该角色保存到会话状态中，以便在页面间导航时保留它——即使返回到 `app.py`。

将以下 `app.py` 文件添加到您的工作目录：

```python
import streamlit as st
from menu import menu

# 将 st.session_state.role 初始化为 None
if "role" not in st.session_state:
    st.session_state.role = None

# 从会话状态检索角色以初始化小部件
st.session_state._role = st.session_state.role

def set_role():
    # 回调函数，将角色选择保存到会话状态
    st.session_state.role = st.session_state._role


# 选择框以选择角色
st.selectbox(
    "选择您的角色:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)
menu() # 渲染动态菜单！
```

### 向应用添加其他页面

添加以下 `pages/user.py` 文件：

```python
import streamlit as st
from menu import menu_with_redirect

# 如果未登录则重定向到 app.py，否则显示导航菜单
menu_with_redirect()

st.title("此页面对所有用户可用")
st.markdown(f"您当前以 {st.session_state.role} 角色登录。")
```

如果用户手动通过URL导航到页面，会话状态会重置。因此，如果用户尝试在此示例中访问管理员页面，会话状态将被清除，他们将被重定向到主页作为未验证用户。然而，仍建议在每个受限页面顶部包含角色检查。如果角色不在白名单中，您可以使用 `st.stop` 停止应用。

`pages/admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# 如果未登录则重定向到 app.py，否则显示导航菜单
menu_with_redirect()

# 验证用户角色
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("您没有权限查看此页面。")
    st.stop()

st.title("此页面对所有管理员可用")
st.markdown(f"您当前以 {st.session_state.role} 角色登录。")
```

`pages/super-admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# 如果未登录则重定向到 app.py，否则显示导航菜单
menu_with_redirect()

# 验证用户角色
if st.session_state.role not in ["super-admin"]:
    st.warning("您没有权限查看此页面。")
    st.stop()

st.title("此页面对超级管理员可用")
st.markdown(f"您当前以 {st.session_state.role} 角色登录。")
```

如上所述，`menu_with_redirect()` 中的重定向将阻止用户看到管理员页面上的警告消息。如果您想看到警告，请在 `app.py` 底部添加另一个 `st.page_link("pages/admin.py")` 按钮，这样您可以在选择"用户"角色后导航到管理员页面。😉