---
title: 会话状态
slug: /develop/api-reference/caching-and-state/st.session_state
description: st.session_state 是一种在每次用户会话的重运行之间共享变量的方式。
keywords: session state, state management, variables, reruns, user session, persistence, callbacks, widgets, multipage
---

# 会话状态

会话状态是一种在每次用户会话的重运行之间共享变量的方式。除了存储和持久化状态的能力外，Streamlit 还公开了使用回调操作状态的能力。会话状态还跨[多页应用](/develop/concepts/multipage-apps)中的应用持久化。

观看 Streamlit 开发者倡导者 Marisa Smith 博士的这个会话状态基础教程视频开始：

<YouTube videoId="92jUAXBmZyU" />

### 在会话状态中初始化值

会话状态 API 遵循基于字段的 API，与 Python 字典非常相似：

```python
# 初始化
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# 会话状态还支持基于属性的语法
if 'key' not in st.session_state:
    st.session_state.key = 'value'
```

### 读取和更新

通过传递给 `st.write` 来读取会话状态中项目的价值并显示它：

```python
# 读取
st.write(st.session_state.key)

# 输出：value
```

通过为其分配值来更新会话状态中的项目：

```python
st.session_state.key = 'value2'     # 属性 API
st.session_state['key'] = 'value2'  # 字典式 API
```

好奇会话状态中有什么？使用 `st.write` 或魔法：

```python
st.write(st.session_state)

# 使用魔法：
st.session_state
```

如果访问未初始化的变量，Streamlit 会抛出一个方便的异常：

```python
st.write(st.session_state['value'])

# 抛出异常！
```

![state-uninitialized-exception](/images/state_uninitialized_exception.png)

### 删除项目

使用删除任何 Python 字典中项目的语法删除会话状态中的项目：

```python
# 删除单个键值对
del st.session_state[key]

# 删除会话状态中的所有项目
for key in st.session_state.keys():
    del st.session_state[key]
```

还可以通过转到设置 → 清除缓存，然后重新运行应用来清除会话状态。

![state-clear-cache](/images/clear_cache.png)

### 会话状态和窗口小部件状态关联

每个带有键的窗口小部件都会自动添加到会话状态：

```python
st.text_input("Your name", key="name")

# 这现在存在：
st.session_state.name
```

### 使用回调更新会话状态

回调是一个 Python 函数，当输入窗口小部件更改时被调用。

**执行顺序**：在响应**事件**更新会话状态时，回调函数首先被执行，然后应用从上到下执行。

回调可以使用参数 `on_change`（或 `on_click`）、`args` 和 `kwargs` 与窗口小部件一起使用：

**参数**

- **on_change** 或 **on_click** - 用作回调的函数名称
- **args** (_tuple_) - 要传递给回调函数的参数列表
- **kwargs** (_dict_) - 要传递给回调函数的命名参数

支持 `on_change` 事件的窗口小部件：

- `st.checkbox`
- `st.color_picker`
- `st.date_input`
- `st.data_editor`
- `st.file_uploader`
- `st.multiselect`
- `st.number_input`
- `st.radio`
- `st.select_slider`
- `st.selectbox`
- `st.slider`
- `st.text_area`
- `st.text_input`
- `st.time_input`
- `st.toggle`

支持 `on_click` 事件的窗口小部件：

- `st.button`
- `st.download_button`
- `st.form_submit_button`

要添加回调，在窗口小部件声明**上方**定义回调函数，并通过 `on_change`（或 `on_click`）参数将其传递给窗口小部件。

### 表单和回调

表单内的窗口小部件可以通过会话状态 API 访问和设置其值。`st.form_submit_button` 可以有与之关联的回调。回调在单击提交按钮时执行。例如：

```python
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
```

### 可序列化的会话状态

序列化是指将对象或数据结构转换为可以持久化和共享的格式，并允许您恢复数据的原始结构的过程。Python 的内置 [pickle](https://docs.python.org/3/develop/pickle.html) 模块将 Python 对象序列化为字节流（"pickling"）并将流反序列化为对象（"unpickling"）。

默认情况下，Streamlit 的[会话状态](/develop/concepts/architecture/session-state)允许您在会话期间持久化任何 Python 对象，无论对象的 pickle 可序列化性如何。此属性让您可以存储 Python 原始类型，如整数、浮点数、复数和布尔值、数据框，甚至函数返回的 [lambdas](https://docs.python.org/3/reference/expressions.html#lambda)。但是，一些执行环境可能需要序列化会话状态中的所有数据，因此在开发期间检测不兼容性可能很有用，或者当执行环境将来停止支持它时。

为此，Streamlit 提供了一个 `runner.enforceSerializableSessionState` [配置选项](/develop/concepts/configuration)，当设置为 `true` 时，只允许会话状态中的 pickle 可序列化对象。要启用该选项，请创建具有以下内容的全局或项目配置文件，或将其用作命令行标志：

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

通过 "_pickle 可序列化_"，我们意味着调用 `pickle.dumps(obj)` 不应引发 [`PicklingError`](https://docs.python.org/3/develop/pickle.html#pickle.PicklingError) 异常。当配置选项启用时，向会话状态添加不可序列化数据应导致异常。例如，

```python
import streamlit as st

def unserializable_data():
		return lambda x: x

#👇 当 enforceSerializableSessionState 开启时导致异常
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png" clean />

<Warning>

当 `runner.enforceSerializableSessionState` 设置为 `true` 时，会话状态隐式使用 `pickle` 模块，这已知是不安全的。确保从会话状态保存和检索的所有数据都是可信的，因为可以构造恶意 pickle 数据，在 unpickling 期间执行任意代码。永远不要以不安全模式加载可能来自不可信来源的数据或可能已被篡改的数据。**仅加载您信任的数据**。

</Warning>

### 注意事项和限制

- Streamlit 会话状态绑定到 WebSocket 连接。当用户重新加载浏览器选项卡或使用 Markdown 链接导航时，WebSocket 连接和关联的会话状态数据会被重置。
- 只有 `st.form_submit_button` 在表单中有回调。表单内的其他窗口小部件不允许有回调。
- `on_change` 和 `on_click` 事件仅在输入类型窗口小部件上受支持。
- 在实例化窗口小部件后，通过会话状态 API 修改其值是不允许的，并会引发 `StreamlitAPIException`。例如：

  ```python
  slider = st.slider(
      label='My Slider', min_value=1,
      max_value=10, value=5, key='my_slider')

  st.session_state.my_slider = 7

  # 抛出异常！
  ```

  ![state-modified-instantiated-exception](/images/state_modified_instantiated_exception.png)

- 通过会话状态 API 设置窗口小部件状态并在窗口小部件声明中使用 `value` 参数是不推荐的，并在第一次运行时抛出警告。例如：

  ```python
  st.session_state.my_slider = 7

  slider = st.slider(
      label='Choose a Value', min_value=1,
      max_value=10, value=5, key='my_slider')
  ```

  ![state-value-api-exception](/images/state_value_api_exception.png)

- 通过会话状态 API 设置按钮式窗口小部件的状态：`st.button`、`st.download_button` 和 `st.file_uploader` 是不允许的。此类窗口小部件默认情况下为 _False_，并且具有仅对单个运行有效的短暂 _True_ 状态。例如：

  ```python
  if 'my_button' not in st.session_state:
      st.session_state.my_button = True

  st.button('My button', key='my_button')

  # 抛出异常！
  ```

  ![state-button-exception](/images/state_button_exception.png)
