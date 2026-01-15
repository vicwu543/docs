---
title: 静态文件服务
slug: /develop/concepts/configuration/serving-static-files
description: 了解 Streamlit 中的静态文件服务，以托管和提供支持媒体嵌入和自定义内容用例的媒体文件、资产和资源。
keywords: 静态文件, 文件服务, 媒体托管, 资产服务, 静态资产, 文件托管, 媒体文件, 资源服务, 静态内容
---

# 静态文件服务

Streamlit 应用可以托管和提供小型静态媒体文件，以支持无法使用普通[媒体元素](/develop/api-reference/media)的媒体嵌入用例。

要启用此功能，请在配置文件中的 `[server]` 下设置 `enableStaticServing = true`，或环境变量 `STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true`。

存储在相对于运行应用文件的文件夹 `./static/` 中的媒体在路径 `app/static/[filename]` 下提供服务，例如 `http://localhost:8501/app/static/cat.png`。

## 使用详情

- 具有以下扩展名的文件将被正常提供服务：
  - 常见图像类型：`.jpg`, `.jpeg`, `.png`, `.gif`
  - 常见字体类型：`.otf`, `.ttf`, `.woff`, `.woff2`
  - 其他类型：`.pdf`, `.xml`, `.json`
    任何其他文件将以头 `Content-Type:text/plain` 发送，这将导致浏览器以纯文本渲染。
    这是出于安全考虑 - 需要渲染的其他文件类型应该在应用外部托管。
- Streamlit 还为从静态目录渲染的所有文件设置 `X-Content-Type-Options:nosniff`。
- 对于在 Streamlit Community Cloud 上运行的应用：
  - Github 仓库中可用的文件将始终被提供服务。任何在应用运行时生成的基于用户交互的文件（文件上传等）不保证在用户会话之间持久存在。
  - 存储和提供许多文件或大文件的应用可能会遇到资源限制并被关闭。

## 示例用法

- 将图像 `cat.png` 放入文件夹 `./static/`
- 在您的 `.streamlit/config.toml` 中的 `[server]` 下添加 `enableStaticServing = true`
- `./static/` 文件夹中的任何媒体都以相对 URL 提供服务，如 `app/static/cat.png`

```toml
# .streamlit/config.toml

[server]
enableStaticServing = true
```

```python
# app.py
import streamlit as st

with st.echo():
    st.title("CAT")

    st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")

```

附加资源：

- [https://docs.streamlit.io/develop/concepts/configuration](https://docs.streamlit.io/develop/concepts/configuration)
- [https://static-file-serving.streamlit.app/](https://static-file-serving.streamlit.app/)

<Cloud name="static-file-serving" height="1000px" />
