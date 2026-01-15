---
title: Community Cloud应用的应用依赖
slug: /deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
description: 了解如何使用requirements.txt、packages.txt和其他包管理器为Community Cloud应用管理Python和外部依赖。
keywords: dependencies, requirements.txt, packages.txt, pip, apt-get, python packages, external dependencies, package managers
---

# Community Cloud应用的应用依赖

应用无法正确构建的主要原因是Streamlit Community Cloud找不到你的依赖！你的应用可能有两种依赖：Python依赖和外部依赖。Python依赖是你`import`到脚本中的其他Python包（就像Streamlit一样！）。外部依赖不太常见，但它们包括脚本正常运行所需的任何其他软件。由于Community Cloud在Linux上运行，这些将是在Python环境外使用`apt-get`安装的Linux依赖。

为了确保你的依赖被正确安装，请确保你：

1. 为Python依赖添加[需求文件](#add-python-dependencies)。
2. 可选：要管理任何外部依赖，请添加`packages.txt`文件。

<Note>

Python需求文件应放在你的仓库根目录或与你应用的入口文件相同的目录中。

</Note>

## 添加Python依赖

每当你在脚本中使用`import`语句时，你就引入了一个Python依赖。你需要告诉Community Cloud如何通过Python包管理器安装这些依赖。我们推荐使用`requirements.txt`文件，它基于`pip`。

你_不应该_在`requirements.txt`文件中包含<a href="https://docs.python.org/3/py-modindex.html" target="_blank">内置Python库</a>如`math`、`random`或`distutils`。这些是Python的一部分，不需要单独安装。另外，Community Cloud默认已安装了`streamlit`。除非你想固定或限制版本，否则不必严格包含`streamlit`。如果你部署的应用没有`requirements.txt`文件，你的应用将在只安装了`streamlit`（及其依赖）的环境中运行。

<Important>

Python的版本很重要！内置库在不同的Python版本之间会发生变化，其他库也可能有特定的版本要求。每当Streamlit支持新的Python版本时，Community Cloud会快速跟进并默认该新的Python版本。始终在与部署应用相同的Python版本中开发应用。有关部署应用时设置Python版本的更多信息，请参阅[可选：配置秘密和Python版本](/deploy/streamlit-community-cloud/deploy-your-app/deploy#optional-configure-secrets-and-python-version)。

</Important>

如果你有如下脚本，则不需要额外的依赖，因为`pandas`和`numpy`已安装为`streamlit`的直接依赖。同样，`math`和`random`是Python的内置库。

```python
import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write("Hi!")
```

但是，一个有效的`requirements.txt`文件将是：

```none
streamlit
pandas
numpy
```

或者，如果你需要指定某些版本，另一个有效的例子将是：

```none
streamlit==1.24.1
pandas>2.0
numpy<=1.25.1
```

在上面的例子中，`streamlit`被固定到版本`1.24.1`，`pandas`必须严格大于版本2.0，`numpy`必须在版本1.25.1或以下。你的`requirements.txt`文件中的每一行都是你想要在云环境中`pip install`的内容。

<Tip>
    要了解Community Cloud的Python环境的限制，请参阅[Community Cloud状态和限制](/deploy/streamlit-community-cloud/status#python-environments)。
</Tip>

### 其他Python包管理器

除了`pip`之外，还有其他Python包管理器。如果你想考虑使用`requirements.txt`文件的替代方案，Community Cloud将使用它找到的第一个依赖文件。Community Cloud将搜索你的入口文件所在的目录，然后将搜索你仓库的根目录。在每个位置中，依赖文件的优先顺序如下：

<table style={{ textAlign: 'center' }}>
    <tr>
        <th style={{ fontSize: '1.2em' }}> Recognized Filename</th>
        <th style={{ fontSize: '1.2em' }}>Python Package Manager</th>
    </tr>
    <tr>
        <td style={{ fontSize: '1em' }}><code>uv.lock</code></td>
        <td style={{ fontSize: '1em' }}><a href="https://docs.astral.sh/uv/concepts/projects/sync/" target="_blank">uv</a></td>
    </tr>
    <tr>
        <td style={{ fontSize: '1em' }}><code>Pipfile</code></td>
        <td style={{ fontSize: '1em' }}><a href="https://pipenv-fork.readthedocs.io/en/latest/basics.html" target="_blank">pipenv</a></td>
    </tr>
    <tr>
        <td style={{ fontSize: '1em' }}><code>environment.yml</code></td>
        <td style={{ fontSize: '1em' }}><a href="https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually" target="_blank">conda</a></td>
    </tr>
    <tr>
        <td style={{ fontSize: '1em' }}><code>requirements.txt</code></td>
        <td style={{ fontSize: '1em' }}><a href="https://pip.pypa.io/en/stable/user_guide/#requirements-files" target="_blank">pip</a><sup>&dagger;</sup></td>
    </tr>
    <tr>
        <td style={{ fontSize: '1em' }}><code>pyproject.toml</code></td>
        <td style={{ fontSize: '1em' }}><a href="https://python-poetry.org/docs/basic-usage/" target="_blank">poetry</a></td>
    </tr>
</table>

&dagger; 为了效率起见，Community Cloud将尝试使用`uv`处理`requirements.txt`，但在需要时将回退到`pip`。`uv`通常比`pip`更快更高效。

<Warning>

你应该只为你的应用使用一个依赖文件。如果你包含多个（例如`requirements.txt`和`environment.yaml`），如上所述，只会使用第一个找到的文件，入口文件目录中的任何依赖文件优先于仓库根目录中的任何依赖文件。

</Warning>

## apt-get dependencies

For many apps, a `packages.txt` file is not required. However, if your script requires any software to be installed that is not a Python package, you need a `packages.txt` file. Community Cloud is built on Debian Linux. Anything you want to `apt-get install` must go in your `packages.txt` file. To browse available packages that can be installed, see the Debian 11 ("bullseye") [package list](https://packages.debian.org/bullseye/).

If `packages.txt` exists in the root directory of your repository we automatically detect it, parse it, and install the listed packages. You can read more about apt-get in <a href="https://linux.die.net/man/8/apt-get" target="_blank">Linux documentation</a>.

Add **apt-get** dependencies to `packages.txt` &mdash; one package name per line. For example, <a href="https://github.com/PyMySQL/mysqlclient" target="_blank"><code>mysqlclient</code></a> is a Python package which requires additional software be installed to function. A valid `packages.txt` file to enable `mysqlclient` would be:

```bash
    build-essential
    pkg-config
    default-libmysqlclient-dev
```
