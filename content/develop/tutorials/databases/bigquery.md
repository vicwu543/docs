---
title: 连接 Streamlit 到 Google BigQuery
slug: /develop/tutorials/databases/bigquery
description: 了解如何使用服务账户认证和 st.connection 将 Streamlit 应用连接到 Google BigQuery 以查询大型数据集。
keywords: BigQuery, Google Cloud, st.connection, large datasets, service account, cloud database, data warehouse, secure connections, database tutorial
---

# 连接 Streamlit 到 Google BigQuery

## 简介

本指南解释了如何从 Streamlit Community Cloud 安全地访问 BigQuery 数据库。它使用
[google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) 库和
Streamlit 的 [密钥管理](/develop/concepts/connections/secrets-management)。

## 创建 BigQuery 数据库

<Note>

如果您已经有一个想要使用的数据库，请随时
[跳到下一步](#启用-bigquery-api)。

</Note>

对于此示例，我们将使用来自 BigQuery 的 [示例数据集之一](https://cloud.google.com/bigquery/public-data#sample_tables)（即 `shakespeare` 表）。如果您想创建新数据集，请按照 [Google 的快速入门指南](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui) 操作。

## 启用 BigQuery API

对 BigQuery 的程序化访问通过 [Google Cloud Platform](https://cloud.google.com) 控制。创建账户或登录并前往 [APIs & Services 仪表板](https://console.cloud.google.com/apis/dashboard)（如果询问请选择或创建项目）。如下所示，搜索 BigQuery API 并启用它：

<Flex>
<Image alt="Bigquery 截图 1" src="/images/databases/big-query-1.png" />
<Image alt="Bigquery 截图 2" src="/images/databases/big-query-2.png" />
<Image alt="Bigquery 截图 3" src="/images/databases/big-query-3.png" />
</Flex>

## 创建服务账户和密钥文件

要从 Streamlit Community Cloud 使用 BigQuery API，您需要一个 Google Cloud Platform 服务账户（一种用于程序化数据访问的特殊账户类型）。转到 [服务账户](https://console.cloud.google.com/iam-admin/serviceaccounts) 页面并创建一个具有 **Viewer** 权限的账户（这将允许该账户访问数据但不能更改数据）：

<Flex>
<Image alt="Bigquery 截图 4" src="/images/databases/big-query-4.png" />
<Image alt="Bigquery 截图 5" src="/images/databases/big-query-5.png" />
<Image alt="Bigquery 截图 6" src="/images/databases/big-query-6.png" />
</Flex>

<Note>

如果按钮 **CREATE SERVICE ACCOUNT** 是灰色的，说明您没有正确的权限。请联系您的 Google Cloud 项目的管理员寻求帮助。

</Note>

点击 **DONE** 后，您应该返回到服务账户概览页面。为新账户创建一个 JSON 密钥文件并下载它：

<Flex>
<Image alt="Bigquery 截图 7" src="/images/databases/big-query-7.png" />
<Image alt="Bigquery 截图 8" src="/images/databases/big-query-8.png" />
<Image alt="Bigquery 截图 9" src="/images/databases/big-query-9.png" />
</Flex>

## 将密钥文件添加到本地应用密钥

您的本地 Streamlit 应用将从应用根目录下的 `.streamlit/secrets.toml` 文件读取密钥。如果该文件尚不存在，请创建它，并按照下面所示将您刚刚下载的密钥文件内容添加到其中：

```toml
# .streamlit/secrets.toml

[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

<Important>

将此文件添加到 `.gitignore` 并且不要将其提交到 GitHub 仓库中！

</Important>

## 将应用密钥复制到云端

由于上面的 `secrets.toml` 文件未提交到 GitHub，因此需要将其内容单独传递给部署的应用（在 Streamlit Community Cloud 上）。转到 [应用仪表板](https://share.streamlit.io/)，在应用的下拉菜单中，点击 **Edit Secrets**。将 `secrets.toml` 的内容复制到文本区域。更多信息请参阅 [密钥管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)。

![密钥管理器截图](/images/databases/edit-secrets.png)

## 将 google-cloud-bigquery 添加到需求文件

将 [google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) 包添加到 `requirements.txt` 文件中，最好固定其版本（将 `x.x.x` 替换为您希望安装的版本）：

```bash
# requirements.txt
google-cloud-bigquery==x.x.x
```

## 编写您的 Streamlit 应用

将以下代码复制到您的 Streamlit 应用并运行。如果您不使用示例表，请确保调整查询。

```python
# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# 创建 API 客户端。
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# 执行查询。
# 使用 st.cache_data 只在查询更改或10分钟后重新运行。
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # 转换为字典列表。st.cache_data 需要哈希返回值。
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")

# 打印结果。
st.write("莎士比亚的一些智慧之言:")
for row in rows:
    st.write("✍️ " + row['word'])
```

看到了上面的 `st.cache_data` 吗？如果没有它，Streamlit 会在应用每次重新运行时（例如在小部件交互时）执行查询。有了 `st.cache_data`，它只在查询更改或10分钟后运行（这就是 `ttl` 的作用）。请注意：如果您的数据库更新更频繁，您应该调整 `ttl` 或移除缓存，以便查看者始终看到最新数据。了解更多请参阅 [缓存](/develop/concepts/architecture/caching)。

另外，您可以使用 pandas 从 BigQuery 直接读取到数据框中！按照上述所有步骤，安装 [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/index.html) 库（别忘了将其添加到 `requirements.txt` 中！），并调用 `pandas.read_gbq(query, credentials=credentials)`。更多信息请参阅 [pandas 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_gbq.html)。

如果一切顺利（并且您使用了示例表），您的应用应该如下所示：

![最终应用截图](/images/databases/big-query-10.png)