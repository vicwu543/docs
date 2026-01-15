---
title: 状态和限制
slug: /deploy/streamlit-community-cloud/status
description: 了解 Community Cloud 状态、限制、GitHub OAuth 范围、Python 环境、配置覆盖和 IP 地址。
keywords: status, limitations, github oauth, python environments, configuration, ip addresses, debian, linux, security
---

# Community Cloud 的状态和限制

## Community Cloud 状态

您可以在 [streamlitstatus.com](https://www.streamlitstatus.com/) 查看 Community Cloud 的当前状态。

## GitHub OAuth 范围

要部署您的应用，Streamlit 需要访问 GitHub 中的应用源代码以及管理与存储库关联的公钥的能力。默认的 GitHub OAuth 范围足以处理公开 GitHub 存储库中的应用。但是，要访问您的专有存储库，我们创建一个只读 [GitHub 部署密钥](https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys)，然后使用 SSH 密钥访问您的存储库。当我们创建此密钥时，GitHub 会以安全措施的形式通知存储库管理员创建。

Streamlit 需要来自 GitHub 的额外 `repo` OAuth 范围才能使用您的专有存储库并管理部署密钥。我们意识到 `repo` 范围为 Streamlit 提供了我们不真正需要的额外权限，作为重视安全的人，我们宁愿根本不被授予。这是创建 Community Cloud 时 GitHub 提供的权限模型。但是，我们正在采用新的 GitHub 权限模型来减少不必要的权限。

### 开发者权限

由于上述 OAuth 限制，开发者必须具有存储库的管理权限才能从中部署应用。

## 存储库文件结构

您可以从存储库部署多个应用，您的入口文件可能在目录结构的任何位置。但是，Community Cloud 从存储库的根目录初始化所有应用，即使入口文件在子目录中也是如此。这具有以下后果：

- Community Cloud 仅在存储库的根目录（每个分支）识别一个 `.streamlit/configuration.toml` 文件。
- 您必须声明 Streamlit 命令的图像、视频和音频文件路径相对于存储库的根目录。例如，`st.image`、`st.logo` 和 `st.set_page_config` 中的 `page_icon` 参数期望文件位置相对于您的工作目录（即执行 `streamlit run` 的位置）。

## Linux 环境

Community Cloud 建立在 Debian Linux 上。

- Community Cloud 使用 Debian 11（"bullseye"）。要浏览可安装的可用包，请参阅 [包列表](https://packages.debian.org/bullseye/)。
- 所有文件路径必须使用正斜杠路径分隔符。

## Python 环境

- 您不能为单个应用混合和匹配 Python 包管理器。Community Cloud 根据它找到的第一个环境配置文件配置应用的 Python 环境。有关更多信息，请参阅 [其他 Python 包管理器](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#other-python-package-managers)。
- 我们建议您使用最新版本的 Streamlit 以确保完整的 Community Cloud 功能。规划您的环境时，请务必注意 Streamlit 对包兼容性的 [当前要求](https://github.com/streamlit/streamlit/blob/develop/lib/setup.py)，特别是 `protobuf>=3.20,<6`。
- 如果您固定 `streamlit< 1.20.0`，您还必须固定 `altair<5`。早期版本的 Streamlit 没有正确限制 Altair 的版本。在 Community Cloud 上运行的解决方案脚本将在检测到较新版本时强制安装 `altair<5`。这可能会无意中升级 Altair 的依赖项，违反您的环境配置。较新的 Streamlit 版本支持 Altair 版本 5。
- Community Cloud 仅支持仍在接收安全更新的已发布 Python 版本。您可能不会使用生命周期终止、预发布或功能版本的 Python。有关更多信息，请参阅 [Python 版本状态](https://devguide.python.org/versions/)。

## 配置

以下配置选项在 Community Cloud 中设置，并将覆盖 `config.toml` 文件中的任何相反设置：

```toml
[client]
showErrorDetails = false

[runner]
fastReruns = true

[server]
runOnSave = true
enableXsrfProtection = true

[browser]
gatherUsageStats = true
```

## IP 地址

如果您需要将 IP 地址列入白名单以建立连接，Community Cloud 目前由以下 IP 地址提供服务：

<Warning>

    这些 IP 地址可能随时更改，恕不另行通知。

</Warning>

<Flex wrap >
    <div style={{ width: "150px" }}>35.230.127.150</div>
    <div style={{ width: "150px" }}>35.203.151.101</div>
    <div style={{ width: "150px" }}>34.19.100.134</div>
    <div style={{ width: "150px" }}>34.83.176.217</div>
    <div style={{ width: "150px" }}>35.230.58.211</div>
    <div style={{ width: "150px" }}>35.203.187.165</div>
    <div style={{ width: "150px" }}>35.185.209.55</div>
    <div style={{ width: "150px" }}>34.127.88.74</div>
    <div style={{ width: "150px" }}>34.127.0.121</div>
    <div style={{ width: "150px" }}>35.230.78.192</div>
    <div style={{ width: "150px" }}>35.247.110.67</div>
    <div style={{ width: "150px" }}>35.197.92.111</div>
    <div style={{ width: "150px" }}>34.168.247.159</div>
    <div style={{ width: "150px" }}>35.230.56.30</div>
    <div style={{ width: "150px" }}>34.127.33.101</div>
    <div style={{ width: "150px" }}>35.227.190.87</div>
    <div style={{ width: "150px" }}>35.199.156.97</div>
    <div style={{ width: "150px" }}>34.82.135.155</div>
</Flex>

## 其他限制

- 当您在云日志中打印内容时，您可能需要在其显示之前执行 `sys.stdout.flush()`。
- Community Cloud 在美国托管所有应用。这目前不可配置。
- Community Cloud 将 GitHub 中的应用更新速率限制为每分钟最多五个。
