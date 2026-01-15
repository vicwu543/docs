---
title: 如何增加Streamlit Community Cloud上st.file_uploader的上传限制？
slug: /knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud
---

# 如何增加Streamlit Community Cloud上st.file_uploader的上传限制？

## 概述

默认情况下，使用[`st.file_uploader()`](/develop/api-reference/widgets/st.file_uploader)上传的文件限制为200MB。你可以使用`server.maxUploadSize`配置选项配置此项。

Streamlit提供[四种不同的方法来设置配置选项](/develop/concepts/configuration)：

1. 在**全局配置文件**中，位macOS/Linux的`~/.streamlit/config.toml`或Windows的`%userprofile%/.streamlit/config.toml`：
   ```toml
   [server]
   maxUploadSize = 200
   ```
2. 在**每个项目配置文件**中，位于`$CWD/.streamlit/config.toml`，其中`$CWD`是你从中运行Streamlit的文件夹。
3. 通过`STREAMLIT_*`**一气辏式匉8渔字段**，例如：
   ```bash
   export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
   ```
4. 运行`streamlit run`时作为**命令行标志**：
   ```bash
   streamlit run your_script.py --server.maxUploadSize 200
   ```

对于部署到[Streamlit Community Cloud](/deploy/streamlit-community-cloud)的应用，你应该选择四种方案中的哪一个？🤔

## 解决方案

将应用部署到Streamlit Community Cloud时，你应该**使用方案 1**。即，在上传到应用GitHub仓库的全局配置文件(`.streamlit/config.toml`)中设置`maxUploadSize`配置选项。🎈

例如，要将上传限制增加到400MB，请将包含以下行的`.streamlit/config.toml`文件上传到应用的GitHub仓库：

```toml
[server]
maxUploadSize = 400
```

## 相关资源

- [Streamlit拖放限制为200MB，需要解决方案](https://discuss.streamlit.io/t/streamlit-drag-and-drop-capping-at-200mb-need-workaround/19803/2)
- [文件上传器小部件API](/develop/api-reference/widgets/st.file_uploader)
- [如何设置Streamlit配置选项](/develop/concepts/configuration)
