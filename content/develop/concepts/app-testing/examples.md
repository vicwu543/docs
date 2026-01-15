---
title: 应用测试示例
slug: /develop/concepts/app-testing/examples
description: 测试 Streamlit 登录页面的完整示例，包括身份验证逻辑、密钥管理、安全最佳实践和全面的测试覆盖。
keywords: testing example, login testing, authentication testing, secrets testing, security testing, test example, complete test, login page example, testing patterns
---

# 应用测试示例

## 测试登录页面

让我们考虑一个登录页面。在此示例中，`secrets.toml` 不存在。我们将在测试中直接手动声明虚拟密钥。为了避免[定时攻击](https://en.wikipedia.org/wiki/Timing_attack)，登录脚本使用 `hmac` 将用户的密码与密钥值进行比较，作为安全最佳实践。

### 项目摘要

#### 登录页面行为

在深入应用代码之前，让我们思考一下这个页面应该做什么。无论您使用测试驱动开发还是在代码之后编写单元测试，考虑需要测试的功能都是一个好主意。登录页面应该表现如下：

- 在用户与应用交互之前：
  - 他们的状态是"未验证"。
  - 显示密码提示。
- 如果用户输入错误密码：
  - 他们的状态是"错误"。
  - 显示错误消息。
  - 从输入中清除密码尝试。
- 如果用户输入正确密码：
  - 他们的状态是"已验证"。
  - 显示确认消息。
  - 显示注销按钮（没有登录提示）。
- 如果已登录用户点击**注销**按钮：
  - 他们的状态是"未验证"。
  - 显示密码提示。

#### 登录页面项目结构

```none
myproject/
├── app.py
└── tests/
    └── test_app.py
```

#### 登录页面 Python 文件

页面规范中提到的用户状态在 `st.session_state.status` 中编码。此值在脚本开始时初始化为"未验证"，并在密码提示接收到新条目时通过回调更新。

```python
"""app.py"""
import streamlit as st
import hmac

st.session_state.status = st.session_state.get("status", "unverified")
st.title("我的登录页面")


def check_password():
    if hmac.compare_digest(st.session_state.password, st.secrets.password):
        st.session_state.status = "verified"
    else:
        st.session_state.status = "incorrect"
    st.session_state.password = ""

def login_prompt():
    st.text_input("输入密码:", key="password", on_change=check_password)
    if st.session_state.status == "incorrect":
        st.warning("密码错误。请重试。")

def logout():
    st.session_state.status = "unverified"

def welcome():
    st.success("登录成功。")
    st.button("注销", on_click=logout)


if st.session_state.status != "verified":
    login_prompt()
    st.stop()
welcome()
```

#### 登录页面测试文件

这些测试严格遵循上述应用规范。在每个测试中，在运行应用并继续进行进一步模拟和检查之前，会设置虚拟密钥。

```python
from streamlit.testing.v1 import AppTest

def test_no_interaction():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    assert at.session_state["status"] == "unverified"
    assert len(at.text_input) == 1
    assert len(at.warning) == 0
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""

def test_incorrect_password():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    at.text_input[0].input("balloon").run()
    assert at.session_state["status"] == "incorrect"
    assert len(at.text_input) == 1
    assert len(at.warning) == 1
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""
    assert "密码错误" in at.warning[0].value

def test_correct_password():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    at.text_input[0].input("streamlit").run()
    assert at.session_state["status"] == "verified"
    assert len(at.text_input) == 0
    assert len(at.warning) == 0
    assert len(at.success) == 1
    assert len(at.button) == 1
    assert "登录成功" in at.success[0].value
    assert at.button[0].label == "注销"

def test_log_out():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.session_state["status"] = "verified"
    at.run()
    at.button[0].click().run()
    assert at.session_state["status"] == "unverified"
    assert len(at.text_input) == 1
    assert len(at.warning) == 0
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""
```

看到最后一个测试中如何修改会话状态了吗？测试不是完全模拟用户登录，而是通过设置 `at.session_state["status"] = "verified"` 直接跳转到已登录状态。运行应用后，测试继续模拟用户注销。

### 自动化测试

如果将 `myproject/` 作为仓库推送到 GitHub，您可以使用 [Streamlit 应用 Action](https://github.com/marketplace/actions/streamlit-app-action) 添加 GitHub Actions 测试自动化。这就像在 `myproject/.github/workflows/` 添加工作流文件一样简单：

```yaml
# .github/workflows/streamlit-app.yml
name: Streamlit 应用

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - uses: streamlit/streamlit-app-action@v0.0.3
        with:
          app-path: app.py
```