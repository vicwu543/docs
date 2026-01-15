---
title: 应用测试速查表
slug: /develop/concepts/app-testing/cheat-sheet
description: Streamlit 应用测试的快速参考指南，涵盖文本元素、部件、图表和交互组件的常见测试模式。
keywords: testing cheat sheet, apptest reference, testing patterns, quick reference, testing examples, streamlit testing guide, test methods, testing syntax
---

# 应用测试速查表

## 文本元素

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# 标题
assert "我的应用" in at.title[0].value
assert "新主题" in at.header[0].value
assert "有趣的子主题" in at.subheader[0].value
assert len(at.divider) == 2

# 正文 / 代码
assert "Hello, world!" in at.markdown[0].value
assert "import streamlit as st" in at.code[0].value
assert "一个很酷的图表" in at.caption[0].value
assert "Hello again, world!" in at.text[0].value
assert "\int a x^2 \,dx" in at.latex[0].value
```

## 输入部件

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# 按钮
assert at.button[0].value == False
at.button[0].click().run()
assert at.button[0].value == True

# 复选框
assert at.checkbox[0].value == False
at.checkbox[0].check().run() # uncheck() 也支持
assert at.checkbox[0].value == True

# 颜色选择器
assert at.color_picker[0].value == "#FFFFFF"
at.color_picker[0].pick("#000000").run()

# 日期输入
assert at.date_input[0].value == datetime.date(2019, 7, 6)
at.date_input[0].set_value(datetime.date(2022, 12, 21)).run()

# 表单提交按钮 - 显示得像普通按钮一样
assert at.button[0].value == False
at.button[0].click().run()
assert at.button[0].value == True

# 多选
assert at.multiselect[0].value == ["foo", "bar"]
at.multiselect[0].select("baz").unselect("foo").run()

# 数字输入
assert at.number_input[0].value == 5
at.number_input[0].increment().run()

# 单选按钮
assert at.radio[0].value == "Bar"
assert at.radio[0].index == 3
at.radio[0].set_value("Foo").run()

# 选择框
assert at.selectbox[0].value == "Bar"
assert at.selectbox[0].index == 3
at.selectbox[0].set_value("Foo").run()

# 选择滑块
assert at.select_slider[0].value == "Feb"
at.select_slider[0].set_value("Mar").run()
at.select_slider[0].set_range("Apr", "Jun").run()

# 滑块
assert at.slider[0].value == 2
at.slider[0].set_value(3).run()
at.slider[0].set_range(4, 6).run()

# 文本区域
assert at.text_area[0].value == "Hello, world!"
at.text_area[0].set_value("Hello, yourself!").run()

# 文本输入
assert at.text_input[0].value == "Hello, world!")
at.text_input[0].set_value("Hello, yourself!").run()

# 时间输入
assert at.time_input[0].value == datetime.time(8, 45)
at.time_input[0].set_value(datetime.time(12, 30))

# 开关
assert at.toggle[0].value == False
assert at.toggle[0].label == "调试模式"
at.toggle[0].set_value(True).run()
assert at.toggle[0].value == True
```

## 数据元素

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# 数据框
expected_df = pd.DataFrame([1, 2, 3])
assert at.dataframe[0].value.equals(expected_df)

# 指标
assert at.metric[0].value == "9500"
assert at.metric[0].delta == "1000"

# json
assert at.json[0].value == '["hi", {"foo": "bar"}]'

# 表格
table_df = pd.DataFrame([1, 2, 3])
assert at.table[0].value.equals(table_df)
```

## 布局和容器

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# 侧边栏
at.sidebar.text_input[0].set_value("Jane Doe")

# 列
at.columns[1].markdown[0].value == "Hello, world!"

# 选项卡
at.tabs[2].markdown[0].value == "Hello, yourself!"
```

## 聊天元素

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# 聊天输入
at.chat_input[0].set_value("你知道什么笑话吗？").run()
# 注意：chat_input 值在每次重新运行后清除（像真实应用中一样）

# 聊天消息
assert at.chat_message[0].markdown[0].value == "你知道什么笑话吗？"
assert at.chat_message[0].avatar == "user"
```

## 状态元素

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# 异常
assert len(at.exception) == 1
assert "TypeError" in at.exception[0].value

# 其他内联警报：success, info, warning, error
assert at.success[0].value == "做得好！"
assert at.info[0].value == "请输入API密钥以继续"
assert at.warning[0].value == "抱歉，密码不匹配"
assert at.error[0].value == "出了些问题 :("

# toast
assert at.toast[0].value == "那真是太棒了！" and at.toast[0].icon == "🔥"
```

## 限制

截至 Streamlit 1.28，以下 Streamlit 功能不被 `AppTest` 原生支持。但是，通过使用 `AppTest.get()` 直接检查底层 proto，许多功能可以实现变通方法。我们计划定期添加对缺失元素的支持，直到所有功能都得到支持。

- 图表元素（`st.bar_chart`、`st.line_chart` 等）
- 媒体元素（`st.image`、`st.video`、`st.audio`）
- `st.file_uploader`
- `st.data_editor`
- `st.expander`
- `st.status`
- `st.camera_input`
- `st.download_button`
- `st.link_button`