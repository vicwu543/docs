---
title: 缓存和状态
slug: /develop/api-reference/caching-and-state
description: 使用 st.cache_data、st.cache_resource、会话状态和查询参数优化 Streamlit 应用的性能并管理状态，以实现高效应用。
keywords: caching, state, session state, cache_data, cache_resource, query_params, context, performance, optimization
---

# 缓存和状态

优化性能并为您的应用添加状态性！

## 缓存

Streamlit 为数据和全局资源提供强大的[缓存原语](/develop/concepts/architecture/caching)。它们允许您的应用即使在从网络加载数据、操作大型数据集或执行昂贵计算时也能保持性能。

<TileContainer>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_data" size="half">

<h4>缓存数据</h4>

函数装饰器，用于缓存返回数据（例如数据框转换、数据库查询、ML 推理）的函数。

```python
@st.cache_data
def long_function(param1, param2):
  # 在这里执行昂贵计算或
  # 从网络获取数据
  return data
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_resource" size="half">

<h4>缓存资源</h4>

函数装饰器，用于缓存返回全局资源（例如数据库连接、ML 模型）的函数。

```python
@st.cache_resource
def init_model():
  # 在这里返回全局资源
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )
```

</RefCard>

</TileContainer>

## 浏览器和服务器状态

Streamlit 在每次用户交互时重新执行您的脚本。窗口小部件在重运行之间具有内置的状态性，但会话状态让您可以做更多！

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.context">

<h4>上下文</h4>

`st.context` 提供只读接口来访问 cookies、headers、locale 和其他浏览器会话信息。

```python
st.context.cookies
st.context.headers
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.session_state">

<h4>会话状态</h4>

在重运行和页面之间保存数据。

```python
st.session_state["foo"] = "bar"
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.query_params">

<h4>查询参数</h4>

获取、设置或清除显示在浏览器 URL 栏中的查询参数。

```python
st.query_params[key] = value
st.query_params.clear()
```

</RefCard>

</TileContainer>

## 已弃用的命令

<TileContainer>

<RefCard href="/develop/api-reference/caching-and-state/st.experimental_get_query_params" size="half" deprecated={true}>

<h4>获取查询参数</h4>

获取显示在浏览器 URL 栏中的查询参数。

```python
param_dict = st.experimental_get_query_params()
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.experimental_set_query_params" size="half" deprecated={true}>

<h4>设置查询参数</h4>

设置显示在浏览器 URL 栏中的查询参数。

```python
st.experimental_set_query_params(
  {"show_all"=True, "selected"=["asia", "america"]}
)
```

</RefCard>
</TileContainer>
