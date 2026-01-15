---
title: 处理时区
slug: /develop/concepts/design/timezone-handling
description: 了解 Streamlit 如何处理时区，包括在不同用户时区中显示日期时间信息的最佳实践。
keywords: 时区, 时区处理, 日期时间, 时区感知, 朴素日期时间, 时区转换, 时间显示, 国际用户, 时区最佳实践
---

# 处理时区

一般来说，处理时区可能很棘手。你的 Streamlit 应用用户不一定与运行你的应用的服务器位于同一时区。对于公开应用尤其如此，世界上任何时区的任何人都可以访问你的应用。因此，了解 Streamlit 如何处理时区至关重要，这样你可以避免在显示 `datetime` 信息时出现意外行为。

## Streamlit 如何处理时区

Streamlit 始终在前端显示 `datetime` 信息与其后端对应 `datetime` 实例相同的信息。即，日期或时间信息不会自动调整到用户的时区。我们区分以下两种情况：

### **不带时区的 `datetime` 实例（朴素）**

当你提供 _不指定时区的_ `datetime` 实例时，前端会显示没有时区信息的 `datetime` 实例。例如（这也适用于其他小部件，如 [`st.dataframe`](/develop/api-reference/data/st.dataframe)）：

```python
import streamlit as st
from datetime import datetime

st.write(datetime(2020, 1, 10, 10, 30))
# 输出: 2020-01-10 10:30:00
```

上面应用的用户始终看到输出为 `2020-01-10 10:30:00`。

### **带时区的 `datetime` 实例**

当你提供 _并指定时区的_ `datetime` 实例时，前端会显示该时区中的 `datetime` 实例。例如（这也适用于其他小部件，如 [`st.dataframe`](/develop/api-reference/data/st.dataframe)）：

```python
import streamlit as st
from datetime import datetime
import pytz

st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
# 输出: 2020-01-10 10:30:00-05:00
```

上面应用的用户始终看到输出为 `2020-01-10 10:30:00-05:00`。

在这两种情况下，日期或时间信息都不会在前端自动调整到用户的时区。用户看到的与后端对应的 `datetime` 实例相同。目前不可能自动将日期或时间信息调整到查看应用的用户的时区。

<Note>

`st.dataframe` 的旧版本在时区方面有问题。我们不计划为旧版数据框推出额外的修复或增强功能。如果你需要稳定的时区支持，请考虑通过更改[配置设置](/develop/concepts/configuration)来切换到箭头序列化，_config.dataFrameSerialization = "arrow"_。

</Note>
