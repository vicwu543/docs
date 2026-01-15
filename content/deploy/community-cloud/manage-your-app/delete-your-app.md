---
title: 删除您的应用
slug: /deploy/streamlit-community-cloud/manage-your-app/delete-your-app
description: 了解如何从 Community Cloud 删除您的 Streamlit 应用，并了解何时可能需要删除。
keywords: delete, remove, app, community cloud, confirmation, subdomain, reuse, data deletion
---

# 删除您的应用

如果您需要删除您的应用，它很简单且容易。有几种情况您可能需要删除您的应用：

- 您已经完成了示例应用的试用。
- 您想从私有仓库部署，但已经有一个私有应用。
- 您想为您的应用[更改 Python 版本](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)。
- 您想[重命名您的仓库](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app)或移动您的入口点文件。

如果您删除您的应用并打算立即重新部署，您的自定义子域应该立即可供重用。阅读更多关于[Streamlit 信任和安全](/deploy/streamlit-community-cloud/get-started/trust-and-security#data-deletion)中的数据删除。

您可以删除您的应用：

- [从您的工作区](#delete-your-app-from-your-workspace)。
- [从您的 Cloud 日志](#delete-your-app-from-your-cloud-logs)。

### 从您的工作区删除您的应用

1. 从您在 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 的工作区，单击您的应用旁边的溢出图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)。单击"**删除**"。

   ![从您的工作区删除您的应用](/images/streamlit-community-cloud/workspace-app-delete.png)

2. 将显示确认。输入所需的确认字符串并单击"**删除**"。

   <div style={{ maxWidth: '50%', margin: 'auto' }}>
   <Image alt="确认从 Streamlit Community Cloud 删除您的应用" src="/images/streamlit-community-cloud/workspace-app-delete-confirm.png" clean />
   </div>

### 从您的 Cloud 日志删除您的应用

1. 从您的应用 `<your-custom-subdomain>.streamlit.app`，单击右下角的"**管理应用**"。

   ![从您的应用访问 Streamlit Community Cloud 日志](/images/streamlit-community-cloud/cloud-logs-open.png)

2. 单击溢出菜单图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) 并单击"**删除应用**"。

   ![从您的 Cloud 日志删除您的应用](/images/streamlit-community-cloud/cloud-logs-menu-delete.png)

3. 将显示确认。输入所需的确认字符串并单击"**删除**"。

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="确认从 Streamlit Community Cloud 删除您的应用" src="/images/streamlit-community-cloud/workspace-app-delete-confirm.png" clean />
</div>
