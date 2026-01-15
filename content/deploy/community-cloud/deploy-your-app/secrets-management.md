---
title: Community Cloud应用的秘密管理
slug: /deploy/streamlit-community-cloud/deploy-your-app/secrets-management
description: 了解如何使用秘密管理界面为Community Cloud应用安全地管理秘密、凭证和API密钥。
keywords: 秘密, 凭证, api密钥, 安全, st.secrets, secrets.toml, 环境变量, 高级设置
---

# Community Cloud应用的秘密管理

## 介绍

如果你正在[连接到数据源](/develop/tutorials/databases)，你可能需要处理凭证或秘密。在git仓库中存储未加密的秘密是不好的做法。如果你的应用需要访问敏感的凭证，推荐的解决方案是将这些凭证存储在不提交到仓库的文件中，并将其作为环境变量传递。

## 如何使用秘密管理

Community Cloud允许你在应用的设置中保存秘密。在本地开发时，你可以在代码中使用`st.secrets`从`.streamlit/secrets.toml`文件读取秘密。但是，此`secrets.toml`文件永远不应该提交到仓库。相反，当你部署应用时，你可以将`secrets.toml`文件的内容粘贴到"**高级设置**"对话框中。你可以通过工作空间中应用的设置随时更新秘密。

### 先决条件

- 你应该了解如何使用`st.secrets`和`secrets.toml`。请参阅[秘密管理](/develop/concepts/connections/secrets-management)。

### 高级设置

在部署应用时，你可以访问"**高级设置**"来设置你的秘密。部署应用后，你可以通过应用的设置查看或更新秘密。完整的部署工作流程在下一页中描述，但"**高级设置**"对话框看起来像这样：

<div style={{ maxWidth: '70%', margin: 'auto' }}>
<Image alt="部署你的应用的高级设置" src="/images/streamlit-community-cloud/deploy-an-app-advanced.png" />
</div>

只需将本地`secrets.toml`文件的内容复制并粘贴到对话框内的"秘密"字段中。在你点击"**保存**"以提交更改后，就完成了！

### 编辑你的应用秘密

如果你需要为已经部署的应用添加或编辑秘密，你可以通过[应用设置](/deploy/streamlit-community-cloud/manage-your-app/app-settings)访问秘密。请参阅[查看或更新你的秘密](/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-update-your-secrets)。
