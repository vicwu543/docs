---
title: 如何使用st.file_uploader检索上传的文件的文件名？
slug: /knowledge-base/using-streamlit/retrieve-filename-uploaded
---

# 如何使用st.file_uploader检索上传的文件的文件名？

对于上传单个文件时`accept_multiple_files=False`，你可以通过返回的UploadedFile对象使用`.name`属性来获取文件名。

```python
import streamlit as st

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
   st.write("Filename: ", uploaded_file.name)
```

对于上传多个文件时`accept_multiple_files=True`，你可以通过返回的列表中的每个UploadedFile对象使用`.name`属性来获取每个上传的文件名。

```python
import streamlit as st

uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)

if uploaded_files:
   for uploaded_file in uploaded_files:
       st.write("Filename: ", uploaded_file.name)
```

相关论坛帖子：

- https://discuss.streamlit.io/t/is-it-possible-to-get-uploaded-file-file-name/7586

