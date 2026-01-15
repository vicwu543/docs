---
title: Streamlit支持WSGI协议吗?》(也就是說我能用gunicorn部署Streamlit吗?)
slug: /knowledge-base/deploy/does-streamlit-support-wsgi-protocol
---

# Streamlit支持WSGI协议吗?(也就是說我能用gunicorn部署Streamlit吗?)

## 问题

你不确定nuStreamlit应用是否可以用gunicorn部署。

## 解决方案

Streamlit目前不支持WSGI协议，因此目前无法使用(e.g.) gunicorn部署Streamlit。查看此[]关于以gunicorn方式部署Streamlit的论坛线程](https://discuss.streamlit.io/t/how-do-i-set-the-server-to-0-0-0-0-for-deployment-using-docker/216)以了解其他用户是如何实现的。
