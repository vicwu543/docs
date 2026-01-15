---
title: 缓存概述
slug: /develop/concepts/architecture/caching
description: 了解 Streamlit 的缓存机制，包括 st.cache_data 和 st.cache_resource，用于提高应用性能和管理耗时计算。
keywords: streamlit caching, st.cache_data, st.cache_resource, performance optimization, cache management, expensive computations, app performance, cache invalidation, cached functions
---

# 缓存概述

Streamlit 在每次用户交互或代码更改时都会从头到尾运行您的脚本。这种执行模型使得开发变得非常简单。但它带来了两个主要挑战：

1. 长时间运行的函数一遍又一遍地运行，这减慢了您的应用。
2. 对象一次又一次地重新创建，这使得在重新运行或会话之间保持它们变得困难。

但是不用担心！Streamlit 让您使用其内置的缓存机制解决这两个问题。缓存存储缓慢函数调用的结果，因此它们只需要运行一次。这使您的应用更快，并有助于在重新运行之间持久化对象。缓存值可供应用的所有用户使用。如果您需要保存只能在会话内访问的结果，请改用 [会话状态](/develop/concepts/architecture/session-state)。

<Collapse title="目录" expanded={true}>

1. [最小示例](#最小示例)
2. [基本用法](#基本用法)
3. [高级用法](#高级用法)
4. [从 st.cache 迁移](#从-stcache-迁移)

</Collapse>

## 最小示例

要在 Streamlit 中缓存函数，您必须使用两个装饰器之一（[st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 或 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)）装饰它：

```python
@st.cache_data
def long_running_function(param1, param2):
    return …
```

在此示例中，用 `@st.cache_data` 装饰 `long_running_function` 告诉 Streamlit，每当调用该函数时，它会检查两件事：

1. 输入参数的值（在此情况下为 `param1` 和 `param2`）。
2. 函数内部的代码。

如果这是 Streamlit 第一次看到这些参数值和函数代码，它会运行该函数并将返回值存储在缓存中。下次使用相同参数和代码调用该函数时（例如，当用户与应用交互时），Streamlit 将完全跳过执行该函数并返回缓存值。在开发过程中，缓存随着函数代码的变化自动更新，确保最新的更改反映在缓存中。

如前所述，有两个缓存装饰器：

- `st.cache_data` 是缓存返回数据的计算的推荐方法：从 CSV 加载 DataFrame，转换 NumPy 数组，查询 API，或任何其他返回可序列化数据对象（str、int、float、DataFrame、数组、列表等）的函数。它在每次函数调用时创建数据的新副本，使其能够防止[变异和竞态条件](#变异和并发问题)。`st.cache_data` 的行为就是您大多数情况下想要的——所以如果您不确定，请从 `st.cache_data` 开始，看看是否有效！
- `st.cache_resource` 是缓存全局资源（如 ML 模型或数据库连接）的推荐方法——不可序列化的对象，您不想多次加载。使用它，您可以在应用的所有重新运行和会话中共享这些资源，而无需复制或重复。请注意，对缓存返回值的任何更改都会直接影响缓存中的对象（详情见下文）。

<Image src="/images/caching-high-level-diagram.png" caption="Streamlit 的两个缓存装饰器及其用例。" alt="Streamlit 的两个缓存装饰器及其用例。对任何可以存储在数据库中的内容使用 st.cache_data。对无法存储在数据库中的内容使用 st.cache_resource，比如数据库连接或机器学习模型。" />

## 基本用法

### st.cache_data

[st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 是所有返回数据的函数的首选命令——无论是 DataFrames、NumPy 数组、str、int、float 还是其他可序列化类型。几乎在所有用例中都是正确的命令！在每个用户会话中，用 `@st.cache_data` 装饰的函数返回缓存返回值的 _副本_（如果值已被缓存）。

#### 用法

<br />

让我们来看一个使用 `st.cache_data` 的示例。假设您的应用从互联网将 [Uber 乘车共享数据集](https://github.com/plotly/datasets/blob/master/uber-rides-data1.csv) —— 一个 50MB 的 CSV 文件 —— 加载到 DataFrame 中：

```python
def load_data(url):
    df = pd.read_csv(url)  # 👈 下载数据
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
```

运行 `load_data` 函数需要 2 到 30 秒，具体取决于您的网络连接。（提示：如果您网络较慢，请改用 [这个 5MB 数据集](https://github.com/plotly/datasets/blob/master/26k-consumer-complaints.csv)）。如果不使用缓存，每次加载应用或用户交互时都会重新运行下载。自己试试点击我们添加的按钮！不太好的体验… 😕

现在让我们在 `load_data` 上添加 `@st.cache_data` 装饰器：

```
@st.cache_data  # 👈 添加缓存装饰器
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
```

再次运行应用。您会注意到缓慢的下载只在第一次运行时发生。每个后续重新运行应该几乎是瞬间的！ 💨

#### 行为

<br />

这是如何工作的？让我们逐步深入了解 `st.cache_data` 的行为：

- 在第一次运行时，Streamlit 识别到它从未使用指定的参数值（CSV 文件的 URL）调用过 `load_data` 函数。所以它运行该函数并下载数据。
- 现在我们的缓存机制开始生效：返回的 DataFrame 通过 [pickle](https://docs.python.org/3/library/pickle.html) 序列化（转换为字节）并存储在缓存中（连同 `url` 参数的值）。
- 在下一次运行时，Streamlit 检查具有特定 `url` 的 `load_data` 的缓存条目。存在！所以它检索缓存的对象，反序列化为 DataFrame，并返回它而不是重新运行函数并再次下载数据。

序列化和反序列化缓存对象的这一过程创建了我们原始 DataFrame 的副本。虽然这种复制行为看起来可能是不必要的，但这正是我们在缓存数据对象时所期望的，因为它有效地防止了变异和并发问题。阅读下面的 "[变异和并发问题](#变异和并发问题)" 部分以更详细地了解这一点。

<Warning>

[st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 隐式使用 `pickle` 模块，众所周知它是不安全的。您的缓存函数返回的任何内容都被序列化并存储，然后在检索时反序列化。确保您的缓存函数返回可信的值，因为在反序列化期间可能构造恶意的 pickle 数据以执行任意代码。永远不要在不安全模式下加载可能来自不受信任来源的数据，或可能已被篡改的数据。**只加载您信任的数据**。

</Warning>

#### 示例

<br/>

**DataFrame 变换**

在上面的示例中，我们已经展示了如何缓存加载 DataFrame。缓存 DataFrame 变换（如 `df.filter`、`df.apply` 或 `df.sort_values`）也很有用。特别是对于大型 DataFrame，这些操作可能会很慢。

```python
@st.cache_data
def transform(df):
    df = df.filter(items=['one', 'three'])
    df = df.apply(np.sum, axis=0)
	return df
```

**数组计算**

同样，缓存 NumPy 数组上的计算是有意义的：

```python
@st.cache_data
def add(arr1, arr2):
	return arr1 + arr2
```

**数据库查询**

在使用数据库时，通常会对数据库进行 SQL 查询以将数据加载到您的应用中。反复运行这些查询可能很慢，花费金钱，并降低数据库的性能。我们强烈建议缓存应用中的任何数据库查询。另请参见 [我们关于将 Streamlit 连接到不同数据库的指南](/develop/tutorials/databases)，了解详细示例。

```python
connection = database.connect()

@st.cache_data
def query():
    return pd.read_sql_query("SELECT * from table", connection)
```

<Tip>

您应该设置 `ttl`（生存时间）以从数据库获取新结果。如果设置 `st.cache_data(ttl=3600)`，Streamlit 会在 1 小时（3600 秒）后使任何缓存值失效并重新运行缓存函数。详情请参见 [控制缓存大小和持续时间](#控制缓存大小和持续时间)。

</Tip>

**API 调用**

同样，缓存 API 调用是有意义的。这样做还可以避免速率限制。

```python
@st.cache_data
def api_call():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return response.json()
```

**运行 ML 模型（推理）**

运行复杂的机器学习模型可能需要大量时间和内存。为了避免一遍又一遍地运行相同的计算，请使用缓存。

```python
@st.cache_data
def run_model(inputs):
    return model(inputs)
```

### st.cache_resource

[st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 是缓存应该在所有用户、会话和重新运行中全局可用的“资源”的正确命令。它的用例比 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 更有限，特别是用于缓存数据库连接和 ML 模型。在每个用户会话中，用 `@st.cache_resource` 装饰的函数返回返回值的缓存实例（如果值已被缓存）。因此，由 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 缓存的对象表现得像单例并可以改变。

#### 用法

作为 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 的示例，让我们看一个典型的机器学习应用。第一步，我们需要加载一个 ML 模型。我们使用 [Hugging Face 的 transformers 库](https://huggingface.co/docs/transformers/index)：

```python
from transformers import pipeline
model = pipeline("sentiment-analysis")  # 👈 加载模型
```

如果我们直接将此代码放入 Streamlit 应用中，应用将在每次重新运行或用户交互时加载模型。重复加载模型会带来两个问题：

- 加载模型需要时间并减慢应用。
- 每个会话都从头开始加载模型，这占用了大量内存。

相反，一次性加载模型并在所有用户和会话中使用同一个对象更有意义。这正是 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 的用例！让我们将其添加到我们的应用中并处理用户输入的一些文本：

```python
from transformers import pipeline

@st.cache_resource  # 👈 添加缓存装饰器
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

query = st.text_input("Your query", value="I love Streamlit! 🎈")
if query:
    result = model(query)[0]  # 👈 分类查询文本
    st.write(result)
```

如果运行此应用，您会看到应用只在一次调用 `load_model` —— 即应用启动时。后续运行将重用存储在缓存中的同一模型，节省时间和内存！

#### 行为

<br />

使用 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 与使用 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 非常相似。但有一些重要的行为差异：

- [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) **不会** 创建缓存返回值的副本，而是将对象本身存储在缓存中。对该函数返回值的所有变更都会直接影响缓存中的对象，因此您必须确保多个会话的变更不会导致问题。简而言之，返回值必须是线程安全的。

    <Warning>

  对非线程安全对象使用 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 可能导致崩溃或损坏数据。在下方 [变异和并发问题](#变异和并发问题) 部分了解更多。
  </Warning>

- 不创建副本意味着只有一个全局缓存返回对象实例，这节省了内存，例如在使用大型 ML 模型时。在计算机科学术语中，我们创建了一个 [单例](https://en.wikipedia.org/wiki/Singleton_pattern)。
- 函数的返回值不需要是可序列化的。这种行为非常适合本质上不可序列化的类型，例如数据库连接、文件句柄或线程。使用 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 缓存这些对象是不可能的。

#### 示例

<br />

**数据库连接**

[st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 对连接数据库很有用。通常，您正在创建一个连接对象，您希望在每个查询中全局重用它。在每次运行时创建新的连接对象效率低下，并可能导致连接错误。这正是 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 可以做到的，例如对于 Postgres 数据库：

```python
@st.cache_resource
def init_connection():
    host = "hh-pgsql-public.ebi.ac.uk"
    database = "pfmegrnargs"
    user = "reader"
    password = "NWDMCE5xdipIjRrp"
    return psycopg2.connect(host=host, database=database, user=user, password=password)

conn = init_connection()
```

当然，您也可以对任何其他数据库执行相同操作。查看 [我们关于如何将 Streamlit 连接到数据库的指南](/develop/tutorials/databases) 以获得详细的示例。

**加载 ML 模型**

您的应用应始终缓存 ML 模型，这样它们就不会在每次新会话中重新加载到内存中。有关此操作如何与 🤗 Hugging Face 模型一起工作的示例，请参见上面的[示例](#用法-1)。您可以对 PyTorch、TensorFlow 等执行相同操作。这里是 PyTorch 的示例：

```python
@st.cache_resource
def load_model():
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)
    model.eval()
    return model

model = load_model()
```

### 决定使用哪个缓存装饰器

<br />

上面的章节展示了每种缓存装饰器的许多常见示例。但对于边缘情况，决定使用哪种缓存装饰器并不那么简单。最终，这一切归结为"数据"和"资源"之间的区别：

- 数据是可序列化的对象（可通过 [pickle](https://docs.python.org/3/library/pickle.html) 转换为字节的对象）您可以轻松地将其保存到磁盘。想象一下您通常存储在数据库或文件系统中的所有类型——基本类型如 str、int 和 float，但也包括数组、DataFrames、图像或这些类型的组合（列表、元组、字典等）。
- 资源是不可序列化的对象，您通常不会将其保存到磁盘或数据库。它们通常是更复杂、非永久性的对象，如数据库连接、ML 模型、文件句柄、线程等。

从上面列出的类型来看，应该很明显 Python 中的大多数对象都是"数据"。这也是为什么 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 是几乎所有用例的正确命令。[st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 是一个更特殊的命令，您只应在特定情况下使用它。

或者如果您懒得思考太多，查看下表中的用例或返回类型 😉：

| 用例                                 |                                                                                                       典型返回类型 |                                                                                                                                            缓存装饰器 |
| :----------------------------------- | -------------------------------------------------------------------------------------------------------------------------: | -----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| 使用 pd.read_csv 读取 CSV 文件 |                                                                                                           pandas.DataFrame |                                                                                                                                                st.cache_data |
| 读取文本文件                         |                                                                                                           str, list of str |                                                                                                                                                st.cache_data |
| 转换 pandas 数据框                 |                                                                                            pandas.DataFrame, pandas.Series |                                                                                                                                                st.cache_data |
| 使用 numpy 数组计算              |                                                                                                              numpy.ndarray |                                                                                                                                                st.cache_data |
| 使用基本类型进行简单计算             |                                                                                                         str, int, float, … |                                                                                                                                                st.cache_data |
| 查询数据库                           |                                                                                                           pandas.DataFrame |                                                                                                                                                st.cache_data |
| 查询 API                             |                                                                                                pandas.DataFrame, str, dict |                                                                                                                                                st.cache_data |
| 运行 ML 模型（推理）               |                                                                                     pandas.DataFrame, str, int, dict, list |                                                                                                                                                st.cache_data |
| 创建或处理图像                       |                                                                                             PIL.Image.Image, numpy.ndarray |                                                                                                                                                st.cache_data |
| 创建图表                             |                                                        matplotlib.figure.Figure, plotly.graph_objects.Figure, altair.Chart | st.cache_data（但有些库需要 st.cache_resource，因为图表对象不可序列化——确保不要在创建后修改图表！） |
| 惰性计算                             |                                                                                                           polars.LazyFrame |                                                                          st.cache_resource（但可能最好在收集结果上使用 st.cache_data） |
| 加载 ML 模型                         |                                                             transformers.Pipeline, torch.nn.Module, tensorflow.keras.Model |                                                                                                                                            st.cache_resource |
| 初始化数据库连接                     | pyodbc.Connection, sqlalchemy.engine.base.Engine, psycopg2.connection, mysql.connector.MySQLConnection, sqlite3.Connection |                                                                                                                                            st.cache_resource |
| 打开持久文件句柄                     |                                                                                                         \_io.TextIOWrapper |                                                                                                                                            st.cache_resource |
| 打开持久线程                         |                                                                                                           threading.thread |                                                                                                                                            st.cache_resource |

## 高级用法

### 控制缓存大小和持续时间

如果您的应用运行很长时间并不断缓存函数，您可能会遇到两个问题：

1. 应用因缓存太大而耗尽内存。
2. 缓存中的对象变得陈旧，例如，因为您缓存了来自数据库的旧数据。

您可以使用 `ttl` 和 `max_entries` 参数来解决这些问题，这些参数对于两个缓存装饰器都可用。

**`ttl`（生存时间）参数**

`ttl` 设置缓存函数的生存时间。如果时间到了并且您再次调用该函数，应用将丢弃任何旧的、缓存的值，并重新运行该函数。然后将新计算的值存储在缓存中。这种行为对于防止陈旧数据（问题 2）和缓存增长过大（问题 1）很有用。特别是从数据库或 API 拉取数据时，您应始终设置 `ttl`，以免使用旧数据。这是一个示例：

```python
@st.cache_data(ttl=3600)  # 👈 缓存数据 1 小时（=3600 秒）
def get_api_data():
    data = api.get(...)
    return data
```

<Tip>

您还可以使用 `timedelta` 设置 `ttl` 值，例如 `ttl=datetime.timedelta(hours=1)`。

</Tip>

**`max_entries` 参数**

`max_entries` 设置缓存中的最大条目数。限制缓存条目的上限对于限制内存（问题 1）很有用，特别是在缓存大对象时。当向满的缓存中添加新条目时，将删除最旧的条目。这是一个示例：

```python
@st.cache_data(max_entries=1000)  # 👈 缓存中最多 1000 个条目
def get_large_array(seed):
    np.random.seed(seed)
    arr = np.random.rand(100000)
    return arr
```

### 自定义加载动画

默认情况下，当缓存函数运行时，Streamlit 会在应用中显示一个小的加载动画。您可以使用 `show_spinner` 参数轻松修改它，该参数对于两个缓存装饰器都可用：

```python
@st.cache_data(show_spinner=False)  # 👈 禁用加载动画
def get_api_data():
    data = api.get(...)
    return data

@st.cache_data(show_spinner="从 API 获取数据...")  # 👈 使用自定义文本作为加载动画
def get_api_data():
    data = api.get(...)
    return data
```

### 排除输入参数

在缓存函数中，所有输入参数必须是可哈希的。让我们快速解释一下原因和含义。当调用函数时，Streamlit 会查看其参数值以确定之前是否已缓存。因此，它需要一种可靠的方法来比较跨函数调用的参数值。对于字符串或整数来说很简单——但对于任意对象就复杂了！Streamlit 使用 [哈希](https://en.wikipedia.org/wiki/Hash_function) 来解决这个问题。它将参数转换为稳定的键并存储该键。在下一次函数调用时，它再次对参数进行哈希处理并与存储的哈希键进行比较。

不幸的是，并非所有参数都是可哈希的！例如，您可能将不可哈希的数据库连接或 ML 模型传递给您的缓存函数。在这种情况下，您可以从缓存中排除输入参数。只需在参数名称前面加上下划线（例如，`_param1`），它就不会用于缓存。即使它改变了，如果所有其他参数匹配，Streamlit 也会返回缓存的结果。

这是一个示例：

```python
@st.cache_data
def fetch_data(_db_connection, num_rows):  # 👈 不对 _db_connection 进行哈希
    data = _db_connection.fetch(num_rows)
    return data

connection = init_connection()
fetch_data(connection, 10)
```

但是如果您想缓存一个接受不可哈希参数的函数呢？例如，您可能想缓存一个接受 ML 模型作为输入并返回该模型层名称的函数。由于模型是唯一的输入参数，您不能将其排除在缓存之外。在这种情况下，您可以使用 `hash_funcs` 参数为模型指定自定义哈希函数。

### `hash_funcs` 参数

如上所述，Streamlit 的缓存装饰器对输入参数和缓存函数的签名进行哈希处理，以确定该函数之前是否已运行并有返回值存储（"缓存命中"）或需要运行（"缓存未命中"）。Streamlit 的哈希实现无法哈希的输入参数可以通过在其名称前加下划线来忽略。但有两种罕见情况这是不可取的，即您想对 Streamlit 无法哈希的参数进行哈希：

1. 当 Streamlit 的哈希机制无法对参数进行哈希处理时，引发 `UnhashableParamError`。
2. 当您想覆盖参数的 Streamlit 默认哈希机制时。

让我们依次讨论这些情况的示例。

#### 示例 1：对自定义类进行哈希

Streamlit 不知道如何对自定义类进行哈希。如果您将自定义类传递给缓存函数，Streamlit 将引发 `UnhashableParamError`。例如，让我们定义一个自定义类 `MyCustomClass`，它接受一个初始整数分数。让我们还定义一个缓存函数 `multiply_score`，它将分数乘以倍数：

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

@st.cache_data
def multiply_score(obj: MyCustomClass, multiplier: int) -> int:
    return obj.my_score * multiplier

initial_score = st.number_input("输入初始分数", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(multiply_score(score, multiplier))
```

如果您运行此应用，您会看到 Streamlit 引发了 `UnhashableParamError`，因为它不知道如何对 `MyCustomClass` 进行哈希：

```python
UnhashableParamError: Cannot hash argument 'obj' (of type __main__.MyCustomClass) in 'multiply_score'.
```

为了解决这个问题，我们可以使用 `hash_funcs` 参数告诉 Streamlit 如何对 `MyCustomClass` 进行哈希。我们通过将字典传递给 `hash_funcs` 来实现，该字典将参数名称映射到哈希函数。哈希函数的选择由开发人员决定。在这种情况下，让我们定义一个自定义哈希函数 `hash_func`，它将自定义类作为输入并返回分数。我们希望分数成为对象的唯一标识符，因此我们可以使用它来确定性地对对象进行哈希：

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

def hash_func(obj: MyCustomClass) -> int:
    return obj.my_score  # 或任何其他唯一标识对象的值

@st.cache_data(hash_funcs={MyCustomClass: hash_func})
def multiply_score(obj: MyCustomClass, multiplier: int) -> int:
    return obj.my_score * multiplier

initial_score = st.number_input("输入初始分数", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(multiply_score(score, multiplier))
```

现在如果您运行应用，您会看到 Streamlit 不再引发 `UnhashableParamError`，应用按预期运行。

现在让我们考虑 `multiply_score` 是 `MyCustomClass` 的属性并且我们想对整个对象进行哈希的情况：

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("输入初始分数", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))
```

如果您运行此应用，您会看到 Streamlit 引发了 `UnhashableParamError`，因为它无法对参数 `'self' (of type __main__.MyCustomClass) in 'multiply_score'` 进行哈希。一个简单的解决方法是使用 Python 的 `hash()` 函数对对象进行哈希：

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data(hash_funcs={"__main__.MyCustomClass": lambda x: hash(x.my_score)})
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("输入初始分数", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))
```

以上，哈希函数定义为 `lambda x: hash(x.my_score)`。这基于 `MyCustomClass` 实例的 `my_score` 属性创建哈希。只要 `my_score` 保持不变，哈希也保持不变。因此，`multiply_score` 的结果可以从缓存中检索而无需重新计算。

作为一个敏锐的 Python 程序员，您可能曾想过使用 Python 的 `id()` 函数来对对象进行哈希，如下所示：

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data(hash_funcs={"__main__.MyCustomClass": id})
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("输入初始分数", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))
```

如果您运行应用，您会注意到即使 `my_score` 没有改变，Streamlit 也会每次都重新计算 `multiply_score`！困惑吗？在 Python 中，`id()` 返回对象的标识，在对象的生命周期内是唯一且不变的。这意味着即使两个 `MyCustomClass` 实例的 `my_score` 值相同，`id()` 也会为这两个实例返回不同的值，从而导致不同的哈希值。因此，Streamlit 认为这两个不同的实例需要单独的缓存值，因此即使 `my_score` 没有改变，它也会每次都重新计算 `multiply_score`。

这就是为什么我们不鼓励使用它作为哈希函数，而是鼓励返回确定性的真正哈希值的函数。也就是说，如果您知道自己在做什么，可以使用 `id()` 作为哈希函数。只需注意后果。例如，当您将 `@st.cache_resource` 函数的结果作为输入参数传递给另一个缓存函数时，`id` 通常是正确的哈希函数。有很多类型否则不可哈希的对象。

#### 示例 2：对 Pydantic 模型进行哈希

让我们考虑另一个例子，我们要对 Pydantic 模型进行哈希：

```python
import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_data
def identity(person: Person):
    return person

person = identity(Person(name="Lee"))
st.write(f"这个人是 {person.name}")
```

以上，我们使用 Pydantic 的 `BaseModel` 定义了一个自定义类 `Person`，它有一个名为 name 的属性。我们还定义了一个 `identity` 函数，它接受一个 `Person` 实例作为参数并将其返回而不做修改。此函数旨在缓存结果，因此，如果多次使用相同的 `Person` 实例调用它，它不会重新计算而是返回缓存的实例。

然而，如果您运行应用，您会遇到 `UnhashableParamError: Cannot hash argument 'person' (of type __main__.Person) in 'identity'` 错误。这是因为 Streamlit 不知道如何对 `Person` 类进行哈希。为了解决这个问题，我们可以使用 `hash_funcs` 关键字参数告诉 Streamlit 如何对 `Person` 进行哈希。

在下面的版本中，我们定义了一个自定义哈希函数 `hash_func`，它将 `Person` 实例作为输入并返回 name 属性。我们希望 name 成为对象的唯一标识符，因此我们可以使用它来确定性地对对象进行哈希：

```python
import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_data(hash_funcs={Person: lambda p: p.name})
def identity(person: Person):
    return person

person = identity(Person(name="Lee"))
st.write(f"这个人是 {person.name}")
```

#### 示例 3：对 ML 模型进行哈希

在某些情况下，您可能想将您最喜欢的机器学习模型传递给缓存函数。例如，假设您想基于用户在应用中选择的模型将 TensorFlow 模型传递给缓存函数。您可能尝试这样的操作：

```python
import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_base_model(option):
    if option == 1:
        return tf.keras.applications.ResNet50(include_top=False, weights="imagenet")
    else:
        return tf.keras.applications.MobileNetV2(include_top=False, weights="imagenet")

@st.cache_resource
def load_layers(base_model):
    return [layer.name for layer in base_model.layers]

option = st.radio("模型 1 或 2", [1, 2])

base_model = load_base_model(option)

layers = load_layers(base_model)

st.write(layers)
```

在上述应用中，用户可以选择两个模型之一。基于选择，应用加载相应的模型并将其传递给 `load_layers`。然后此函数返回模型中的层名称。如果您运行应用，您会看到 Streamlit 引发了 `UnhashableParamError`，因为它无法对参数 `'base_model' (of type keras.engine.functional.Functional) in 'load_layers'` 进行哈希。

如果您通过在名称前加下划线来禁用对 `base_model` 的哈希，您会观察到无论选择哪个基础模型，显示的层都是一样的。这个微妙的错误是由于 `load_layers` 函数在基础模型更改时不重新运行。这是因为 Streamlit 不对 `base_model` 参数进行哈希，所以它不知道在基础模型更改时需要重新运行函数。

为了解决这个问题，我们可以使用 `hash_funcs` 关键字参数告诉 Streamlit 如何对 `base_model` 参数进行哈希。在下面的版本中，我们定义了一个自定义哈希函数 `hash_func`：`Functional: lambda x: x.name`。我们选择的哈希函数是基于我们知道 `Functional` 对象或模型的 `name` 属性唯一地标识它。只要 `name` 属性保持不变，哈希也保持不变。因此，`load_layers` 的结果可以从缓存中检索而无需重新计算。

```python
import streamlit as st
import tensorflow as tf
from keras.engine.functional import Functional

@st.cache_resource
def load_base_model(option):
    if option == 1:
        return tf.keras.applications.ResNet50(include_top=False, weights="imagenet")
    else:
        return tf.keras.applications.MobileNetV2(include_top=False, weights="imagenet")

@st.cache_resource(hash_funcs={Functional: lambda x: x.name})
def load_layers(base_model):
    return [layer.name for layer in base_model.layers]

option = st.radio("模型 1 或 2", [1, 2])

base_model = load_base_model(option)

layers = load_layers(base_model)

st.write(layers)
```

在上述情况下，我们也可以使用 `hash_funcs={Functional: id}` 作为哈希函数。这是因为当您将 `@st.cache_resource` 函数的结果作为输入参数传递给另一个缓存函数时，`id` 通常是正确的哈希函数。

#### 示例 4：覆盖 Streamlit 的默认哈希机制

让我们考虑另一个示例，我们想覆盖 Streamlit 对 pytz 本地化日期时间对象的默认哈希机制：

```python
from datetime import datetime
import pytz
import streamlit as st

tz = pytz.timezone("Europe/Berlin")

@st.cache_data
def load_data(dt):
    return dt

now = datetime.now()
st.text(load_data(dt=now))

now_tz = tz.localize(datetime.now())
st.text(load_data(dt=now_tz))
```

令人惊讶的是，尽管 `now` 和 `now_tz` 都属于 `<class 'datetime.datetime'>` 类型，但 Streamlit 不知道如何对 `now_tz` 进行哈希，并引发了 `UnhashableParamError`。在这种情况下，我们可以通过将自定义哈希函数传递给 `hash_funcs` 关键字参数来覆盖 Streamlit 对 `datetime` 对象的默认哈希机制：

```python
from datetime import datetime

import pytz
import streamlit as st

tz = pytz.timezone("Europe/Berlin")

@st.cache_data(hash_funcs={datetime: lambda x: x.strftime("%a %d %b %Y, %I:%M%p")})
def load_data(dt):
    return dt

now = datetime.now()
st.text(load_data(dt=now))

now_tz = tz.localize(datetime.now())
st.text(load_data(dt=now_tz))
```

现在让我们考虑一个我们想覆盖 Streamlit 对 NumPy 数组默认哈希机制的情况。虽然 Streamlit 本地对 Pandas 和 NumPy 对象进行哈希，但在某些情况下，您可能想覆盖这些对象的 Streamlit 默认哈希机制。

例如，假设我们创建一个带缓存装饰的 `show_data` 函数，它接受一个 NumPy 数组并将其返回而不做修改。在下面的应用中，`data = df["str"].unique()`（这是一个 NumPy 数组）被传递给 `show_data` 函数。

```python
import time
import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
    df = pd.DataFrame({"num": [112, 112, 2, 3], "str": ["be", "a", "be", "c"]})
    return df

@st.cache_data
def show_data(data):
    time.sleep(2)  # 这使得函数运行 2 秒
    return data

df = get_data()
data = df["str"].unique()

st.dataframe(show_data(data))
st.button("Re-run")
```

由于 `data` 总是相同的，我们期望 `show_data` 函数返回缓存的值。但是，如果您运行应用并单击 `Re-run` 按钮，您会注意到 `show_data` 函数每次都重新运行。我们可以假设这种行为是 Streamlit 对 NumPy 数组的默认哈希机制的结果。

为了解决这个问题，让我们定义一个自定义哈希函数 `hash_func`，它接受一个 NumPy 数组作为输入并返回数组的字符串表示：

```python
import time
import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
    df = pd.DataFrame({"num": [112, 112, 2, 3], "str": ["be", "a", "be", "c"]})
    return df

@st.cache_data(hash_funcs={np.ndarray: str})
def show_data(data):
    time.sleep(2)  # 这使得函数运行 2 秒
    return data

df = get_data()
data = df["str"].unique()

st.dataframe(show_data(data))
st.button("Re-run")
```

现在如果您运行应用并单击 `Re-run` 按钮，您会注意到 `show_data` 函数不再每次都重新运行。这里需要注意的是，我们选择的哈希函数是非常简单的，不一定是最佳选择。例如，如果 NumPy 数组很大，将其转换为字符串表示可能代价高昂。在这种情况下，作为开发人员，您需要为您的用例定义一个好的哈希函数是什么。

#### 静态元素

从 1.16.0 版本开始，缓存函数可以包含 Streamlit 命令！例如，您可以这样做：

```python
@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("从 API 获取数据！")  # 👈 显示成功消息
    return data
```

正如我们所知，Streamlit 只有在之前未缓存过时才会运行此函数。在第一次运行时，`st.success` 消息将出现在应用中。但是在后续运行中会发生什么？它仍然会出现！Streamlit 意识到缓存函数内部有一个 `st.` 命令，在第一次运行时保存它，并在后续运行中重播它。静态元素重播适用于两个缓存装饰器。

您还可以使用此功能缓存整个 UI 部分：

```python
@st.cache_data
def show_data():
    st.header("数据分析")
    data = api.get(...)
    st.success("从 API 获取数据！")
    st.write("这是数据的图表：")
    st.line_chart(data)
    st.write("这是原始数据：")
    st.dataframe(data)
```

#### 输入小部件

您还可以在缓存函数中使用 [交互式输入小部件](/develop/api-reference/widgets) 如 `st.slider` 或 `st.text_input`。小部件重播目前是一个实验性功能。要启用它，您需要设置 `experimental_allow_widgets` 参数：

```python
@st.cache_data(experimental_allow_widgets=True)  # 👈 设置参数
def get_data():
    num_rows = st.slider("要获取的行数")  # 👈 添加滑块
    data = api.get(..., num_rows)
    return data
```

Streamlit 将滑块视为缓存函数的额外输入参数。如果更改滑块位置，Streamlit 将查看它是否已经为该滑块值缓存了函数。如果是，则返回缓存值。如果不是，则使用新的滑块值重新运行函数。

在缓存函数中使用小部件非常强大，因为它允许您缓存应用的整个部分。但这可能很危险！由于 Streamlit 将小部件值视为额外的输入参数，它很容易导致内存使用过多。想象一下，您的缓存函数有五个滑块并返回一个 100MB 的 DataFrame。然后对于这些五个滑块值的 _每个排列_，我们将向缓存添加 100MB——即使滑块不影响返回的数据！这些增加会使您的缓存迅速爆炸。如果您在缓存函数中使用小部件，请注意此限制。我们建议仅在 UI 的孤立部分使用此功能，其中小部件直接影响缓存的返回值。

<Warning>

对缓存函数中小部件的支持是实验性的。我们可能随时更改或删除它，恕不另行通知。请谨慎使用！
</Warning>

<Note>

目前两种小部件在缓存函数中不受支持：`st.file_uploader` 和 `st.camera_input`。我们将来可能会支持它们。如果您需要它们，请随时 [打开一个 GitHub 问题](https://github.com/streamlit/streamlit/issues)！
</Note>

### 处理大数据

如我们所解释的，您应该使用 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 缓存数据对象。但对于极其庞大的数据，例如超过一亿行的 DataFrames 或数组，这可能会很慢。这是因为 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 的[复制行为](#复制行为)：在第一次运行时，它将返回值序列化为字节，并在后续运行时反序列化。这两种操作都需要时间。

如果您正在处理极其庞大的数据，使用 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 可能更有意义。它不会通过序列化/反序列化创建返回值的副本，几乎是即时的。但要注意：对函数返回值的任何更改（如从 DataFrame 中删除列或在数组中设置值）都会直接操作缓存中的对象。您必须确保这不会损坏您的数据或导致崩溃。请参见下面的 [变异和并发问题](#变异和并发问题) 部分。

在对具有四列的 pandas DataFrames 上基准测试 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 时，我们发现当超过一亿行时它变得很慢。表格显示了不同行数下两种缓存装饰器的运行时间（所有都具有四列）：

|                   |                 | 10M 行 | 50M 行 | 100M 行 | 200M 行 |
| ----------------- | --------------- | :------: | :------: | :-------: | :-------: |
| st.cache_data     | 第一次运行\*     |  0.4 秒   |   3 秒    |   14 秒    |   28 秒    |
|                   | 后续运行 |  0.2 秒   |   1 秒    |    2 秒    |    7 秒    |
| st.cache_resource | 第一次运行\*     |  0.01 秒  |  0.1 秒   |   0.2 秒   |    1 秒    |
|                   | 后续运行 |   0 秒    |   0 秒    |    0 秒    |    0 秒    |

|                                                                                                                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _\*对于第一次运行，表格仅显示使用缓存装饰器的开销时间。它不包括缓存函数本身的运行时间。_ |

### 变异和并发问题

在上面的章节中，我们谈了很多关于变异缓存函数返回对象的问题。这个话题很复杂！但它对于理解 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 和 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 之间的行为差异至关重要。所以让我们更深入一点。

首先，我们应该明确定义变异和并发的含义：

- 通过 **变异**，我们指的是在调用函数 _之后_ 对缓存函数返回值所做的任何更改。例如：

  ```python
  @st.cache_data
  def create_list():
      l = [1, 2, 3]

  l = create_list()  # 👈 调用函数
  l[0] = 2  # 👈 变异其返回值
  ```

- 通过 **并发**，我们指的是多个会话可以同时引起这些变异。Streamlit 是一个 Web 框架，需要处理连接到应用的多个用户和会话。如果两个人同时查看应用，他们都会导致 Python 脚本重新运行，这可能同时操作缓存的返回对象——并发。

变异缓存的返回对象可能是危险的。它可能导致应用中的异常，甚至损坏您的数据（这可能比崩溃的应用更糟！）。下面，我们将首先解释 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 的复制行为，并展示它如何避免变异问题。然后，我们将展示并发变异如何导致数据损坏以及如何防止它。

#### 复制行为

[st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 在每次调用函数时都会创建缓存返回值的副本。这避免了大多数变异和并发问题。要详细了解，请回到上面 [st.cache_data 部分](#用法) 中的 [Uber 乘车共享示例](#用法)。我们对其进行了两项修改：

```python
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("...")  # 👈 df is a copy of the cached return value

# 👇 We drop the first row from the DataFrame!
first_row = df.iloc[0]
df.drop(df.index[0], inplace=True)

# The original cached object is not affected by this manipulation.
# Only the copy gets changed!
```

上面，我们操纵了从 `load_data` 返回的 DataFrame。这不会影响缓存中的原始对象，因为 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 创建了一个副本。即使我们对 `df` 进行了修改，也不会影响缓存中的原始对象。这确保了即使在多个会话中操纵数据也不会出现并发问题。我们称这种行为为"安全变异"，因为任何对返回对象的变异都不会影响缓存中的原始对象。

#### Mutations with st.cache_resource

与 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 不同，[st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) **不** 创建返回值的副本。相反，它返回原始对象本身。这意味着任何对返回值的变异都会直接影响缓存中的对象。让我们修改上面的示例以使用 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)：

```python
@st.cache_resource
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("...")  # 👈 df is the original cached object!

# 👇 We drop the first row from the DataFrame!
first_row = df.iloc[0]
df.drop(df.index[0], inplace=True)

# The original cached object IS affected by this manipulation!
# All sessions will see the modified DataFrame!
```

上面，我们操纵了从 `load_data` 返回的 DataFrame。由于我们使用了 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)，`df` 是缓存中的原始对象，而不是副本。当我们删除第一行时，我们实际上是在修改缓存中的原始对象。这会影响使用此缓存对象的所有会话！这可能会导致严重的问题，因为多个会话可能会同时修改同一个对象，从而导致数据损坏。

因此，只有在您确定变异是安全的情况下才使用 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)。例如，当缓存数据库连接或机器学习模型时，这些通常不会在应用代码中被修改。如果您确实需要变异使用 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 缓存的对象，请确保您的代码是线程安全的。

## 从 st.cache 迁移

在 Streamlit 1.18.0 之前，只有一个缓存命令：`st.cache`。它试图同时处理数据和资源缓存，导致行为不一致和意外问题。我们引入了 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 和 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 以明确区分这两种用例。`st.cache` 现在已弃用，将在未来版本中删除。

`st.cache` 的行为介于 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 和 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24) 之间，但偏向于 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)。因此，从 `st.cache` 迁移时：

- 如果您的缓存函数返回数据（如 DataFrame、numpy 数组、字典等），请迁移到 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)。
- 如果您的缓存函数返回资源（如数据库连接、ML 模型等），请迁移到 [st.cache_resource](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)。

<Tip>

如果您不确定要使用哪一个，请先尝试 [st.cache_data](file:///D:/github_st/docs/lib/purejs/versionHelpers.js#L3-L24)。它是最安全的选择，适用于大多数用例。

</Tip>

要自动将您的代码从 `st.cache` 迁移到新缓存命令，请使用 [我们的迁移脚本](https://gist.github.com/tvst/fe4d55c61e876905d7a84f237bfc9fec)。
