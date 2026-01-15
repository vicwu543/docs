---
title: 部署应用时管理密钥
slug: /deploy/concepts/secrets
description: 了解在将 Streamlit 应用部署到生产环境时安全管理密钥、凭证和 API 密钥的最佳实践。
keywords: secrets, credentials, api keys, security, environment variables, st.secrets, deployment
---

# 部署应用时管理密钥

如果您连接到数据源或外部服务，您可能正在处理机密信息，如凭证或密钥。机密信息应以安全的方式存储和传输。部署应用时，请确保您了解您的平台的功能和处理密钥的机制，以便您可以遵循最佳实践。

避免直接在代码中保存密钥，并保持 `.gitignore` 最新以防止意外将本地密钥提交到存储库。有用的提醒，请参阅 [安全提醒](/develop/concepts/connections/security-reminders)。

如果您使用 Streamlit Community Cloud，[密钥管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) 允许您保存环境变量并将密钥存储在代码之外。如果您使用为 Streamlit 设计的另一个平台，请检查他们是否有内置的机制来处理密钥。在某些情况下，他们甚至可能支持 `st.secrets` 或安全地上传您的 `secrets.toml` 文件。

有关使用带有环境变量的 `st.connection` 的信息，请参阅 [全局密钥、管理多个应用和多个数据存储](/develop/concepts/connections/connecting-to-data#global-secrets-managing-multiple-apps-and-multiple-data-stores)。
