---
title: 多页应用的概述
slug: /develop/concepts/multipage-apps/overview
description: 了解使用 st.navigation、st.Page 和 pages 目录创建多页应用的 Streamlit 功能，以及自动导航。
keywords: 多页, 导航, 页面, st.navigation, st.Page, 路由, 侧边栏
---

# 多页应用的概述

Streamlit 提供了两种内置机制来创建多页应用。最简单的方法是使用 `pages/` 目录。然而，首选且更可定制的方法是使用 `st.navigation`。

## `st.Page` 和 `st.navigation`

如果您想要在定义多页应用时获得最大灵活性，我们推荐使用 `st.Page` 和 `st.navigation`。使用 `st.Page`，您可以将任何 Python 文件或 `Callable` 声明为应用中的页面。此外，您可以在入口点文件中定义页面的公共元素（您传递给 `streamlit run` 的文件）。使用这些方法，您的入口点文件就像所有页面共享的画框一样。

您必须在入口点文件中包含 `st.navigation` 来配置应用的导航菜单。这也是您的入口点文件作为页面之间路由器的方式。

## `pages/` 目录

如果您正在寻找快速简单的解决方案，只需在入口点文件旁边放置一个 `pages/` 目录。对于 `pages/` 目录中的每个 Python 文件，Streamlit 将为您的应用创建额外的页面。Streamlit 从文件名确定页面标签和 URL，并自动在应用侧边栏顶部填充导航菜单。

```
your_working_directory/
├── pages/
│   ├── a_page.py
│   └── another_page.py
└── your_homepage.py
```

Streamlit 从文件名确定导航中的页面顺序。您可以在文件名中使用数字前缀来调整页面顺序。有关更多信息，请参见[侧边栏中的页面排序方式](/develop/concepts/multipage-apps/pages-directory#how-pages-are-sorted-in-the-sidebar)。如果您想使用此选项自定义导航菜单，您可以通过[配置](/develop/api-reference/configuration/config.toml)（`client.showSidebarNavigation = false`）停用默认导航。然后，您可以使用 `st.page_link` 手动构建自定义导航菜单。使用 `st.page_link`，您可以更改导航菜单中的页面标签和图标，但不能更改页面的 URL。

## 页面术语

页面有四个识别部分，如下所示：

- **页面源**：这是包含页面源代码的 Python 文件或可调用函数。
- **页面标签**：这是页面在导航菜单中的标识方式。请参见 <i style={{ verticalAlign: "-.25em" }} class="material-icons-sharp">looks_one</i>。
- **页面标题**：这是 HTML `<title>` 元素的内容，以及页面在浏览器标签页中的标识方式。请参见 <i style={{ verticalAlign: "-.25em" }} class="material-icons-sharp">looks_two</i>。
- **页面 URL 路径名**：这是从应用根 URL 的页面相对路径。请参见 <i style={{ verticalAlign: "-.25em" }} class="material-icons-sharp">looks_3</i>。

此外，页面可以有两个图标，如下所示：

- **页面 favicon**：这是页面标题旁边在浏览器标签页中的图标。请参见 <i style={{ verticalAlign: "-.25em" }} class="material-icons-sharp">looks_4</i>。
- **页面图标**：这是导航菜单中页面标签旁边的图标。请参见 <i style={{ verticalAlign: "-.25em" }} class="material-icons-sharp">looks_5</i>。

通常，页面图标和 favicon 是相同的，但可以使它们不同。

<div style={{ maxWidth: '564px', margin: 'auto' }}>
<Image caption="1. 页面标签, 2.页面标题, 3. 页面 URL 路径名, 4.页面 favicon, 5. 页面图标" src="/images/page_parts.jpg" frame />
</div>

## Automatic page labels and URLs

If you use `st.Page` without declaring the page title or URL pathname, Streamlit falls back on automatically determining the page label, title, and URL pathname in the same manner as when you use a `pages/` directory with the default navigation menu. This section describes this naming convention which is shared between the two approaches to multipage apps.

### Parts of filenames and callables

Filenames are composed of four different parts as follows (in order):

1. `number`: A non-negative integer.
2. `separator`: Any combination of underscore (`"_"`), dash (`"-"`), and space (`" "`).
3. `identifier`: Everything up to, but not including, `".py"`.
4. `".py"`

For callables, the function name is the `identifier`, including any leading or trailing underscores.

### How Streamlit converts filenames into labels and titles

Within the navigation menu, Streamlit displays page labels and titles as follows:

1. If your page has an `identifier`, Streamlit displays the `identifier`. Any underscores within the page's `identifier` are treated as spaces. Therefore, leading and trailing underscores are not shown. Sequential underscores appear as a single space.
2. Otherwise, if your page has a `number` but does not have an `identifier`, Streamlit displays the `number`, unmodified. Leading zeros are included, if present.
3. Otherwise, if your page only has a `separator` with no `number` and no `identifier`, Streamlit will not display the page in the sidebar navigation.

The following filenames and callables would all display as "Awesome page" in the sidebar navigation.

- `"Awesome page.py"`
- `"Awesome_page.py"`
- `"02Awesome_page.py"`
- `"--Awesome_page.py"`
- `"1_Awesome_page.py"`
- `"33 - Awesome page.py"`
- `Awesome_page()`
- `_Awesome_page()`
- `__Awesome_page__()`

### How Streamlit converts filenames into URL pathnames

Your app's homepage is associated to the root URL of app. For all other pages, their `identifier` or `number` becomes their URL pathname as follows:

- If your page has an `identifier` that came from a filename, Streamlit uses the `identifier` with one modification. Streamlit condenses each consecutive grouping of spaces (`" "`) and underscores (`"_"`) to a single underscore.
- Otherwise, if your page has an `identifier` that came from the name of a callable, Streamlit uses the `identifier` unmodified.
- Otherwise, if your page has a `number` but does not have an `identifier`, Streamlit uses the `number`. Leading zeros are included, if present.

For each filename in the list above, the URL pathname would be "Awesome_page" relative to the root URL of the app. For example, if your app was running on `localhost` port `8501`, the full URL would be `localhost:8501/awesome_page`. For the last two callables, however, the pathname would include the leading and trailing underscores to match the callable name exactly.

## Navigating between pages

The primary way users navigate between pages is through the navigation widget. Both methods for defining multipage apps include a default navigation menu that appears in the sidebar. When a user clicks this navigation widget, the app reruns and loads the selected page. Optionally, you can hide the default navigation UI and build your own with [`st.page_link`](/develop/api-reference/widgets/st.page_link). For more information, see [Build a custom navigation menu with `st.page_link`](/develop/tutorials/multipage/st.page_link-nav).

If you need to programmatically switch pages, use [`st.switch_page`](/develop/api-reference/navigation/st.switch_page).

Users can also navigate between pages using URLs as noted above. When multiple files have the same URL pathname, Streamlit picks the first one (based on the ordering in the navigation menu. Users can view a specific page by visiting the page's URL.

<Important>
    Navigating between pages by URL creates a new browser session. In particular, clicking markdown links to other pages resets ``st.session_state``. In order to retain values in ``st.session_state``, handle page switching through Streamlit navigation commands and widgets, like ``st.navigation``, ``st.switch_page``, ``st.page_link``, and the built-in navigation menu.
</Important>

If a user tries to access a URL for a page that does not exist, they will see a modal like the one below, saying "Page not found."

<div style={{ maxWidth: '75%', margin: 'auto' }}>
<Image alt="Page not found" src="/images/mpa-page-not-found.png" />
</div>
