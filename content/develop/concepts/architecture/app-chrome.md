---
title: 应用 chrome
slug: /develop/concepts/architecture/app-chrome
description: 了解 Streamlit 的应用 chrome，包括状态区域、工具栏和可配置的应用菜单，具有开发者选项和部署功能。
keywords: 应用 chrome, streamlit chrome, 应用菜单, 状态区域, 工具栏, 开发者选项, 应用界面, streamlit ui, 应用导航, 部署菜单
---

# 应用 chrome

你的 Streamlit 应用在右上角有一些小部件，可以在你开发时帮助你。这些小部件也可以在你的观看者使用你的应用时帮助他们。我们称这些东西为"应用 chrome"。chrome 包括一个状态区域、工具栏和应用菜单。

你的应用菜单是可配置的。默认情况下，当在本地查看应用或在 Streamlit Community Cloud 上查看并以具有管理员访问权限的帐户登录时，你可以从应用菜单访问开发者选项。查看应用时，点击右上角的图标来访问菜单。

![应用菜单](/images/app-menu/app-menu-developer.png)

## 菜单选项

菜单分为两个部分。上部分包含对所有观看者都可用的选项，下部分包含开发者的选项。在此页面的末尾了解有关[自定义此菜单](#customize-the-menu)的更多信息。

### 重新运行

你可以通过从应用菜单中点击"**重新运行**"来手动触发应用的重新运行。此重新运行不会重置你的会话。你的小部件状态和存储在 [`st.session_state`](/develop/concepts/architecture/session-state) 中的值将被保留。作为快捷方式，不打开应用菜单，你可以通过按键盘上的"**R**"来重新运行你的应用（如果你当前未专注于输入元素）。

### 设置

使用"**设置**"选项，你可以控制应用运行时的外观。如果在本地查看应用，你可以设置应用如何响应源代码的更改。请参阅[基本概念](/get-started/fundamentals/main-concepts#development-flow)中有关开发流的更多信息。你也可以强制你的应用以宽模式显示，即使未在使用 [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) 的脚本中设置。

#### 主题设置

从应用菜单中点击"**设置**"后，你可以为应用的基础主题选择"**浅色**"、"**深色**"或"**使用系统设置**"。点击"**编辑活动主题**"来逐个修改主题颜色。

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-settings-modal.png" alt="Settings" clean />
</div>

<br />

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-settings-theme.png" alt="Theme" clean />
</div>

### 打印

点击"**打印**"或使用键盘快捷键（`⌘+P` 或 `Ctrl+P`）打开打印对话框。此选项使用你浏览器的内置打印为 PDF 功能。要修改打印的外观，你可以执行以下操作：

- 在打印前展开或折叠侧边栏，分别将其包括或排除在打印中。
- 通过点击和拖动其右边框，在你的应用中调整侧边栏的大小以实现你想要的宽度。
- 如果在深色模式下打印，你可能需要在打印对话框中启用"**背景图形**"。
- 你可能需要在[设置](#settings)中禁用宽模式或调整打印缩放以防止元素裁剪出页面。

### 录制截屏

你可以直接从应用中轻松录制屏幕！最新版本的 Chrome、Edge 和 Firefox 支持屏幕录制。确保你的浏览器是最新的以兼容。根据你的当前设置，你可能需要授予浏览器权限来录制你的屏幕或使用你的麦克风来录制旁白。

1. 查看你的应用时，从右上角打开应用菜单。
2. 点击"**录制截屏**"。
3. 如果你想通过麦克风录制音频，请检查"**也录制音频**"。
4. 点击"**开始录制**"。（你的操作系统可能会提示你的浏览器来录制你的屏幕或使用你的麦克风。）

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-2.png" alt="Record" />
</div>

5. 从列出的选项中选择要录制的选项卡、窗口或监视器。界面将根据你的浏览器而有所不同。

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-3.png" alt="Record" />
</div>

6. 点击"**分享**"。

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-4.png" alt="Record" />
</div>

7. 录制时，你会在应用的标签页和应用菜单图标上看到红色圆圈。如果你想取消录制，请在应用的底部点击"**停止分享**"。

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-5.png" alt="Record" />
</div>

8. 完成录制后，在键盘上按"**Esc**"或从你的应用菜单中点击"**停止录制**"。

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-6.png" alt="Record" />
</div>

9. 按照你浏览器的说明保存你的录制。你保存的录制将在你的浏览器保存下载的地方。

整个过程如下所示：

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record.gif" alt="Record" />
</div>

### 关于

你可以方便地从"**关于**"选项中检查正在运行的 Streamlit 版本。开发者也可以选择使用 [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) 自定义此处显示的消息。

## 开发者选项

默认情况下，开发者选项仅在本地查看应用时或在 Streamlit Community Cloud 应用上查看时以管理员权限登录时显示。如果你想为所有用户提供这些选项，你可以[自定义菜单](#customize-the-menu)。

### 清除缓存

通过从应用的菜单中点击"**清除缓存**"或在不专注于输入元素时在键盘上按"**C**"来重置应用的缓存。这将删除 [`@st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) 和 [`@st.cache_resource`](/develop/api-reference/caching-and-state/st.cache_resource) 的所有缓存条目。

### 部署此应用

如果你在 git 仓库中本地运行应用，你可以通过几次简单点击将应用部署到 Streamlit Community Cloud！在开始之前，请确保你的工作已推送到在线 GitHub 仓库。为了获得最大的便利，请确保你已经创建了[社区云帐户](/deploy/streamlit-community-cloud/get-started/create-your-account)并已登录。

1. 点击应用菜单图标（<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>）旁边的"**部署**"。

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-deploy.png" alt="Settings" />
</div>

2. 点击"**立即部署**"。

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-deploy-1.png" alt="Settings" />
</div>

3. 你将被带到 Community Cloud 的"部署应用"页面。你的应用的仓库、分支和文件名将被预填充以匹配你的当前应用！了解更多关于在 Streamlit Community Cloud 上[部署应用](/deploy/streamlit-community-cloud/deploy-your-app)的信息。

整个过程如下所示：

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/deploy-from-local.gif" alt="Settings" />
</div>

## 自定义菜单

使用你应用的[配置](/develop/concepts/configuration)中的 `client.toolbarMode`，你可以使应用菜单以以下方式显示：

- `"developer"` &mdash; 向所有观看者显示开发者选项。
- `"viewer"` &mdash; 隐藏所有观看者的开发者选项。
- `"minimal"` &mdash; 仅显示在外部设置的那些选项。这些选项可以通过 [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) 声明或通过 Streamlit Community Cloud 填充。
- `"auto"` &mdash; 这是默认设置，当通过 localhost 访问或通过 Streamlit Community Cloud 访问应用的管理员帐户登录时，将显示开发者选项。否则，开发者选项将不显示。
