---
title: 分享你的应用
slug: /deploy/streamlit-community-cloud/share-your-app
description: 了解如何公开或私有地分享已部署的 Streamlit 应用，邀请查看者及添加 GitHub 徽章以提高可发现性。
keywords: share, app, public, private, viewers, invite, social media, github badge, collaboration
---

# 分享你的应用

现在你的应用已经部署，你可以轻松地分享并进行协作。首先，让我们停下来庆祝一下你成功部署了应用！👩💃

你的应用现在可以在一个固定的URL上访问。根据你的需求与任何你想分享的人分享吧。你的应用将从GitHub仓库继承权限，这意味着如果你的仓库是私有的，你的应用将是私有的；如果你的仓库是公开的，你的应用将是公开的。如果你想改变这一点，你可以简单地从应用设置菜单中改变。

一次只允许一个私有应用。如果你从私有仓库部署，你将需要将该应用设为公开或删除它，才能从私有仓库部署另一个应用。只有开发者可以改变你的应用的公开和私有状态。

- [使你的应用公开或私有](#make-your-app-public-or-private)
- [分享你的公开应用](#share-your-public-app)
- [分享你的私有应用](#share-your-private-app)

## 使你的应用公开或私有

如果你从公开仓库部署你的应用，你的应用默认情况下将是公开的。如果你从私有仓库部署你的应用，你将需要将该应用设为公开，或者如果你想仅与特定人分享。

### 从应用设置中设置为公开或私有

1. 访问你的[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)并转到"分享"部分。

   ![Streamlit Community Cloud中的分享设置](/images/streamlit-community-cloud/workspace-app-settings-sharing.png)

2. 在"谁能查看此应用"下设置你的应用为公开或私有。选择"此应用是公开的且可发现的"使你的应用公开。选择"只有特定人士可以查看此应用"使你的应用私有。

## 分享你的公开应用

有很多方式可以与他人分享你的公开应用：

- **直接共享链接**——将你的应用URL复制粘贴到任何地方——电子邮件、Slack、Twitter等。
- **社交媒体**——当你在社交媒体上分享你的公开应用链接时，会自动生成一个含有你的应用标题、描述和预览图像的卡片。更多关于[共享预览](/deploy/streamlit-community-cloud/share-your-app/share-previews)的信息。
- **GitHub徽章**——将一个漂亮的Streamlit徽章添加到你的仓库README中，指向你的应用。更多关于[GitHub徽章](#add-a-github-badge)的信息。

### 添加GitHub徽章

为了让更多人能够发现你的应用，你可以在GitHub仓库的README中添加一个GitHub徽章。这是一个简单的链接，当点击时会带你到你的应用。

1. 将以下代码行复制到你的README文件中：

   ```markdown
   [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-STREAMLIT-CLOUD-URL)
   ```

2. 将`YOUR-STREAMLIT-CLOUD-URL`替换为你的应用实际的URL。

   例如，如果你的应用URL是`https://share.streamlit.io/username/repo/app.py`，你的徽章代码应该看起来像这样：

   ```markdown
   [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/username/repo/app.py)
   ```

有几个Streamlit徽章变体可用。你可以在以下链接找到它们：

- 黑色和白色（推荐）：`https://static.streamlit.io/badges/streamlit_badge_black_white.svg`
- 黑色背景：`https://static.streamlit.io/badges/streamlit_badge_black.svg`
- 红色背景：`https://static.streamlit.io/badges/streamlit_badge_red.svg`

## 分享你的私有应用

对于私有应用，你可以邀请特定的人查看你的应用。

### 邀请查看者

1. 访问你的[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)并转到"分享"部分。
2. 在"邀请查看者"下，输入你想邀请的人的电子邮件地址。
3. 点击"邀请"。你邀请的人将收到一封邮件邀请他们查看你的应用。

### 管理查看者访问

1. 访问你的[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)并转到"分享"部分。
2. 在"查看者访问"下，你会看到所有受邀查看你应用的人员的列表。
3. 要删除某人的访问权限，请点击他们旁边的"删除"按钮。

<Note>

当你删除某人的访问权限时，他们将无法再查看你的应用。

</Note>
