---
title: 管理您的应用
slug: /deploy/streamlit-community-cloud/manage-your-app
description: 了解如何在 Community Cloud 上管理您的已部署 Streamlit 应用，包括编辑、分析、设置和资源优化。
keywords: manage, app, analytics, settings, edit, reboot, delete, resources, optimization, workspace
---

# Manage your app

You can manage your deployed app from your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> or directly from `<your-custom-subdomain>.streamlit.app`. You can view, deploy, delete, reboot, or favorite an app.

## Manage your app from your workspace

Streamlit Community Cloud is organized into workspaces, which automatically group your apps according to their repository's owner in GitHub. Your workspace is indicated in the upper-left corner. For more information, see [Switching workspaces](/deploy/streamlit-community-cloud/get-started/explore-your-workspace#switching-workspaces).

To deploy or manage any app, always switch to the workspace matching the repository's owner first.

### 排序您的应用

如果您的工作区中有许多应用，可以通过将应用标记为收藏 (<i style={{ verticalAlign: "-.25em", color: "#faca2b" }} className={{ class: "material-icons-sharp" }}>star</i>) 来将应用固定到顶部。有关更多信息，请参阅[收藏您的应用](/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app)。

### 应用溢出菜单

每个应用都有一个菜单，可从右侧的溢出图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) 访问。

- **使用 Codespaces 编辑** &mdash; 请参阅[使用 GitHub Codespaces 编辑您的应用](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app#edit-your-app-with-github-codespaces)
- **重启** &mdash; 请参阅[重启您的应用](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)
- **删除** &mdash; 请参阅[删除您的应用](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)
- **分析** &mdash; 请参阅[应用分析](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)
- **设置** &mdash; 请参阅[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)

![您的工作区中的应用溢出菜单](/images/streamlit-community-cloud/workspace-app-overflow.png)

如果您对某个应用具有仅查看权限，则应用菜单中的所有选项都将被禁用，除了分析。

![您的工作区中的仅查看应用溢出菜单](/images/streamlit-community-cloud/workspace-view-only.png)

## 直接从应用管理您的应用

您可以直接从应用本身管理已部署的应用！只需确保您已登录到 Community Cloud，然后访问您的应用。

### 云日志

1. 从您的应用 `<your-custom-subdomain>.streamlit.app`，单击右下角的"**管理应用**"。

   ![从应用右下角的"管理应用"访问云日志](/images/streamlit-community-cloud/cloud-logs-open.png)

2. 单击"**管理应用**"后，您将能够查看应用的日志。这是您排查应用问题的主要位置。

   ![Streamlit Community Cloud 日志](/images/streamlit-community-cloud/cloud-logs.png)

3. 您可以通过单击云日志底部的溢出图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) 来访问更多开发者选项。要方便地下载日志，请单击"**下载日志**"。

   ![下载您的 Streamlit Community Cloud 日志](/images/streamlit-community-cloud/cloud-logs-menu-download.png)

<Flex>

<div>

从云日志访问的其他选项包括：

- **分析** &mdash; 请参阅 [应用分析](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)。
- **重启应用** &mdash; 请参阅 [重启您的应用](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)。
- **删除应用** &mdash; 请参阅 [删除您的应用](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)。
- **设置** &mdash; 请参阅 [应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)。
- **您的应用** &mdash; 带您前往您的 [应用工作区](#manage-your-app-from-your-workspace)。
- **文档** &mdash; 带您前往我们的文档。
- **支持** &mdash; 带您前往 <a href="https://discuss.streamlit.io/" target="_blank">我们的论坛</a>！

</div>

<div style={{ maxWidth: '30%', margin: "auto" }}>
    <Image src="/images/streamlit-community-cloud/cloud-logs-menu-XL.png" clean />
</div>

</Flex>

### 应用界面

从 `<your-custom-subdomain>.streamlit.app` 的应用，您始终可以访问 [应用界面](/develop/concepts/architecture/app-chrome)，就像在本地开发时一样。部署应用的选项已被删除，但您仍然可以从这里清除缓存。

![Streamlit Community Cloud 中的应用菜单](/images/streamlit-community-cloud/app-menu.png)

## 在 GitHub 中管理您的应用

### 更新您的应用

您的 GitHub 存储库是应用的源，这意味着每当您将更新推送到存储库时，您将看到应用中的更改几乎实时反映。试试看！

Streamlit 还会聪明地检测您是否修改了依赖项，在这种情况下，它将自动为您进行完整重新部署，这将花费更多时间。但由于大多数更新不涉及依赖项更改，您通常应该看到应用实时更新。

### 添加或删除依赖项

要随时添加或删除依赖项，只需更新 `requirements.txt`（Python 依赖项）或 `packages.txt`（Linux 依赖项），然后将更改提交到 GitHub 上的存储库。Community Cloud 检测到您的依赖项中的更改，并自动触发（重新）安装。

最好的做法是在 `requirements.txt` 中固定您的 Streamlit 版本。否则，版本可能在您不知情的情况下随时自动升级，这可能导致不期望的结果（例如，当我们在 Streamlit 中弃用功能时）。

## 应用资源和限制

### 资源限制

所有 Community Cloud 用户都可以访问相同的资源，并受相同限制的约束。这些限制可能随时更改，恕不另行通知。如果您的应用达到或超过其限制，它可能会因限流而变慢或无法正常运行。截至 2024 年 2 月，限制大约如下：

- CPU：最小 0.078 核，最大 2 核
- 内存：最小 690MB，最大 2.7GB
- 存储：无最小值，最大 50GB

应用资源不足的症状包括以下几项：

- 您的应用运行缓慢。
- 您的应用显示"🤯 此应用已超过其资源限制"。
- 您的应用显示"😦 哎呀"。

### 对世界有益

Streamlit 为具有对世界有益的用例的应用提供增加的资源。通常，这些应用由教育机构或非营利组织使用、属于开源项目的一部分，或以某种方式造福世界。如果您的应用 **不是** 主要由营利公司使用，您可以 [申请增加资源](https://info.snowflake.com/streamlit-resource-increase-request.html)。

### 优化您的应用

如果您的应用运行缓慢或显示上述错误页面，我们首先强烈建议您通读以下博客文章中的建议并加以实施，以防止您的应用达到资源限制，并检测您的 Streamlit 应用是否存在内存泄漏：

- <a href="https://blog.streamlit.io/common-app-problems-resource-limits/" target="_blank">常见应用问题：资源限制</a>
- <a href="https://blog.streamlit.io/3-steps-to-fix-app-memory-leaks/" target="_blank">修复应用内存泄漏的 3 个步骤</a>

如果您的应用超过其资源限制，开发人员和查看者都会看到"😦 哎呀"。

<div style={{ maxWidth: '70%', margin: 'auto' }}>
<Image alt="应用状态：哎呀。运行应用时出错。" src="/images/streamlit-community-cloud/app-state-oh-no.png" />
</div>

如果查看应用时看到"😦 哎呀"，首先检查云日志以查找任何特定错误。如果云日志中没有错误，您可能正在处理资源问题。

#### 开发者视图

如果您以超过限制的应用的开发者账户身份登录，您可以从应用右下角访问"**管理应用**"以重新启动应用并清除其内存。"**管理应用**"将显示为红色并带有警告图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>error</i>)。

![开发者视图：哎呀。运行应用时出错。](/images/streamlit-community-cloud/app-state-oh-no-developer.png)

### 应用休眠

12 小时无流量的所有应用都会进入休眠。Community Cloud 将应用置于休眠状态以节省资源并允许平台的最佳共享使用。要保持应用保持活跃，只需访问您的应用。

当有人访问处于睡眠状态的应用时，他们将看到睡眠页面：

<div style={{ maxWidth: '80%', margin: 'auto' }}>
<Image alt="应用状态：Zzzz。此应用由于不活动而进入睡眠。" src="/images/streamlit-community-cloud/app-state-zzzz.png" />
</div>

要唤醒应用，请单击"**是的，让此应用重新启动！**"这可以由 *任何* 可以查看应用的人完成，而不仅仅是应用开发者！

您可以从工作区查看哪些应用处于睡眠状态。睡眠应用右侧有一个月亮图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>bedtime</i>)。

![应用状态：Zzzz。此应用由于不活动而进入睡眠](/images/streamlit-community-cloud/workspace-sleeping-app.png)
