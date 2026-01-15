---
title: 重命名或更改您的应用的 GitHub 坐标
slug: /deploy/streamlit-community-cloud/manage-your-app/rename-your-app
description: 了解如何安全地重命名您的 GitHub 仓库或更改应用坐标，而不会丢失对您的 Streamlit 应用的访问权限。
keywords: rename, github coordinates, repository, username, view-only access, delete, redeploy, access control, coordinates
---

# 重命名或更改您的应用的 GitHub 坐标

Streamlit Community Cloud 通过 GitHub 坐标（所有者、仓库、分支、入口点文件路径）识别应用。如果您在没有准备的情况下移动或重命名这些坐标之一，您将失去管理任何关联应用的访问权限。

## 删除、重命名、重新部署

如果您需要重命名您的仓库、移动您的入口点文件，或以其他方式更改已部署应用的 GitHub 坐标，请执行以下操作：

1. 删除您的应用。
1. 在 GitHub 中进行您想要的更改。
1. 重新部署您的应用。

## 当您已经更改了应用的 GitHub 坐标时重新获得访问权限

如果您更改了仓库，使得 Community Cloud 无法再在 GitHub 上找到您的应用，您的应用将丢失或显示为仅查看。仅查看意味着您无法编辑、重启、删除或查看应用的设置。您只能访问分析。

您可以通过以下方式重新获得控制权：

1. 恢复您对应用的更改，以便 Community Cloud 可以看到它期望的所有者、仓库、分支和入口点文件。
1. 退出 Community Cloud 和 GitHub。
1. 重新登录 Community Cloud 和 GitHub。
1. 如果您已重新获得访问权限，请删除您的应用。继续进行您的原始更改，并重新部署您的应用。

   如果这不能恢复对您的应用的访问权限，请[联系 Snowflake 支持](/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud)寻求帮助。他们可以删除您的断开连接的应用，以便您重新部署它们。为了获得最快的帮助，请按 URL 提供您的受影响应用的完整列表。
