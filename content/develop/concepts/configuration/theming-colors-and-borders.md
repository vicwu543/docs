---
title: 颜色和边框
slug: /develop/concepts/configuration/theming-customize-colors-and-borders
description: 了解如何使用主题配置选项和颜色值在 Streamlit 应用中自定义颜色、边框、背景和 UI 元素。
keywords: colors, borders, theming, UI customization, color values, background colors, border styling, visual design, theme colors, app styling
---

# 自定义 Streamlit 应用中的颜色和边框

## 颜色值

对于所有接受颜色的配置选项，您可以使用以下字符串之一指定值：

- 一个 CSS [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) 如 `"darkBlue"` 或 `"maroon"`。
- 一个十六进制字符串如 `"#483d8b"` 或 `"#6A5ACD"`。
- 一个 RGB 字符串如 `"rgb(106, 90, 205)"` 或 `"RGB(70, 130, 180)"`。
- 一个 HSL 字符串如 `"hsl(248, 53%, 58%)"` 或 `"HSL(147, 50%, 47%)"`。

<Tip>

虽然您可以为颜色指定 alpha 值，但这对于大多数选项来说并不是必要的。Streamlit 会调整颜色的 alpha 值，以确保背景和前景之间的上下文适当着色。

</Tip>

## 默认 Streamlit 颜色

Streamlit 附带两个预配置的主题：浅色和深色。如果您不指定任何主题配置选项，Streamlit 将尝试使用最匹配每个用户浏览器设置的预配置主题。这些主题特色是红色主色调，还包括一个基本调色板（红、橙、黄、绿、蓝、紫和灰/灰色），用于着色 Markdown 文本等元素。

## 颜色和边框配置选项

大多数主题配置选项可以为整个应用设置，但您可以使用不同的值覆盖侧边栏的某些选项。例如，应用的主要颜色 (`primaryColor`) 用于突出显示交互元素和显示焦点。如果设置 `theme.primaryColor`，这将更改整个应用的主要颜色。但是，如果设置 `theme.sidebar.primaryColor`，这将在侧边栏中覆盖 `theme.primaryColor`，允许您使用两种不同的主要颜色。

以下两个配置选项只能应用于整个应用：

- `theme.base` 将应用主题的默认颜色设置为匹配 Streamlit 两个默认主题之一（`"light"` 或 `"dark"`）。如果使用了任何主题配置选项且未设置 `theme.base`，则 Streamlit 将使用 `"light"`。
- `theme.showSidebarBorder` 设置侧边栏与应用主体之间的边框可见性。
- `theme.chartCategoricalColors` 和 `theme.chartSequentialColors` 设置 Plotly、Altair 和 Vega-Lite 图表的系列颜色。

以下配置选项可以通过在 `config.toml` 中使用 `[theme.sidebar]` 表而不是 `[theme]` 表为侧边栏单独设置：

- `theme.primaryColor`
- `theme.backgroundColor`
- `theme.secondaryBackgroundColor`
- `theme.textColor`
- `theme.linkColor`
- `theme.linkUnderline`
- `theme.codeTextColor`
- `theme.codeBackgroundColor`
- `theme.baseRadius`
- `theme.buttonRadius`
- `theme.borderColor`
- `theme.dataframeBorderColor`
- `theme.dataframeHeaderBackgroundColor`
- `theme.showWidgetBorder`
- 所有调色板选项

为简洁起见，在本页其余部分，主题配置选项将不包含 `theme.` 或 `theme.sidebar.` 前缀。

### 基本调色板

Streamlit 中的各种元素使用或让您从预定义的颜色调色板中选择：红、橙、黄、绿、蓝、紫和灰/灰色。以下是使用此基本调色板的一些元素：

- Markdown 文本和背景颜色（包括 `st.badge`）。
- `st.metric` 火花线和增量。
- 数据框图表列。
- 聊天消息头像。
- 警告元素如 `st.success` 和 `st.warning`。

对于调色板中的每种颜色，您可以定义基础颜色、背景颜色和文本颜色。如果您只定义基础颜色，Streamlit 会调整亮度/暗度和不透明度以自动提供相应的背景和文本颜色。但是，您也可以手动定义每一项。以下是调色板选项：

- `redColor`, `redBackgroundColor`, `redTextColor`
- `orangeColor`, `orangeBackgroundColor`, `orangeTextColor`
- `yellowColor`, `yellowBackgroundColor`, `yellowTextColor`
- `greenColor`, `greenBackgroundColor`, `greenTextColor`
- `blueColor`, `blueBackgroundColor`, `blueTextColor`
- `violetColor`, `violetBackgroundColor`, `violetTextColor`
- `grayColor`, `grayBackgroundColor`, `grayTextColor`

### `primaryColor`

`primaryColor` 定义在整个 Streamlit 应用中最常使用的强调色。
以下功能和效果使用您的主要颜色：

- 按钮悬停效果
- 焦点中的元素
- 选中的元素

<Tip>

当您的主要颜色用作背景时，Streamlit 将文本颜色更改为白色。例如，这发生在 `type="primary"` 按钮和 `st.multiselect` 中的选中项目上。

为了可读性，请始终选择足够深的主要颜色，以便与白色文本形成良好的对比。

</Tip>

#### 示例 1：主要颜色

以下配置示例具有 `"forestGreen"` 主要颜色。在侧边栏中，配置覆盖主要颜色为 `"darkGoldenrod"`。如果您点击部件内部以使其获得焦点，Streamlit 会在部件周围显示主要颜色边框。此外，如果您悬停在次要和三级按钮上，悬停颜色与主要颜色匹配。

```toml
[theme]
base="dark"
primaryColor="forestGreen"

[theme.sidebar]
primaryColor="darkGoldrod"
```

<Cloud name="doc-theming-color-primarycolor" height="350px" />

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, 和 `dataframeHeaderBackgroundColor`

- `backgroundColor` 定义应用的背景色。
- `secondaryBackgroundColor` 用于以下位置的对比：
  - 部件的输入或选择区域的背景
  - `st.help` 和 `st.dataframe` 等元素内的标题（如果未设置 `dataframeHeaderBackgroundColor`）
  - 代码块和行内代码（如果未设置 `codeBackgroundColor`）
- `codeBackgroundColor` 设置代码块和行代码的背景。如果未设置 `codeBackgroundColor`，Streamlit 将使用 `secondaryBackgroundColor`。
- `dataframeHeaderBackgroundColor` 设置数据框标题的背景（包括用于行选择和添加的单元格，如果存在的话）。

<Note>

如果您未定义侧边栏的背景色，Streamlit 将在侧边栏中交换 `backgroundColor` 和 `secondaryBackgroundColor`：

- 如果未定义 `theme.sidebar.backgroundColor`，Streamlit 使用 `theme.secondaryBackgroundColor`。
- 如果未定义 `theme.sidebar.secondaryBackgroundColor`，Streamlit 使用 `theme.backgroundColor`。

</Note>

#### 示例 2：背景色

以下配置示例具有 `"white"` 背景，以及薰衣草色调的 `"ghostWhite"` 侧边栏背景。整个应用的次要颜色是 `"lavender"`，代码背景色是 `"powderBlue"`。代码背景色在 `[theme]` 中配置一次，并在侧边栏中继承。但是，由于 Streamlit 在侧边栏继承背景色时会交换它们，因此次要背景色在 `[theme]` 和 `[theme.sidebar]` 中都设置了。要查看次要颜色用于悬停效果，请悬停在数据框单元格上或打开多选下拉菜单。

```toml
[theme]
base="light"
backgroundColor="white"
secondaryBackgroundColor="lavender"
codeBackgroundColor="powderBlue"

[theme.sidebar]
backgroundColor="ghostWhite"
secondaryBackgroundColor="lavender"
```

<Cloud name="doc-theming-color-backgroundcolor" height="450px" />

### `textColor`, `codeTextColor`, `linkColor`, 和 `linkUnderline`

您可以配置正文、代码和链接文本的颜色。

`textColor` 设置应用中所有文本的默认文本颜色，除了代码块中的语言高亮、行内代码和链接之外。
`codeTextColor` 设置行内代码的默认文本颜色，但不影响代码块。
`linkColor` 设置应用中所有 Markdown 链接的默认字体颜色。如果 `linkUnderline` 设置为 true（默认值），则链接下划线颜色与 `linkColor` 匹配。

以下元素受 `textColor` 影响：

- Markdown 文本，链接除外
- 代码块中没有通过语言高亮着色的文本
- 应用界面和侧边栏菜单图标
- 部件标签、图标、选项文本和占位符文本
- 数据框和表格文本
- 非 Markdown 链接，如 `st.page_link`、`st.link_button` 和导航菜单

如前所述，当文本显示在您的主要颜色之上时，Streamlit 会将文本颜色更改为白色。

#### 示例 3：文本颜色

以下配置示例在 `"dark"` 基础上具有 `"darkGoldenrod"` 文本和 `"darkOrchid"` 链接。按钮（包括 `st.link_button`）使用 `"darkGoldenrod"` 文本颜色。在多选部件中，占位符文本、下拉菜单和工具提示都具有 `"darkGoldenrod"` 文本。如果您悬停在侧边栏上，滚动条和折叠图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>chevron_left</i>）都是 `"darkGoldenrod"`。

```toml
[theme]
base="dark"
textColor="darkGoldenrod"
linkColor="darkOrchid"
```

<Cloud name="doc-theming-color-textcolor" height="400px" />

### `baseRadius` 和 `buttonRadius`

`baseRadius` 定义以下元素的边框和背景的半径：

- 部件上的按钮和输入区域
- 选中项目，包括 `st.multiselect` 和导航菜单中的项目
- 代码块和行内代码
- 数据框（外部）
- 徽章和 Markdown 文本背景
- 带边框的容器，包括扩展器、表单、对话框、弹窗和通知
- 工具提示，包括图表内的工具提示
- 状态和异常消息块
- 图像，包括显示为静态图像的 `st.graphviz` 和 `st.pyplot`

`buttonRadius` 为按钮和 `st.segmented_control` 覆盖 `baseRadius`。

有几个元素明显不完全受 `baseRadius` 影响。交互式图表和视频，由于具有更复杂的底层 HTML，将始终具有直角。这包括 `st.video`、`st.map` 和 `st.pydeck_chart`。相反，`st.chat_input` 和 `st.audio_input` 将始终完全圆角。像工具提示这样的子元素仍然受 `baseRadius` 影响。

#### 示例 4：边框半径

在以下配置示例中，应用的主体使用 `"full"`（1rem）基础半径，侧边栏使用 `"none"`（0rem）。为了更好地突出这一差异，示例包括对比鲜明的主要颜色和背景色。

```toml
[theme]
base="light"
primaryColor="slateBlue"
backgroundColor="mintCream"
secondaryBackgroundColor="darkSeaGreen"
baseRadius="full"

[theme.sidebar]
backgroundColor="aliceBlue"
secondaryBackgroundColor="skyBlue"
baseRadius="none"
```

<Cloud name="doc-theming-color-baseradius" height="500px" />

### `borderColor`, `dataframeBorderColor`, 和 `showWidgetBorder`

Streamlit 默认不显示未聚焦部件的边框（按钮除外）。当用户聚焦于部件时，Streamlit 会在输入区域周围以您的 `primaryColor` 显示边框。当用户移除焦点时，Streamlit 会隐藏边框。

如果设置 `showWidgetBorder=true`，Streamlit 将在部件未聚焦时显示部件边框。对于这些部件，边框颜色由 `borderColor` 设置。如果未设置 `borderColor`，Streamlit 通过向您的 `textColor` 添加透明度来推断颜色。

以下元素具有您可以修改的边框：

- 带边框的容器，包括扩展器、表单、对话框、弹窗和通知
- 侧边栏，包括右边缘和导航菜单下方的边界
- 数据框和表格
- `st.tabs`（底部边框）
- 按钮，包括 `st.button`、`st.pills` 和 `st.segmented_control`
- 输入区域的边框

`dataframeBorderColor` 为数据框和表格覆盖 `borderColor`。

#### 示例 5：边框颜色和可见性

以下配置示例在整个应用中使用 `"mediumSlateBlue"` 边框颜色。在侧边栏中，显示部件边框。在应用的主体中，不显示部件边框，并且除了在聚焦状态下之外，多选、文本或聊天输入区域周围没有边框。但是，许多其他元素，如按钮和数据框，具有始终可见的边框。

```toml
[theme]
base="dark"
borderColor="mediumSlateBlue"
showWidgetBorder=false

[theme.sidebar]
showWidgetBorder=true
```

<Cloud name="doc-theming-color-bordercolor" height="420px" />