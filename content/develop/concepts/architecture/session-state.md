---
title: 为应用添加状态性
slug: /develop/concepts/architecture/session-state
description: 了解会话状态，用于在重新运行之间共享变量，实现回调，并在用户会话间构建有状态的应用程序。
keywords: session state, statefulness, st.session_state, callbacks, state management, stateful apps, variable persistence, user sessions, state sharing, app state
---

# 为应用添加状态性

## 什么是状态？

我们将浏览器标签页中对 Streamlit 应用的访问定义为一个**会话**。对于每个连接到 Streamlit 服务器的浏览器标签页，都会创建一个新会话。每当您与应用交互时，Streamlit 会从头到尾重新运行您的脚本。每次重新运行都在一个空白的状态下进行：运行之间不共享变量。

会话状态是一种在每次重新运行之间共享变量的方法，针对每个用户会话。除了存储和持久化状态的能力外，Streamlit 还提供了使用回调操作状态的能力。会话状态还会在[多页面应用](/develop/concepts/multipage-apps)的页面之间保持持久。

在本指南中，我们将通过构建一个有状态的计数器应用来演示**会话状态**和**回调**的使用。

有关会话状态和回调 API 的详细信息，请参阅我们的[会话状态 API 参考指南](/develop/api-reference/caching-and-state/st.session_state)。

此外，还请观看 Streamlit 开发者倡导者 Marisa Smith 博士制作的会话状态基础教程视频以开始学习：

<YouTube videoId="92jUAXBmZyU" />

## 构建计数器

让我们将我们的脚本命名为 `counter.py`。它初始化一个 `count` 变量，并有一个按钮来增加 `count` 变量中存储的值：

```python
import streamlit as st

st.title('计数器示例')
count = 0

increment = st.button('增加')
if increment:
    count += 1

st.write('计数 = ', count)
```

无论我们在上面的应用中多少次按下**_增加_**按钮，`count` 都保持在 1。让我们了解一下原因：

- 每次我们按下**_增加_**按钮时，Streamlit 都会从头到尾重新运行 `counter.py`，而且每次运行时，`count` 都会被初始化为 `0`。
- 随后按下**_增加_**会将 1 加到 0 上，因此无论我们多少次按下**_增加_**，`count=1`。

正如我们稍后将看到的，我们可以通过将会话状态存储为会话状态变量来避免这个问题。通过这样做，我们向 Streamlit 表明应该在应用重新运行时维护会话状态变量中存储的值。

让我们进一步了解使用会话状态的 API。

### 初始化

会话状态 API 遵循基于字段的 API，这与 Python 字典非常相似：

```python
import streamlit as st

# 检查 'key' 是否已存在于 session_state 中
# 如果没有，则初始化它
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# 会话状态也支持基于属性的语法
if 'key' not in st.session_state:
    st.session_state.key = 'value'
```

### 读取和更新

通过将项目传递给 `st.write` 来读取会话状态中的项目值：

```python
import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# 读取
st.write(st.session_state.key)

# 输出: value
```

通过为其分配一个值来更新会话状态中的项目：

```python
import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# 更新
st.session_state.key = 'value2'     # 属性 API
st.session_state['key'] = 'value2'  # 类似字典的 API
```

如果访问未初始化的变量，Streamlit 会抛出异常：

```python
import streamlit as st

st.write(st.session_state['value'])

# 抛出异常！
```

![state-uninitialized-exception](/images/state_uninitialized_exception.png)

现在让我们来看看一些示例，说明如何将会话状态添加到我们的计数器应用中。

### 示例 1: 添加会话状态

现在我们已经掌握了会话状态 API，让我们更新我们的计数器应用以使用会话状态：

```python
import streamlit as st

st.title('计数器示例')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('增加')
if increment:
    st.session_state.count += 1

st.write('计数 = ', st.session_state.count)
```

如您在上面的示例中所见，按下**_增加_**按钮每次都会更新 `count`。

### 示例 2: 会话状态和回调

现在我们已经使用会话状态构建了一个基本的计数器应用，让我们转向稍微复杂一点的内容。下一个示例将使用回调与会话状态。

**回调**: 回调是一个 Python 函数，当输入小部件发生变化时会调用该函数。回调可以与小部件一起使用，使用参数 `on_change`（或 `on_click`）、`args` 和 `kwargs`。完整的回调 API 可在我们的[会话状态 API 参考指南](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state)中找到。

```python
import streamlit as st

st.title('使用回调的计数器示例')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('增加', on_click=increment_counter)

st.write('计数 = ', st.session_state.count)
```

现在，按下**_增加_**按钮通过调用 `increment_counter()` 函数每次更新计数。

### 示例 3: 在回调中使用 args 和 kwargs

回调还支持使用小部件中的 `args` 参数传递参数：

```python
import streamlit as st

st.title('使用带 args 回调的计数器示例')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('输入一个值', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

increment = st.button('增加', on_click=increment_counter,
    args=(increment_value, ))

st.write('计数 = ', st.session_state.count)
```

此外，我们还可以在小部件中使用 `kwargs` 参数将命名参数传递给回调函数，如下所示：

```python
import streamlit as st

st.title('使用带 kwargs 回调的计数器示例')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value

st.button('增加', on_click=increment_counter,
	kwargs=dict(increment_value=5))

st.button('减少', on_click=decrement_counter,
	kwargs=dict(decrement_value=1))

st.write('计数 = ', st.session_state.count)
```

### 示例 4: 表单和回调

假设我们现在不仅要增加 `count`，还要存储上次更新的时间。我们使用回调和 `st.form` 来演示如何实现：

```python
import streamlit as st
import datetime

st.title('计数器示例')
if 'count' not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key='my_form'):
    st.time_input(label='输入时间', value=datetime.datetime.now().time(), key='update_time')
    st.number_input('输入一个值', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label='更新', on_click=update_counter)

st.write('当前计数 = ', st.session_state.count)
st.write('上次更新 = ', st.session_state.last_updated)
```

## 高级概念

### 会话状态和小部件状态关联

会话状态提供了在重新运行之间存储变量的功能。小部件状态（即小部件的值）也存储在会话中。

为了简化，我们已在一处_统一_了这些信息。即会话状态。此便捷功能使您可以在应用代码中的任何地方轻松读取或写入小部件的状态。会话状态变量使用 `key` 参数镜像小部件的值。

我们用以下示例来说明这一点。假设我们有一个带有滑块的应用，表示摄氏温度。我们可以通过使用会话状态 API 来**设置**和**获取**温度小部件的值，如下所示：

```python
import streamlit as st

if "celsius" not in st.session_state:
    # 设置滑块小部件的初始默认值
    st.session_state.celsius = 50.0

st.slider(
    "摄氏温度",
    min_value=-100.0,
    max_value=100.0,
    key="celsius"
)

# 这将获取滑块小部件的值
st.write(st.session_state.celsius)
```

使用会话状态 API 设置小部件值存在局限性。

<Important>

Streamlit **不允许**通过会话状态 API 为 `st.button` 和 `st.file_uploader` 设置小部件值。

</Important>

以下示例在尝试通过会话状态 API 设置 `st.button` 的状态时将引发 `StreamlitAPIException`：

```python
import streamlit as st

if 'my_button' not in st.session_state:
    st.session_state.my_button = True
    # Streamlit 在尝试设置按钮状态时会引发异常

st.button('提交', key='my_button')
```

<Image alt="state-button-exception" src="/images/state_button_exception.png" clean />

### 可序列化的会话状态

序列化是指将对象或数据结构转换为可以持久化和共享的格式的过程，让您能够恢复数据的原始结构。Python 的内置 [pickle](https://docs.python.org/3/library/pickle.html) 模块将 Python 对象序列化为字节流（"pickle化"）并将流反序列化为对象（"unpickle化"）。

默认情况下，Streamlit 的[会话状态](/develop/concepts/architecture/session-state)允许您在会话期间持久化任何 Python 对象，不管对象的 pickle 可序列化性如何。此属性允许您存储 Python 基本类型，如整数、浮点数、复数和布尔值、数据框，甚至函数返回的[lambdas](https://docs.python.org/3/reference/expressions.html#lambda)。但是，某些执行环境可能需要序列化会话状态中的所有数据，因此在开发期间检测不兼容性，或在执行环境将来停止支持时可能很有用。

为此，Streamlit 提供了一个 `runner.enforceSerializableSessionState` [配置选项](/develop/concepts/configuration)，当设置为 `true` 时，只允许在会话状态中使用可 pickle 序列化的对象。要启用此选项，可以创建一个全局或项目配置文件，其中包含以下内容，或将其用作命令行标志：

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

通过"_pickle-serializable_"，我们的意思是调用 `pickle.dumps(obj)` 不应引发 [`PicklingError`](https://docs.python.org/3/library/pickle.html#pickle.PicklingError) 异常。当启用配置选项时，向会话状态添加不可序列化的数据会导致异常。例如，

```python
import streamlit as st

def unserializable_data():
	return lambda x: x

#👇 当 enforceSerializableSessionState 开启时会导致异常
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png" clean />

<Warning>

当 `runner.enforceSerializableSessionState` 设置为 `true` 时，会话状态隐式使用 `pickle` 模块，这被认为是不安全的。确保保存和从会话状态检索的所有数据都是可信的，因为可以构造恶意的 pickle 数据，在 unpickling 期间执行任意代码。切勿在不安全模式下加载可能来自不受信任来源或可能已被篡改的数据。**仅加载您信任的数据**。

</Warning>

### 注意事项和限制

使用会话状态时需要记住一些限制：

- 会话状态在标签页打开并连接到 Streamlit 服务器期间存在。一旦您关闭标签页，存储在会话状态中的所有内容都将丢失。
- 会话状态不会持久化。如果 Streamlit 服务器崩溃，则存储在会话状态中的所有内容都会被清除
- 有关会话状态 API 的注意事项和限制，请参阅[API 限制](/develop/api-reference/caching-and-state/st.session_state#caveats-and-limitations)。