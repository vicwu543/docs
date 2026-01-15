---
title: 编辑您的应用
slug: /deploy/streamlit-community-cloud/manage-your-app/edit-your-app
description: 了解如何使用 GitHub Codespaces 或任何开发环境编辑您的已部署 Streamlit 应用，并实现自动部署更新。
keywords: edit, codespaces, development, environment, github, automatic, deployment, updates, cloud, editing
---

# 编辑您的应用

您可以使用您选择的任何开发环境编辑您的应用。Streamlit Community Cloud 将监控您的仓库并自动复制您提交的任何文件更改。对于大多数更改（例如对您的应用 Python 文件的编辑），您将立即在已部署的应用中看到提交的反映。

Community Cloud 还使跳过设置开发环境的工作变得容易。只需几次点击，您就可以使用 GitHub Codespaces 配置开发环境。

## 使用 GitHub Codespaces 编辑您的应用

在几分钟内为您的已部署应用启动基于云的开发环境。您可以在您的 codespace 中运行您的应用，以享受在安全、沙盒环境中实验。当您完成代码编辑后，您可以将更改提交到您的仓库，或者只是将它们留在您的 codespace 中稍后返回。

### 为您的已部署应用创建 codespace

1. 从您在 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 的工作区，单击您的应用旁边的溢出图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)。单击"**使用 Codespaces 编辑**"。

   ![使用 GitHub Codespaces 编辑您的应用](/images/streamlit-community-cloud/workspace-app-edit.png)

   Community Cloud 将向您的仓库添加一个 `.devcontainer/devcontainer.json` 文件。如果您的仓库中已经有一个同名文件，它不会被更改。如果您希望您的仓库接收 Community Cloud 创建的实例，请删除或重命名您现有的 devcontainer 配置。

1. 等待 GitHub 设置您的 codespace。

   完全初始化您的 codespace 可能需要几分钟时间。在您的 codespace 中出现 Visual Studio Code 编辑器后，可能需要几分钟来安装 Python 并启动 Streamlit 服务器。完成后，分屏视图将在左侧显示代码编辑器，在右侧显示运行的应用。代码编辑器默认打开两个选项卡：仓库的自述文件和应用的入口点文件。

   ![您的新 GitHub Codespace](/images/streamlit-community-cloud/deploy-template-blank-codespace.png)

1. 可选：为了有更多工作空间，在另一个选项卡中打开应用预览。

   如果您有多个显示器并想要更多工作空间，请将应用预览在另一个选项卡中打开，而不是使用 Visual Studio Code 中的简单浏览器。只需从简单浏览器复制 URL 到另一个选项卡，然后关闭简单浏览器。现在您有更多空间编辑您的代码。本页面的其余步骤将继续显示 Visual Studio Code 中的分屏视图。

1. 对您的应用进行更改。

   当您对您的应用进行更改时，文件会在您的 codespace 中自动保存。您的编辑不会影响您的仓库或已部署的应用，直到您提交这些更改，这将在后面的步骤中解释。右侧显示的应用预览是您的 codespace 本地的。

1. 为了在右侧自动看到更新，在您的第一次编辑后提示时单击"**始终重新运行**"。

   ![选择"始终重新运行"以在运行的应用中自动看到编辑](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit.png)

   或者，您可以单击"**重新运行**"以避免在编写代码时不必要的重新运行。因为您的代码会持续保存，自动重新运行应用会在您在代码行中途暂停时引发错误。无论您选择哪个，您都可以通过应用 chrome 更改设置。只需单击预览应用右上角的溢出图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)，单击"**设置**"，然后切换"**保存时运行**"。

1. 继续编辑您的应用。您的 codespace 将继续在您处理文件时自动保存它们，并且预览将继续在应用重新运行时更新。

### 可选：发布您的更改

在对您的应用进行编辑后，您可以选择将您的编辑提交到您的仓库以立即更新您的已部署应用。如果您只想将您的编辑保留在您的 codespace 中稍后返回，请跳到[停止或删除您的 codespace](#stop-or-delete-your-codespace)。

1. 在左侧导航栏中，单击源代码控制图标。

   ![单击源代码控制图标](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-source-control.png)

1. 在左侧的源代码控制侧边栏中，为您的提交输入名称。
1. 单击"**<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>check</i> 提交**"。

   ![查看您的已部署 Streamlit 应用](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-commit.png)

1. 要暂存和提交您的所有更改，在确认对话框中单击"**是**"。您的更改在您的 codespace 中本地提交。
1. 要将您的提交推送到 GitHub，在左侧的源代码控制侧边栏中，单击"**<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>cached</i> 1 <i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>arrow_upward</i>**"。
1. 要将提交推送到"origin/main"，在确认对话框中单击"**确定**"。

   您的更改现在保存到您的 GitHub 仓库。Community Cloud 将立即在您的已部署应用中反映更改。

1. 可选：要查看您的更新、已发布的应用，返回到您在 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 的工作区的"**我的应用**"部分，并单击您的应用。

### 停止或删除您的 codespace

当您停止与您的 codespace 交互时，GitHub 通常会为您停止 codespace。但是，避免不 desired 使用容量的最可靠方法是在完成后停止或删除您的 codespace。

1. 转到 <a href="https://github.com/codespaces" target="_blank">github.com/codespaces</a>。在页面底部，列出了您的所有 codespace。单击您的 codespace 的溢出菜单图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_horiz</i>)。

   ![停止或删除您的 GitHub Codespace](/images/streamlit-community-cloud/deploy-hello-codespace-manage.png)

2. 如果您想稍后返回工作，单击"**停止 codespace**"。否则，单击"**删除**"。

   <div style={{ maxWidth: '40%', margin: 'auto' }}>
   <Image alt="停止您的 GitHub codespace" src="/images/streamlit-community-cloud/codespace-menu.png" />
   </div>

3. 恭喜！您刚刚将应用部署到 Community Cloud。🎉 返回到您在 <a href="https://share.streamlit.io/" target="_blank">share.streamlit.io/</a> 的工作区并[部署另一个 Streamlit 应用](/deploy/streamlit-community-cloud/deploy-your-app)。

   ![查看您的已部署 Streamlit 应用](/images/streamlit-community-cloud/deploy-template-blank-edited.png)
