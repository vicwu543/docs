---
title: 连接你的GitHub账户
slug: /deploy/streamlit-community-cloud/get-started/connect-your-github-account
description: 连接GitHub账户到Community Cloud，以使用适当权限从公共和私有仓库部署应用。
keywords: github, 连接, oauth, 仓库, 公共, 私有, 权限, 组织, 访问
---

# 连接你的GitHub账户

将GitHub连接到你的Streamlit Community Cloud账户允许你直接从存储在仓库中的文件部署应用。它还使系统能够检查这些文件的更新并自动更新你的应用。首次将GitHub账户连接到Community Cloud账户时，你将能够将应用从公共仓库部署到Community Cloud。如果你想从私有仓库部署，你可以给予Community Cloud额外权限来这样做。有关这些权限的更多信息，请参阅[GitHub OAuth范围](/deploy/streamlit-community-cloud/status#github-oauth-scope)。

<Important>
    为了部署应用，你必须对其仓库有**管理员**权限。如果你没有管理员访问权限，请联系仓库的所有者或fork仓库来创建你自己的副本。如需更多帮助，请参阅我们的<a href="https://discuss.streamlit.io/" target="_blank">社区论坛</a>。
</Important>

如果你是GitHub组织的成员，该组织将显示在每个GitHub OAuth提示的底部。在这种情况下，我们建议在执行连接GitHub账户的步骤之前阅读本页末尾的[组织访问](#organization-access)。你必须是GitHub中的组织所有者才能向该组织授予访问权限。

## 先决条件

- 你必须拥有Community Cloud账户。请参阅[创建你的账户](/deploy/streamlit-community-cloud/get-started/create-your-account)。
- 你必须拥有GitHub账户。

## 添加对公共仓库的访问权限

1. 在左上角，点击"**工作空间 <i style={{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}>warning</i>**"。

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="将GitHub账户连接到新的Community Cloud账户" src="/images/streamlit-community-cloud/workspace-unconnected-setup.png" />
</div>

1. 从下拉菜单中，点击"**连接GitHub账户**"。
1. 输入你的GitHub凭据并遵循GitHub的认证提示。
1. 点击"**授权streamlit**"。

   <div style={{ maxWidth: '40%', margin: 'auto' }}>
   <Image alt="授权Community Cloud连接到你的GitHub账户" src="/images/streamlit-community-cloud/GitHub-auth1-none.png" />
   </div>

   这将"Streamlit" OAuth应用程序添加到你的GitHub账户。这允许Community Cloud与你的公共仓库配合使用并为你创建codespaces。在下一部分中，你也可以允许Community Cloud访问你的私有仓库。有关在你账户上使用和审查OAuth应用程序的更多信息，请参阅GitHub文档中的[使用OAuth应用](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps)。

## 可选：添加对私有仓库的访问权限

在你的Community Cloud账户有权从公共仓库部署后，你可以遵循这些额外步骤来授予对私有仓库的访问权限。

1. 在左上角，点击你的GitHub用户名。

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="访问你的工作空间设置" src="/images/streamlit-community-cloud/workspace-empty-menu.png" />
</div>

1. 从下拉菜单中，点击"**设置**"。
1. 在对话框的左侧，选择"**链接账户**"。
1. 在"源代码控制"下，点击"**在此连接 <i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>arrow_forward</i>**"。
1. 点击"**授权streamlit**"。

<div style={{ maxWidth: '40%', margin: 'auto' }}>
<Image alt="授权Community Cloud连接到你的私有GitHub仓库" src="/images/streamlit-community-cloud/GitHub-auth2-none.png" />
</div>

## 组织访问

要从GitHub组织拥有的仓库部署应用，Community Cloud必须有权访问组织的仓库。如果在连接GitHub账户时你是GitHub组织的成员，你的OAuth提示将包括标记为"组织访问"的部分。

<div style={{ maxWidth: '40%', margin: 'auto' }}>
<Image alt="包含组织访问的GitHub Oauth提示" src="/images/streamlit-community-cloud/GitHub-auth1-organizations.png" />
</div>

如果你已经连接了GitHub账户并需要添加组织的访问权限，请遵循[管理你的GitHub连接](/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection)中的步骤来断开你的GitHub账户并重新开始。或者，如果你不是组织的所有者，你可以请求所有者为自己创建Community Cloud账户并直接添加权限。

### 你拥有的组织

对于你拥有的任何组织，如果之前未授予或拒绝授权，你可以在点击"**授权streamlit**"之前点击"**授予**"。

<div style={{ maxWidth: '80%', margin: 'auto' }}>
<Image alt="在你拥有的GitHub组织上授权你的Streamlit" src="/images/streamlit-community-cloud/GitHub-auth-grant-XL.png" />
</div>

### 由他人拥有的组织

对于你不拥有的组织，如果之前未授予或拒绝授权，你可以在点击"**授权streamlit**"之前点击"**请求**"。

<div style={{ maxWidth: '80%', margin: 'auto' }}>
<Image alt="在他人拥有的GitHub组织上授权你的Streamlit" src="/images/streamlit-community-cloud/GitHub-auth-request-XL.png" />
</div>

### 先前或待处理的授权

如果有人已经启动了为你的组织授权Streamlit的过程，OAuth提示将显示当前状态。

#### 已批准访问

如果组织已经授予Streamlit访问权限，OAuth提示显示绿色勾号（<i style={{ verticalAlign: "-.25em", color: "#1a7f37" }} className={{ class: "material-icons-sharp" }}>check</i>）。

<div style={{ maxWidth: '60%', margin: 'auto' }}>
<Image alt="组织对Streamlit的已批准授权" src="/images/streamlit-community-cloud/GitHub-auth-granted-XL.png" />
</div>

#### 待处理访问

如果之前发送了请求但尚未批准，OAuth提示显示"访问请求待处理"。与组织的所有者跟进以在GitHub中接受请求。

<div style={{ maxWidth: '60%', margin: 'auto' }}>
<Image alt="组织对Streamlit的待处理授权" src="/images/streamlit-community-cloud/GitHub-auth-pending-XL.png" />
</div>

#### 拒绝访问

如果之前发送了请求并被拒绝，OAuth提示显示红色X（<i style={{ verticalAlign: "-.25em", color: "#d1242f" }} className={{ class: "material-icons-sharp" }}>close</i>）。在这种情况下，组织所有者将需要从GitHub授权Streamlit。请参阅GitHub关于<a href="https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations" target="_blank">OAuth应用和组织</a>的文档。

<div style={{ maxWidth: '60%', margin: 'auto' }}>
<Image alt="组织对Streamlit的拒绝授权" src="/images/streamlit-community-cloud/GitHub-auth-denied-XL.png" />
</div>

## 接下来呢？

现在你有了账户，你可以[探索你的工作空间](/deploy/streamlit-community-cloud/get-started/explore-your-workspace)。或者如果你已准备好，直接跳进去并[部署你的应用](/deploy/streamlit-community-cloud/deploy-your-app)。
