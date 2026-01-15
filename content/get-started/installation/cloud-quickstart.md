---
title: 使用社区云和 GitHub Codespaces 进行开发
slug: /get-started/installation/community-cloud
description: 快速入门指南，使用社区云和 GitHub Codespaces 进行基于浏览器的开发，无需本地安装。
keywords: community cloud, github codespaces, cloud development, browser development, codespaces, streamlit cloud, no installation, cloud ide
---

# 使用社区云和 GitHub Codespaces 进行开发

要使用 GitHub Codespaces 进行 Streamlit 开发，您需要一个正确配置的 `devcontainer.json` 文件来设置环境。幸运的是，Streamlit 社区云可以帮助您！虽然社区云主要用于向全世界部署和共享应用程序，但我们内置了一些便捷功能，使 GitHub Codespaces 的使用变得更加容易。本指南将解释如何创建社区云账户并使用自动化工作流程进入 GitHub codespace 并实时编辑 Streamlit 应用程序。所有这些操作都在浏览器中完成，无需安装。

如果您已经创建了社区云账户并连接了 GitHub，请跳转至[从模板创建新应用](/get-started/installation/community-cloud#create-a-new-app-from-a-template)。

## 前提条件

- 您必须拥有 GitHub 账户。

## 注册 Streamlit 社区云

1. 访问 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>。
1. 点击"**继续登录**。"
1. 点击"**继续使用 GitHub**。"
1. 输入您的 GitHub 凭据并按照 GitHub 的身份验证提示操作。
1. 填写您的账户信息，然后点击底部的"**我接受**"。

## 添加对公共仓库的访问权限

1. 在左上角，点击"**工作区 <i style={{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}>warning</i>**。"

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="将您的 GitHub 账户连接到新的社区云账户" src="/images/streamlit-community-cloud/workspace-unconnected-setup.png" />
</div>

1. 从下拉菜单中，点击"**连接 GitHub 账户**。"
1. 输入您的 GitHub 凭据并按照 GitHub 的身份验证提示操作。
1. 点击"**授权 streamlit**。"

<div style={{ maxWidth: '40%', margin: 'auto' }}>
<Image alt="授权社区云连接到您的 GitHub 账户" src="/images/streamlit-community-cloud/GitHub-auth1-none.png" />
</div>

## 可选：添加对私有仓库的访问权限

1. 在左上角，点击您的 GitHub 用户名。

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="访问您的工作区设置" src="/images/streamlit-community-cloud/workspace-empty-menu.png" />
</div>

1. 从下拉菜单中，点击"**设置**。"
1. 在对话框左侧，选择"**已连接的账户**。"
1. 在"源代码管理"下，点击"**在此连接 <i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>arrow_forward</i>**。"
1. 点击"**授权 streamlit**。"

<div style={{ maxWidth: '40%', margin: 'auto' }}>
<Image alt="授权社区云连接到您的私有 GitHub 仓库" src="/images/streamlit-community-cloud/GitHub-auth2-none.png" />
</div>

## 从模板创建新应用

1. 在右上角，点击"**创建应用**。"

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="在 Streamlit 社区云中从工作区创建新应用" src="/images/streamlit-community-cloud/deploy-empty-new-app.png" />
</div>

1. 当询问"您是否已有应用？"时，点击"**没有，从模板创建一个**。"
1. 从左侧的模板列表中，选择"**空白应用**。"
1. 在底部，选择"**打开 GitHub Codespaces...**"选项
1. 在底部，点击"**部署**。"

## 在 GitHub Codespaces 中编辑您的应用

1. 等待 GitHub 设置您的 codespace。

   完全初始化您的 codespace 可能需要几分钟时间。在您看到 codespace 中的 Visual Studio Code 编辑器后，可能还需要几分钟来安装 Python 并启动 Streamlit 服务器。完成后，您将看到一个分屏视图，左侧为代码编辑器，右侧为正在运行的应用程序。代码编辑器默认打开两个标签：仓库的 readme 文件和应用程序入口文件。

   <div style={{ maxWidth: '90%', margin: 'auto' }}>
   <Image alt="您的新 GitHub Codespace" src="/images/streamlit-community-cloud/deploy-template-blank-codespace.png" />
   </div>

1. 在左侧面板中转到应用程序入口文件(`streamlit_app.py`)，并在第3行中在 `st.title` 内添加"Streamlit"。

   ```diff
   -st.title("🎈 My new app")
   +st.title("🎈 My new Streamlit app")
   ```

   在 codespace 中，每次编辑都会自动保存文件。

1. 输入更改后片刻，您右侧的应用程序将显示重新运行提示。点击"**始终重新运行**。"

   <div style={{ maxWidth: '90%', margin: 'auto' }}>
   <Image alt="编辑示例 Streamlit 应用的标题" src="/images/streamlit-community-cloud/deploy-template-blank-codespace-edit.png" />
   </div>

   如果在您点击之前重新运行提示消失，您可以悬停在溢出菜单图标(<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)上将其恢复。

1. 可选：继续进行编辑并观察几秒钟内的更改。

## 发布您的更改

1. 在左侧导航栏中，点击源代码管理图标。

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="查看已部署的 Streamlit 应用" src="/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-source-control.png" />
</div>

1. 在左侧的源代码管理侧边栏中，为您的提交输入一个名称。
1. 点击"**<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>check</i> 提交**。"

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="查看已部署的 Streamlit 应用" src="/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-commit.png" />
</div>

1. 在确认对话框中，点击"**是**"以暂存并提交所有更改。您的更改已在 codespace 中本地提交。
1. 在左侧的源代码管理侧边栏中，点击"**<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>cached</i> 1 <i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>arrow_upward</i>**"以将您的提交推送到 GitHub。
1. 在确认对话框中，点击"**确定**"以将提交推送到"origin/main"。

   您的更改现在已保存到 GitHub 仓库中。社区云将立即在您部署的应用程序中反映这些更改。

1. 可选：要查看更新后的已发布应用，请返回到 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 工作区中的"**我的应用**"部分，然后点击您的应用。

## 学习 Streamlit 基础知识

如果您还没有学习 Streamlit 的基本概念，现在是转到[基础知识](/get-started/fundamentals)的好时机。使用您的 codespace 浏览并尝试基本的 Streamlit 命令。完成后，回到这里了解如何清理您的 codespace。

## 停止或删除您的 codespace

当您停止与 codespace 交互时，GitHub 通常会为您停止 codespace。但是，避免容量意外使用的最可靠方法是在完成后停止或删除 codespace。

1. 访问 <a href="https://github.com/codespaces" target="_blank">github.com/codespaces</a>。在页面底部，列出所有您的 codespaces。点击您 codespace 的溢出菜单图标(<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_horiz</i>)。

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="停止或删除您的 GitHub Codespace" src="/images/streamlit-community-cloud/deploy-hello-codespace-manage.png" />
</div>

2. 如果您想稍后返回工作，请点击"**停止 codespace**。否则，请点击"**删除**。"

   <div style={{ maxWidth: '40%', margin: 'auto' }}>
   <Image alt="停止您的 GitHub codespace" src="/images/streamlit-community-cloud/codespace-menu.png" />
   </div>

3. 恭喜！您刚刚将应用部署到了 Streamlit 社区云。🎉 返回 <a href="https://share.streamlit.io/" target="_blank">share.streamlit.io/</a> 工作区并[部署另一个 Streamlit 应用](/deploy/streamlit-community-cloud/deploy-your-app)。

   <div style={{ maxWidth: '90%', margin: 'auto' }}>
   <Image alt="查看您已部署的 Streamlit 应用" src="/images/streamlit-community-cloud/deploy-template-blank-edited.png" />
   </div>