---
title: 什么是可序列化的会话状态？
slug: /knowledge-base/using-streamlit/serializable-session-state
---

# 什么是可序列化的会话状态？

## 可序列化会话状态

序列化是指将对象或数据结构转换为可以保存和共享的格式，并允许您恢复数据的原始结构的过程。Python的内置[pickle](https://docs.python.org/3/library/pickle.html)模块将Python对象序列化为字节流("pickling")并反序列化流为对象("unpickling")。

默认情况下，Streamlit的[会话状态](/develop/concepts/architecture/session-state)允许您在会话期间保留任何Python对象，无论对象是否可pickle序列化。此属性让您可以存储Python基础类型，如整数、浮点数、复数和布尔值、数据框，甚至函数返回的[lambdas](https://docs.python.org/3/reference/expressions.html#lambda)。但是，某些执行环境可能需要序列化会话状态中的所有数据，因此在开发过程中检测不兼容性可能会很有用，或者在执行环境将来停止支持它时。

为此，Streamlit提供了`runner.enforceSerializableSessionState`[配置选项](/develop/concepts/configuration)，设置为`true`时，仅允许会话状态中的pickle可序列化对象。要启用该选项，请创建具有以下内容的全局或项目配置文件，或将其用作命令行标志：

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

通过"_pickle可序列化_"，我们的意思是调用`pickle.dumps(obj)`不应抛出[`PicklingError`](https://docs.python.org/3/library/pickle.html#pickle.PicklingError)异常。启用配置选项后，将不可序列化的数据添加到会话状态应会导致异常。例如，

```python
import streamlit as st

def unserializable_data():
		return lambda x: x

#👇 当enforceSerializableSessionState打开时导致异常
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png" clean />
