---
title: 在 Streamlit Community Cloud 上升级您的应用的 Streamlit 版本
slug: /deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit
description: 了解如何使用依赖文件或重启您的应用在 Community Cloud 上升级您的 Streamlit 库版本。
keywords: upgrade streamlit, streamlit version, dependencies, requirements.txt, reboot, pin version, latest version, dependency file
---

# 在 Streamlit Community Cloud 上升级您的应用的 Streamlit 版本

想要使用一个很酷的新 Streamlit 功能，但您的应用在 Streamlit Community Cloud 上运行的是旧版本的 Streamlit 库？如果是这样，别担心！以下是如何升级您的应用的 Streamlit 版本，基于您如何管理您的[应用依赖项](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)：

## 没有依赖文件

当您的仓库中没有依赖文件时，您的应用将使用上次重启时存在的最新 Streamlit 版本。在这种情况下，只需[重启您的应用](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app)，Community Cloud 将安装最新版本。

如果您的应用依赖于特定版本的 Streamlit，您可能想要避免陷入这种情况。这就是为什么我们鼓励您使用依赖文件并固定您想要的 Streamlit 版本。

## 使用依赖文件

当您的应用包含依赖文件时，重启您的应用或按如下方式更改您的依赖文件：

- 如果 Streamlit 未包含在您的依赖文件中，如上所述重启应用。

  请注意，我们不推荐有不完整的依赖文件，因为 `pip` 在解析您的依赖项的兼容版本时无法包含 `streamlit`。

- 如果 Streamlit 包含在您的依赖文件中，但版本未固定或未限制，如上所述重启应用。

  当 Community Cloud 重启您的应用时，它将重新解析您的依赖文件。您的应用随后将拥有与您的依赖文件一致的所有依赖项的最新版本。

- 如果 Streamlit 包含在您的依赖文件中，并且版本已固定（例如，`streamlit==1.37.0`），更新您的依赖文件。

  当您在您的仓库中提交对依赖文件的更改时，Community Cloud 将检测更改并自动解析新依赖项。这就是您添加、删除或更改所有 Python 依赖项的一般方式。您不需要手动重启您的应用，但如果您想，可以这样做。
