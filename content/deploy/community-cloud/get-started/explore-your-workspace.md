---
title: 探索你的工作空间
slug: /deploy/streamlit-community-cloud/get-started/explore-your-workspace
description: 了解如何导航Community Cloud工作空间、在工作空间之间切换以及管理你的应用和配置文件。
keywords: 工作空间, 探索, 切换, 应用, 配置文件, 开发者, 权限, github, 协作
---

# 探索你的工作空间

如果你刚刚[创建了你的账户](/deploy/streamlit-community-cloud/get-started/create-your-account)并[连接了GitHub账户](/deploy/streamlit-community-cloud/get-started/connect-your-github-account)，恭喜！你现在已登录并准备好出发。如果你加入别人的工作空间，你可能已经看到了一些应用。

## 工作空间

GitHub账户和组织中的每一个都在Community Cloud中关联一个工作空间。当你第一次登录Community Cloud时，你将进入与GitHub用户账户关联的个人工作空间。Community Cloud的左上角显示你当前的工作空间。

![Streamlit Community Cloud中的新的空工作空间。工作空间所有者显示在左上角。](/images/streamlit-community-cloud/workspace-empty-SM.png)

### 切换工作空间

要在工作空间之间切换，点击左上角的工作空间名称并选择新的工作空间。

其他工作空间对你可用如下：

- 当你对仓库有写入权限且仓库所有者已加入Community Cloud时，你可以选择关联的工作空间。所有者可以是GitHub用户或组织。
- 如果有人通过Community Cloud与你分享了应用，你将看到应用的关联工作空间。这是仅查看访问。

![此工作空间用于用户`sammy-streamlit`，他有权访问其个人工作空间和组织`we-love-streamlit`的另一个工作空间。](/images/streamlit-community-cloud/workspace-empty-switch.png)

### 邀请其他开发者到你的工作空间

邀请其他开发者很简单：只需给他们对GitHub仓库的写入权限，这样你们就可以一起编码。当他们登录<a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>时，他们将有权访问你的工作空间。

Streamlit Community Cloud从GitHub继承开发者权限。当其他人登录Community Cloud时，他们将自动看到与你共享的工作空间。从那里，你们都可以一起部署、管理和分享应用。

<Note>

当用户被添加到GitHub上的仓库时，最多需要15分钟才能在Community Cloud上部署或管理应用。如果用户从GitHub上的仓库中被移除，最多需要15分钟才能撤销他们从该仓库管理应用的权限。

</Note>

记住，每当团队中的任何人在GitHub上更新代码时，应用都会自动为你更新！

## 我的应用

工作空间的"**我的应用**"部分是你部署和管理应用的基地。当你部署应用时，它会被添加到工作空间的这一部分。

### 部署应用

如果你已经将应用保存到GitHub仓库，你可以直接部署它。否则，Community Cloud提供你可以使用的模板。当你从模板部署时，Community Cloud将fork一个项目到你的GitHub账户并从新的fork部署。如果你还没有创建Streamlit应用，这是一个便捷的开始方式。

要开始，只需在右上角点击"**创建应用**"。要了解更多，请参阅[部署你的应用](/deploy/streamlit-community-cloud/deploy-your-app)和[从模板部署](/deploy/streamlit-community-cloud/get-started/deploy-from-a-template)。

## 我的配置文件

工作空间的"**我的配置文件**"部分让你自定义Streamlit应用的个人组合与世界分享。策展和展示你的Streamlit应用来展示你的工作。

## 探索

如需灵感，请查看"**探索**"部分。这是Streamlit社区创建的Streamlit应用的画廊。查看热门和趋势应用，或搜索你感兴趣的领域中的应用。
