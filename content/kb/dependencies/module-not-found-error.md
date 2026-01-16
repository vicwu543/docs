---
title: "ModuleNotFoundError: No module named"
slug: /knowledge-base/dependencies/module-not-found-error
---

# ModuleNotFoundError: No module named

## 问题

在[Streamlit Community Cloud](https://streamlit.io/cloud)上部署应用时，你会收到错误 `ModuleNotFoundError: No module named`。

## 解决方案

当你在 Streamlit Community Cloud 上导入一个未包含在 requirements 文件中的模块时，会发生此错误。任何不与[标准 Python 安装](https://docs.python.org/3/py-modindex.html)一起分发的外部[Python 依赖项](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies)都应包含在 requirements 文件中。

例如，如果你不在 requirements 文件中包含 `scikit-learn` 并在你的应用中 `import sklearn`，你会看到 `ModuleNotFoundError: No module named 'sklearn'`。

相关主论坛帖子：

- https://discuss.streamlit.io/t/getting-error-modulenotfounderror-no-module-named-beautifulsoup/9126
- https://discuss.streamlit.io/t/modulenotfounderror-no-module-named-vega-datasets/16354
