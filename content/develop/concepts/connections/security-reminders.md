---
title: 安全提醒
slug: /develop/concepts/connections/security-reminders
description: 了解 Streamlit 应用的重要安全实践，包括保护密钥、安全编码实践和防止安全漏洞。
keywords: security, security practices, protect secrets, secure coding, security vulnerabilities, app security, security best practices, data protection
---

# 安全提醒

## 保护您的密钥

切勿直接在代码中保存用户名、密码或安全密钥，也不要将它们提交到您的仓库。

### 使用环境变量

通过使用环境变量来避免在代码中放置敏感信息。请务必查看 [`st.secrets`](/develop/concepts/connections/secrets-management)。研究您使用的任何平台，以遵循其安全最佳实践。如果您使用 Streamlit Community Cloud，[密钥管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) 允许您保存环境变量并在代码之外存储密钥。

### 保持 `.gitignore` 更新

如果您在开发过程中使用任何敏感或私有信息，请确保这些信息保存在与代码分离的文件中。确保 `.gitignore` 配置正确，以防止将私有信息保存到您的仓库。

## Pickle 警告

Streamlit 的 [`st.cache_data`](/develop/concepts/architecture/caching#stcache_data) 和 [`st.session_state`](/develop/concepts/architecture/session-state#serializable-session-state) 隐式使用 `pickle` 模块，该模块已知不安全。有可能构建恶意的 pickle 数据，在反序列化期间执行任意代码。切勿在不安全模式下加载可能来自不受信任来源或可能已被篡改的数据。**仅加载您信任的数据**。

- 使用 `st.cache_data` 时，函数返回的任何内容都会被 pickle 并存储，然后在检索时反序列化。确保您的缓存函数返回可信值。此警告也适用于 [`st.cache`](/develop/api-reference/caching-and-state/st.cache)（已弃用）。
- 当 `runner.enforceSerializableSessionState` [配置选项](<(/develop/concepts/configuration#runner)>) 设置为 `true` 时，确保从会话状态保存和检索的所有数据都是可信的。