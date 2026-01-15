---
title: 部件行为
slug: /develop/concepts/architecture/widget-behavior
description: 了解 Streamlit 部件如何在重新运行中表现，处理状态持久化，管理用户交互，以及控制应用程序中的部件生命周期。
keywords: widget behavior, widget state, user interactions, widget persistence, rerun behavior, interaction handling, state management, widget lifecycle
---

# 理解部件行为

部件（如 `st.button`、`st.selectbox` 和 `st.text_input`）是 Streamlit 应用的核心。它们是 Streamlit 的交互元素，将用户信息传递到您的 Python 代码中。部件是神奇的，通常按您想要的方式工作，但在某些情况下它们可能会有令人惊讶的行为。了解部件的不同部分以及事件发生的精确顺序有助于您实现所需的结果。

本指南涵盖有关部件的高级概念。通常，它从更简单的概念开始并逐渐增加复杂性。对于大多数初学者来说，这些细节不需要马上知道。当您想要动态更改部件或在页面之间保留部件信息时，这些概念就很重要了。我们建议在阅读本指南之前先基本了解[会话状态](/develop/api-reference/caching-and-state/st.session_state)。

<Collapse title="🎈 简而言之" expanded={false}>

1. 一个用户的行为不会影响任何其他用户的部件。
2. 部件命令返回部件的当前值，这是一个简单的 Python 类型。例如，`st.button` 返回一个布尔值。
3. 部件在首次调用时返回其默认值，直到用户与其交互。
4. 部件的身份取决于传递给部件命令的参数。**如果提供了键，只有键决定部件的身份，但有一些限制，因为这仍在实施中。** 如果没有提供键，更改部件的标签、最小或最大值、默认值、占位符文本或帮助文本将导致它重置。
5. 如果您在脚本运行中不调用部件命令，Streamlit 将删除部件的信息——_包括其在会话状态中的键值对_。如果您稍后调用相同的部件命令，Streamlit 将其视为新部件。
6. 部件在页面之间不是有状态的。如果您在不同页面上有两个具有相同键的部件，它们将被视为两个不同的部件。

最后三点（部件身份和部件删除）在动态更改部件或使用多页面应用时最相关。本指南后面将详细介绍：[部件的状态性](#部件的状态性) 和 [部件生命周期](#部件生命周期)。

</Collapse>

<Important>

**部件行为的最近变化**

从 v1.46.0 到 v1.52.0，引入了部件状态性的重大变化：

- **v1.46.0**：在页面之间导航时，`st.session_state` 中的部件键在新页面脚本运行开始时而非结束时删除。
- **v1.50.0-1.52.0**：当提供键时，部件身份由键和选择参数（最小/最大值和选项）确定。这是实施期间的过渡阶段，直到部件完全转换为仅键身份。

这些变化影响部件在页面导航和参数更改时如何保持状态。要查看哪些部件已转换为基于键的身份，请参阅 [v1.50.0](https://docs.streamlit.io/release-notes/v1.50.0)、[v1.51.0](https://docs.streamlit.io/release-notes/v1.51.0) 和 [v1.52.0](https://docs.streamlit.io/release-notes/v1.52.0) 的发行说明。

截至 v1.52.0，以下部件**尚未**转换为基于键的身份：`st.data_editor` 和具有选择模式的元素，如 `st.dataframe` 和图表。

</Important>

## 部件的组成

使用部件时需要记住四个部分：

1. 用户看到的前端组件。
2. 后端（Python）内存中的值。
3. `st.session_state` 中的键值对，提供对部件值的程序访问。
4. 部件函数返回的值。

### 部件依赖于会话

部件状态依赖于特定会话（浏览器连接）。一个用户的行为不会影响任何其他用户的部件。此外，如果用户打开多个标签页访问应用，每个标签页将是唯一的会话。更改一个标签页中的部件不会影响另一个标签页中的相同部件。

### 部件返回简单的 Python 数据类型

通过 `st.session_state` 看到的部件值以及部件函数返回的值都是简单的 Python 类型。例如，`st.button` 返回一个布尔值，如果使用键，将在 `st.session_state` 中保存相同的布尔值。首次调用部件函数时（在用户与其交互之前），它将返回其默认值。例如，`st.selectbox` 默认返回第一个选项。除了 `st.button` 和 `st.file_uploader` 等少数特殊情况外，所有部件都可以配置默认值。

### 键帮助区分部件并访问其值

部件键有三个用途：

1. 区分两个其他方面相同的部件。
2. 在更改参数的同时保持部件的状态性（v1.50.0+）。
3. 创建通过 `st.session_state` 访问和操作部件值的方法。

此外，为了开发人员的便利，键在 DOM 中作为带有 Streamlit 特定前缀的 HTML 属性重复，以防止冲突。确切的前缀和属性名称不能保证在版本之间稳定。

#### 部件身份：基于键 vs 基于参数

只要可能，Streamlit 会在前端增量更新部件，而不是在每次重新运行时重建它们。这意味着 Streamlit 根据传递给部件命令的参数为每个部件分配一个部件身份。

**以前的行为（v1.50.0 之前）：** 部件身份由所有参数确定，包括标签、选项、最小/最大值、默认值、占位符文本、帮助文本和键。

**当前行为（v1.50.0+）：** 部件身份取决于是否提供了键：

- **带键：** 只有键、最小/最大值和选项参数决定部件身份。其他参数可以更改而不会重置部件。
- **无键：** 部件的参数（标签、选项、最小/最大值、默认值、占位符、帮助文本）决定部件身份。更改这些参数之一将重置部件。请注意，回调函数、回调参数和关键字参数、标签可见性以及禁用部件不会影响部件身份。

在所有情况下，部件身份和状态不会在页面之间保留。更多信息请参见下面的[部件的状态性](#部件的状态性)。

#### Streamlit 无法理解同一页面上的两个相同部件

如果在同一页面上有两个相同类型和相同参数的部件，您将收到 `DuplicateWidgetID` 错误。在这种情况下，为两个部件分配唯一键。

以下示例将导致 `DuplicateWidgetID` 错误。

```python
st.button("确定")
st.button("确定")
```

以下示例正确为两个按钮分配唯一键以避免 `DuplicateWidgetID` 错误。

```python
st.button("确定", key="privacy")
st.button("确定", key="terms")
```

## 操作顺序

当用户与部件交互时，部件被更新并按以下顺序触发重新运行：

1. `st.session_state` 中的部件值被更新。
2. 回调函数（如果有）被执行。
3. 页面重新运行，部件命令返回其新值。

如果回调函数在屏幕上显示任何内容，该内容将出现在页面上方。回调函数作为脚本运行的_前缀_运行。因此，这意味着通过回调函数编写的任何内容都会在用户执行下一个操作时消失。一般不应在回调函数中调用部件命令。

<Note>

如果回调函数传递了任何参数或关键字参数，这些参数将在部件命令调用时建立，而不是在用户与部件交互时建立。特别是，如果您想在部件自身的回调函数中使用部件的值，不能通过 `args` 参数将该值传递给回调函数；您必须为部件分配一个键，并使用 `st.session_state` 在回调函数_内_查找其值。

</Note>

### 将回调函数与表单一起使用

将回调函数与表单一起使用需要了解此操作顺序。

```python
import streamlit as st

if "attendance" not in st.session_state:
    st.session_state.attendance = set()


def take_attendance():
    if st.session_state.name in st.session_state.attendance:
        st.info(f"{st.session_state.name} 已经被记录过了。")
    else:
        st.session_state.attendance.add(st.session_state.name)


with st.form(key="my_form"):
    st.text_input("姓名", key="name")
    st.form_submit_button("我在这里！", on_click=take_attendance)
```

<Cloud name="doc-guide-widgets-form-callbacks" height="250px"/>

## 部件的状态性

只要部件身份保持相同并且该部件持续在前端渲染，它就有状态并记住用户输入。

### 更改部件的身份将重置它

如果确定部件身份的任何参数发生变化，Streamlit 将将其视为新部件并重置。使用新的基于键的身份系统，提供键可以保护部件免受其他参数更改时的重置。在这种情况下，默认值的使用尤为重要。如果您使用键并更改部件的默认值，部件状态不会有变化。如果您不使用键，更改部件的默认值将重置部件为该默认值。

在此示例中，我们有两个滑块，您可以更改最小值、最大值和默认值。尝试与每个滑块交互以更改其值，然后更改最小值或最大值设置以查看发生了什么。当您更改最小值或最大值时，两个滑块身份都将更新，它们将重置为其当前默认值。但是，如果您更改默认值，只有没有键的滑块会重置。有键的滑块将保持有状态。

```python
import streamlit as st

cols = st.columns([2, 1, 2])
minimum = cols[0].number_input("最小值", 1, 3)
maximum = cols[2].number_input("最大值", 8, 10, 10)
value = cols[1].number_input("默认值", 4, 7, 5)

st.slider("无键", minimum, maximum, value)
st.slider("带键", minimum, maximum, value, key="a")
```

<Cloud name="doc-guide-widgets-change-parameters" height="550px"/>

### 部件在不连续渲染时不保留

如果在脚本运行期间未调用特定部件实例的部件命令，则不会保留其任何部分，包括其在 `st.session_state` 中的值。如果部件有键并且您从此部件导航离开，其在 `st.session_state` 中的键和关联值将被删除。即使是临时隐藏部件也会导致它重新出现时重置；Streamlit 将将其视为新部件。要在页面之间或部件暂时隐藏时保留部件状态，请将值保存到单独的占位键中，如下所示。

#### 在会话状态中保存部件值以在页面之间保留它们

如果您想离开部件并返回它同时保持其值，请使用 `st.session_state` 中的单独键独立于部件保存信息。也建议使用此技术将部件的状态携带到另一页上的新实例。在此示例中，使用带有部件的下划线前缀的临时键。因此，`"_my_key"` 用作部件键，但数据被复制到 `"my_key"` 以在页面之间保留它。

```python
import streamlit as st

def store_value():
    # 将值复制到永久键
    st.session_state["my_key"] = st.session_state["_my_key"]

# 将保存的值复制到临时键
st.session_state["_my_key"] = st.session_state["my_key"]
st.number_input("过滤器数量", key="_my_key", on_change=store_value)
```

如果将其函数化以处理多个部件，可能看起来像这样：

```python
import streamlit as st

def store_value(key):
    st.session_state[key] = st.session_state["_"+key]
def load_value(key):
    st.session_state["_"+key] = st.session_state[key]

load_value("my_key")
st.number_input("过滤器数量", key="_my_key", on_change=store_value, args=["my_key"])
```

## 部件生命周期

当调用部件命令时，Streamlit 将检查是否已经有一个具有相同身份的部件。如果 Streamlit 认为部件已存在，它将重新连接。否则，它将创建一个新部件。

如前所述，Streamlit 根据部件是否有键以不同方式确定部件身份。页面名称也会影响部件身份，其中部件身份在页面之间不保留。另一方面，回调函数、回调参数和关键字参数、标签可见性以及禁用部件从不影响部件身份。

### 当部件尚不存在时调用部件命令

如果您的脚本重新运行调用具有更改身份的部件命令，或调用在上次脚本运行中未使用的部件命令：

1. Streamlit 将构建部件的前端和后端部分，使用其默认值。
2. 如果部件已分配键，Streamlit 将检查该键是否已存在于会话状态中。
   a. 如果键存在且**不**与具有不同身份的部件关联，Streamlit 将将该键的值分配给部件。
   b. 如果键存在且与具有不同身份的部件关联，Streamlit 将用默认值覆盖键值对。
   b. 如果键不存在，Streamlit 将使用默认值创建新的键值对。
3. 如果有回调函数的参数或关键字参数，它们将在内存中评估和保存。
4. 然后函数返回部件值。

对于第2步，v1.46.0 之前，如果值来自另一页面的部件实例，Streamlit 将忽略会话状态中的值。这是因为另一页面上的部件必然具有不同的身份。从 v1.46.0 开始，Streamlit 在新页面脚本运行开始时删除此类值。

### 当部件已存在时调用部件命令

在不更改部件身份的情况下重新运行脚本时：

1. Streamlit 将连接到现有的前端和后端部分。
2. 如果部件有从 `st.session_state` 中删除的键，则 Streamlit 将使用当前前端值重新创建键。这是因为从会话状态中删除键不会将部件恢复为默认值。
3. 部件命令将返回部件的当前值。

### 部件清理过程

Streamlit 在每次脚本运行结束时以及在新页面上脚本运行开始时清理部件数据。

当 Streamlit 到达脚本运行结束时，它将删除内存中所有未在屏幕上渲染的部件的数据。最重要的是，这意味着 Streamlit 将删除与当前不在屏幕上显示的部件相关的 `st.session_state` 中的所有键值对。当您切换页面时，Streamlit 将删除与前一页部件相关的所有数据。

### 更改部件身份时保持状态性

如果您只需要操作影响身份的参数而不在页面之间携带部件状态，可以使用回调直接维护部件状态。这是我们之前更改滑块最小值和最大值示例的解决方案。请注意，部件的初始值是通过会话状态而不是其 `value` 参数设置的。当您以编程方式更改部件时，应该只使用会话状态来维护部件状态以避免意外行为。

```python
import streamlit as st

# 设置部件的默认值
st.session_state.setdefault("a", 5)

cols = st.columns(2)
minimum = cols[0].number_input("最小值", 1, 5, key="min")
maximum = cols[1].number_input("最大值", 6, 10, 10, key="max")


def update_value():
    # 辅助函数，确保部件参数和值之间的一致性
    st.session_state.a = min(st.session_state.a, maximum)
    st.session_state.a = max(st.session_state.a, minimum)


# 渲染前验证滑块值
update_value()
st.slider("A", minimum, maximum, key="a")
```

<Cloud name="doc-guide-widgets-change-parameters-solution" height="250px"/>

`update_value()` 辅助函数确保部件参数和值之间的一致性。此外，通过写入 `st.session_state.a`，我们确保键值对可用于"新"部件。如果此脚本不写入 `st.session_state.a`，Streamlit 将解释键值对与不同部件关联并覆盖键值对。

## 最佳实践和建议

### 对于多页面应用

**主要建议：** 在入口点文件中使用通用部件和 [`st.navigation`](/develop/api-reference/navigation/st.navigation) 来完全绕过页面身份问题：

```python
# streamlit_app.py (入口点)
import streamlit as st

# 在所有页面上持续存在的通用部件
user_name = st.sidebar.text_input("姓名", key="global_name")
user_role = st.sidebar.selectbox("角色", ["用户", "管理员"], key="global_role")

# 导航
page = st.navigation([
    st.Page("page1.py", title="仪表板"),
    st.Page("page2.py", title="设置"),
])
page.run()
```

**次要建议：** 对于必须在各个页面上的部件，请使用占位键模式。更多信息请参见[在会话状态中保存部件值以在页面之间保留它们](#在会话状态中保存部件值以在页面之间保留它们)。

### 对于参数更改

- 当您需要部件在参数更改时保持状态时使用键。
- 如果您需要更改影响部件身份的参数，请使用占位键，就像对多页面应用一样，
  或使用回调直接维护部件状态。更多信息请参见[更改部件身份时保持状态性](#更改部件身份时保持状态性)。
- 要强制部件重置，请更新其键，或在不使用键的情况下更新参数。