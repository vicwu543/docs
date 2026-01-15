---
title: 嵌入你的应用
slug: /deploy/streamlit-community-cloud/share-your-app/embed-your-app
description: 了解如何使用iframe和oEmbed方法在网站、博客和平台中嵌入Streamlit应用，具有可自定义的选项。
keywords: 嵌入, iframe, oembed, 网站, 博客, 平台, 集成, 自定义, 选项, 共享
---

# 嵌入你的应用

在网站、博客和平台中嵌入Streamlit Community Cloud应用可以通过将交互式、数据驱动的应用直接集成到页面中来丰富你的内容。无论你是在写博客文章、技术文档，还是在Medium、Notion甚至StackOverflow等平台上共享资源，嵌入Streamlit应用都会为你的内容添加动态组件。这允许你的观众与你的想法互动，而不仅仅是阅读或查看截图。

Streamlit Community Cloud支持使用[iframe](#embedding-with-iframes)和[oEmbed](#embedding-with-oembed)两种方法来嵌入**公开**应用。这种灵活性使你能够在各种平台上分享你的应用，扩大应用的可见性和影响力。在本指南中，我们将介绍如何有效地使用两种方法与世界分享Streamlit应用。

## 使用iframe嵌入

Streamlit Community Cloud支持使用子域方案嵌入**公开**应用。要嵌入公开应用，将查询参数`/?embed=true`添加到`*.streamlit.app` URL的末尾。

例如，假设你想嵌入[30DaysOfStreamlit应用](https://30days.streamlit.app/)。要在iframe中包含的URL是：`https://30days.streamlit.app/?embed=true`：

```javascript
<iframe
  src="https://30days.streamlit.app?embed=true"
  style="height: 450px; width: 100%;"
></iframe>
```

<Important>

对于嵌入私有应用，将没有正式支持。

</Important>

除了允许你通过iframe嵌入应用，`?embed=true`查询参数还执行以下操作：

- 移除带有应用菜单图标的工具栏。
- 移除应用顶部和底部的填充。
- 移除页脚。
- 移除应用顶部的彩色线。

为了对嵌入行为进行细粒度控制，Streamlit允许你指定一个或多个`?embed_options`查询参数实例（例如显示工具栏、以深色主题打开应用等）。[点击此处查看完整的嵌入选项列表。](#embed-options)

## 使用oEmbed嵌入

Streamlit的oEmbed支持提供了更简单的嵌入体验。你可以直接将Streamlit应用的URL放入Medium、Ghost或Notion页面（或任何支持oEmbed或embed.ly的700多个内容提供商）。嵌入的应用将自动出现！这有助于Streamlit Community Cloud应用无缝集成到这些平台中，提高应用的可见性和可访问性。

### 示例

在Notion页面、Medium文章或Ghost博客中创建内容时，你只需粘贴应用的URL并按"Enter"。然后应用将在内容中的该位置自动呈现。你可以使用不带`?embed=true`查询参数的应用URL。

```
https://30days.streamlit.app/
```

oEmbed应该可以在几个平台上开箱即用，包括但不限于：

- Medium
- Notion
- Looker
- Tableau
- Ghost
- Discourse
- StackOverflow
- W3
- Reddit

请查看具体平台的文档以验证对oEmbed的支持。

### iframe与oEmbed的比较

这两种方法之间唯一值得注意的区别是iframe允许你使用下一部分中描述的各种`?embed_options`来自定义应用的嵌入行为（例如显示工具栏、以深色主题打开应用等）。

## 嵌入选项

当使用iframe嵌入时，Streamlit允许你指定一个或多个`?embed_options`查询参数实例来对嵌入行为进行细粒度控制。

`?embed`和`?embed_options`对`st.query_params`及其前身`st.experimental_get_query_params`和`st.experimental_set_query_params`都是不可见的。你无法获取或设置它们的值。

`?embed_options`的支持值如下所列：

1. 显示应用右上角的工具栏，包括应用菜单、运行按钮和GitHub链接。

   ```javascript
   /?embed=true&embed_options=show_toolbar
   ```

2. 显示应用顶部和底部的填充。

   ```javascript
   /?embed=true&embed_options=show_padding
   ```

3. 显示读取"Made with Streamlit."的页脚。（这不适用于Streamlit 1.29.0及更高版本，因为页脚已从库中移除。）

   ```javascript
   /?embed=true&embed_options=show_footer
   ```

4. 显示应用顶部的彩色线。

   ```javascript
   /?embed=true&embed_options=show_colored_line
   ```

5. 隐藏应用加载时出现的"骨架"。

   ```javascript
   /?embed=true&embed_options=hide_loading_screen
   ```

6. 禁用应用主体的滚动。（侧栏仍可滚动。）

   ```javascript
   /?embed=true&embed_options=disable_scrolling
   ```

7. 使用浅色主题打开应用。

   ```javascript
   /?embed=true&embed_options=light_theme
   ```

8. 使用深色主题打开应用。

   ```javascript
   /?embed=true&embed_options=dark_theme
   ```

你也可以组合这些参数：

```javascript
/?embed=true&embed_options=show_toolbar&embed_options=show_padding&embed_options=show_footer&embed_options=show_colored_line&embed_options=disable_scrolling
```

### 构建嵌入链接

你可以方便地直接从应用构建嵌入链接！

1. 从`<your-custom-subdomain>.streamlit.app`的应用，点击右上角的"共享"。
2. 点击"嵌入"以访问可选择的嵌入选项列表。
3. 选择嵌入选项并点击"获取嵌入链接"以将嵌入链接复制到剪贴板。
