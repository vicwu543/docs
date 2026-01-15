---
title: 主题
slug: /develop/concepts/configuration/theming
description: 了解 config.toml 中的主题选项，包括配色方案、字体和视觉样式。
keywords: theming, app customization, visual styling, color schemes, app appearance, theme configuration, config.toml, styling options, UI customization
---

# 主题概述

在本指南中，我们将概述 Streamlit 应用的主题和视觉定制。Streamlit 主题使用配置选项定义，通常在 `.streamlit/config.toml` 文件中定义。有关设置配置选项的更多信息，请参见[使用配置选项](/develop/concepts/configuration/options)。有关配置选项和定义的完整列表，请参见 [config.toml](/develop/api-reference/configuration/config.toml#theme) 的 API 参考。

您可以为应用配置浅色和深色主题，用户可以通过设置菜单进行切换。几乎所有的主题选项中，侧边栏都可以与主应用分开配置。

以下选项可以在 `config.toml` 的 `[theme]` 表中设置，不能在侧边栏、深色主题或浅色主题表中单独设置：

- **基础配色方案**：设置自定义主题以继承 Streamlit 的浅色或深色主题，或使用外部主题 TOML 文件。
- **基础字体**：设置基础字体粗细和大小。（这可以单独配置标题和代码字体。）
- **图表颜色**：为 Plotly、Altair 和 Vega-Lite 图表设置系列颜色。
- **侧边栏边框**：设置侧边栏边框的可见性。

以下选项可以为主应用主体和侧边栏分别配置。它们也可以分别指定为深色和浅色主题（`[theme.light]`、`[theme.light.sidebar]`、`[theme.dark]`、`[theme.dark.sidebar]`）：

- **字体系列**：设置正文文本、标题和代码的字体系列。
- **字体样式**：设置标题和代码字体的粗细和大小，并设置链接下划线的可见性。
- **文字颜色**：设置正文、行内代码和链接文本的颜色。
- **主色调**：设置交互元素和高亮的颜色。
- **背景色**：设置应用、部件、代码块和数据框标题的背景色。
- **边框半径**：设置元素和部件的圆角程度。
- **边框颜色**：设置元素、部件、侧边栏和数据框边框的颜色和可见性。
- **基本调色板**：设置用于 Markdown 文本着色和火花线等的调色板（红、橙、黄、绿、蓝、紫和灰/灰色）。

## 示例主题

以下浅色主题灵感来自 [Anthropic](https://docs.anthropic.com/en/home)。
<Cloud name="doc-theming-overview-anthropic-light-inspired" height="500px" />

以下深色主题灵感来自 [Spotify](https://open.spotify.com/)。
<Cloud name="doc-theming-overview-spotify-inspired" height="500px" />

## 在开发过程中使用主题配置

大多数主题配置选项可以在应用运行时更新。这使得迭代自定义主题变得容易。如果您更改应用的主要颜色，保存 `config.toml` 文件并重新运行应用，您将立即看到新颜色。但是，某些配置选项（如 `[[theme.fontFace]]`）需要您重启 Streamlit 服务器才能反映更新。如有疑问，在更新应用配置时，请在终端中停止 Streamlit 服务器，并使用 `streamlit run` 命令重新启动应用。