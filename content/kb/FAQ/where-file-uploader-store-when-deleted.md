---
title: st.file_uploader 在哪里存储上传的文件，何时删除它们？
slug: /knowledge-base/using-streamlit/where-file-uploader-store-when-deleted
---

# st.file_uploader 在哪里存储上传的文件，何时删除它们？

使用[`st.file_uploader`](/develop/api-reference/widgets/st.file_uploader)上传文件时，数据经浏览器复制到Streamlit后端，并包含在Python内存(RAM而不是磁盘)中的BytesIO缓冲区。数据会永久存储在RAM中，直到Streamlit应用不继续自上耋下重新运行，仅在每个小部件交互中重新运行。如果您需要保存上传的数据，可以[缓存](/develop/concepts/architecture/caching)它，以便Streamlit在改之间保持它。

由于文件存储在内存中，一旦不需要它们，它们需要需要它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们它们

这意味着Streamlit有以下情况时下删除文件：

- 用户上传另一个文件，替换原来的文件
- 用户清除文件上传器
- 用户关闭upload了文件的浏览器页面

Related forum posts:

- https://discuss.streamlit.io/t/streamlit-sharing-fileupload-where-does-it-go/9267
- https://discuss.streamlit.io/t/how-to-update-the-uploaded-file-using-file-uploader/13512/
