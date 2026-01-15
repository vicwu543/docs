---
title: 重启您的应用
slug: /deploy/streamlit-community-cloud/manage-your-app/reboot-your-app
description: 了解如何在 Community Cloud 上重启您的 Streamlit 应用以清除内存、强制全新构建和解决问题。
keywords: reboot, restart, memory, fresh build, redeploy, workspace, cloud logs, confirmation, troubleshooting
---

# 重启您的应用

如果您需要清除您的应用的内存或在修改 Streamlit Community Cloud 不监控的文件后强制全新构建，您可能需要重启您的应用。这将中断任何当前可能正在使用您的应用的用户，并且您的应用重新部署可能需要几分钟时间。在重启期间，访问您的应用的任何人都会看到"您的应用正在烘焙中"。

在 Community Cloud 上重启您的应用很容易！您可以重启您的应用：

- [从您的工作区](#reboot-your-app-from-your-workspace)。
- [从您的 Cloud 日志](#reboot-your-app-from-your-cloud-logs)。

### 从您的工作区重启您的应用

1. 从您在 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 的工作区，单击您的应用旁边的溢出图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)。单击"**重启**"。

   ![从您的工作区重启您的应用](/images/streamlit-community-cloud/workspace-app-reboot.png)

2. 将显示确认。单击"**重启**"。

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="确认在 Streamlit Community Cloud 中重启您的应用" src="/images/streamlit-community-cloud/workspace-app-reboot-confirm.png" clean />
</div>

### 从您的 Cloud 日志重启您的应用

1. 从您的应用 `<your-custom-subdomain>.streamlit.app`，单击右下角的"**管理应用**"。

   ![从您的应用访问 Streamlit Community Cloud 日志](/images/streamlit-community-cloud/cloud-logs-open.png)

2. 单击溢出菜单图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) 并单击"**重启应用**"。

   ![从您的 Cloud 日志重启您的应用](/images/streamlit-community-cloud/cloud-logs-menu-reboot.png)

3. 将显示确认。单击"**重启**"。

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="确认在 Streamlit Community Cloud 中重启您的应用" src="/images/streamlit-community-cloud/workspace-app-reboot-confirm.png" clean />
</div>
