---
title: 如何将 Pandas DataFrame 下载为 CSV？
slug: /knowledge-base/using-streamlit/how-download-pandas-dataframe-csv
---

# 如何将 Pandas DataFrame 下载为 CSV？

使用 Streamlit 中原生内置的 [`st.download_button`](/develop/api-reference/widgets/st.download_button) 小部件。查看一个 [示例应用](https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/)，演示如何使用 `st.download_button` 下载常见的文件格式。

## 使用示例

```python
import streamlit as st
import pandas as pd

df = pd.read_csv("dir/file.csv")

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
```

其他资源：

- [https://blog.streamlit.io/0-88-0-release-notes/](https://blog.streamlit.io/0-88-0-release-notes/)
- [https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/](https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/)
- https://docs.streamlit.io/develop/api-reference/widgets/st.download_button
