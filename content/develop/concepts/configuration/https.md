---
title: HTTPS 支持
slug: /develop/concepts/configuration/https-support
description: 为 Streamlit 应用配置 HTTPS/SSL，使用 TLS 协议、SSL 终止、反向代理以及生产部署的安全最佳实践。
keywords: HTTPS, SSL, TLS, 安全, 反向代理, SSL 终止, 安全连接, 负载均衡器, 生产部署, 应用安全
---

# HTTPS 支持

许多应用需要使用 SSL / [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) 协议或 `https://` 访问。

我们推荐在反向代理或负载均衡器中执行 SSL 终止，用于自托管和生产用例，而不是直接在应用中。[Streamlit Community Cloud](/deploy/streamlit-community-cloud) 使用此方法，每个主要的云和应用托管平台都应该允许您配置它并提供广泛的文档。您可以在我们的[部署教程](/deploy/tutorials)中找到其中一些平台。

要在您的 Streamlit 应用中终止 SSL，您必须配置 `server.sslCertFile` 和 `server.sslKeyFile`。了解如何在[配置](/develop/concepts/configuration)中设置配置选项。

## 使用详情

- 配置值应该是证书文件和密钥文件的本地文件路径。这些必须在应用启动时可用。
- 必须指定 `server.sslCertFile` 和 `server.sslKeyFile` 两者。如果只指定一个，您的应用将以错误退出。
- 此功能在 Community Cloud 中不起作用。Community Cloud 已经使用 TLS 为您的应用提供服务。

<Warning>

在生产环境中，我们推荐由负载均衡器或反向代理执行 SSL 终止，而不是使用此选项。Streamlit 中使用此选项尚未经过广泛的安全审计或性能测试。

</Warning>

## 示例用法

```toml
# .streamlit/config.toml

[server]
sslCertFile = '/path/to/certchain.pem'
sslKeyFile = '/path/to/private.key'
```
