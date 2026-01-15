---
title: 使用配置选项
slug: /develop/concepts/configuration/options
description: 了解配置选项，包括 config.toml 文件、环境变量、命令行标志和运行时配置管理。
keywords: configuration options, config.toml, environment variables, command line flags, streamlit config, app configuration, runtime settings, configuration precedence
---

# 使用配置选项

Streamlit 提供了四种不同的方式来设置配置选项。此列表按优先级逆序排列，即当多次提供相同配置选项时，命令行标志优先于环境变量。

<Note>

如果在应用运行时更改 `.streamlit/config.toml` 中的主题设置，这些更改将立即反映。如果在应用运行时更改 `.streamlit/config.toml` 中的非主题设置，则需要重启服务器才能在应用中反映更改。

</Note>

1. 在**全局配置文件**中，位于 `~/.streamlit/config.toml`（macOS/Linux）或 `%userprofile%/.streamlit/config.toml`（Windows）：

   ```toml
   [server]
   port = 80
   ```

2. 在**每个项目的配置文件**中，位于 `$CWD/.streamlit/config.toml`，
   其中 `$CWD` 是您运行 Streamlit 的文件夹。

3. 通过 `STREAMLIT_*` **环境变量**，例如：

   ```bash
   export STREAMLIT_SERVER_PORT=80
   export STREAMLIT_SERVER_COOKIE_SECRET=dontforgottochangeme
   ```

4. 在运行 `streamlit run` 时作为**命令行标志**：

   ```bash
   streamlit run your_script.py --server.port 80
   ```

## 可用选项

所有可用的配置选项都记录在 [`config.toml`](/develop/api-reference/configuration/config.toml) 中。这些选项可以在 TOML 文件中声明，作为环境变量，或作为命令行选项。

当使用环境变量覆盖 `config.toml` 时，将变量（包括其节标题）转换为大写蛇形格式并添加 `STREAMLIT_` 前缀。例如，`STREAMLIT_CLIENT_SHOW_ERROR_DETAILS` 等同于 TOML 中的以下内容：

```toml
[client]
showErrorDetails = true
```

当使用命令行选项覆盖 `config.toml` 和环境变量时，使用与 TOML 文件中相同的大小写，并将节标题作为点分隔的前缀。例如，命令行选项 `--server.enableStaticServing true` 等同于以下内容：

```toml
[server]
enableStaticServing = true
```

## 遥测

如安装过程中所述，Streamlit 收集使用统计信息。您可以通过阅读我们的[隐私声明](https://streamlit.io/privacy-policy)了解更多，但简要说明是，虽然我们收集遥测数据，但我们无法查看也不存储 Streamlit 应用中包含的信息。

如果您希望退出使用统计信息收集，请在配置文件中添加以下内容：

```toml
[browser]
gatherUsageStats = false
```

## 主题

您可以使用配置系统的 `[theme]` 部分更改应用的基本颜色。
要了解更多信息，请参见[主题](/develop/concepts/configuration/theming)。

## 查看所有配置选项

如[命令行选项](/develop/api-reference/cli)中所述，您可以使用以下命令查看所有可用的配置选项：

```bash
streamlit config show
```