---
title: 如何在域上部署Streamlit以使其显示在常规端口(即端口 80)上运行？
slug: /knowledge-base/deploy/deploy-streamlit-domain-port-80
---

# 如何在域上部署Streamlit以使其显示在常规端口(即端口 80)上运行？

## 问题

你想在一个域上部署Streamlit应用程序，使其显示在端口 80 上运行。

## 解决方案

- 你应该使用**反向代理**来从[Apache](https://httpd.apache.org/)或[Nginx](https://www.nginx.com/)等web服务器转发请求到你的Streamlit应用程序运行所在的端口。你可以以许多不同的方案完成此作。最简单的方案是[转发所有发送到你的域的请求](https://discuss.streamlit.io/t/permission-denied-in-ec2-port-80/798/3)，以便Streamlit应用程序车止作为你的应用程序内容。

- 另一个方法是配置你的web服务器以转发请求到指定的子文件夹(例如 _http://awesomestuff.net/streamlitapp_)到同一域上的不同Streamlit应用程序，如此[Nginx配置示例](https://discuss.streamlit.io/t/how-to-use-streamlit-with-nginx/378/7)于Streamlit穆族会员提交。

Related forum posts:

- https://discuss.streamlit.io/t/permission-denied-in-ec2-port-80/798/3
- https://discuss.streamlit.io/t/how-to-use-streamlit-with-nginx/378/7
