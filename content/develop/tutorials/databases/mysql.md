---
title: 连接 Streamlit 到 MySQL
slug: /develop/tutorials/databases/mysql
description: 了解如何使用 st.connection 和密钥管理将 Streamlit 应用连接到远程 MySQL 数据库进行 SQL 查询和数据访问。
keywords: MySQL, database connection, st.connection, secrets management, SQL database, remote database, database tutorial, secure connections
---

# 连接 Streamlit 到 MySQL

## 简介

本指南解释了如何从 Streamlit Community Cloud 安全地访问 **_远程_** MySQL 数据库。它使用 [st.connection](/develop/api-reference/connections/st.connection) 和 Streamlit 的 [密钥管理](/develop/concepts/connections/secrets-management)。下面的示例代码将 **仅适用于 Streamlit 版本 >= 1.28**，因为 `st.connection` 是在该版本中添加的。

## 创建 MySQL 数据库

<Note>

如果您已经有一个想要使用的数据库，请随时
[跳到下一步](#将用户名和密码添加到本地应用密钥)。

</Note>

首先，按照 [此教程](https://dev.mysql.com/doc/mysql-getting-started/en/) 安装 MySQL 并启动 MySQL 服务器（记下用户名和密码！）。一旦您的 MySQL 服务器启动并运行，使用 `mysql` 客户端连接到它并输入以下命令来创建数据库和具有某些示例值的表：

```sql
CREATE DATABASE pets;

USE pets;

CREATE TABLE mytable (
    name varchar(80),
    pet varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## 将用户名和密码添加到本地应用密钥

您的本地 Streamlit 应用将从应用根目录下的 `.streamlit/secrets.toml` 文件读取密钥。了解更多关于 [Streamlit 密钥管理的信息](/develop/concepts/connections/secrets-management)。如果该文件尚不存在，请创建它，并按照下面所示添加 MySQL 服务器的数据库名称、用户和密码：

```toml
# .streamlit/secrets.toml

[connections.mysql]
dialect = "mysql"
host = "localhost"
port = 3306
database = "xxx"
username = "xxx"
password = "xxx"
query = { charset = "xxx" }
```

如果在定义连接时使用 `query`，则必须使用 `streamlit>=1.35.0`。

<Important>

当复制应用密钥到 Streamlit Community Cloud 时，请务必用远程 MySQL 数据库的 **host**、**port**、**database**、**username** 和 **password** 替换这些值！

将此文件添加到 `.gitignore` 并且不要将其提交到 GitHub 仓库中！

</Important>

## 将应用密钥复制到云端

由于上面的 `secrets.toml` 文件未提交到 GitHub，因此需要将其内容单独传递给部署的应用（在 Streamlit Community Cloud 上）。转到 [应用仪表板](https://share.streamlit.io/)，在应用的下拉菜单中，点击 **Edit Secrets**。将 `secrets.toml` 的内容复制到文本区域。更多信息请参阅 [密钥管理](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)。

![密钥管理器截图](/images/databases/edit-secrets.png)

## 将依赖项添加到需求文件

将 [mysqlclient](https://github.com/PyMySQL/mysqlclient) 和 [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) 包添加到 `requirements.txt` 文件中，最好固定其版本（将 `x.x.x` 替换为您希望安装的版本）：

```bash
# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x
```

## 编写您的 Streamlit 应用

将以下代码复制到您的 Streamlit 应用并运行。确保适配 `query` 以使用您的表名。

```python
# streamlit_app.py

import streamlit as st

# 初始化连接。
conn = st.connection('mysql', type='sql')

# 执行查询。
df = conn.query('SELECT * from mytable;', ttl=600)

# 打印结果。
for row in df.itertuples():
    st.write(f"{row.name} 有一只 :{row.pet}:")
```

看到了上面的 `st.connection` 吗？这会处理密钥检索、设置、查询缓存和重试。默认情况下，`query()` 结果会被缓存而不会过期。在这种情况下，我们设置了 `ttl=600` 以确保查询结果的缓存时间不超过10分钟。您也可以设置 `ttl=0` 来禁用缓存。了解更多请参阅 [缓存](/develop/concepts/architecture/caching)。

如果一切顺利（并且您使用了上面我们创建的示例表），您的应用应该如下所示：

![完成的应用截图](/images/databases/streamlit-app.png)