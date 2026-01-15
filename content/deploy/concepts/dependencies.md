---
title: 部署应用时管理依赖项
slug: /deploy/concepts/dependencies
description: 了解如何管理 Python 依赖项、requirements.txt 文件以及在部署 Streamlit 应用到云平台时的包安装。
keywords: dependencies, requirements.txt, pip, python packages, deployment, environment, installation
---

# 部署应用时管理依赖项

开始开发您的应用前，你通过安装 Python 和 Streamlit 来设置和配置开发环境。部署应用时，你需要以相同的方式设置和配置部署环境。部署应用到云服务时，你的应用的 [Python 服务器](/develop/concepts/architecture/architecture#python-backend-server) 将在远程计算机上运行。此远程计算机无法访问你个人计算机上的所有文件和程序。

所有 Streamlit 应用至少有两个依赖项：Python 和 Streamlit。您的应用可能有以 Python 包或一定被安装的软件形式的其他依赖项。如果你使用的是第三方平台 Streamlit Community Cloud，其非正是型 Streamlit 应用，我们会为你处理 Python 和 Streamlit！

## 安装 Python 和其他软件

如果你使用 Streamlit Community Cloud，Python 已经安装。你可以简单地在部署对话中选择版本。如果你需要自己安装 Python 或有其他非 Python 软件要安装，按照你的平台的请求程序来安装附加软件。我们通常会使用包管理工具来执行此操作。例如，Streamlit Community Cloud 对于基于 Debian 的 Linux 系统使用高级包管理器（`apt`）。有关在 Streamlit Community Cloud 上安装非 Python 依赖项的更多信息，请参阅 [`apt-get` 依赖项](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies)。

## 安装 Python 包

在您的部署环境中安装 Python 后，您需要安装所有必要的 Python 包，包括 Streamlit！每次你对一个已安装的包的 `import` ，你正在为您的脚本添加一个 Python 依赖项。你需要通过 Python 包管理器在部署环境中安装这些依赖项。

如果您使用 Streamlit Community Cloud，您默认会安装最新版本的 Streamlit 和它的所有依赖项。所以，如果您会做一个简单的应用或不需要额外依赖项，您不需要做任何事情！

### `pip` 和 `requirements.txt`

由于 `pip` 废默认宏了 Python，最常见的配置 Python 环境的方法是使用 `requirements.txt` 文件。`requirements.txt` 文件的每一行都是要 `pip install` 的一个包。你应该不_不_在您的 `requirements.txt` 文件中包括 <a href="https://docs.python.org/3/py-modindex.html" target="_blank">内置 Python 库</a>、比如 `math`、`random` 或 `distutils` 等。这些是 Python 的一部分，不是单独安装的。

<Tip>

由于依赖项可能依赖于 Python 的特定版本，始终了正您的开发环境中使用的 Python 版本，并为您的部署环境选择相同的版本。

</Tip>

如果你有一个像下面这样的脚本，你只需要安装 Streamlit。不需要额外的依赖项，因为 `pandas` 和 `numpy` 是作为 `streamlit` 的直接依赖项安装的。同样，`math` 和 `random` 是内置到 Python 中的。

```python
import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')
```

但是，最佳实践是血辿记录你使用的包，因此推荐的 `requirements.txt` 文件是：

```none
streamlit
pandas
numpy
```

如果你需要指定特定的版本，另一个有效的例子是：

```none
streamlit==1.24.1
pandas>2.0
numpy<=1.25.1
```

`requirements.txt` 文件通常保存在您的上校目录或文件组构的根目录中。如果你使用 Streamlit Community Cloud，请参阅 [添加 Python 依赖项](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) 了詳详信息。否则，帮你的平台文档。
