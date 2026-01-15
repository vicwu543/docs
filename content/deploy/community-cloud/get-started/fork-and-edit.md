---
title: Fork和编辑公共应用
slug: /deploy/streamlit-community-cloud/get-started/fork-and-edit-a-public-app
description: 了解如何从Community Cloud中fork和编辑公共Streamlit应用，使用GitHub Codespaces进行即时开发。
keywords: fork, 公共应用, 编辑, github codespaces, 开发, 仓库, 子域, 自定义
---

# Fork和编辑公共应用

Community Cloud就是关于学习、分享和探索Streamlit世界。对于具有公共仓库的应用，你可以快速fork副本到你的GitHub账户、部署你自己的版本并跳入GitHub上的codespace以开始编辑和探索Streamlit代码。

1. 从可fork的应用，在右上角点击"**Fork**"。

   ![在公共应用的右上角点击Fork](/images/streamlit-community-cloud/fork-public-hello.png)

1. 可选：在"应用URL"字段中，为你的应用选择自定义子域。

   每个Community Cloud应用都部署到`streamlit.app`上的子域，但你可以随时更改应用的子域。有关更多信息，请参阅[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)。

1. 点击"**Fork!**"

   仓库将被fork到你的GitHub账户。如果你已经fork了仓库，Community Cloud将使用现有的fork。如果你现有的fork已经有关联的codespace，codespace将被重用。

   <Warning>
      在以下情况下不要使用此方法：
      - 你有与fork名称匹配的现有仓库（但不是此应用的fork）。
      - 你有此应用的现有fork，但你已更改仓库的名称。

   如果你有此应用的现有fork并保持了原始仓库名称，Community Cloud将使用你现有的fork。如果你之前部署了应用并打开了codespace，Community Cloud将打开你现有的codespace。
   </Warning>

   ![点击Fork以确认和部署你的应用](/images/streamlit-community-cloud/fork-public-hello-deploy.png)

1. 等待GitHub设置你的codespace。

   完全初始化你的codespace可能需要几分钟。在Visual Studio Code编辑器出现在你的codespace中后，安装Python并启动Streamlit服务器可能需要几分钟。完成后，分割屏幕视图在左侧显示代码编辑器，在右侧显示运行应用。代码编辑器默认打开两个选项卡：仓库的readme文件和应用的入口文件。

   ![点击Fork以确认和部署你的应用](/images/streamlit-community-cloud/fork-public-hello-codespace.png)

   <Important>
      你的codespace中显示的应用不是你在Community Cloud上部署的同一个实例。你的codespace是一个独立的开发环境。当你在codespace内进行编辑时，这些编辑在你提交到仓库之前不会离开codespace。当你提交更改到仓库时，Community Cloud检测更改并更新你部署的应用。要了解更多，请参阅[编辑你的应用](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app)。
   </Important>

1. 根据需要编辑你新fork的应用。有关使用GitHub Codespaces的更多说明，请参阅[编辑你的应用](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app)。
