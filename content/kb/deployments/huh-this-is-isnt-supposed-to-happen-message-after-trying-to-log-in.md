---
title: 登录时出现"呃。这不应该发生"消息
slug: /knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in
---

# 登录时出现"呃。这不应该发生"消息

本文帮助解决由GitHub和Streamlit Community Cloud之间电子邮件不匹配引起的登录问题。

## 问题

登录到你的Streamlit Community Cloud账户后，你会看到以下消息：

![Huh. This is isn't supposed to happen message](/images/knowledge-base/huh-this-isnt-supposed-to-happen.png)

此消息通常表示我们的系统已将你的GitHub用户名与你当前登录的电子邮件地址以外的电子邮件地址关联。

## 解决方案

别担心–你只需要：

1. 完全退出Streamlit Community Cloud(通过你的电子邮件和GitHub账户)。
2. 首先使用你的电子邮件账户登录(你可以通过["Continue with Google"](/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out#sign-in-with-google)或["Continue with email"](/knowledge-base/deploy/sign-in-without-sso)进行)。
3. 使用你的[GitHub账户](/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out#sign-in-with-email)登录。
