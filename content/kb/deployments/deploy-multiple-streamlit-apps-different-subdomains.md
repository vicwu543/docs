---
title: 如何在不同子域上部署多个 Streamlit 应用？
slug: /knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains
---

# 如何在不同子域上部署多个 Streamlit 应用？

## 问题

你想在不同子域上部署多个 Streamlit 应用。

## 解决方案

与在端口 80 等更常见的端口上运行 Streamlit 应用一样，子域由 Apache 或 Nginx 等 web 服务器处理：

- 在具有公共 IP 地址的计算机上设置 web 服务器，然后使用 DNS 服务器将所有所需子域指向你的 web 服务器的 IP 地址

- 配置你的 web 服务器，以将每个子域名的请求路由到你的 Streamlit 应用运行所在的不同端口

例如，假设你有两个 Streamlit 应用，分别称为 `Calvin` 和 `Hobbes`。应用 `Calvin` 运行在端口 **8501** 上。你将应用 `Hobbes` 设置为运行在端口 **8502** 上。然后你的 web 服务器会设置为监听子域 `calvin.somedomain.com` 和 `hobbes.subdomain.com` 上的请求，并分别将请求路由到端口 **8501** 和 **8502**。

查看这两个关于 Apache2 和 Nginx 的教程，它们涉及设置 web 服务器以将子域重定向到不同端口：

- [Apache2 subdomains](https://stackoverflow.com/questions/8541182/apache-redirect-to-another-port)
- [NGinx subdomains](https://gist.github.com/soheilhy/8b94347ff8336d971ad0)
