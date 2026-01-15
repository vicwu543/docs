---
title: 应用设置
slug: /deploy/streamlit-community-cloud/manage-your-app/app-settings
description: 了解如何配置您的 Streamlit 应用设置，包括 URL 自定义、共享权限和秘密管理。
keywords: settings, url, subdomain, sharing, permissions, secrets, configuration, customize, manage
---

# 应用设置

此页面关于 Streamlit Community Cloud 上的应用设置。从您的应用设置中，您可以[查看或更改您的应用的 URL](/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-change-your-apps-url)，管理[对您的应用的公共或私有访问](/deploy/streamlit-community-cloud/share-your-app)，并更新您的应用的已保存[秘密](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)。

如果您从运行应用的右上角的[应用 chrome](/develop/concepts/architecture/app-chrome) 访问"**设置**"，您可以访问控制应用运行时外观的功能。

## 访问您的应用设置

您可以通过以下方式访问您的应用设置：

- [从您的工作区](#access-app-settings-from-your-workspace)。
- [从您的 Cloud 日志](#access-app-settings-from-your-cloud-logs)。

### 从您的工作区访问应用设置

从您在 <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> 的工作区，单击您的应用旁边的溢出图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)。单击"**设置**"。

![从您的工作区访问应用设置](/images/streamlit-community-cloud/workspace-app-settings.png)

### 从您的 Cloud 日志访问应用设置

从您的应用 `<your-custom-subdomain>.streamlit.app`，单击右下角的"**管理应用**"。

![从您的应用访问 Streamlit Community Cloud 日志](/images/streamlit-community-cloud/cloud-logs-open.png)

单击溢出菜单图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) 并单击"**设置**"。

![从您的 Cloud 日志访问应用设置](/images/streamlit-community-cloud/cloud-logs-menu-settings.png)

## 更改您的应用设置

### 查看或更改您的应用的 URL

要从仪表板查看或自定义您的应用子域：

1. 如上所述访问您的应用设置。
1. 在"应用设置"对话框的"**常规**"选项卡中，在"应用 URL"字段中查看您的应用的唯一子域。

   ![Streamlit Community Cloud 上的常规应用设置：自定义子域](/images/streamlit-community-cloud/workspace-app-settings-general.png)

1. 可选：输入一个新的自定义子域，长度在 6 到 63 个字符之间，然后单击"**保存**"。

   ![您的应用的新自定义子域](/images/streamlit-community-cloud/workspace-app-settings-general-valid-domain.png)

   如果自定义子域不可用（例如，因为它已被占用或包含受限词），您将看到错误消息。按照指示更改您的子域。

   ![您的应用的无效自定义子域](/images/streamlit-community-cloud/workspace-app-settings-general-invalid-domain.png)

### 更新您的应用的共享设置

了解如何[共享您的应用](/deploy/streamlit-community-cloud/share-your-app)。

![Streamlit Community Cloud 上的共享设置](/images/streamlit-community-cloud/workspace-app-settings-sharing.png)

### 查看或更新您的秘密

1. 如上所述访问您的应用设置。
1. 在"应用设置"对话框的"**秘密**"选项卡中，在"秘密"字段中查看您的应用的秘密。

   ![Streamlit Community Cloud 上的秘密应用设置](/images/streamlit-community-cloud/workspace-app-settings-secrets.png)

1. 可选：添加、编辑或删除您的秘密，然后单击"**保存**"。

了解更多关于[您的 Community Cloud 应用的秘密管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)。
