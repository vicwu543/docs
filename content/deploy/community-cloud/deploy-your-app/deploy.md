---
title: 在Community Cloud上部署你的应用
slug: /deploy/streamlit-community-cloud/deploy-your-app/deploy
description: 分步指南，在Community Cloud上部署Streamlit应用，包括仓库选择、配置和部署过程。
keywords: 部署, community cloud, 仓库, 入口文件, python版本, 秘密, 子域, 部署过程
---

# 在Community Cloud上部署你的应用

在你[整理了你的文件](/deploy/streamlit-community-cloud/deploy-your-app/file-organization)和[添加了你的依赖](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)如前面页面所述后，你已准备好将你的应用部署到Community Cloud！

## 选择你的仓库和入口文件

1. 从你在 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 的工作空间，在右上角点击"**创建应用**"。

   ![从你的工作空间部署新应用](/images/streamlit-community-cloud/deploy-empty-new-app.png)

1. 当被问及"你已经有应用吗？"时，点击"**是的，我有应用**"。
1. 填入你的仓库、分支和文件路径。或者，要直接粘贴GitHub上的`your_app.py`链接，点击"**粘贴GitHub URL**"。
1. 可选：在"应用URL"字段中，为你的新应用选择一个子域。

   每个Community Cloud应用都部署到`streamlit.app`上的子域，但你可以随时更改应用的子域。有关更多信息，请参阅[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)。在下面的示例中，Community Cloud将应用部署到`https://red-balloon.streamlit.app/`。

   ![填入你的应用信息以部署你的应用](/images/streamlit-community-cloud/deploy-an-app.png)

   尽管Community Cloud尝试建议可用的仓库和文件，这些建议并不总是完整的。如果任何字段中找不到所需的信息，请手动输入。

## 可选：配置秘密和Python版本

<Note>

Streamlit Community Cloud支持所有仍在接收安全更新的发布的 [Python版本](https://devguide.python.org/versions/)。Streamlit Community Cloud默认为版本3.12。你可以从"高级设置"模态框中的"Python版本"下拉菜单中选择你选择的版本。如果应用运行的Python版本变得不支持，它将被强制升级到最旧的受支持的Python版本，可能会出现问题。

</Note>

1. 点击"**高级设置**"。
1. 选择你想要的Python版本。
1. 要定义环境变量和秘密，在"秘密"字段中粘贴你的`secrets.toml`文件的内容。

   有关更多信息，请参阅[Community Cloud秘密管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)。

1. 点击"**保存**"。

<div style={{ maxWidth: '70%', margin: 'auto' }}>
<Image alt="部署你的应用的高级设置" src="/images/streamlit-community-cloud/deploy-an-app-advanced.png" />
</div>

## 观看你的应用启动

你的应用现在正在被部署，你可以在它启动时观看。大多数应用在几分钟内部署，但如果你的应用有很多依赖，可能需要更长时间。初始部署后，对代码的更改应该立即反映在你的应用中。对依赖的更改将立即处理，但可能需要几分钟时间来安装。

![观看你的应用启动](/images/streamlit-community-cloud/deploy-an-app-provisioning.png)

<Note>

Streamlit Community Cloud日志在你的应用右侧只对具有仓库写入权限的用户可见。这些日志帮助你调试应用的任何问题。了解更多关于[Streamlit Community Cloud日志](/deploy/streamlit-community-cloud/manage-your-app#cloud-logs)。

</Note>

<a name="your-app-url"></a>

## 查看你的应用

就这样&mdash;你完成了！你的应用现在有一个你可以与他人共享的唯一URL。阅读更多关于如何与查看者[共享你的应用](/deploy/streamlit-community-cloud/share-your-app)。

### 唯一的子域

如果在部署应用时"**自定义子域（可选）**"字段为空，将根据你的GitHub仓库结构分配一个URL。URL的子域是以下内容的破折号分隔列表：

- 仓库所有者（GitHub用户或组织）
- 仓库名称
- 入口文件路径
- 分支名称（如果不是`main`或`master`）
- 随机哈希

```bash
https://[GitHub username or organization]-[repo name]-[app path]-[branch name]-[short hash].streamlit.app
```

例如，以下应用从`streamlit`组织部署。仓库是`demo-self-driving`，应用名称是根目录中的`streamlit_app.py`。分支名称是`master`，因此不包括在内。

```bash
https://streamlit-demo-self-driving-streamlit-app-8jya0g.streamlit.app
```

### 自定义子域

设置自定义子域使共享你的应用变得容易得多，因为你可以选择容易记住的名称。要了解如何更改已部署应用的子域，请参阅[查看或更改你的应用URL](/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-change-your-apps-url)。
