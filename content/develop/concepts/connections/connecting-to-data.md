---
title: 连接到数据
slug: /develop/concepts/connections/connecting-to-data
description: 了解如何使用最佳实践进行数据检索、缓存和安全数据连接，将 Streamlit 应用连接到数据库、API 和数据源。
keywords: data connections, databases, APIs, data sources, data retrieval, database connections, API integration, data access, remote data, data management
---

# 连接到数据

大多数 Streamlit 应用都需要某种数据或 API 访问才有用 - 要么检索数据显示，要么保存某些用户操作的结果。这种数据或 API 通常是某种远程服务、数据库或其他数据源的一部分。

**您可以使用 Python 执行的任何操作，包括数据连接，通常都可以在 Streamlit 中工作**。Streamlit 的[教程](/develop/tutorials/databases)是许多数据源的良好起点。然而：

- 在 Python 应用程序中连接到数据通常很繁琐且烦人。
- 从 Streamlit 应用连接到数据有特定的考虑因素，例如缓存和 secrets 管理。

**Streamlit 提供了 [`st.connection()`](/develop/api-reference/connections/st.connection) 来更轻松地将 Streamlit 应用连接到数据和 API，只需几行代码**。此页面提供了使用此功能的基本示例，然后专注于高级用法。

要全面了解此功能，请查看 Streamlit 开发者体验产品经理 Joshua Carroll 的视频教程。您将通过真实示例了解此功能在创建和管理应用内数据连接方面的实用性。

<YouTube videoId="xQwDfW7UHMo" />

## 基本用法

有关基本入门和使用示例，请阅读相关的[数据源教程](/develop/tutorials/databases)。Streamlit 有对 SQL 方言和 Snowflake 的内置连接。我们还维护可安装的[云文件存储](https://github.com/streamlit/files-connection)和[Google 表格](https://github.com/streamlit/gsheets-connection)连接。

如果您刚开始，最好的学习方法是选择您可以访问的数据源，并从上面的页面之一获取最小示例 👆。在这里，我们将提供一个使用 SQLite 数据库的超最小用法示例。之后，本页面的其余部分将专注于高级用法。

### 一个简单起点 - 使用本地 SQLite 数据库

[本地 SQLite 数据库](https://sqlite.org/index.html) 可能对您的应用的半持久数据存储有用。

<Note>

社区云应用不保证本地文件存储的持久性，因此平台可能随时删除使用此技术存储的数据。

</Note>

要查看下面运行的示例，请查看下面的交互式演示：

<Cloud name="experimental-connection" path="SQL" height="600px" />

#### 步骤 1：安装先决条件库 - SQLAlchemy

Streamlit 中的所有 SQLConnection 都使用 SQLAlchemy。对于大多数其他 SQL 方言，您还需要安装驱动程序。但[SQLite 驱动程序随 python3 一起提供](https://docs.python.org/3/develop/sqlite3.html)，所以不需要。

```bash
pip install SQLAlchemy==1.4.0
```

#### 步骤 2：在您的 Streamlit secrets.toml 文件中设置数据库 URL

在您的应用将从中运行的同一目录中创建目录和文件 `.streamlit/secrets.toml`。将以下内容添加到文件中。

```toml
# .streamlit/secrets.toml

[connections.pets_db]
url = "sqlite:///pets.db"
```

#### 步骤 3：在您的应用中使用连接

以下应用创建到数据库的连接，使用它创建表并插入一些数据，然后查询数据并将其显示在数据框中。

```python
# streamlit_app.py

import streamlit as st

# 创建到 pets_db 的 SQL 连接，如您的 secrets 文件中指定的那样。
conn = st.connection('pets_db', type='sql')

# 使用 conn.session 插入一些数据。
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# 查询并显示您插入的数据
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

在此示例中，我们没有在调用 [`conn.query()`](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionquery) 时设置 `ttl=` 值，这意味着只要应用服务器运行，Streamlit 就会无限期地缓存结果。

现在，让我们讨论更多高级主题！🚀

## 高级主题

### 全局 secrets，管理多个应用和多个数据存储

Streamlit [支持在用户主目录中指定的全局 secrets 文件](/develop/concepts/connections/secrets-management)，例如 `~/.streamlit/secrets.toml`。如果您构建或管理多个应用，我们建议在跨应用的本地开发中使用全局凭证或 secrets 文件。使用这种方法，您只需要在一个地方设置和管理您的凭证，将新应用连接到现有数据源实际上就是一行代码。它还降低了意外将您的凭证签入 git 的风险，因为它们不需要存在于项目仓库中。

对于在本地开发期间连接到多个类似数据源的情况（例如本地与暂存数据库），您可以在您的 secrets 或凭证文件中为不同环境定义不同的连接部分，然后在运行时决定使用哪个。`st.connection` 支持使用 _`name=env:<MY_NAME_VARIABLE>`_ 语法来实现此功能。

例如，假设我有一个本地和一个暂存 MySQL 数据库，希望在不同时间将我的应用连接到其中一个。我可以创建一个全局 secrets 文件，如下所示：

```toml
# ~/.streamlit/secrets.toml

[connections.local]
url = "mysql://me:****@localhost:3306/local_db"

[connections.staging]
url = "mysql://jdoe:******@staging.acmecorp.com:3306/staging_db"
```

然后我可以将我的应用连接配置为从指定的环境变量获取其名称

```python
# streamlit_app.py
import streamlit as st

conn = st.connection("env:DB_CONN", "sql")
df = conn.query("select * from mytable")
# ...
```

现在我可以通过设置 `DB_CONN` 环境变量来指定在运行时连接到本地还是暂存环境。

```bash
# 连接到本地
DB_CONN=local streamlit run streamlit_app.py

# 连接到暂存环境
DB_CONN=staging streamlit run streamlit_app.py
```

### 高级 SQLConnection 配置

[SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) 配置使用 SQLAlchemy `create_engine()` 函数。它将接受单个 URL 参数或尝试使用 [`SQLAlchemy.engine.URL.create()`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.URL.create) 从几个部分（用户名、数据库、主机等）构造 URL。

几种流行的 SQLAlchemy 方言，如 Snowflake 和 Google BigQuery，可以使用除 URL 之外的附加参数进行配置到 `create_engine()`。这些可以直接作为 `**kwargs` 传递给 [st.connection](/develop/api-reference/connections/st.connection) 调用，或在名为 `create_engine_kwargs` 的附加 secrets 部分中指定。

例如，snowflake-sqlalchemy 接受附加的 [`connect_args`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine.params.connect_args) 参数作为字典，用于 URL 中不支持的配置。这些可以如下指定：

```toml
# .streamlit/secrets.toml

[connections.snowflake]
url = "snowflake://<user_login_name>@<account_identifier>/"

[connections.snowflake.create_engine_kwargs.connect_args]
authenticator = "externalbrowser"
warehouse = "xxx"
role = "xxx"
```

```python
# streamlit_app.py

import streamlit as st

# 上面 secrets.toml 中的 url 和 connect_args 将被获取并使用
conn = st.connection("snowflake", "sql")
# ...
```

或者，这可以完全在 `**kwargs` 中指定。

```python
# streamlit_app.py

import streamlit as st

# 不需要 secrets.toml
conn = st.connection(
    "snowflake",
    "sql",
    url = "snowflake://<user_login_name>@<account_identifier>/",
    connect_args = dict(
        authenticator = "externalbrowser",
        warehouse = "xxx",
        role = "xxx",
    )
)
# ...
```

您也可以同时提供 kwargs 和 secrets.toml 值，它们将被合并（通常 kwargs 优先）。

### 在频繁使用或长时间运行的应用中的连接考虑

默认情况下，连接对象使用 [`st.cache_resource`](/develop/api-reference/caching-and-state/st.cache_resource) 进行缓存，没有过期时间。在大多数情况下这是期望的。如果希望连接对象在一段时间后过期，可以执行 `st.connection('myconn', type=MyConnection, ttl=<N>)`。

许多连接类型预期是长期运行的或完全无状态的，因此不需要过期。假设连接变陈旧（例如缓存的令牌过期或服务器端连接被关闭）。在这种情况下，每个连接都有一个 `reset()` 方法，它将使缓存的版本失效，并导致 Streamlit 在下次检索时重新创建连接。

像 `query()` 和 `read()` 这样的便利方法通常默认使用 [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) 缓存结果而不设过期时间。当应用可以运行许多具有大结果的不同读取操作时，随着时间的推移可能导致高内存使用，结果在长时间运行的应用中变陈旧，这与使用任何其他 `st.cache_data` 的情况相同。对于生产用例，我们建议在这些读取操作上设置适当的 `ttl`，例如 `conn.read('path/to/file', ttl="1d")`。请参阅[缓存](/develop/concepts/architecture/caching)以获取更多信息。

对于可能获得显著并发使用的应用，请确保您了解连接的任何线程安全含义，特别是在使用第三方构建的连接时。Streamlit 构建的连接应默认提供线程安全操作。

### 构建自己的连接

在大多数情况下，使用现有驱动程序或 SDK 构建自己的基本连接实现非常简单。但是，您可以通过进一步努力添加更复杂的功能。这种自定义实现是将支持扩展到新数据源并为 Streamlit 生态系统做贡献的好方法。

为具有频繁使用的访问模式和数据源的组织维护跨多个应用的定制内部连接实现可能是一种强大的实践。

查看下面 st.experimental 连接演示应用中的[构建您自己的连接页面](https://experimental-connection.streamlit.app/Build_your_own)以获取快速教程和工作实现。此演示在 DuckDB 之上构建了一个最小但功能非常完善的连接。

<Cloud name="experimental-connection" path="Build_your_own" height="600px" />

典型步骤是：

1. 声明 Connection 类，扩展 [`ExperimentalBaseConnection`](/develop/api-reference/connections/st.connections.experimentalbaseconnection)，并将类型参数绑定到底层连接对象：

   ```python
   from streamlit.connections import ExperimentalBaseConnection
   import duckdb

   class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection])
   ```

2. 实现 `_connect` 方法，该方法读取任何 kwargs、外部配置/凭证位置和 Streamlit secrets 以初始化底层连接：

   ```python
   def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
       if 'database' in kwargs:
           db = kwargs.pop('database')
       else:
           db = self._secrets['database']
       return duckdb.connect(database=db, **kwargs)
   ```

3. 添加对您的连接有用的辅助方法（在需要缓存的地方用 `st.cache_data` 包装）

### 连接构建最佳实践

我们建议应用以下最佳实践，使您的连接与 Streamlit 内置连接和更广泛的 Streamlit 生态系统保持一致。对于您打算公开分发的连接，这些实践尤其重要。

1. **扩展现有驱动程序或 SDK，并默认采用对现有用户有意义的语义。**

   在构建连接时，很少需要从零开始实现复杂的数据访问逻辑。尽可能使用现有的流行 Python 驱动程序和客户端。这样做使您的连接更容易维护、更安全，并使用户能够获得最新功能。例如，[SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) 扩展 SQLAlchemy，[FileConnection](https://github.com/streamlit/files-connection) 扩展 [fsspec](https://filesystem-spec.readthedocs.io/en/latest/)，[GsheetsConnection](https://github.com/streamlit/gsheets-connection) 扩展 [gspread](https://docs.gspread.org/en/latest/) 等。

   考虑使用与底层包一致的访问模式、方法/参数命名和返回值，并熟悉该包现有用户的习惯。

2. **直观、易于使用的读取方法。**

   st.connection 的大部分功能在于提供直观、易于使用的读取方法，使应用开发人员能够快速开始。大多数连接应至少公开一个读取方法，该方法：
   - 用简单动词命名，如 `read()`、`query()` 或 `get()`
   - 默认情况下由 `st.cache_data` 包装，至少支持 `ttl=` 参数
   - 如果结果是表格格式，则返回 pandas DataFrame
   - 提供常用的关键字参数（如分页或格式化）并带有合理的默认值 - 理想情况下，常见情况只需要 1-2 个参数。

3. **配置、secrets 和 `_connect` 方法中的优先级。**

   每个连接都应该支持通过 Streamlit secrets 和关键字参数提供的常用连接参数。名称应与初始化或配置底层包时使用的名称匹配。

   此外，在相关的情况下，连接应支持通过现有的标准环境变量或配置/凭证文件进行数据源特定配置。在许多情况下，底层包提供已经可以轻松处理此问题的构造函数或工厂函数。

   当您可以在多个地方指定相同的连接参数时，我们建议在可能的情况下使用以下优先级顺序（从高到低）：
   - 代码中指定的关键字参数
   - Streamlit secrets
   - 数据源特定配置（如适用）

4. **处理线程安全和陈旧连接。**

   连接应在实践中提供线程安全操作（大多数时候都是如此）并清楚地记录与此相关的任何注意事项。大多数底层驱动程序或 SDK 应提供线程安全对象或方法 - 请尽可能使用这些。

   如果底层驱动程序或 SDK 有状态连接对象变陈旧或无效的风险，请考虑在访问方法中构建低影响健康检查或重置/重试模式。内置到 Streamlit 中的 SQLConnection 有一个很好的示例，使用 [tenacity](https://tenacity.readthedocs.io/) 和内置的 [Connection.reset()](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionreset) 方法。另一种方法是鼓励开发人员在 `st.connection()` 调用上设置适当的 TTL，以确保定期重新初始化连接对象。