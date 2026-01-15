---
title: 从模板部署应用
slug: /deploy/streamlit-community-cloud/get-started/deploy-from-a-template
description: 了解如何使用Community Cloud的模板选择器与GitHub Codespaces集成从模板部署Streamlit应用。
keywords: 模板, 部署, fork, github codespaces, 模板选择器, gdp仪表板, python版本, 子域
---

# 从模板部署应用

Streamlit Community Cloud让你用几个便捷的模板轻松入门。只需选择一个模板，Community Cloud就会将其fork到你的账户并部署它。你推送到新fork的任何编辑都会立即显示在部署的应用中。此外，如果你不想使用本地开发环境，Community Cloud让你轻松创建一个为Streamlit应用开发完全配置的GitHub codespace。

## 访问模板选择器

开始部署模板有两种方式："**创建应用**"按钮和工作空间底部的模板库。

- 如果你点击"**创建应用**"按钮，Community Cloud会问你"你已经有应用吗？"选择"**否，从模板创建一个**"。
- 如果你滚动到工作空间底部的"**我的应用**"部分，你可以看到最受欢迎的模板。直接点击一个，或选择"**查看所有模板**"。

模板选择器在左侧显示可用模板列表。当前选定模板的预览显示在右侧。

![Community Cloud上的"从模板部署"页面](/images/streamlit-community-cloud/deploy-template-picker.png)

## 选择模板

1. 从左侧的模板列表中，选择"**GDP仪表板**"。
1. 可选：对于"新GitHub仓库的名称"，输入新fork仓库的名称。

   当你从模板部署时，Community Cloud会将模板仓库fork到你的GitHub账户。Community Cloud根据选定的模板为此仓库选择默认名称。如果你之前使用默认名称部署了相同的模板，Community Cloud会将自动递增的数字附加到名称。

   <Note>
       即使你有另一个用户或组织的工作空间已选中，Community Cloud也始终会从你的个人工作空间部署模板应用。也就是说，Community Cloud始终会将模板fork到你的GitHub用户账户。如果你想从组织部署模板应用，在GitHub中手动fork模板，并在关联的工作空间中从你的fork部署它。
   </Note>

1. 可选：在"应用URL"字段中，为新应用选择子域。

   每个Community Cloud应用都部署到`streamlit.app`上的子域，但你可以随时更改应用的子域。有关更多信息，请参阅[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)。

1. 可选：要立即在GitHub codespace中编辑模板，选择"**打开GitHub Codespaces...**"的选项。

   你可以在任何时候为应用创建codespace。要了解如何在部署应用后创建codespace，请参阅[编辑你的应用](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app)。

1. 可选：要更改Python版本，在屏幕底部点击"**高级设置**"，选择Python版本，然后点击"**保存**"。

   <Important>
       部署应用后，在不删除和重新部署应用的情况下，你无法更改Python版本。
   </Important>

1. 在底部点击"**部署**"。

## 查看你的应用

- 如果你没有选择打开GitHub Codespaces的选项，你会被重定向到你的新应用。

  ![GDP仪表板模板应用](/images/streamlit-community-cloud/deploy-template-GDP.png)

- 如果你选择了打开GitHub Codespaces的选项，你会被重定向到新的codespace，完全初始化可能需要几分钟。在Visual Studio Code编辑器出现在你的codespace中后，安装Python并启动Streamlit服务器可能需要几分钟。完成后，分割屏幕视图在左侧显示代码编辑器，在右侧显示运行应用。代码编辑器默认打开两个选项卡：仓库的readme文件和应用的入口文件。

  ![codespace中的GDP仪表板模板应用](/images/streamlit-community-cloud/deploy-template-GDP-codespace.png)

<Important>
    你的codespace中显示的应用不是你在Community Cloud上部署的同一个实例。你的codespace是一个独立的开发环境。当你在codespace内进行编辑时，这些编辑在你提交到仓库之前不会离开codespace。当你提交更改到仓库时，Community Cloud检测更改并更新你部署的应用。要了解更多，请参阅[编辑你的应用](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app)。
</Important>
