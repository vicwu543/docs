---
title: ImportError: libGL.so.1: 无法打开共享对象文件: 没有那个文件或目录
slug: /knowledge-base/dependencies/libgl
---

# ImportError: libGL.so.1: 无法打开共享对象文件: 没有那个文件或目录

## 问题

在[Streamlit Community Cloud](https://streamlit.io/cloud)上部署的应用中使用 OpenCV 时，你会收到错误 `ImportError: libGL.so.1: cannot open shared object file: No such file or directory`。

## 解决方案

如果你在应用中使用 OpenCV，在 Streamlit Community Cloud 的 requirements 文件中用 `opencv-python-headless` 代替 `opencv_contrib_python` 和 `opencv-python`。

如果 `opencv-python` 是你的应用或应用使用的库的依赖项的*必需*（非可选）依赖项，上述解决方案不适用。相反，你可以使用以下解决方案：

在你的仓库中创建一个 `packages.txt` 文件，包含以下行以安装[apt-get 依赖项](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies) `libgl`：

```
libgl1
```
