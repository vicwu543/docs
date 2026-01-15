---
title: 在 Community Cloud 上升级您的应用的 Python 版本
slug: /deploy/streamlit-community-cloud/manage-your-app/upgrade-python
description: 了解如何通过删除和使用高级设置重新部署来在 Community Cloud 上升级您的 Streamlit 应用的 Python 版本。
keywords: upgrade python, python version, advanced settings, delete, redeploy, subdomain, secrets, github coordinates
---

# 在 Community Cloud 上升级您的应用的 Python 版本

Python 中的依赖项可以通过简单地更改您的环境配置文件（通常是 `requirements.txt`）来就地升级。但是，Python 本身在部署后无法更改。

当您部署应用时，您可以通过"**高级设置**"对话框选择 Python 的版本。在您部署应用后，您必须删除它并重新部署它来更改它使用的 Python 版本。

1. 记下您的应用设置：
   - 当前的自定义子域。
   - GitHub 坐标（仓库、分支和入口点文件路径）。
   - 秘密。

   当您删除应用时，其自定义子域立即可供重用。

1. [删除您的应用](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app)。
1. [部署您的应用](/deploy/streamlit-community-cloud/deploy-your-app)。
   1. 在部署页面上，选择您的应用的 GitHub 坐标。
   1. 将您的自定义域设置为与您的已删除实例匹配。
   1. 单击"**高级设置**"。
   1. 选择您想要的 Python 版本。
   1. 可选：如果您的应用有秘密，请重新输入它们。
   1. 单击"**保存**"。
   1. 单击"**部署**"。

在几分钟内，Community Cloud 将重定向您到您的重新部署的应用。
