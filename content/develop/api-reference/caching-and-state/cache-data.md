---
title: st.cache_data
slug: /develop/api-reference/caching-and-state/st.cache_data
description: st.cache_data 用于缓存返回数据（例如数据框转换、数据库查询、ML 推理）的函数。
keywords: cache_data, caching, data, dataframe, database, ml inference, performance, optimization, memoization
---

<Tip>

此页面仅包含有关 `st.cache_data` API 的信息。有关缓存的深入探讨以及如何使用它，请查看[缓存](/develop/concepts/architecture/caching)。

</Tip>

<Autofunction function="streamlit.cache_data" oldName="streamlit.experimental_memo" />

<Warning>

`st.cache_data` 隐式使用 `pickle` 模块，这已知是不安全的。您的缓存函数返回的任何内容都会被 pickle 并存储，然后在检索时 unpickle。确保您的缓存函数返回可信值，因为可以构造恶意 pickle 数据，在 unpickling 期间执行任意代码。永远不要以不安全模式加载可能来自不可信来源的数据或可能已被篡改的数据。**仅加载您信任的数据**。

</Warning>

<Autofunction function="streamlit.cache_data.clear" oldName="streamlit.experimental_memo.clear" />

#### 示例

在下面的示例中，按下"Clear All"按钮将清除所有用 `@st.cache_data` 装饰的函数的记忆值。

```python
import streamlit as st

@st.cache_data
def square(x):
    return x**2

@st.cache_data
def cube(x):
    return x**3

if st.button("Clear All"):
    # 清除 *所有* 内存中和磁盘上的数据缓存的值：
    # 即清除 square 和 cube 的值
    st.cache_data.clear()
```

<Autofunction function="CachedFunc.clear" />

## 在缓存函数中使用 Streamlit 命令

### 静态元素

从版本 1.16.0 开始，缓存函数可以包含 Streamlit 命令！例如，您可以这样做：

```python
@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # 👈 显示成功消息
    return data
```

我们知道，Streamlit 仅在之前未缓存时运行此函数。在第一次运行时，`st.success` 消息将出现在应用中。但在后续运行中会发生什么？它仍然会出现！Streamlit 意识到缓存函数内部有 `st.` 命令，在第一次运行期间保存它，并在后续运行中重放它。重放静态元素适用于两个缓存装饰器。

您还可以使用此功能来缓存您的 UI 的整个部分：

```python
@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)
```

### 输入窗口小部件

您还可以在缓存函数中使用[交互式输入窗口小部件](/develop/api-reference/widgets)，如 `st.slider` 或 `st.text_input`。窗口小部件重放目前是一个实验性功能。要启用它，您需要设置 `experimental_allow_widgets` 参数：

```python
@st.cache_data(experimental_allow_widgets=True)  # 👈 设置参数
def get_data():
    num_rows = st.slider("Number of rows to get")  # 👈 添加滑块
    data = api.get(..., num_rows)
    return data
```

Streamlit 将滑块视为缓存函数的附加输入参数。如果您更改滑块位置，Streamlit 将查看是否已经为此滑块值缓存了函数。如果是，它将返回缓存值。如果不是，它将使用新的滑块值重新运行函数。

在缓存函数中使用窗口小部件非常强大，因为它让您可以缓存应用的整个部分。但它可能很危险！由于 Streamlit 将窗口小部件值视为附加输入参数，它很容易导致过多的内存使用。想象您的缓存函数有五个滑块并返回一个 100 MB 的 DataFrame。然后我们将为这些五个滑块值的 _每个排列_ 添加 100 MB 到缓存中 - 即使滑块不影响返回的数据！这些添加可以使您的缓存非常快速地爆炸。如果您在缓存函数中使用窗口小部件，请注意此限制。我们建议仅在 UI 的隔离部分使用此功能，其中窗口小部件直接影响缓存的返回值。

<Warning>

对缓存函数中窗口小部件的支持目前是实验性的。我们可能随时更改或删除它而不会发出警告。请谨慎使用！
</Warning>

<Note>

两个窗口小部件目前在缓存函数中不受支持：`st.file_uploader` 和 `st.camera_input`。我们将来可能会支持它们。如果您需要它们，请随时[打开 GitHub 问题](https://github.com/streamlit/streamlit/issues)！
</Note>
