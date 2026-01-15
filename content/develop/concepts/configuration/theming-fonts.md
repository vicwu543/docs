---
title: 自定义字体
slug: /develop/concepts/configuration/theming-customize-fonts
description: 了解如何通过从 URL 或静态文件服务加载自定义字体文件，在 Streamlit 应用中配置字体，并为不同文本元素提供配置选项。
keywords: fonts, font customization, typography, custom fonts, font loading, static files, font configuration, text styling, font families, web fonts
---

# 在您的 Streamlit 应用中自定义字体

Streamlit 允许您更改和自定义应用中的字体。您可以从公共 URL 加载字体文件，或使用[静态文件服务](/develop/concepts/configuration/serving-static-files)与您的应用一起托管它们。

## 默认 Streamlit 字体

Streamlit 附带 [Source Sans](https://fonts.adobe.com/fonts/source-sans)、[Source Serif](https://fonts.adobe.com/fonts/source-serif) 和 [Source Code](https://fonts.adobe.com/fonts/source-code-pro) 字体。这些字体文件包含在 Streamlit 库中，因此客户端不会从第三方下载它们。默认情况下，Streamlit 对除行内代码和代码块之外的所有文本使用 Source Sans，而行内代码和代码块使用 Source Code。

要使用这些默认字体，您可以在 `config.toml` 中将以下配置选项设置为 `"sans-serif"`（Source Sans）、`"serif"`（Source Serif）或 `"monospace"`（Source Code）：

```toml filename=".streamlit/config.toml"
[theme]
font = "sans-serif"
headingFont = "sans-serif"
codeFont = "monospace"
[theme.sidebar]
font = "sans-serif"
headingFont = "sans-serif"
codeFont = "monospace"
```

您可以在 `config.toml` 的 `[theme]` 表中设置基础字体粗细和大小。这些不能在侧边栏中单独配置。

- `theme.baseFontSize` 设置应用的根字体大小。
- `theme.baseFontWeight` 设置应用的根字体粗细。

以下配置选项可以通过在 `config.toml` 中使用 `[theme.sidebar]` 表而不是 `[theme]` 表为侧边栏单独设置：

- `theme.font` 设置应用中所有文本的默认字体（除行内代码和代码块外）。默认为 `"sans-serif"`（Source Sans）。
- `theme.headingFont` 设置应用中所有标题的默认字体。如果未设置此项，Streamlit 将使用 `theme.font`。
- `theme.headingFontSizes` 设置 `<h1>`-`<h6>` 标题的字体大小。
- `theme.headingFontWeights` 设置 `<h1>`-`<h6>` 标题的字体粗细。
- `theme.codeFont` 设置所有行内代码和代码块的默认字体。默认为 `"monospace"`（Source Code）。
- `theme.codeFontSize` 设置代码块中、`st.json` 和 `st.help`（但不包括行内代码）的代码文本大小。
- `theme.codeFontWeight` 设置代码块中、`st.json` 和 `st.help`（但不包括行内代码）的代码文本粗细。

当未在 `[theme.sidebar]` 中声明字体时，Streamlit 将在默认为较不具体的选项之前从 `[theme]` 继承每个选项。例如，如果未设置 `theme.sidebar.headingFont`，Streamlit 将按优先顺序使用 `theme.headingFont`、`theme.sidebar.font` 或 `theme.font`。

在以下 `config.toml` 示例中，Streamlit 在应用主体中使用 Source Serif，在侧边栏中使用 Source Sans。

```toml filename=".streamlit/config.toml"
[theme]
font = "serif"
[theme.sidebar]
font = "sans-serif"
```

## 外部托管字体

如果您使用像 Google Fonts 或 Adobe Fonts 这样的字体服务，您可以通过将字体系列（名称）和 CSS URL 编码为 `{font_name}:{css_url}` 形式的单个字符串直接使用这些字体。如果您的字体系列包含空格，请在字体系列上使用内引号。在以下 `config.toml` 示例中，Streamlit 对除代码外的所有文本使用 Nunito 字体，而代码则使用 Space Mono。Space Mono 有内引号，因为它有空格。

```toml filename=".streamlit/config.toml"
[theme]
font = "Nunito:https://fonts.googleapis.com/css2?family=Nunito&display=swap"
codeFont = "'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono&display=swap"
```

<Important>

如果您将应用配置为包含任何第三方集成，包括外部托管的字体，您的应用可能会将用户数据（例如 IP 地址）传输到外部服务器。作为应用开发人员，您有责任通知用户这些第三方集成，提供相关隐私政策的访问途径，并确保遵守所有适用的数据保护法律和法规。

</Important>

## 托管替代字体

如果您有要与应用一起托管的字体文件，则必须在 `config.toml` 下的 `[[theme.fontFaces]]` 中声明字体。对于多个替代字体，在配置文件中声明多个 `[[theme.fontFaces]]` 表。您可以使用 Streamlit 静态文件服务自托管字体，或者可以指向公开托管的字体文件。

<Important>

Streamlit 支持对 OTF、TTF、WOFF 和 WOFF2 字体文件格式的自托管。其他字体文件格式必须外部托管。

</Important>

字体在其 `[[theme.fontFaces]]` 表中使用以下属性定义：

- `family`: 这是字体的名称，用于标识字体以供其他配置选项使用。
- `url`: 这是字体文件的位置。如果您与应用一起自托管字体文件，该值将类似于 `"app/static/font_file.woff"`。
- `weight`（可选）：这声明了字体文件中字体的粗细（例如 `400`、`"200 800"` 或 `"bold"`）。更多信息，请参见 [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-weight) CSS `@font-face` 描述符。
- `style`（可选）：这声明了字体文件中字体的样式（例如 `"normal"`、`"italic"` 或 `"oblique"`）。更多信息，请参见 [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-style) CSS `@font-face` 描述符。
- `unicodeRange`（可选）：这声明了字体文件中的特定字符范围（例如 `"U+0025-00FF, U+4??"`）。更多信息，请参见 [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/unicode-range) CSS `@font-face` 描述符。

<Note>

字体文件可以是静态的或可变的。静态字体文件包含单个粗细和样式。如果您使用静态字体文件，通常需要加载多个文件以在不同粗细（常规、粗体）和样式（常规、斜体）中完全支持字体。可变字体文件参数化一个或多个字体属性，这意味着单个字体文件可以支持多种粗细和样式。

</Note>

### 示例 1：使用可变字体文件定义替代字体

以下示例使用静态文件服务托管 Google 的 [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) 和 [Noto Sans Mono](https://fonts.google.com/noto/specimen/Noto+Sans+Mono) 字体，并配置应用使用它们。这两种字体都使用包含参数化粗细的可变字体文件定义。然而，由于字体样式没有参数化，Noto Sans 需要两个文件来分别定义常规和斜体样式。Noto Sans Mono 不包含其斜体样式的单独文件。根据 [CSS 规则](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style#italic)，如果没有显式提供斜体样式，它将通过倾斜常规样式字体来模拟。

此示例的逐行解释可在[教程](/develop/tutorials/configuration-and-theming/variable-fonts)中获得。

```toml filename=".streamlit/config.toml"
[server]
enableStaticServing = true

[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-Italic-VariableFont_wdth,wght.ttf"
style="italic"
[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-VariableFont_wdth,wght.ttf"
style="normal"
[[theme.fontFaces]]
family="noto-mono"
url="app/static/NotoSansMono-VariableFont_wdth,wght.ttf"

[theme]
font="noto-sans"
codeFont="noto-mono"
```

```none filename="Directory structure"
project_directory/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
│   ├── NotoSans-VariableFont_wdth,wght.ttf
│   └── NotoSansMono-VariableFont_wdth,wght.ttf
└── streamlit_app.py
```

### 示例 2：使用静态字体文件定义替代字体

在此配置示例中，使用多个静态字体文件声明替代字体。要覆盖基本 Markdown 格式，每种字体至少应有四个静态文件来定义以下粗细-样式对：

- normal normal
- normal bold
- italic normal
- italic bold

如果您的应用使用没有匹配粗细-样式定义的字体，用户的浏览器将使用最接近的可用字体。`<h2>`-`<h6>` 标题的默认粗细为半粗体（600）。为了完整性，包含额外的字体文件以覆盖半粗体粗细和应用中的所有字体粗细。以下示例使用 [Tuffy](https://fonts.google.com/specimen/Tuffy) 字体。该字体有四个静态字体文件，覆盖四种粗细-样式对。

此示例的逐行解释可在[教程](/develop/tutorials/configuration-and-theming/static-fonts)中获得。

```toml filename=".streamlit/config.toml"
[server]
enableStaticServing = true

[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Regular.ttf"
style="normal"
weight=400
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Bold.ttf"
style="normal"
weight=700
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Italic.ttf"
style="italic"
weight=400
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-BoldItalic.ttf"
style="italic"
weight=700

[theme]
font="tuffy"
```

```none filename="Directory structure"
project_directory/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── Tuffy-Bold.ttf
│   ├── Tuffy-BoldItalic.ttf
│   ├── Tuffy-Italic.ttf
│   └── Tuffy-Regular.ttf
└── streamlit_app.py
```

## 字体回退

如果您使用可能与所有浏览器不兼容的复杂字体，或者如果您使用外部托管字体，最佳做法是包含字体回退。

### 示例 3：定义带有回退的替代字体

在您的配置文件中，无论您在哪里声明默认字体，您都可以使用逗号分隔的字体列表代替。字体（或逗号分隔的字体列表）传递给 CSS [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) 属性。

您始终可以包含 Streamlit 的默认字体之一作为最终回退。以下示例使用 [Nunito](https://fonts.google.com/specimen/Nunito) 和 [Space Mono](https://fonts.google.com/specimen/Space+Mono) 字体。配置文件指向 Google 托管的字体文件，并将 Streamlit 的内置字体标识为备份。

此示例的逐行解释可在[教程](/develop/tutorials/configuration-and-theming/external-fonts)中获得。

```toml filename=".streamlit/config.toml"
[theme]
font="Nunito:https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000, sans-serif"
codeFont="'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap, monospace"
```

<Tip>

如果您的任何字体系列名称包含空格且您正在声明回退序列，请在名称周围使用内引号。例如，如果将字体命名为 `"Nunito Sans"`，请使用 `font="'Nunito Sans', sans-serif"`。

</Tip>

## 字体大小

您可以用像素设置应用的基础字体大小。必须将基础字体大小指定为整数。以下配置相当于 16 像素的默认基础字体大小：

```toml filename=".streamlit/config.toml"
[theme]
baseFontSize=16
```

此外，您可以设置代码块的字体大小。字体大小可以以像素或 rem 声明。以下配置相当于 0.875rem 的默认代码字体大小。

```toml filename=".streamlit/config.toml"
[theme]
codeFontSize="0.875rem"
```

<Note>

Markdown 中的行内代码不受 `theme.codeFontSize` 影响。行内代码设置为 0.75em。

</Note>

## 字体颜色

字体颜色选项在[在 Streamlit 应用中自定义颜色和边框](/develop/concepts/configuration/theming-customize-colors-and-borders#textcolor-and-linkcolor)中描述。

## 设计提示

在 Streamlit 应用中使用替代字体时，请牢记良好的设计实践。字体的可读性受其大小、与背景的对比度和形状的强烈影响。Streamlit 允许您为标题声明与其余文本不同的字体。如果您引入更精美的字体，请将其限制在标题中。由于 `theme.font` 和 `theme.sidebar.font` 用于设置部件标签、工具提示、列标题和数据框单元格中的字体，它们始终应该是高度可读的字体。

获取灵感，请参见 [Fonts in Use](https://fontsinuse.com/)。