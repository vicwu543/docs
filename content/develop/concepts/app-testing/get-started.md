---
title: 开始应用测试
slug: /develop/concepts/app-testing/get-started
description: 了解 Streamlit 应用测试的基础知识，通过实际示例涵盖测试结构、AppTest 初始化、元素检索、部件操作和结果检查。
keywords: app testing, get started testing, AppTest, pytest, test structure, element retrieval, widget manipulation, test examples, testing fundamentals, streamlit tests
---

# 开始应用测试

本指南将介绍一个简单的示例，说明测试在项目中的结构以及如何使用 `pytest` 执行它们。在了解了整体情况后，请继续阅读以了解[应用测试基础](#应用测试基础)：

- 初始化和运行模拟应用
- 检索元素
- 操作部件
- 检查结果

Streamlit 的应用测试框架不绑定到任何特定的测试工具，但我们将使用 `pytest` 作为示例，因为它是最常见的 Python 测试框架之一。要尝试本指南中的示例，请确保在开始之前将 `pytest` 安装到您的 Streamlit 开发环境中：

```bash
pip install pytest
```

## 使用 `pytest` 进行简单测试示例

本节解释了如何使用 `pytest` 构建和执行简单测试。有关 `pytest` 的全面介绍，请查看 Real Python 的 [Effective Python testing with pytest](https://realpython.com/pytest-python-testing/) 指南。

### `pytest` 的结构

`pytest` 使用文件和函数的命名约定来方便地执行测试。将测试脚本命名为 `test_<name>.py` 或 `<name>_test.py` 形式。例如，您可以使用 `test_myapp.py` 或 `myapp_test.py`。在您的测试脚本中，每个测试都写成一个函数。每个函数的名称以 `test` 开头或结尾。在本指南的示例中，我们将所有测试脚本和测试函数都以前缀 `test_` 开头。

您可以在单个测试脚本中编写任意数量的测试（函数）。当在目录中调用 `pytest` 时，其中的所有 `test_<name>.py` 文件都将用于测试。这包括子目录中的文件。这些文件中的每个 `test_<something>` 函数都将作为测试执行。您可以将测试文件放在项目目录中的任何位置，但通常会将测试收集到一个专门的 `tests/` 目录中。有关结构化和执行测试的其他方法，请查看 `pytest` 文档中的 [How to invoke pytest](https://docs.pytest.org/how-to/usage.html)。

### 包含应用测试的示例项目

考虑以下项目：

```none
myproject/
├── app.py
└── tests/
    └── test_app.py
```

主应用文件：

```python
"""app.py"""
import streamlit as st

# 初始化 st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("豆子计数器 :paw_prints:")

addend = st.number_input("要添加的豆子", 0, 10)
if st.button("添加"):
    st.session_state.beans += addend
st.markdown(f"已计算的豆子: {st.session_state.beans}")
```

测试文件：

```python
"""test_app.py"""
from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    """用户增加数字输入，然后点击添加"""
    at = AppTest.from_file("app.py").run()
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 1"
```

在运行之前，让我们快速了解一下此应用和测试中的内容。主应用文件 (`app.py`) 在渲染时包含四个元素：`st.title`、`st.number_input`、`st.button` 和 `st.markdown`。测试脚本 (`test_app.py`) 包含单个测试（名为 `test_increment_and_add` 的函数）。我们将在本指南的后半部分详细介绍测试语法，但这里是对此测试的简要说明：

1. 初始化模拟应用并执行第一次脚本运行。
   ```python
   at = AppTest.from_file("app.py").run()
   ```
2. 模拟用户点击加号图标 (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>add</i>) 来增加数字输入（以及由此产生的脚本重新运行）。
   ```python
   at.number_input[0].increment().run()
   ```
3. 模拟用户点击"**添加**"按钮（以及由此产生的脚本重新运行）。
   ```python
   at.button[0].click().run()
   ```
4. 检查是否在末尾显示了正确的消息。
   ```python
   assert at.markdown[0].value == "Beans counted: 1"
   ```

断言是测试的核心。当断言为真时，测试通过。当断言为假时，测试失败。一个测试可以有多个断言，但保持测试专注是好习惯。当测试专注于单一行为时，更容易理解和响应失败。

### 使用 `pytest` 尝试简单测试

1. 将上面的文件复制到新的 "myproject" 目录中。
2. 打开终端并切换到您的项目目录。
   ```bash
   cd myproject
   ```
3. 执行 `pytest`:
   ```bash
   pytest
   ```

测试应该成功执行。您的终端应该显示如下内容：

![使用 pytest 成功完成的测试](/images/app-testing-pytest-intro.png)

通过在项目目录的根目录执行 `pytest`，所有带有测试前缀的 Python 文件（`test_<name>.py`）将被扫描以查找测试函数。在每个测试文件中，每个带有测试前缀的函数都将作为测试执行。`pytest` 然后计算成功次数并列出失败项。您也可以指导 `pytest` 仅扫描您的测试目录。例如，从项目目录的根目录执行：

```bash
pytest tests/
```

### 使用 `pytest` 处理文件路径和导入

测试脚本中的导入和路径应相对于调用 `pytest` 的目录。这就是为什么测试函数使用路径 `app.py` 而不是 `../app.py`，即使应用文件比测试脚本高一级目录。您通常会在包含主应用文件的目录中调用 `pytest`。这通常是项目目录的根目录。

另外，如果在您调用 `pytest` 的目录中存在 `.streamlit/`，其中的任何 `config.toml` 和 `secrets.toml` 都可供您的模拟应用访问。例如，您的模拟应用将能够访问此常见设置中的 `config.toml` 和 `secrets.toml` 文件：

项目结构：

```none
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
```

在 `test_app.py` 中的初始化：

```python
# 应用文件路径相对于 myproject/
at = AppTest.from_file("app.py").run()
```

执行测试的命令：

```bash
cd myproject
pytest tests/
```

## 应用测试基础

现在您了解了 `pytest` 的基础知识，让我们深入了解使用 Streamlit 的应用测试框架。每个测试都始于初始化和运行您的模拟应用。使用其他命令来检索、操作和检查元素。

在下一页，我们将[超越基础](/develop/concepts/app-testing/beyond-the-basics)并涵盖更高级的场景，如使用 secrets、会话状态或多功能页面应用。

### 如何初始化和运行模拟应用

要测试 Streamlit 应用，您必须首先使用应用一个页面的代码初始化 [`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest) 的实例。有三种初始化模拟应用的方法。这些作为类方法提供给 `AppTest`。我们将重点关注 `AppTest.from_file()`，它允许您提供应用页面的路径。这是在应用开发期间构建自动测试的最常见场景。`AppTest.from_string()` 和 `AppTest.from_function()` 可能对某些简单或实验性场景有帮助。

让我们继续[上面的示例](#包含应用测试的示例项目)。

回想测试文件：

```python
"""test_app.py"""
from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    """用户增加数字输入，然后点击添加"""
    at = AppTest.from_file("app.py").run()
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 1"
```

查看测试函数中的第一行：

```python
at = AppTest.from_file("app.py").run()
```

这正在做两件事，等效于：

```python
# 初始化应用。
at = AppTest.from_file("app.py")
# 运行应用。
at.run()
```

`AppTest.from_file()` 返回一个 `AppTest` 实例，用 `app.py` 的内容初始化。`.run()` 方法用于首次运行应用。查看测试，注意 `.run()` 方法手动执行每次脚本运行。测试必须显式运行应用每次。这适用于应用的首次运行和任何因模拟用户输入而导致的重新运行。

### 如何检索元素

`AppTest` 类的属性返回元素序列。元素按渲染应用中的显示顺序排序。可以通过索引检索特定元素。此外，具有键的部件可以通过键检索。

#### 按索引检索元素

`AppTest` 的每个属性都返回关联元素类型的序列。可以通过索引检索特定元素。在上面的示例中，`at.number_input` 返回应用中所有 `st.number_input` 元素的序列。因此，`at.number_input[0]` 是应用中的第一个此类元素。同样，`at.markdown` 返回所有 `st.markdown` 元素的集合，其中 `at.markdown[0]` 是第一个此类元素。

查看 [`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest) 类或[应用测试速查表](/develop/concepts/app-testing/cheat-sheet)的"属性"部分中支持的元素的当前列表。您也可以使用 `.get()` 方法并传递属性名称。`at.get("number_input")` 和 `at.get("markdown")` 分别等效于 `at.number_input` 和 `at.markdown`。

返回的元素序列按页面上的外观顺序排列。如果使用容器以不同顺序插入元素，这些序列可能与代码中的顺序不匹配。考虑以下使用容器在页面上切换两个按钮顺序的示例：

```python
import streamlit as st

first = st.container()
second = st.container()

second.button("A")
first.button("B")
```

如果测试上述应用，第一个按钮（`at.button[0]`）将标记为"B"，第二个按钮（`at.button[1]`）将标记为"A"。作为真实断言，这些将是：

```python
assert at.button[0].label == "B"
assert at.button[1].label == "A"
```

#### 按键检索部件

您可以按其键而非页面上的顺序检索带键的部件。部件的键作为参数或关键字参数传递。例如，查看此应用和以下（真实的）断言：

```python
import streamlit as st

st.button("下一步", key="submit")
st.button("返回", key="cancel")
```

```python
assert at.button(key="submit").label == "下一步"
assert at.button("cancel").label == "返回"
```

#### 检索容器

您还可以通过检索特定容器来缩小元素序列。每个检索到的容器具有与 `AppTest` 相同的属性。例如，`at.sidebar.checkbox` 返回侧边栏中所有复选框的序列。`at.main.selectbox` 返回应用主体中所有选择框的序列（不在侧边栏中）。

对于 `AppTest.columns` 和 `AppTest.tabs`，返回容器序列。因此 `at.columns[0].button` 将是应用中第一个列中所有按钮的序列。

### 如何操作部件

所有部件都有一个通用的 `.set_value()` 方法。此外，许多部件有特定的方法来操作它们的值。[测试元素类](/develop/api-reference/app-testing/testing-element-classes) 的名称与 `AppTest` 属性的名称紧密匹配。例如，查看 [`AppTest.button`](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestbutton) 的返回类型以查看相应的 [`Button`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton) 类。除了使用 `.set_value()` 设置按钮的值外，您还可以使用 `.click()`。查看每个测试元素类以了解其特定方法。

### 如何检查元素

所有元素（包括部件）都有一个通用的 `.value` 属性。这返回元素的内容。对于部件，这与会话状态中的返回值或值相同。对于非输入元素，这将是主要内容参数的值。例如，`.value` 返回 `st.markdown` 或 `st.error` 的 `body` 值。它返回 `st.dataframe` 或 `st.table` 的 `data` 值。

此外，您可以检查部件的许多其他详细信息，如标签或禁用状态。有许多参数可用于检查，但并非全部。使用 linting 软件查看当前支持的内容。这是一个示例：

```python
import streamlit as st

st.selectbox("A", [1,2,3], None, help="选择一个数字", placeholder="选择我")
```

```python
assert at.selectbox[0].value == None
assert at.selectbox[0].label == "A"
assert at.selectbox[0].options == ["1","2","3"]
assert at.selectbox[0].index == None
assert at.selectbox[0].help == "选择一个数字"
assert at.selectbox[0].placeholder == "选择我"
assert at.selectbox[0].disabled == False
```

<Tip>

请注意，`st.selectbox` 的 `options` 被声明为整数，但断言为字符串。如 [`st.selectbox`](/develop/api-reference/widgets/st.selectbox) 文档中所述，选项在内部转换为字符串。如果您发现自己得到意外结果，请仔细检查文档中有关内部类型转换的任何注释。
</Tip>