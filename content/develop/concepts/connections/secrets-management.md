---
title: Secrets 管理
slug: /develop/concepts/connections/secrets-management
description: 了解如何使用原生 secrets 管理和环境变量在 Streamlit 应用中管理 API 密钥、凭证和敏感数据。
keywords: secrets management, API keys, credentials, security, environment variables, sensitive data, secure storage, configuration secrets, app security
---

# Secrets 管理

在 git 仓库中存储未加密的 secrets 是一种不良实践。对于需要访问敏感凭证的应用程序，推荐的解决方案是将这些凭证存储在仓库外部 - 例如使用不提交到仓库的凭证文件或将它们作为环境变量传递。

Streamlit 提供了基于文件的原生 secrets 管理，以便在您的 Streamlit 应用中轻松存储和安全访问您的 secrets。

<Note>

现有的 secrets 管理工具，例如 [dotenv 文件](https://pypi.org/project/python-dotenv/)、[AWS 凭证文件](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials)、[Google Cloud Secret Manager](https://pypi.org/project/google-cloud-secret-manager/) 或 [Hashicorp Vault](https://www.vaultproject.io/use-cases/secrets-management)，在 Streamlit 中都能正常工作。我们只是在需要时添加了原生 secrets 管理。

</Note>

## 如何使用 secrets 管理

### 本地开发并设置 secrets

Streamlit 提供了两种使用 [TOML](https://toml.io/en/latest) 格式在本地设置 secrets 的方法：

1. 在**全局 secrets 文件**中，位于 `~/.streamlit/secrets.toml`（macOS/Linux）或 `%userprofile%/.streamlit/secrets.toml`（Windows）：

   ```toml
   # 此部分中的所有内容都将作为环境变量提供
   db_username = "Jane"
   db_password = "mypassword"

   # 您也可以添加其他部分（如果愿意）。
   # 如下所示的部分内容不会成为环境变量，
   # 但无论如何它们很容易从 Streamlit 内部访问，正如
   # 本文档后面所展示的那样。
   [my_other_secrets]
   things_i_like = ["Streamlit", "Python"]
   ```

   如果您使用全局 secrets 文件，当多个 Streamlit 应用共享相同 secrets 时，您不必在多个项目级文件中重复 secrets。

2. 在**每个项目的 secrets 文件**中，位于 `$CWD/.streamlit/secrets.toml`，其中 `$CWD` 是您运行 Streamlit 的文件夹。如果全局 secrets 文件和每个项目的 secrets 文件都存在，_项目级文件中的 secrets 将覆盖全局文件中定义的 secrets_。

<Important>

将此文件添加到您的 `.gitignore` 中，以免您提交 secrets！

</Important>

### 在您的应用中使用 secrets

通过查询 `st.secrets` 字典或作为环境变量访问您的 secrets。例如，如果您输入上面部分中的 secrets，以下代码展示了如何在您的 Streamlit 应用中访问它们。

```python
import streamlit as st

# 所有内容都可以通过 st.secrets 字典访问：

st.write("数据库用户名:", st.secrets["db_username"])
st.write("数据库密码:", st.secrets["db_password"])

# 根级别的 secrets 也可以作为环境变量访问：

import os

st.write(
    "环境变量是否已设置:",
    os.environ["db_username"] == st.secrets["db_username"],
)
```

<Tip>

除了键表示法（例如 `st.secrets["key"]`）外，您还可以使用属性表示法（例如 `st.secrets.key`）访问 `st.secrets` — 像 [st.session_state](/develop/api-reference/caching-and-state/st.session_state) 一样。

</Tip>

您甚至可以紧凑地使用 TOML 部分将多个 secrets 作为一个属性传递。考虑以下 secrets：

```toml
[db_credentials]
username = "my_username"
password = "my_password"
```

而不是将每个 secrets 作为函数中的属性传递，您可以更紧凑地传递部分以实现相同结果。请参见下面的概念代码，它使用了上面的 secrets：

```python
# 详细版本
my_db.connect(username=st.secrets.db_credentials.username, password=st.secrets.db_credentials.password)

# 更紧凑的版本！
my_db.connect(**st.secrets.db_credentials)
```

### 错误处理

以下是使用 secrets 管理时可能遇到的一些常见错误。

- 如果在应用运行时创建了 `.streamlit/secrets.toml`，则需要重启服务器以使更改在应用中生效。
- 如果您尝试访问一个 secret，但不存在 `secrets.toml` 文件，Streamlit 将引发 `FileNotFoundError` 异常：
  <Image alt="Secrets management FileNotFoundError" src="/images/secrets-filenotfounderror.png" clean />
- 如果您尝试访问一个不存在的 secret，Streamlit 将引发 `KeyError` 异常：

  ```python
  import streamlit as st

  st.write(st.secrets["nonexistent_key"])
  ```

    <Image alt="Secrets management KeyError" src="/images/secrets-keyerror.png" clean />

### 在 Streamlit Community Cloud 中使用 secrets

当您将应用部署到 [Streamlit Community Cloud](https://streamlit.io/cloud) 时，您可以使用与本地相同的 secrets 管理工作流程。但是，您还需要在 Community Cloud Secrets Management 控制台中设置您的 secrets。了解如何操作，请参阅云特定的 [Secrets 管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) 文档。