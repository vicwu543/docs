---
title: 组件
slug: /develop/concepts/custom-components
description: 了解如何构建和使用自定义 Streamlit 组件，以使用第三方 Python 模块和自定义 UI 元素扩展应用功能。
keywords: 自定义组件, 第三方模块, 组件开发, 扩展功能, 自定义 UI, 组件集成, Streamlit 组件
---

# 自定义组件

组件是扩展 Streamlit 可能性的第三方 Python 模块。

## 如何使用组件

组件非常容易使用：

1. 首先找到您想要使用的组件。两个很好的资源是：
   - [组件画廊](https://streamlit.io/components)
   - [此线程](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)，
     由我们的论坛的 Fanilo A. 提供。

2. 使用您喜欢的 Python 包管理器安装组件。此步骤以及所有后续步骤都在您的组件说明中描述。

   例如，要使用出色的 [AgGrid 组件](https://github.com/PablocFonseca/streamlit-aggrid)，您首先使用以下命令安装它：

   ```python
   pip install streamlit-aggrid
   ```

3. 在您的 Python 代码中，按照其说明导入组件。对于 AgGrid，此步骤是：

   ```python
   from st_aggrid import AgGrid
   ```

4. ...现在您准备好使用它了！对于 AgGrid，就是：

   ```python
   AgGrid(my_dataframe)
   ```

## 制作您自己的组件

如果您有兴趣制作自己的组件，请查看以下资源：

- [创建组件](/develop/concepts/custom-components/create)
- [发布组件](/develop/concepts/custom-components/publish)
- [组件 API](/develop/concepts/custom-components/intro)
- [我们推出组件时的博客文章！](https://blog.streamlit.io/introducing-streamlit-components/)

或者，如果您喜欢使用视频学习，我们的工程师 Tim Conkling 准备了一些令人惊叹的教程：

##### 视频教程，第 1 部分

<YouTube videoId="BuD3gILJW-Q" />

##### 视频教程，第 2 部分

<YouTube videoId="QjccJl_7Jco" />
