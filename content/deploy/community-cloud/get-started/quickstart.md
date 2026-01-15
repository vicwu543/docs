---
title: 快速入门
slug: /deploy/streamlit-community-cloud/get-started/quickstart
description: 快速入门指南，创建您的社区云账户，部署示例应用程序，并在几分钟内开始使用 GitHub Codespaces 进行编辑。
keywords: 快速入门, 社区云, 账户, 部署, 示例应用程序, github codespaces, 模板, 编辑
---

# 快速入门

这是一套简洁的步骤，用于创建您的 Streamlit 社区云账户、部署示例应用程序，并使用 GitHub Codespaces 开始编辑。对于其他选项和完整说明，请从 [创建您的账户](/deploy/streamlit-community-cloud/get-started/create-your-account) 开始。

在此过程中，您将登录到您的 GitHub 账户。社区云将使用您 GitHub 账户中的电子邮件来创建您的社区云账户。对于其他登录选项，请参见 [创建您的账户](/deploy/streamlit-community-cloud/get-started/create-your-account)。

## 先决条件

- 您必须拥有一个 GitHub 账户。

## 注册 Streamlit 社区云

1. 前往 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>。
1. 点击"**继续登录**"。
1. 点击"**使用 GitHub 继续**"。
1. 输入您的 GitHub 凭据并按照 GitHub 的身份验证提示操作。
1. 填写您的账户信息，然后点击底部的"**我接受**"。

## 添加对公共仓库的访问权限

1. 在左上角，点击"**工作空间 <i style={{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}>warning</i>**。"

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
1. 在"源码控制"下，点击"**在此连接 <i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>arrow_forward</i>**。"
1. 点击"**授权 streamlit**。"

<div style={{ maxWidth: '40%', margin: 'auto' }}>
<Image alt="授权社区云连接到您的私有 GitHub 仓库" src="/images/streamlit-community-cloud/GitHub-auth2-none.png" />
</div>

## 从模板创建新应用程序

1. 在右上角，点击"**创建应用程序**。"

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="在 Streamlit 社区云中从工作区创建新应用程序" src="/images/streamlit-community-cloud/deploy-empty-new-app.png" />
</div>

1. 当被问到"您已经有应用程序了吗？"时，点击"**没有，从模板创建一个**。"
1. 从左侧的模板列表中，选择"**空白应用程序**。"
1. 在底部，选择"**打开 GitHub Codespaces...**"选项
1. 在底部，点击"**部署**。"

## 在 GitHub Codespaces 中编辑您的应用程序

1. 等待 GitHub 设置您的代码空间。

   完全初始化您的代码空间可能需要几分钟时间。在 Visual Studio Code 编辑器出现在您的代码空间中后，安装 Python 并启动 Streamlit 服务器可能还需要几分钟时间。完成后，分屏视图显示左侧的代码编辑器和右侧正在运行的应用程序。代码编辑器默认打开两个标签：仓库的 readme 文件和应用程序的入口文件。

   <div style={{ maxWidth: '90%', margin: 'auto' }}>
   <Image alt="您的新 GitHub 代码空间" src="/images/streamlit-community-cloud/deploy-template-blank-codespace.png" />
   </div>

1. 在左窗格中转到应用程序的入口文件（`streamlit_app.py`），并在第3行中在 `st.title` 内添加"Streamlit"。

   ```diff
   -st.title("🎈 My new app")
   +st.title("🎈 My new Streamlit app")
   ```

   在您的代码空间中，每次编辑时文件都会自动保存。

1. 输入更改后片刻，您右侧的应用程序将显示重新运行提示。点击"**始终重新运行**。"

   <div style={{ maxWidth: '90%', margin: 'auto' }}>
   <Image alt="编辑示例 Streamlit 应用程序的标题" src="/images/streamlit-community-cloud/deploy-template-blank-codespace-edit.png" />
   </div>

   如果您点击之前重新运行提示消失，可以悬停在溢出菜单图标上（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>）将其恢复。

1. 可选：继续进行编辑并在几秒钟内观察更改。

## 发布您的更改

1. 在左侧导航栏中，点击源码控制图标。

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="查看您已部署的 Streamlit 应用程序" src="/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-source-control.png" />
</div>

1. 在左侧的源码控制侧边栏中，为您的提交输入一个名称。
1. 点击"**<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>check</i> 提交**。"

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="查看您已部署的 Streamlit 应用程序" src="/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-commit.png" />
</div>

1. 要暂存并提交所有更改，在确认对话框中点击"**是**。"您的更改在代码空间中本地提交。
1. 要将您的提交推送到 GitHub，在左侧的源码控制侧边栏中点击"**<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>cached</i> 1 <i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>arrow_upward</i>**。"
1. 要将提交推送到"origin/main"，在确认对话框中点击"**确定**。"

   您的更改现在已保存到您的 GitHub 仓库。社区云将立即在您已部署的应用程序中反映更改。

1. 可选：要查看您更新后的已发布应用程序，请返回到 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 工作区的"**我的应用程序**"部分，然后点击您的应用程序。

## 停止或删除您的代码空间

当您停止与代码空间交互时，GitHub 通常会为您停止代码空间。然而，避免不必要使用容量的最可靠方法是在完成后停止或删除代码空间。

1. 前往 <a href="https://github.com/codespaces" target="_blank">github.com/codespaces</a>。在页面底部，列出您的所有代码空间。点击您代码空间的溢出菜单图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_horiz</i>）。

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="停止或删除您的 GitHub 代码空间" src="/images/streamlit-community-cloud/deploy-hello-codespace-manage.png" />
</div>

2. 如果您想稍后返回您的工作，请点击"**停止代码空间**。否则，请点击"**删除**。"

   <div style={{ maxWidth: '40%', margin: 'auto' }}>
   <Image alt="停止您的 GitHub 代码空间" src="/images/streamlit-community-cloud/codespace-menu.png" />
   </div>

3. 恭喜！您刚刚将应用程序部署到 Streamlit 社区云。🎉 返回到 <a href="https://share.streamlit.io/" target="_blank">share.streamlit.io/</a> 的工作区并 [部署另一个 Streamlit 应用程序](/deploy/streamlit-community-cloud/deploy-your-app)。

   <div style={{ maxWidth: '90%', margin: 'auto' }}>
   <Image alt="查看您已部署的 Streamlit 应用程序" src="/images/streamlit-community-cloud/deploy-template-blank-edited.png" />
   </div>