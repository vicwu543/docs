---
title: st.query_params
slug: /develop/api-reference/caching-and-state/st.query_params
description: st.query_params 读取和操作浏览器 URL 栏中的查询参数。
keywords: query_params, query parameters, url, browser, get, set, clear, from_dict, to_dict, get_all, repeated keys
---

## st.query_params

`st.query_params` 从 Streamlit 1.30.0 开始提供字典式接口来访问应用 URL 中的查询参数。它与 `st.session_state` 的行为类似，但值得注意的是，应用的 URL 中可能重复键。重复键的处理需要特别考虑，如下所述。

`st.query_params` 可以使用键和属性表示法。例如，`st.query_params.my_key` 和 `st.query_params["my_key"]`。所有键和值都将设置为字符串并返回。当您写入 `st.query_params` 时，以 `?` 为前缀的键值对会添加到应用的 URL 末尾。每个额外的对以 `&` 而不是 `?` 为前缀。在多页应用中导航时，查询参数会被清除。

例如，考虑以下 URL：

```javascript
https://your_app.streamlit.app/?first_key=1&second_key=two&third_key=true
```

上述 URL 中的参数将在 `st.query_params` 中可访问为：

```python
{
    "first_key" : "1",
    "second_key" : "two",
    "third_key" : "true"
}
```

这意味着您可以在应用中使用这些参数，如下所示：

```python
# 您可以使用键表示法读取查询参数
if st.query_params["first_key"] == "1":
    do_something()

# ...或使用属性表示法
if st.query_params.second_key == "two":
    do_something_else()

# 您可以通过写入来更改参数
st.query_params.first_key = 2  # 这会自动转换为字符串
```

### 重复键

当应用的 URL 中重复键（`?a=1&a=2&a=3`）时，字典式方法将仅返回最后一个值。在此示例中，`st.query_params["a"]` 返回 `"3"`。要获取所有键作为列表，请使用下面显示的 [`.get_all()`](/develop/api-reference/caching-and-state/st.query_params#stquery_paramsget_all) 方法。要设置重复键的值，请将值分配为列表。例如，`st.query_params.a = ["1", "2", "3"]` 会产生本段开头给出的重复键。

### 限制

`st.query_params` 无法获取或设置[嵌入您的应用](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options)中描述的嵌入设置。`st.query_params.embed` 和 `st.query_params.embed_options` 在尝试获取或设置其值时会引发 `AttributeError` 或 `StreamlitAPIException`。

<Autofunction function="streamlit.query_params.clear" />

<Autofunction function="streamlit.query_params.from_dict" />

<Autofunction function="streamlit.query_params.get_all" />

<Autofunction function="streamlit.query_params.to_dict" />
