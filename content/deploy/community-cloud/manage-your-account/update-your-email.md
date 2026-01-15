---
title: 更新你的电子邮件
slug: /deploy/streamlit-community-cloud/manage-your-account/update-your-email
description: 了解如何使用账户合并或GitHub账户更改来更新Streamlit Community Cloud上的电子邮件地址。
keywords: 更新电子邮件, 更改电子邮件, 账户合并, github, 认证, 身份, 账户管理
---

# 更新你的电子邮件

要更新Streamlit Community Cloud上的电子邮件，你有两个选项：你可以创建新账户并将现有账户合并到其中，或者你可以使用GitHub账户更新你的电子邮件。

## 选项1：创建新账户并合并它

两个Community Cloud账户不能对源代码控制有相同的GitHub账户。当你将GitHub账户连接到新Community Cloud账户以进行源代码控制时，Community Cloud会自动合并任何具有相同源代码控制的现有账户。

因此，你可以使用所需的电子邮件创建新账户，并连接相同的GitHub账户以将它们合并在一起。

1. 使用你的新电子邮件创建新账户。
1. 连接你的GitHub账户。

你的旧账户和新账户现在已合并，你已有效更改了电子邮件地址。

## 选项2：使用你的GitHub账户

或者，你可以更改GitHub账户上的电子邮件，然后使用GitHub登录Community Cloud。

1. 转到GitHub，将你的主要电子邮件地址设置为新电子邮件。
1. 如果你当前登录到Community Cloud，请退出。
1. 使用GitHub登录Community Cloud。

   如果你被重定向到工作空间，你看到现有应用，你已完成！你的电子邮件已更改。要确认当前电子邮件和GitHub账户，点击左上角的工作空间名称，并查看下拉菜单底部。

   如果你被重定向到空工作空间，你看到左上角的"**工作空间 <i style={{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}>warning</i>**"，请继续[连接你的GitHub账户](/deploy/streamlit-community-cloud/get-started/connect-your-github-account)。如果你之前使用新电子邮件创建了账户但没有将GitHub账户连接到它，就可能发生这种情况。

<Important>
   如果你有多个GitHub账户，请小心。为避免意外行为，要么在每个GitHub账户上使用唯一的电子邮件，要么避免使用GitHub登录Community Cloud。
</Important>
