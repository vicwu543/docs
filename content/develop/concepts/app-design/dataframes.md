---
title: 数据框
slug: /develop/concepts/design/dataframes
description: 学习如何在 Streamlit 中使用 st.dataframe 和 st.data_editor 显示和编辑表格数据，包括样式、配置和交互功能。
keywords: 数据框, st.dataframe, st.data_editor, pandas 数据框, 表格数据, 数据显示, 数据编辑, 列配置, 数据框样式, 交互式表格
---

# 数据框

数据框是以表格格式显示和编辑数据的好方法。使用 Pandas 数据框和其他表格数据结构是数据科学工作流的关键。如果开发人员和数据科学家想在 Streamlit 中显示此数据，他们有多个选项：`st.dataframe` 和 `st.data_editor`。如果你想仅在类似表格的 UI 中显示数据，[st.dataframe](/develop/api-reference/data/st.dataframe) 是正确的方法。如果你想以交互方式编辑数据，请使用 [st.data_editor](/develop/api-reference/data/st.data_editor)。我们在以下部分中探讨每个选项的使用情况和优势。

## 使用 st.dataframe 显示数据框

Streamlit 可以通过 `st.dataframe` 在类似表格的 UI 中显示数据框：

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
```

<Cloud name="doc-dataframe-basic" height="300px"/>

## `st.dataframe` UI 功能

`st.dataframe` 通过在底层使用 [glide-data-grid](https://github.com/glideapps/glide-data-grid) 提供额外的功能：

- **列排序**：要排序列，请选择其标题，或从标题菜单中选择"**升序排列**"或"**降序排列**"（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>）。
- **列调整大小**：要调整列的大小，请拖放列标题边框，或从标题菜单中选择"**自动调整**"。
- **列隐藏**：要隐藏列，请从标题菜单中选择"**隐藏列**"。
- **重新排序和固定列**：要重新排序列或将其固定在左侧，请拖放列标题或分别从标题菜单中选择"**固定列**"。
- **格式化数字、日期和时间**：要更改数值列的格式，请在标题菜单中的"**格式**"下选择一个选项。
- **数据框调整大小**：要调整数据框大小，请拖放右下角。
- **全屏视图**：要将数据框放大到全屏，请选择工具栏中的全屏图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>fullscreen</i>）。
- **搜索**：要搜索数据，请选择工具栏中的搜索图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>search</i>）或使用热键（`⌘+F` 或 `Ctrl+F`）。
- **下载**：要将数据下载为 CSV 文件，请选择工具栏中的下载图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>download</i>）。
- **复制到剪贴板**：要将数据复制到剪贴板，请选择一个或多个单元格，使用热键（`⌘+C` 或 `Ctrl+C`），然后将其粘贴到你喜欢的电子表格软件中。

<YouTube videoId="nauAnULRG1c" loop autoplay />

使用上一部分中的嵌入式应用尝试所有 UI 功能。

除了 Pandas DataFrames，`st.dataframe` 还支持其他常见的 Python 类型，例如列表、字典或 numpy 数组。它还支持 [Snowpark](https://docs.snowflake.com/en/developer-guide/snowpark/index) 和 [PySpark](https://spark.apache.org/docs/latest/api/python/) DataFrames，这些允许你懒惰地计算数据和从数据库中提取数据。这对于处理大型数据集很有用。

## 使用 st.data_editor 编辑数据

Streamlit 通过 `st.data_editor` 命令支持可编辑的数据框。在 [st.data_editor](/develop/api-reference/data/st.data_editor) 中查看其 API。它在表格中显示数据框，类似于 `st.dataframe`。但与 `st.dataframe` 不同，这个表格不是静态的！用户可以点击单元格并编辑它们。然后编辑的数据在 Python 端返回。以下是一个示例：

```python
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

edited_df = st.data_editor(df) # 👈 An editable dataframe

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
```

<Cloud name="doc-data-editor" height="300px"/>

尝试一下，双击任何单元格。你会注意到你可以编辑所有单元格值。尝试编辑评分列中的值并观察底部的文本输出如何变化：

## `st.data_editor` UI 功能

`st.data_editor` 还支持一些额外的功能：

- [**添加和删除行**](#add-and-delete-rows)：你可以在调用 `st.data_editor` 时设置 `num_rows="dynamic"` 来做到这一点。这将允许用户根据需要添加和删除行。
- [**复制和粘贴支持**](#copy-and-paste-support)：在 `st.data_editor` 和 Google Sheets、Excel 等电子表格软件之间进行复制和粘贴。
- [**访问编辑的数据**](#access-edited-data)：通过 Session State 仅访问单个编辑，而不是整个编辑的数据结构。
- [**批量编辑**](#bulk-edits)：类似于 Excel，只需拖动一个句柄来编辑相邻的单元格。
- [**自动输入验证**](#automatic-input-validation)：列配置提供强大的数据类型支持和其他可配置的选项。例如，无法将字母输入到数字单元格中。数字单元格可以有指定的最小值和最大值。
- [**编辑常见的数据结构**](#edit-common-data-structures)：`st.data_editor` 支持列表、字典、NumPy 数组等！

<YouTube videoId="6tah69LkfxE" loop autoplay />

### 添加和删除行

使用 `st.data_editor`，观看者可以通过表格 UI 添加或删除行。这个模式可以通过将 `num_rows` 参数设置为 `"dynamic"` 来激活：

```python
edited_df = st.data_editor(df, num_rows="dynamic")
```

- 要添加新行，请点击工具栏中的加号图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>add</i>）。或者，点击表格最后一行下方的带阴影的单元格。
- 要删除行，请使用左侧的复选框选择一个或多个行。点击删除图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>delete</i>）或在键盘上按 `delete` 键。

<Cloud name="doc-data-editor-clipboard" height="400px"/>

### 复制和粘贴支持

数据编辑器支持从 Google Sheets、Excel、Notion 和许多其他类似工具粘贴表格数据。你也可以在 `st.data_editor` 实例之间复制粘贴数据。这个功能由 [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API) 提供支持，对于需要跨多个平台处理数据的用户来说可以是一个巨大的时间节省器。要尝试它：

1. 从 [这个 Google Sheets 文档](https://docs.google.com/spreadsheets/d/1Z0zd-5dF_HfqUaDDq4BWAOnsdlGCjkbTNwDZMBQ1dOY/edit?usp=sharing) 复制数据到你的剪贴板。
2. 在上面的应用中单击 `name` 列中的任何单元格。使用热键（`⌘+V` 或 `Ctrl+V`）粘贴它。

<Note>

粘贴的数据的每个单元格将被单独计算，如果数据与列类型兼容，则插入到单元格中。例如，将非数字文本数据粘贴到数字列中将被忽略。

</Note>

<Tip>

如果你使用 iframe 嵌入应用，你需要允许 iframe 访问剪贴板，如果你想使用复制粘贴功能。为此，请给 iframe [`clipboard-write`](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/write) 和 [`clipboard-read`](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/read) 权限。例如

```javascript
<iframe allow="clipboard-write;clipboard-read;" ... src="https://your-app-url"></iframe>
```

作为开发者，使用 TLS 时确保应用由有效的、受信任的证书提供。如果用户在复制和粘贴数据时遇到问题，请让他们检查他们的浏览器是否已为 Streamlit 应用激活剪贴板访问权限，无论是在提示时还是通过浏览器的网站设置。

</Tip>

### 访问编辑的数据

有时，知道哪些单元格被更改比获得整个编辑的数据框返回更方便。Streamlit 通过使用 [Session State](/develop/concepts/architecture/session-state) 使这变得容易。如果设置了 `key` 参数，Streamlit 将把对数据框所做的任何更改存储在 Session State 中。

这个代码片段展示了如何使用 Session State 访问更改的数据：

```python
st.data_editor(df, key="my_key", num_rows="dynamic") # 👈 设置一个 key
st.write("Session State 中的值是：")
st.write(st.session_state["my_key"]) # 👈 显示 Session State 中的值
```

在这个代码片段中，`key` 参数设置为 `"my_key"`。创建数据编辑器后，Session State 中与 `"my_key"` 关联的值使用 `st.write` 在应用中显示。这显示了进行的添加、编辑和删除。

当处理大数据框时，这可能很有用，你只需要知道哪些单元格已更改，而不是访问整个编辑的数据框。

<Cloud name="doc-data-editor-changed" height="700px"/>

使用我们到目前为止学到的所有内容，并将它们应用到上面的嵌入式应用中。尝试编辑单元格、添加新行和删除行。

注意表格的编辑如何反映在 Session State 中。当你进行任何编辑时，会触发重新运行，将编辑发送到后端。小部件的状态是一个包含三个属性的 JSON 对象：**edited_rows**、**added_rows** 和 **deleted_rows：**。

<Warning>

从 1.23.0 中的 `st.experimental_data_editor` 迁移到 `st.data_editor` 时，数据编辑器在 `st.session_state` 中的表示已更改。`edited_cells` 字典现在称为 `edited_rows`，并使用不同的格式（`{0: {"column name": "edited value"}}` 而不是 `{"0:1": "edited value"}`）。如果你的应用在与 `st.session_state` 结合使用 `st.experimental_data_editor` 时，你可能需要调整代码。"

</Warning>

- `edited_rows` 是包含所有编辑的字典。键是从零开始的行索引，值是将列名映射到编辑的字典（例如 `{0: {"col1": ..., "col2": ...}}`）。
- `added_rows` 是新添加的行列表。每个值都是上述格式相同的字典（例如 `[{"col1": ..., "col2": ...}]`）。
- `deleted_rows` 是已从表中删除的行号列表（例如 `[0, 2]`）。

`st.data_editor` 不支持重新排序行，所以添加的行将始终附加到数据框的末尾，任何编辑和删除都适用于原始行。

### 批量编辑

数据编辑器包括一个允许批量编辑单元格的功能。类似于 Excel，你可以跨单元格选择拖动一个句柄来批量编辑它们的值。你甚至可以在电子表格软件中应用常用的 [键盘快捷键](https://github.com/glideapps/glide-data-grid/blob/main/packages/core/API.md#keybindings)。当你需要对多个单元格进行相同的更改，而不是单独编辑每个单元格时，这很有用。

### 编辑常见的数据结构

编辑不仅适用于 Pandas DataFrames！你还可以编辑列表、元组、集合、字典、NumPy 数组或 Snowpark & PySpark DataFrames。大多数数据类型将以其原始格式返回。但某些类型（例如 Snowpark 和 PySpark）会转换为 Pandas DataFrames。要了解所有支持的类型，请阅读 [st.data_editor](/develop/api-reference/data/st.data_editor) API。

例如，你可以轻松让用户向列表中添加项目：

```python
edited_list = st.data_editor(["red", "green", "blue"], num_rows="dynamic")
st.write("以下是你输入的所有颜色：")
st.write(edited_list)
```

或 numpy 数组：

```python
import numpy as np

st.data_editor(np.array([
	["st.text_area", "widget", 4.92],
	["st.markdown", "element", 47.22]
]))
```

或记录列表：

```python
st.data_editor([
    {"name": "st.text_area", "type": "widget"},
    {"name": "st.markdown", "type": "element"},
])
```

或字典和许多其他类型！

```python
st.data_editor({
	"st.text_area": "widget",
	"st.markdown": "element"
})
```

### 自动输入验证

数据编辑器包括自动输入验证，以帮助防止编辑单元格时出错。例如，如果你有一列包含数值数据，输入字段将自动限制用户仅输入数值数据。这有助于防止用户意外输入非数值数据可能导致的错误。可以通过 [列配置 API](/develop/api-reference/data/st.column_config) 配置其他输入验证。继续阅读下文以获取列配置概述，包括验证选项。

## 配置列

你可以通过 [列配置 API](/develop/api-reference/data/st.column_config) 在 `st.dataframe` 和 `st.data_editor` 中配置列的显示和编辑行为。我们开发了 API 以让你在数据框和数据编辑器列中添加图像、图表和可点击的 URL。此外，你可以使单个列可编辑，将列设置为分类并指定可以取哪些选项，隐藏数据框的索引等。

列配置包括以下列类型：Text、Number、Checkbox、Selectbox、Date、Time、Datetime、List、Link、Image、Line chart、Bar chart 和 Progress。还有一个通用的 Column 选项。查看下面的嵌入式应用以查看这些不同的列类型。每个列类型都在 [列配置 API](/develop/api-reference/data/st.column_config) 文档中单独预览。

<Cloud name="doc-column-config-overview" query="embed_options=disable_scrolling" height="480px"/>

### 格式化值

`format` 参数在 [Text](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)、[Date](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)、[Time](/develop/api-reference/data/st.column_config/st.column_config.timecolumn) 和 [Datetime](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn) 列的列配置中可用。类似图表的列也可以被格式化。[折线图](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn) 和 [柱状图](/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn) 列有 `y_min` 和 `y_max` 参数来设置垂直边界。对于 [Progress 列](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn)，你可以用 `min_value` 和 `max_value` 声明水平边界。

### 验证输入

指定列配置时，你不仅可以声明列的数据类型，还可以声明值限制。所有列配置元素都允许你使用关键字参数 `required=True` 使列为必需。

对于 Text 和 Link 列，你可以使用 `max_chars` 指定最大字符数，或使用正则表达式通过 `validate` 验证条目。数值列，包括 Number、Date、Time 和 Datetime 有 `min_value` 和 `max_value` 参数。Selectbox 列有可配置的 `options` 列表。

Number 列的数据类型默认为 `float`。将类型为 `int` 的值传递给 `min_value`、`max_value`、`step` 或 `default` 中的任何一个都会将列的类型设置为 `int`。

### 配置空数据框

你可以使用 `st.data_editor` 从用户收集表格输入。从空数据框开始时，默认列类型为文本。使用列配置指定你想从用户收集的数据类型。

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(df, column_config = config, num_rows='dynamic')

if st.button('Get results'):
    st.write(result)
```

<Cloud name="doc-column-config-empty" height="300px"/>

## 其他格式化选项

除了列配置外，`st.dataframe` 和 `st.data_editor` 还有一些参数来自定义数据框的显示。

- `hide_index` ：设置为 `True` 以隐藏数据框的索引。
- `column_order` ：传递列标签列表以指定显示顺序。
- `disabled` ：传递列标签列表以禁用它们的编辑。这让你可以避免单独禁用它们。

## 处理大型数据集

`st.dataframe` 和 `st.data_editor` 得益于使用 glide-data-grid 库和 HTML canvas 的高性能实现，已设计为理论上处理包含数百万行的表格。但是，应用可以现实处理的最大数据量将取决于许多其他因素，包括：

1. WebSocket 消息的最大大小：Streamlit 的 WebSocket 消息可通过 `server.maxMessageSize` [配置选项](https://docs.streamlit.io/develop/concepts/configuration#view-all-configuration-options) 配置，这限制了一次可以通过 WebSocket 连接传输的数据量。
2. 服务器内存：应用可以处理的数据量也取决于服务器上可用的内存量。如果服务器的内存被超出，应用可能会变得缓慢或无响应。
3. 用户的浏览器内存：由于所有数据都需要传输到用户的浏览器以进行渲染，用户设备上可用的内存量也会影响应用的性能。如果浏览器的内存被超出，它可能会崩溃或无响应。

除了这些因素外，慢速网络连接也会显著减速处理大型数据集的应用。

处理超过 150,000 行的大型数据集时，Streamlit 应用额外的优化并禁用列排序。这可以帮助减少一次需要处理的数据量，并提高应用的性能。

## 限制

- Streamlit 在内部将所有列名转换为字符串，所以 `st.data_editor` 将返回一个所有列名都是字符串的 DataFrame。
- 数据框工具栏目前不可配置。
- 虽然 Streamlit 的数据编辑功能提供了很多功能，但编辑仅针对有限的列类型集启用（[TextColumn](/develop/api-reference/data/st.column_config/st.column_config.textcolumn)、[NumberColumn](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn)、[LinkColumn](/develop/api-reference/data/st.column_config/st.column_config.linkcolumn)、[CheckboxColumn](/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn)、[SelectboxColumn](/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn)、[DateColumn](/develop/api-reference/data/st.column_config/st.column_config.datecolumn)、[TimeColumn](/develop/api-reference/data/st.column_config/st.column_config.timecolumn) 和 [DatetimeColumn](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)）。我们正在积极开发对其他列类型（如图像、列表和图表）的编辑支持。
- 几乎所有可编辑的数据类型都支持索引编辑。但是，`pandas.CategoricalIndex` 和 `pandas.MultiIndex` 不支持编辑。
- 当 `num_rows="dynamic"` 时，`st.data_editor` 不支持排序。
- 在超过 150,000 行的大型数据集上禁用排序以优化性能。

我们不断致力于改进 Streamlit 对 DataFrame 的处理并向数据编辑添加功能，所以请关注更新。
