---
title: 连接 Streamlit 到 MongoDB
slug: /develop/tutorials/databases/mongodb
description: 了解如何使用 PyMongo 库和密钥管理将 Streamlit 应用连接到远程 MongoDB 数据库进行 NoSQL 文档数据库操作。
keywords: MongoDB, NoSQL, PyMongo, document database, remote database, secrets management, database connection, secure connections, database tutorial
---

# 连接 Streamlit 到 MongoDB

## 简介

本指南解释了如何从 Streamlit Community Cloud 安全地访问 **_远程_** MongoDB 数据库。它使用 [PyMongo](https://github.com/mongodb/mongo-python-driver) 库和 Streamlit 的 [密钥管理](/develop/concepts/connections/secrets-management)。

## 创建 MongoDB 数据库

<Note>

如果您已经有一个想要使用的数据库，请随时
[跳到下一步](#将用户名和密码添加到本地应用密钥)。

</Note>

首先，按照官方教程 [安装 MongoDB](https://docs.mongodb.com/guides/server/install/)，[设置身份验证](https://docs.mongodb.com/guides/server/auth/)（记下用户名和密码！），以及 [连接到 MongoDB 实例](https://docs.mongodb.com/guides/server/drivers/)。连接后，打开 `mongo` shell 并输入以下两个命令来创建一个包含一些示例值的集合：

```sql
use mydb
db.mycollection.insertMany([{"name" : "Mary", "pet": "dog"}, {"name" : "John", "pet": "cat"}, {"name" : "Robert", "pet": "bird"}])
```

## 将用户名和密码添加到本地应用密钥

您的本地 Streamlit 应用将从应用根目录下的 `.streamlit/secrets.toml` 文件读取密钥。如果该文件尚不存在，请创建它，并按照下面所示添加数据库信息：

```toml
# .streamlit/secrets.toml

[mongo]
host = "localhost"
port = 27017
username = "xxx"
password = "xxx"
```

<Important>

当复制应用密钥到 Streamlit Community Cloud 时，请务必用远程 MongoDB 数据库的 **host**、**port**、**username** 和 **password** 替换这些值！

将此文件添加到 `.gitignore` 并且不要将其提交到 GitHub 仓库中！

</Important>

## 将应用密钥复制到云端

由于上面的 `secrets.toml` 文件未提交到 GitHub，因此需要将其内容单独传递给部署的应用（在 Streamlit Community Cloud 上）。转到 [应用仪表板](https://share.streamlit.io/)，在应用的下拉菜单中，点击 **Edit Secrets**。将 `secrets.toml` 的内容复制到文本区域。更多信息请参阅 [密钥管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)。

![密钥管理器截图](/images/databases/edit-secrets.png)

## 将 PyMongo 添加到需求文件

将 [PyMongo](https://github.com/mongodb/mongo-python-driver) 包添加到 `requirements.txt` 文件中，最好固定其版本（将 `x.x.x` 替换为您希望安装的版本）：

```bash
# requirements.txt
pymongo==x.x.x
```

## 编写您的 Streamlit 应用

将以下代码复制到您的 Streamlit 应用并运行。确保适配您的数据库和集合名称。

```python
# streamlit_app.py

import streamlit as st
import pymongo

# 初始化连接。
# 使用 st.cache_resource 只运行一次。
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# 从集合中提取数据。
# 使用 st.cache_data 只在查询更改或10分钟后重新运行。
@st.cache_data(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # 使 st.cache_data 可哈希
    return items

items = get_data()

# 打印结果。
for item in items:
    st.write(f"{item['name']} 有一只 :{item['pet']}:")
```

看到了上面的 `st.cache_data` 吗？如果没有它，Streamlit 会在应用每次重新运行时（例如在小部件交互时）执行查询。有了 `st.cache_data`，它只在查询更改或10分钟后运行（这就是 `ttl` 的作用）。请注意：如果您的数据库更新更频繁，您应该调整 `ttl` 或移除缓存，以便查看者始终看到最新数据。了解更多请参阅 [缓存](/develop/concepts/architecture/caching)。

如果一切顺利（并且您使用了上面我们创建的示例数据），您的应用应该如下所示：

![完成的应用截图](/images/databases/streamlit-app.png)