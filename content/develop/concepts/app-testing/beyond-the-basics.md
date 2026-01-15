---
title: 超越应用测试基础
slug: /develop/concepts/app-testing/beyond-the-basics
description: 了解 Streamlit 应用测试技术，涵盖 AppTest 可变属性，包括 secrets、会话状态、查询参数和高级测试模式。
keywords: advanced testing, apptest attributes, secrets testing, session state testing, query params testing, mutable attributes, advanced apptest, testing patterns
---

# 超越应用测试基础

既然您已经熟悉了为 Streamlit 应用执行基本测试，让我们来看看 [`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest) 的可变属性：

- `AppTest.secrets`
- `AppTest.session_state`
- `AppTest.query_params`

您可以使用类似字典的语法为这三个属性读取和更新值。对于 `.secrets` 和 `.query_params`，您可以使用键表示法，但不能使用属性表示法。例如，`AppTest` 的 `.secrets` 属性接受 `at.secrets["my_key"]`，但**不接受** `at.secrets.my_key`。这与您在主库中使用关联命令的方式不同。另一方面，`.session_state` 允许键表示法和属性表示法。

对于这些属性，典型的模式是在执行应用首次运行之前声明任何值。可以在测试中的任何时候检查值。对于 secrets 和会话状态，还有一些额外的注意事项，我们现在将介绍。

## 在应用测试中使用 secrets

请小心不要直接在测试中包含 secrets。考虑这个使用 `pytest` 在项目根目录执行的简单项目：

```none
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
```

```bash
cd myproject
pytest tests/
```

在上述场景中，您的模拟应用将可以访问您的 `secrets.toml` 文件。但是，由于您不希望将 secrets 提交到您的仓库，您可能需要编写安全地将 secrets 拉入内存或使用虚拟 secrets 的测试。

### 示例：在测试中声明 secrets

在测试中，在初始化 `AppTest` 实例后但在首次运行之前声明每个 secret。（缺少 secret 可能导致应用无法运行！）例如，考虑以下 secrets 文件和相应的测试初始化以手动分配相同的 secrets：

Secrets 文件：

```toml
db_username = "Jane"
db_password = "mypassword"

[my_other_secrets]
things_i_like = ["Streamlit", "Python"]
```

具有等效 secrets 的测试文件：

```python
# 初始化 AppTest 实例。
at = AppTest.from_file("app.py")
# 声明 secrets。
at.secrets["db_username"] = "Jane"
at.secrets["db_password"] = "mypassword"
at.secrets["my_other_secrets.things_i_like"] = ["Streamlit", "Python"]
# 运行应用。
at.run()
```

通常，您希望避免直接在测试中输入您的 secrets。如果您的测试不需要真实的 secrets，您可以声明虚拟 secrets，如上面的示例。如果您的应用使用 secrets 连接到数据库或 API 等外部服务，请考虑在应用测试中模拟该服务。如果您需要使用真实的 secrets 并实际连接，您应该使用 API 来安全匿名地传递它们。如果您正在使用 GitHub Actions 自动化测试，请查看他们的 [安全指南](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)。

```python
at.secrets["my_key"] = <通过 API 提供的值>
```

## 在应用测试中使用会话状态

`AppTest` 的 `.session_state` 属性允许您使用键表示法（`at.session_state["my_key"]`）和属性表示法（`at.session_state.my_key`）读取和更新会话状态值。通过在会话状态中手动声明值，您可以直接跳转到特定状态，而不是模拟许多步骤来达到那里。此外，测试框架不为多页面应用提供原生支持。`AppTest` 的实例只能测试一个页面。您必须手动声明会话状态值以模拟用户从另一页携带数据。

### 示例：测试多页面应用

考虑一个简单的多页面应用，其中第一页可以修改会话状态中的值。要测试第二页，在测试中手动设置会话状态并运行模拟应用：

项目结构：

```none
myproject/
├── pages/
│   └── second.py
├── first.py
└── tests/
    └── test_second.py
```

第一个应用页面：

```python
"""first.py"""
import streamlit as st

st.session_state.magic_word = st.session_state.get("magic_word", "Streamlit")

new_word = st.text_input("魔法词:")

if st.button("设置魔法词"):
    st.session_state.magic_word = new_word
```

第二个应用页面：

```python
"""second.py"""
import streamlit as st

st.session_state.magic_word = st.session_state.get("magic_word", "Streamlit")

if st.session_state.magic_word == "Balloons":
    st.markdown(":balloon:")
```

测试文件：

```python
"""test_second.py"""
from streamlit.testing.v1 import AppTest

def test_balloons():
    at = AppTest.from_file("pages/second.py")
    at.session_state["magic_word"] = "Balloons"
    at.run()
    assert at.markdown[0].value == ":balloon:"
```

通过在测试中设置值 `at.session_state["magic_word"] = "Balloons"`，您可以模拟用户在 `first.py` 上输入并保存 "Balloons" 后导航到 `second.py` 的操作。