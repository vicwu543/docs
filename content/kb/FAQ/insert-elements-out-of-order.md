---
title: 如何按不同的顺序插入元素？
slug: /knowledge-base/using-streamlit/insert-elements-out-of-order
---

# 如何按不同的顺序插入元素？

您可以使用 [`st.empty`](/develop/api-reference/layout/st.empty) 方法作为占位符，以"保留"应用中的一个槽，您可以稍后使用。

```python
st.text('This will appear first')
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text('This will appear last')
# Appends some more text to the app.

my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.
```
