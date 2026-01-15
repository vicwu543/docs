---
title: 使用 fragments
slug: /develop/concepts/architecture/fragments
description: 了解如何使用 Streamlit fragments 通过重新运行代码的一部分而不是整个脚本来优化应用性能，提高复杂应用的效率。
keywords: streamlit fragments, st.fragment, 部分重新运行, 性能优化, 执行控制, fragment 重新运行, 高效重新运行, 应用性能, 执行流
---

# 使用 fragments

重新运行是每个 Streamlit 应用的核心部分。当用户与小部件交互时，你的脚本从头到尾重新运行，你的应用的前端被更新。Streamlit 提供了几个功能来帮助你在这个执行模型中开发你的应用。Streamlit 版本 1.37.0 引入了 fragments 以允许重新运行代码的一部分而不是整个脚本。随着应用变得更大更复杂，这些 fragment 重新运行帮助你的应用高效和高性能。Fragments 给予你对应用执行流的更细致、易于理解的控制。

在阅读关于 fragments 的内容之前，我们建议对[缓存](/develop/concepts/architecture/caching)、[Session State](/concepts/architecture/session-state) 和[表单](/develop/concepts/architecture/forms)有基本的理解。

## Fragments 的用例

Fragments 是多用途的，适用于各种各样的情况。以下是一些常见的 fragments 有用的场景：

- 你的应用有多个可视化，每个都需要时间加载，但你有一个只更新其中一个的过滤输入。
- 你有一个动态表单，不需要更新应用的其余部分（直到表单完成）。
- 你想自动更新单个组件或一组组件来流式传输数据。

## 定义和调用 fragment

Streamlit 提供了一个装饰器（[`st.fragment`](/develop/api-reference/execution-flow/st.fragment)）来将任何函数转换为 fragment 函数。当你调用包含小部件函数的 fragment 函数时，用户会触发一个 _fragment 重新运行_ 而不是完整重新运行来与该 fragment 的小部件交互。在 fragment 重新运行期间，仅你的 fragment 函数被重新执行。fragment 主体内的任何内容都在前端更新，而你的应用的其余部分保持不变。我们稍后将描述跨多个容器编写的 fragments。

这是定义和调用 fragment 函数的基本示例。就像缓存一样，记住在定义函数后调用它。

```python
import streamlit as st

@st.fragment
def fragment_function():
    if st.button("Hi!"):
        st.write("Hi back!")

fragment_function()
```

如果你想让 fragment 的主体显示在侧边栏或另一个容器中，请在上下文管理器中调用你的 fragment 函数。

```python
with st.sidebar:
    fragment_function()
```

### Fragment 执行流

考虑以下代码及其下面的说明和图表。

```python
import streamlit as st

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")

@st.fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()
```

当用户与 fragment 内的输入小部件交互时，只有 fragment 重新运行，而不是完整脚本。当用户与 fragment 外的输入小部件交互时，完整脚本如常重新运行。

如果你运行上述代码，完整脚本将在你的应用初始加载时从头到尾运行。如果你翻转运行中的应用中的切换按钮，第一个 fragment（`toggle_and_text()`）将重新运行，重新绘制切换和文本区域，同时保持其他一切不变。如果你点击复选框，第二个 fragment（`filter_and_file()`）将重新运行并相应地重新绘制复选框和文件上传器。其他一切保持不变。最后，如果你点击更新按钮，完整脚本将重新运行，Streamlit 将重新绘制所有内容。

![Fragment 执行流图表](/images/concepts/fragment_diagram.png)

## Fragment 返回值和与应用的其余部分交互

Streamlit 在 fragment 重新运行期间忽略 fragment 返回值，因此不建议为 fragment 函数定义返回值。相反，如果你的 fragment 需要与应用的其余部分共享数据，请使用 Session State。Fragments 只是你脚本中的函数，所以它们可以访问 Session State、导入的模块和其他 Streamlit 元素，如容器。如果你的 fragment 写入任何在其外创建的容器，请注意以下行为差异：

- 在你的 fragment 主体中绘制的元素在 fragment 重新运行期间被清除并在原位重新绘制。重复的 fragment 重新运行不会导致额外的元素出现。
- 绘制到 fragment 主体外的容器的元素不会在每个 fragment 重新运行时被清除。相反，Streamlit 将以累加方式绘制它们，这些元素将累积直到下一个完整脚本重新运行。
- Fragment 不能在 fragment 主体外的容器中绘制小部件。小部件只能在 fragment 的主体中。

要防止元素在外部容器中累积，请使用 [`st.empty`](/develop/api-reference/layout/st.empty) 容器。有关相关教程，请参见[跨多个容器创建 fragment](/develop/tutorials/execution-flow/create-a-multiple-container-fragment)。

如果你需要从 fragment 内部触发完整脚本重新运行，请调用 [`st.rerun`](/develop/api-reference/execution-flow/st.rerun)。有关相关教程，请参见[从 fragment 内部触发完整脚本重新运行](/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment)。

## 自动 fragment 重新运行

`st.fragment` 包括一个方便的 `run_every` 参数，使 fragment 在指定的时间间隔自动重新运行。这些重新运行是除了任何由你的用户触发的重新运行（fragment 或完整脚本）之外。自动 fragment 重新运行将继续进行，即使你的用户没有与你的应用交互。这是显示现场数据流或运行后台作业状态的好方法，高效地更新你的渲染数据和 _仅_ 你的渲染数据。

```python
@st.fragment(run_every="10s")
def auto_function():
		# This will update every 10 seconds!
		df = get_latest_updates()
		st.line_chart(df)

auto_function()
```

有关相关教程，请参见[启动和停止流式 fragment](/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns)。

## 将 fragments 与其他 Streamlit 功能进行比较

### Fragments vs 表单

以下是 fragments 和表单之间的比较：

- **表单** 允许用户与小部件交互而不重新运行你的应用。Streamlit 在提交表单之前不会将表单内的用户操作发送到你的应用的 Python 后端。表单内的小部件不能动态实时更新其他小部件（表单内或表单外）。
- **Fragments** 独立于代码的其余部分运行。当你的用户与 fragment 小部件交互时，他们的操作立即由你的应用的 Python 后端处理，你的 fragment 代码被重新运行。fragment 内的小部件可以动态实时更新同一 fragment 内的其他小部件。

表单批处理用户输入而小部件之间没有交互。Fragment 立即处理用户输入，但限制了重新运行的范围。

### Fragments vs 回调

以下是 fragments 和回调之间的比较：

- **回调** 允许你在脚本重新运行开始时执行一个函数。回调是你的脚本重新运行的 _单个前缀_。
- **Fragments** 允许你重新运行你的脚本的一部分。Fragment 是你的脚本的 _可重复的后缀_，每当用户与 fragment 小部件交互时，或当设置 `run_every` 时按顺序自动运行。

当回调向你的页面渲染元素时，它们在页面的其余元素之前渲染。当 fragments 向你的页面渲染元素时，它们在每个 fragment 重新运行时更新（除非它们被写入 fragment 外的容器，在这种情况下它们会在那里累积）。

### Fragments vs 自定义组件

以下是 fragments 和自定义组件之间的比较：

- **组件** 是可以与 Python 代码、本地元素和 Streamlit 应用中的小部件交互的自定义前端代码。自定义组件扩展了 Streamlit 可能实现的功能。它们遵循正常的 Streamlit 执行流。
- **Fragments** 是应用中可以独立于完整应用重新运行的部分。Fragments 可以由多个 Streamlit 元素、小部件或任何 Python 代码组成。

一个 fragment 可以包括一个或多个自定义组件。自定义组件不能轻易包括 fragment！

### Fragments vs 缓存

以下是 fragments 和缓存之间的比较：

- **缓存：** 允许你跳过一个函数并返回一个先前计算的值。当你使用缓存时，你执行除了缓存函数之外的所有内容（如果你之前已经运行过）。
- **Fragments：** 允许你冻结应用的大部分并仅执行 fragment。当你使用 fragments 时，你仅执行 fragment（当触发 fragment 重新运行时）。

缓存保存你免于不必要地运行应用的一部分，同时其余的运行。Fragments 保存你免于在你仅想运行一部分时运行整个应用。

## 限制和不支持的行为

- Fragments 无法检测输入值的变化。最好为 fragment 函数使用 Session State 进行动态输入和输出。
- 在同一函数上使用缓存和 fragments 不受支持。
- Fragments 无法在外部创建的容器中渲染小部件；小部件只能在 fragment 的主体中。
