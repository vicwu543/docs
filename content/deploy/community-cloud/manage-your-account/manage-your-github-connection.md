---
title: 管理你的GitHub连接
slug: /deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection
description: 了解如何管理你的GitHub连接到Community Cloud，包括添加组织访问、撤销权限和处理账户更改。
keywords: github连接, 管理, 组织访问, 撤销, 重新授权, oauth, 权限, 账户重命名, 仓库重命名
---

# 管理你的GitHub连接

如果你已创建账户但尚未连接GitHub，请参阅[连接你的GitHub账户](/deploy/streamlit-community-cloud/get-started/connect-your-github-account)。

如果你已连接GitHub账户但仍需允许Streamlit Community Cloud访问私有仓库，请参阅[可选：添加对私有仓库的访问权限](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#optional-add-access-to-private-repositories)。

## 添加组织访问权限

如果你在组织中，你可以在连接GitHub账户时授予或请求对该组织的访问权限。有关更多信息，请参阅[组织访问](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access)。

如果你的GitHub账户已连接，你可以在GitHub设置中移除权限，并在下次登录Community Cloud时强制Streamlit重新提示GitHub授权。

### 撤销和重新授权

1. 从你的工作空间，点击右上角的工作空间名称。要退出Community Cloud，点击"**退出**"。

   ![从Streamlit Community Cloud退出](/images/streamlit-community-cloud/account-sign-out.png)

1. 转到<a href="https://github.com/settings/applications" target="_blank">github.com/settings/applications</a>的GitHub应用设置。
1. 找到"Streamlit"应用，并点击三个点(<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_horiz</i>)以打开溢出菜单。

   如果你曾使用GitHub登录Community Cloud，你也会在GitHub账户中看到"Streamlit Community Cloud"应用。"Streamlit"应用管理仓库访问。"Streamlit Community Cloud"应用仅用于管理你在Community Cloud上的身份（电子邮件）。你只需撤销对"Streamlit"应用的访问权限。

1. 点击"**撤销**"。

   <div style={{ maxWidth: '75%', margin: 'auto' }}>
   <Image alt="撤销Streamlit访问你的GitHub账户的权限" src="/images/streamlit-community-cloud/GitHub-revoke.png" />
   </div>

1. 点击"**我了解，撤销访问**"。

  <div style={{ maxWidth: '50%', margin: 'auto' }}>
  <Image alt="确认撤销Streamlit对你的GitHub账户的访问权限" src="/images/streamlit-community-cloud/GitHub-revoke-confirm.png" />
  </div>

1. 返回<a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>并登录。你将被提示授权GitHub，如[连接GitHub](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access)中所述。

### 授予先前被拒绝的访问权限

如果组织所有者限制了Streamlit的访问或限制了所有OAuth应用，他们可能需要直接在GitHub中修改他们的权限。如果组织限制了Streamlit的访问，当你被提示使用GitHub账户授权时，组织旁边会出现红色X(<i style={{ verticalAlign: "-.25em", color: "#d1242f" }} className={{ class: "material-icons-sharp" }}>close</i>)。

<div style={{ maxWidth: '60%', margin: 'auto' }}>
<Image alt="Streamlit访问你的GitHub账户的拒绝授权" src="/images/streamlit-community-cloud/GitHub-auth-denied-XL.png" />
</div>

请参阅GitHub关于<a href="https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations" target="_blank">OAuth应用和组织</a>的文档。

## 重命名你的GitHub账户或仓库

Community Cloud通过GitHub坐标（所有者、仓库、分支、入口文件路径）识别应用。如果你重命名已从其部署应用的账户或仓库，你将失去管理应用的访问权限。要了解更多，请参阅[在GitHub中重命名你的应用](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)。
