---
title: 创建您的账户
slug: /deploy/streamlit-community-cloud/get-started/create-your-account
description: 了解如何使用电子邮件、Google 或 GitHub 认证方法创建您的 Streamlit 社区云账户。
keywords: 创建账户, 注册, 认证, 电子邮件, Google, GitHub, oauth, 社区云
---

# 创建您的账户

在您开始部署应用程序供全世界查看之前，您需要注册您的 Streamlit 社区云账户。

每个社区云账户都与一个电子邮件关联。两个账户不能使用相同的电子邮件。当分享私有应用程序时，您将通过电子邮件分配查看权限。此外，两个账户不能具有相同源码控制系统（GitHub 账户）。如果您尝试使用相同源码控制系统创建第二个社区云账户，社区云将会合并这些账户。

## 注册

社区云允许您使用以下三种方法之一登录：

- 通过电子邮件发送的单次使用验证码
- Google
- GitHub

<Important>
    即使您通过 GitHub 登录，认证流程也会将您的电子邮件地址返回给社区云。如果您通过 GitHub 登录，更改 GitHub 账户上的电子邮件可能会影响您的社区云账户。
</Important>

1. 前往 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
1. 点击"**继续登录**".
1. 使用下面列出的三个选项之一继续操作。

   ### 选项 1: 使用邮件验证码登录
   1. 在"电子邮件"字段中，输入您的电子邮件地址。
   1. 点击"**继续**"。(如果提示，请验证您是人类。)
   1. 前往您的电子邮件收件箱，复制您的一次性六位数字验证码。验证码有效期为十分钟。
   1. 返回到认证页面，输入您的验证码。(如果提示，请验证您是人类。)

   ### 选项 2: 使用 Google 登录
   1. 点击"**使用 Google 继续**"。
   1. 输入您的 Google 凭据，并按照 Google 的身份验证提示操作。

   ### 选项 3: 使用 GitHub 登录
   1. 点击"**使用 GitHub 继续**"。
   1. 输入您的 GitHub 凭据，并按照 GitHub 的身份验证提示操作。

      这会将"Streamlit 社区云"OAuth 应用程序添加到您的 GitHub 账户。此应用程序仅用于在您登录社区云时传递您的电子邮件。在下一页，您将执行额外步骤以允许社区云访问您的存储库。有关使用和审查您账户上的 OAuth 应用程序的更多信息，请参阅 GitHub 文档中的 [使用 OAuth 应用](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps)。

1. 填写您的信息，然后点击底部的"**继续**"。

   "主要电子邮件"字段预先填入了您用来登录的电子邮件。如果您在账户设置表单中更改此电子邮件，它只会影响营销电子邮件；它不会反映在您的新账户上。要在创建账户后更改与账户关联的电子邮件，请参阅 [更新您的电子邮件地址](/deploy/streamlit-community-cloud/manage-your-account/update-your-email)。

## 完成

恭喜您创建了 Streamlit 社区云账户！左上角 "**工作空间**" 旁边的警告图标 (<i style={{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}>warning</i>) 是正常的；这表示您的账户尚未连接到 GitHub。即使您通过 GitHub 创建了账户，您的账户尚无权访问您的存储库。请继续下一页连接您的 GitHub 账户。