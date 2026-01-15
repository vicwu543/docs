---
title: 应用分析
slug: /deploy/streamlit-community-cloud/manage-your-app/app-analytics
description: 了解如何查看和分析Streamlit应用的观众数据，包括总观众数、唯一访客和隐私考虑。
keywords: 分析, 观众, 观众数, 数据, 隐私, 公开, 私有, 匿名, 追踪, 指标
---

# 应用分析

Streamlit Community Cloud允许你看到每个应用的观众数。具体来说，你可以看到：

- 应用的总观众数（从2022年4月计算）。
- 最近的唯一观众（限制为最后20个观众）。
- 每个唯一观众最后访问的相对时间戳。

![Streamlit Community Cloud上的应用分析](/images/streamlit-community-cloud/workspace-app-analytics-viewers.png)

## 访问应用分析

你可以通过以下方式访问应用的分析：

- [从工作空间](#access-app-analytics-from-your-workspace)。
- [从Cloud日志](#access-app-analytics-from-your-cloud-logs)。

### 从工作空间访问应用分析

从<a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>的工作空间，点击应用旁边的溢出图标(<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)。点击"**分析**"。

![通过应用溢出菜单从工作空间访问应用分析](/images/streamlit-community-cloud/workspace-app-analytics.png)

### 从Cloud日志访问应用分析

从`<your-custom-subdomain>.streamlit.app`的应用，在右下角点击"**管理应用**"。

![从应用访问Streamlit Community Cloud日志](/images/streamlit-community-cloud/cloud-logs-open.png)

点击溢出菜单图标(<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>)并点击"**分析**"。

![从Cloud日志访问应用分析](/images/streamlit-community-cloud/cloud-logs-menu-analytics.png)

## 应用观众

对于公开应用，我们匿名化工作空间外的所有观众以保护其隐私，并将匿名观众显示为随机假名。你仍然能够看到工作空间中的同事的身份，包括你邀请的任何观众（一旦他们接受）。

<Important>

当你邀请观众到应用时，他们也获得分析访问权限。此外，如果有人被邀请作为工作空间中_任何_应用的观众，他们可以看到工作空间中所有公开应用的分析，并可以邀请额外的观众。工作空间中的观众可能通过分析看到工作空间中开发者和其他观众的电子邮件。

</Important>

同时，对于私有应用，你控制谁有访问权限，你将能够看到最近查看应用的特定用户。

此外，你偶尔可能在私有应用中看到匿名用户。放心，这些匿名用户_确实_有你或工作空间成员授予的授权查看访问权限。

用户显示为匿名的常见原因是：

- 应用之前是公开的。
- 给定的观众在2022年4月查看了应用，当时Streamlit团队正在为此功能改进用户识别。

请参阅Streamlit的通用<a href="https://streamlit.io/privacy-policy" target="_blank">隐私通知</a>。
