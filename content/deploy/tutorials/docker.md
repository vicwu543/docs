---
title: 使用 Docker 部署 Streamlit
slug: /deploy/tutorials/docker
description: 了解如何使用 Docker 容器化和部署 Streamlit 应用，包含公司网络和云部署的分步说明。
keywords: docker, 容器化, 部署, 公司网络, 云, dockerfile, 构建, 运行, 端口映射
---

# 使用 Docker 部署 Streamlit

## 介绍

你有一个了不起的应用，想开始与他人分享，你应该怎么做？你有几个选择。首先，你想在哪里运行你的 Streamlit 应用，你想如何访问它？

- **在你的公司网络上** - 大多数公司网络与外部世界隔离。你通常使用 VPN 登录到公司网络并访问那里的资源。出于安全原因，你可以在公司网络的服务器上运行 Streamlit 应用，以确保只有公司内部的人才能访问它。
- **在云上** - 如果你想从公司网络外部访问 Streamlit 应用，或与不在你的家庭网络或笔记本电脑上的人分享应用，你可能会选择此选项。在这种情况下，这取决于你的托管提供商。我们有来自 Heroku、AWS 和其他提供商的[社区提交的指南](/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud)。

无论你决定在哪里部署应用，你首先需要将其容器化。本指南将指导你使用 Docker 部署应用。如果你更喜欢 Kubernetes，请参阅[使用 Kubernetes 部署 Streamlit](/deploy/tutorials/kubernetes)。

## 前置条件

1. [安装 Docker Engine](#install-docker-engine)
2. [检查网络端口可访问性](#check-network-port-accessibility)

### 安装 Docker Engine

如果你还没有安装，请在服务器上安装 [Docker](https://docs.docker.com/engine/install/#server)。Docker 提供来自许多 Linux 发行版的 `.deb` 和 `.rpm` 包，包括：

- [Debian](https://docs.docker.com/engine/install/debian/)
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

通过运行 `hello-world` Docker 镜像验证 Docker Engine 已正确安装：

```bash
sudo docker run hello-world
```

<Tip>

遵循 Docker 的官方[Linux 后安装步骤](https://docs.docker.com/engine/install/linux-postinstall/)，以便以非 root 用户身份运行 Docker，这样你就不必在 `docker` 命令前加上 `sudo`。

</Tip>

### 检查网络端口可访问性

当你和你的用户在公司 VPN 后面时，你需要确保你们都可以访问特定的网络端口。假设端口 `8501`，因为它是 Streamlit 使用的默认端口。联系你的 IT 团队并请求为你和你的用户开放端口 `8501` 的访问权限。

## 创建 Dockerfile

Docker 通过读取 `Dockerfile` 中的指令来构建镜像。`Dockerfile` 是一个文本文档，包含用户可在命令行上调用以组建镜像的所有命令。在 [Dockerfile 参考](https://docs.docker.com/engine/reference/builder/)中了解更多信息。[docker build](https://docs.docker.com/engine/reference/commandline/build/) 命令从 `Dockerfile` 构建镜像。[docker run](https://docs.docker.com/engine/reference/commandline/run/) 命令首先在指定的镜像上创建一个容器，然后使用指定的命令启动它。

下面是一个 `Dockerfile` 示例，你可以将其添加到目录的根目录，即 `/app/`

```docker
# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Dockerfile 演练

让我们逐行演练 Dockerfile：

1. `Dockerfile` 必须以 [`FROM`](https://docs.docker.com/engine/reference/builder/#from) 指令开始。它为容器设置[基础镜像](https://docs.docker.com/glossary/#base-image)（想象成操作系统）：

   ```docker
   FROM python:3.9-slim
   ```

   Docker 有许多基于各种 Linux 发行版的官方 Docker 基础镜像。它们还有随附语言特定模块的基础镜像，例如 [Python](https://hub.docker.com/_/python)。`python` 镜像有许多变种，每一个都为特定用途而设计。在这里，我们使用 `python:3.9-slim` 镜像，这是一个轻量级镜像，附带最新版本的 Python 3.9。

   <Tip>

   你也可以使用自己的基础镜像，前提是你使用的镜像包含 [Streamlit 支持的 Python 版本](/knowledge-base/using-streamlit/sanity-checks#check-0-are-you-using-a-streamlit-supported-version-of-python)。使用任何特定基础镜像没有一刀切的方法，也没有官方的 Streamlit 特定基础镜像。

   </Tip>

2. `WORKDIR` 指令为 `Dockerfile` 中后续的任何 `RUN`、`CMD`、`ENTRYPOINT`、`COPY` 和 `ADD` 指令设置工作目录。让我们将其设置为 `app/`：

   ```docker
   WORKDIR /app
   ```

   <Important>

   如[开发流程](/get-started/fundamentals/main-concepts#development-flow)中所述，对于 Streamlit 版本 1.10.0 及更高版本，Streamlit 应用无法从 Linux 发行版的根目录运行。你的主脚本应该位于除根目录之外的目录中。如果你尝试从根目录运行 Streamlit 应用，Streamlit 将抛出 `FileNotFoundError: [Errno 2] No such file or directory` 错误。有关更多信息，请参阅 GitHub 问题 [#5239](https://github.com/streamlit/streamlit/issues/5239)。

   如果你使用的是 Streamlit 版本 1.10.0 或更高版本，你必须将 `WORKDIR` 设置为除根目录以外的目录。例如，你可以将 `WORKDIR` 设置为 `/app`，如上面的示例 `Dockerfile` 中所示。
   </Important>

3. 安装 `git` 以便我们可以从远程仓库克隆应用代码：

   ```docker
   RUN apt-get update && apt-get install -y \
       build-essential \
       curl \
       software-properties-common \
       git \
       && rm -rf /var/lib/apt/lists/*
   ```

4. 将你驻留在远程仓库中的代码克隆到 `WORKDIR`：

   a. 如果你的代码在公开仓库中：

   ```docker
   RUN git clone https://github.com/streamlit/streamlit-example.git .
   ```

   克隆后，`WORKDIR` 的目录将如下所示：

   ```bash
   app/
   - requirements.txt
   - streamlit_app.py
   ```

   其中 `requirements.txt` 文件包含所有 [Python 依赖](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies)。例如

   ```
   altair
   pandas
   streamlit
   ```

   `streamlit_app.py` 是你的主脚本。例如

   ```python
   from collections import namedtuple
   import altair as alt
   import math
   import pandas as pd
   import streamlit as st

   """
   # Welcome to Streamlit!

   Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

   If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
   forums](https://discuss.streamlit.io).

   In the meantime, below is an example of what you can do with just a few lines of code:
   """

   with st.echo(code_location='below'):
      total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
      num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

      Point = namedtuple('Point', 'x y')
      data = []

      points_per_turn = total_points / num_turns

      for curr_point_num in range(total_points):
         curr_turn, i = divmod(curr_point_num, points_per_turn)
         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
         radius = curr_point_num / total_points
         x = radius * math.cos(angle)
         y = radius * math.sin(angle)
         data.append(Point(x, y))

      st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
         .mark_circle(color='#0068c9', opacity=0.5)
         .encode(x='x:Q', y='y:Q'))
   ```

   b. 如果你的代码在私有仓库中，请阅读[在构建中使用 SSH 访问私有数据](https://docs.docker.com/develop/develop-images/build_enhancements/#using-ssh-to-access-private-data-in-builds)并相应地修改 Dockerfile - 安装 SSH 客户端，下载 [github.com](https://github.com) 的公钥，并克隆你的私有仓库。如果你使用 GitLab 或 Bitbucket 等替代 VCS，请查阅该 VCS 的文档，了解如何将你的代码复制到 Dockerfile 的 `WORKDIR`。

   c. 如果你的代码与 Dockerfile 位于同一目录中，通过用以下内容替换 `git clone` 行，将所有应用文件（包括 `streamlit_app.py`、`requirements.txt` 等）从你的服务器复制到容器中：

   ```docker
   COPY . .
   ```

   更一般地说，目的是将你的应用代码从它驻留在服务器上的任何地方复制到容器中。如果代码不在与 Dockerfile 相同的目录中，请修改上述命令以包含代码的路径。

5. 从克隆的容器中的 `requirements.txt` 安装应用的 [Python 依赖](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies)：

   ```docker
   RUN pip3 install -r requirements.txt
   ```

6. [`EXPOSE`](https://docs.docker.com/engine/reference/builder/#expose) 指令告知 Docker 容器在运行时监听指定的网络端口。你的容器需要监听 Streamlit 的（默认）端口 8501：

   ```docker
   EXPOSE 8501
   ```

7. [`HEALTHCHECK`](https://docs.docker.com/engine/reference/builder/#expose) 指令告诉 Docker 如何测试容器以检查它是否仍在工作。你的容器需要监听 Streamlit 的（默认）端口 8501：

   ```docker
   HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
   ```

8. [`ENTRYPOINT`](https://docs.docker.com/engine/reference/builder/#entrypoint) 允许你配置一个作为可执行文件运行的容器。在这里，它还包含应用的整个 `streamlit run` 命令，因此你不必从命令行调用它：

   ```docker
   ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

## 构建 Docker 镜像

[`docker build`](https://docs.docker.com/engine/reference/commandline/build/) 命令从 `Dockerfile` 构建镜像。从服务器上的 `app/` 目录运行以下命令来构建镜像：

```docker
docker build -t streamlit .
```

`-t` 标志用于标记镜像。在这里，我们标记了镜像 `streamlit`。如果你运行：

```docker
docker images
```

你应该在 REPOSITORY 列下看到 `streamlit` 镜像。例如：

```
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
streamlit    latest    70b0759a094d   About a minute ago   1.02GB
```

## 运行 Docker 容器

现在你已构建了镜像，你可以通过执行以下命令来运行容器：

```docker
docker run -p 8501:8501 streamlit
```

`-p` 标志将容器的端口 8501 发布到服务器的 8501 端口。

如果一切顺利，你应该看到类似于以下的输出：

```
docker run -p 8501:8501 streamlit

  You can now view your Streamlit app in your browser.

  URL: http://0.0.0.0:8501
```

要查看你的应用，用户可以浏览到 `http://0.0.0.0:8501` 或 `http://localhost:8501`

<Note>

根据你的服务器的网络配置，你可以映射到端口 80/443，以便用户可以使用服务器 IP 或主机名查看你的应用。例如：`http://your-server-ip:80` 或 `http://your-hostname:443`。

</Note>
