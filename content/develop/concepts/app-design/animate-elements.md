---
title: 动画化和更新元素
slug: /develop/concepts/design/animate
description: 学习如何通过使用 st.empty、st.add_rows 和其他可更新容器在 Streamlit 中创建动态的、有动画效果的内容，而无需完整的应用重新运行。
keywords: 动画元素, 更新元素, st.empty, st.add_rows, 动态内容, 实时更新, 原位更新, 流数据, 实时更新, 元素动画
---

# 动画化和更新元素

有时你显示一个图表或数据框并想在应用运行时实时修改它（例如，在一个循环中）。某些元素有内置方法允许你原位更新它们而不重新运行应用。

可更新的元素包括以下内容：

- `st.empty` 容器可以按顺序写入，并将始终显示写入的最后一个内容。它们也可以通过调用方法的 `.empty()` 来清除。
- `st.dataframe`、`st.table` 和许多图表元素可以使用 `.add_rows()` 方法更新，该方法附加数据。
- `st.progress` 元素可以通过额外的 `.progress()` 调用进行更新。它们也可以通过 `.empty()` 方法调用来清除。
- `st.status` 容器有一个 `.update()` 方法来改变它们的标签、展开状态和状态。
- `st.toast` 消息可以通过额外的 `.toast()` 调用原位更新。

## `st.empty` 容器

`st.empty` 可以容纳单个元素。当你向 `st.empty` 容器写入任何元素时，Streamlit 会丢弃其以前的内容并显示新元素。你也可以通过调用 `.empty()` 作为方法来清除 `st.empty` 容器。如果你想更新一组元素，请使用放在 `st.empty` 内的普通容器（`st.container()`）并向普通容器写入内容。根据需要经常重写普通容器及其内容以更新应用的显示。

## `.add_rows()` 方法

`st.dataframe`、`st.table` 和所有图表函数可以使用其输出上的 `.add_rows()` 方法进行变异。在以下示例中，我们使用 `my_data_element = st.line_chart(df)`。你可以通过简单地交换 `st.line_chart` 来尝试 `st.table`、`st.dataframe` 和大多数其他简单图表的示例。请注意，`st.dataframe` 默认只显示前十行，并为其他行启用滚动。这意味着添加行不如使用 `st.table` 或图表元素那样在视觉上明显。

```python
import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")
```
