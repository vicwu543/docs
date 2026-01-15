---
title: 用户身份验证和信息
slug: /develop/concepts/connections/authentication
description: 了解如何使用管理员控制、用户信息和跨会话的个性化体验在 Streamlit 应用中实现用户身份验证和个性化。
keywords: user authentication, personalization, admin controls, user information, session management, user identity, authentication systems, personalized apps
---

# 用户身份验证和信息

为您的用户个性化您的应用是让您的应用更具吸引力的好方法。

用户身份验证和个性化为开发人员解锁了大量的用例，包括管理员控制、个性化的股票行情、或具有保存历史记录的会话间聊天机器人应用。

在阅读本指南之前，您应该对[secrets 管理](/develop/concepts/connections/secrets-management)有基本了解。

## OpenID Connect

Streamlit 支持使用 OpenID Connect (OIDC) 进行用户身份验证，这是一种构建在 OAuth 2.0 之上的身份验证协议。OIDC 支持身份验证，但不支持授权：即，OIDC 连接告诉您用户是_谁_（身份验证），但不会给您_模拟_他们的权限（授权）。如果您需要连接通用 OAuth 2.0 提供商或让您的应用代表用户执行操作，请考虑使用或创建自定义组件。

一些流行的 OIDC 提供商包括：

- [Google Identity](https://developers.google.com/identity/openid-connect/openid-connect)
- [Microsoft Entra ID](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-settings)
- [Okta](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm)
- [Auth0](https://auth0.com/docs/get-started/auth0-overview/create-applications/regular-web-apps)

## `st.login()`、`st.user` 和 `st.logout()`

用户身份验证涉及三个命令：

- [`st.login()`](/develop/api-reference/user/st.login) 将用户重定向到您的身份提供商。他们在登录后，Streamlit 会存储一个身份 Cookie，然后将他们重定向到您的应用的新会话主页。
- [`st.user`](/develop/api-reference/user/st.user) 是一个类字典对象，用于访问用户信息。它有一个持久属性 `.is_logged_in`，您可以用来检查用户的登录状态。当他们登录时，其他属性将根据您的身份提供商配置可用。
- [`st.logout()`](/develop/api-reference/user/st.logout) 从用户的浏览器中删除身份 Cookie，并将他们重定向到您的应用的新会话主页。

## 用户 Cookie 和登出

Streamlit 在每个新会话开始时检查身份 Cookie。如果用户在一个标签页中登录您的应用，然后打开新标签页，他们将自动在新标签页中登录您的应用。当您在用户会话中调用 `st.logout()` 时，Streamlit 会删除身份 Cookie 并启动新会话。这会使用户从当前会话登出。但是，如果他们已经在其他会话中登录，他们将在那些会话中保持登录状态。`st.user` 中的信息在会话开始时更新（这就是为什么 `st.login()` 和 `st.logout()` 都在保存或删除身份 Cookie 后启动新会话的原因）。

如果用户在不登出的情况下关闭您的应用，身份 Cookie 将在 30 天后过期。此过期时间不可配置，且与用户身份令牌中可能返回的任何过期时间无关。如果您需要防止在您的应用中持久身份验证，请检查 `st.user` 中身份提供商返回的过期信息，并在需要时手动调用 `st.logout()`。

Streamlit 不会修改或删除直接由您的身份提供商保存的任何 Cookie。例如，如果您使用 Google 作为身份提供商，用户使用 Google 登录您的应用，他们在使用 `st.logout()` 从您的应用登出后，仍将保持登录到他们的 Google 账户。

## 设置身份提供商

为了使用身份提供商，您必须首先通过管理员账户配置您的身份提供商。这通常涉及在身份提供商系统中设置客户端或应用程序。请遵循您身份提供商的文档。总的来说，身份提供商客户端通常执行以下操作：

- 管理您的用户列表。
- 可选：允许用户将自己添加到您的用户列表。
- 声明从每个用户账户传递到客户端的属性集（然后传递到您的 Streamlit 应用）。
- 仅允许来自您的 Streamlit 应用的身份验证请求。
- 在用户认证后将用户重定向回您的 Streamlit 应用。

要配置您的应用，您需要以下内容：

- 您的应用的 URL
  例如，对于大多数本地开发情况，使用 `http://localhost:8501`。
- 重定向 URL，这是您的应用 URL 带有路径名 `oauth2callback`
  例如，对于大多数本地开发情况，使用 `http://localhost:8501/oauth2callback`。
- Cookie 密钥，这应该是一个强随机生成的字符串

在使用此信息配置您的身份提供商客户端后，您将从身份提供商收到以下信息：

- 客户端 ID
- 客户端密钥
- 服务器元数据 URL

流行的 OIDC 提供商配置示例在 `st.login()` 的 API 参考中列出。

## 在 Streamlit 中配置您的 OIDC 连接

在配置好身份提供商客户端后，您也需要配置您的 Streamlit 应用。`st.login()` 使用您的应用的 `secrets.toml` 文件配置您的连接，类似于 `st.connection()` 的工作方式。

无论您有一个 OIDC 提供商还是多个，您都需要在 `secrets.toml` 中有一个 `[auth]` 字典。您必须在 `[auth]` 字典中声明 `redirect_uri` 和 `cookie_secret`。这两个值在您的应用中的所有 OIDC 提供商之间共享。

如果您只使用一个 OIDC 提供商，可以将剩余三个属性（`client_id`、`client_secret` 和 `server_metadata_url`）放在 `[auth]` 中。但是，如果您使用多个提供商，它们应该各自具有唯一名称，以便您可以将它们的唯一值声明在各自的字典中。例如，如果您将连接命名为 `"connection_1"` 和 `"connection_2"`，请将它们的剩余属性分别放在名为 `[auth.connection_1]` 和 `[auth.connection_2]` 的字典中。

## 简单示例

如果您使用 Google Identity 作为身份提供商，本地开发的基本配置将如下 TOML 文件所示：

`.streamlit/secrets.toml`:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

确保 `redirect_uri` 中的端口与您使用的端口匹配。`cookie_secret` 应该是一个强随机生成的密钥。`redirect_uri` 和 `cookie_secret` 都应该已输入到 Google Cloud 上的客户端配置中。您必须在创建客户端后从 Google Cloud 复制 `client_id` 和 `client_secret`。对于某些身份提供商，`server_metadata_url` 可能对您的客户端是唯一的。但对于 Google Cloud，OIDC 客户端共享单个 URL。

在您的应用中，创建一个简单的登录流程：

```python
import streamlit as st

if not st.user.is_logged_in:
    if st.button("使用 Google 登录"):
        st.login()
    st.stop()

if st.button("登出"):
    st.logout()
st.markdown(f"欢迎！{st.user.name}")
```

当您使用 `st.stop()` 时，您的脚本运行在显示登录按钮时结束。这可以让您避免将整个页面嵌套在条件块中。此外，您可以使用回调进一步简化代码：

```python
import streamlit as st

if not st.user.is_logged_in:
    st.button("使用 Google 登录", on_click=st.login)
    st.stop()

st.button("登出", on_click=st.logout)
st.markdown(f"欢迎！{st.user.name}")
```

## 使用多个 OIDC 提供商

如果您使用多个 OIDC 提供商，您需要为每个提供商声明一个唯一名称。如果您想使用 Google Identity 和 Microsoft Entra ID 作为同一应用的两个提供商，本地开发的配置将如下 TOML 文件所示：

`.streamlit/secrets.toml`:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.google]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"
```

Microsoft 的服务器元数据 URL 根据客户端的作用域略有不同。将 `{tenant}` 替换为 Microsoft 文档中[OpenID 配置](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#find-your-apps-openid-configuration-document-uri)描述的适当值。

您的应用代码：

```python
import streamlit as st

if not st.user.is_logged_in:
    if st.button("使用 Google 登录"):
        st.login("google")
    if st.button("使用 Microsoft 登录"):
        st.login("microsoft")
    st.stop()

if st.button("登出"):
    st.logout()
st.markdown(f"欢迎！{st.user.name}")
```

使用回调，这看起来像：

```python
import streamlit as st

if not st.user.is_logged_in:
    st.button("使用 Google 登录", on_click=st.login, args=["google"])
    st.button("使用 Microsoft 登录", on_click=st.login, args=["microsoft"])
    st.stop()

st.button("登出", on_click=st.logout)
st.markdown(f"欢迎！{st.user.name}")
```

## 向您的身份提供商传递关键字

要自定义身份提供商的行为，您可能需要声明额外的关键字。有关 OIDC 参数的完整列表，请参见 [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) 和您的提供商文档。默认情况下，Streamlit 设置 `scope="openid profile email"` 和 `prompt="select_account"`。您可以通过将设置字典传递给 `client_kwargs` 来更改这些和其他 OIDC 参数。用于安全性的 `state` 和 `nonce` 会自动处理，无需指定。

例如，如果您使用 Auth0 并且需要强制用户每次都登录，请使用 Auth0 [自定义注册和登录提示](https://auth0.com/docs/customize/login-pages/universal-login/customize-signup-and-login-prompts)中描述的 `prompt="login"`。您的配置将如下所示：

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.auth0]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{account}.{region}.auth0.com/.well-known/openid-configuration"
client_kwargs = { "prompt" = "login" }
```

<Note>
  GitHub Codespaces 等托管代码环境具有额外的安全控制措施，阻止登录重定向被正确处理。
</Note>