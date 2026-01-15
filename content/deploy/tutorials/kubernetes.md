---
title: 使用 Kubernetes 部署 Streamlit
slug: /deploy/tutorials/kubernetes
description: 了解如何使用 Kubernetes 部署你的 Streamlit 应用，包括 Google Container Registry、OAuth 认证和 TLS 支持。
keywords: kubernetes, k8s, 部署, gcr, google container registry, OAuth, 认证, tls, 负载均衡器, 编排
---

# 使用 Kubernetes 部署 Streamlit

## 介绍

你有一个了不起的应用，想开始与他人分享，你应该怎么做？你有几个选择。首先，你想在哪里运行你的 Streamlit 应用，你想如何访问它？

- **在你的公司网络上** - 大多数公司网络与外部世界隔离。你通常使用 VPN 登录到公司网络并访问那里的资源。出于安全原因，你可以在公司网络的服务器上运行 Streamlit 应用，以确保只有公司内部的人才能访问它。
- **在云上** - 如果你想从公司网络外部访问 Streamlit 应用，或与不在你的家庭网络或笔记本电脑上的人分享应用，你可能会选择此选项。在这种情况下，这取决于你的托管提供商。我们有来自 Heroku、AWS 和其他提供商的[社区提交的指南](/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud)。

无论你决定在哪里部署应用，你首先需要将其容器化。本指南将指导你使用 Kubernetes 部署应用。如果你更喜欢 Docker，请参阅[使用 Docker 部署 Streamlit](/deploy/tutorials/docker)。

## 前置条件

1. [安装 Docker Engine](#install-docker-engine)
2. [安装 gcloud CLI](#install-the-gcloud-cli)

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

### 安装 gcloud CLI

在本指南中，我们将使用 Kubernetes 编排 Docker 容器，并在 Google Container Registry (GCR) 上托管 docker 镜像。由于 GCR 是 Google 支持的 Docker 注册表，我们需要将 [`gcloud`](https://cloud.google.com/sdk/gcloud/reference) 注册为 Docker 凭证帮助程序。

按照官方文档[安装 gcloud CLI](https://cloud.google.com/sdk/docs/install) 并初始化它。

## 创建 Docker 容器

我们需要创建一个包含所有依赖和应用代码的 docker 容器。下面你可以看到入口点，即容器启动时运行的命令，以及 Dockerfile 定义。

### 创建入口点脚本

创建一个包含以下内容的 `run.sh` 脚本：

```bash
#!/bin/bash

APP_PID=
stopRunningProcess() {
    # Based on https://linuxconfig.org/how-to-propagate-a-signal-to-child-processes-from-a-bash-script
    if test ! "${APP_PID}" = '' && ps -p ${APP_PID} > /dev/null ; then
       > /proc/1/fd/1 echo "Stopping ${COMMAND_PATH} which is running with process ID ${APP_PID}"

       kill -TERM ${APP_PID}
       > /proc/1/fd/1 echo "Waiting for ${COMMAND_PATH} to process SIGTERM signal"

        wait ${APP_PID}
        > /proc/1/fd/1 echo "All processes have stopped running"
    else
        > /proc/1/fd/1 echo "${COMMAND_PATH} was not started when the signal was sent or it has already been stopped"
    fi
}

trap stopRunningProcess EXIT TERM

source ${VIRTUAL_ENV}/bin/activate

streamlit run ${HOME}/app/streamlit_app.py &
APP_ID=${!}

wait ${APP_ID}
```

### 创建 Dockerfile

Docker 通过读取 `Dockerfile` 中的指令来构建镜像。`Dockerfile` 是一个文本文档，包含用户可在命令行上调用以组建镜像的所有命令。在 [Dockerfile 参考](https://docs.docker.com/engine/reference/builder/)中了解更多信息。[docker build](https://docs.docker.com/engine/reference/commandline/build/) 命令从 `Dockerfile` 构建镜像。[docker run](https://docs.docker.com/engine/reference/commandline/run/) 命令首先在指定的镜像上创建一个容器，然后使用指定的命令启动它。

下面是一个可以添加到目录根目录的示例 `Dockerfile`。

```docker
FROM python:3.9-slim

RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid 1000 -ms /bin/bash appuser

RUN pip3 install --no-cache-dir --upgrade \
    pip \
    virtualenv

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git

USER appuser
WORKDIR /home/appuser

RUN git clone https://github.com/streamlit/streamlit-example.git app

ENV VIRTUAL_ENV=/home/appuser/venv
RUN virtualenv ${VIRTUAL_ENV}
RUN . ${VIRTUAL_ENV}/bin/activate && pip install -r app/requirements.txt

EXPOSE 8501

COPY run.sh /home/appuser
ENTRYPOINT ["./run.sh"]
```

<Important>

如[开发流程](/get-started/fundamentals/main-concepts#development-flow)中所述，对于 Streamlit 版本 1.10.0 及更高版本，Streamlit 应用无法从 Linux 发行版的根目录运行。你的主脚本应该位于除根目录之外的目录中。如果你尝试从根目录运行 Streamlit 应用，Streamlit 将抛出 `FileNotFoundError: [Errno 2] No such file or directory` 错误。有关更多信息，请参阅 GitHub 问题 [#5239](https://github.com/streamlit/streamlit/issues/5239)。

如果你使用的是 Streamlit 版本 1.10.0 或更高版本，你必须将 `WORKDIR` 设置为除根目录以外的目录。例如，你可以将 `WORKDIR` 设置为 `/home/appuser`，如上面的示例 `Dockerfile` 中所示。
</Important>

### 构建 Docker 镜像

将上述文件（`run.sh` 和 `Dockerfile`）放在同一文件夹中并构建 docker 镜像：

```docker
docker build --platform linux/amd64 -t gcr.io/<GCP_PROJECT_ID>/k8s-streamlit:test .
```

<Important>

将上述命令中的 `<GCP_PROJECT_ID>` 替换为你的 Google Cloud 项目的名称。

</Important>

### 将 Docker 镜像上传到容器注册表

下一步是将 Docker 镜像上传到容器注册表。在本示例中，我们将使用 [Google Container Registry (GCR)](https://cloud.google.com/container-registry)。首先启用 Container Registry API。登录 Google Cloud 并导航到你的项目的 **Container Registry**，然后单击 **Enable**。

我们现在可以从上一步构建 Docker 镜像并将其推送到我们的项目的 GCR。确保将 docker push 命令中的 `<GCP_PROJECT_ID>` 替换为你的项目名称：

```bash
gcloud auth configure-docker
docker push gcr.io/<GCP_PROJECT_ID>/k8s-streamlit:test
```

## 创建 Kubernetes 部署

对于此步骤，你需要：

- 正在运行的 Kubernetes 服务
- 可以为其生成 TLS 证书的自定义域
- DNS 服务，你可以在其中配置你的自定义域以指向应用程序 IP

由于镜像在上一步中已上传到容器注册表，我们可以使用以下配置在 Kubernetes 中运行它。

### 安装和运行 Kubernetes

确保你的 [Kubernetes 客户端](https://kubernetes.io/docs/tasks/tools/#kubectl) `kubectl` 已安装并在你的机器上运行。

### 配置 Google OAuth 客户端和 OAuth2-Proxy

有关配置 Google OAuth 客户端，请参阅 [Google Auth Provider](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider#google-auth-provider)。将 OAuth2-Proxy 配置为使用所需的 [OAuth 提供商配置](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider)，并更新配置映射中的 OAuth2-Proxy 配置。

以下配置包含一个处理 Google 认证的 OAuth2-Proxy sidecar 容器。你可以从 [`oauth2-proxy` 仓库](https://github.com/oauth2-proxy/oauth2-proxy)了解更多信息。

### 创建 Kubernetes 配置文件

创建一个名为 `k8s-streamlit.yaml` 的 [YAML](https://yaml.org/) [配置文件](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#organizing-resource-configurations)：

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: streamlit-configmap
data:
  oauth2-proxy.cfg: |-
    http_address = "0.0.0.0:4180"
    upstreams = ["http://127.0.0.1:8501/"]
    email_domains = ["*"]
    client_id = "<GOOGLE_CLIENT_ID>"
    client_secret = "<GOOGLE_CLIENT_SECRET>"
    cookie_secret = "<16, 24, or 32 bytes>"
    redirect_url = <REDIRECT_URL>

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: streamlit-deployment
  labels:
    app: streamlit
spec:
  replicas: 1
  selector:
    matchLabels:
      app: streamlit
  template:
    metadata:
      labels:
        app: streamlit
    spec:
      containers:
        - name: oauth2-proxy
          image: quay.io/oauth2-proxy/oauth2-proxy:v7.2.0
          args: ["--config", "/etc/oauth2-proxy/oauth2-proxy.cfg"]
          ports:
            - containerPort: 4180
          livenessProbe:
            httpGet:
              path: /ping
              port: 4180
              scheme: HTTP
          readinessProbe:
            httpGet:
              path: /ping
              port: 4180
              scheme: HTTP
          volumeMounts:
            - mountPath: "/etc/oauth2-proxy"
              name: oauth2-config
        - name: streamlit
          image: gcr.io/<GCP_PROJECT_ID>/k8s-streamlit:test
          imagePullPolicy: Always
          ports:
            - containerPort: 8501
          livenessProbe:
            httpGet:
              path: /_stcore/health
              port: 8501
              scheme: HTTP
            timeoutSeconds: 1
          readinessProbe:
            httpGet:
              path: /_stcore/health
              port: 8501
              scheme: HTTP
            timeoutSeconds: 1
          resources:
            limits:
              cpu: 1
              memory: 2Gi
            requests:
              cpu: 100m
              memory: 745Mi
      volumes:
        - name: oauth2-config
          configMap:
            name: streamlit-configmap

---
apiVersion: v1
kind: Service
metadata:
  name: streamlit-service
spec:
  type: LoadBalancer
  selector:
    app: streamlit
  ports:
    - name: streamlit-port
      protocol: TCP
      port: 80
      targetPort: 4180
```

<Important>

虽然上述配置可以逐字复制，但你必须更新以下占位符：`<GOOGLE_CLIENT_ID>`、`<GOOGLE_CLIENT_SECRET>`、`<REDIRECT_URL>` 和 `<GCP_PROJECT_ID>`。

</Important>

现在使用 [`kubectl create`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create) 命令从文件在 Kubernetes 中创建配置：

```bash
kubctl create -f k8s-streamlit.yaml
```

### 设置 TLS 支持

由于你使用 Google 认证，你需要设置 TLS 支持。在 [TLS 配置](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/tls)中了解如何执行此操作。

### 验证部署

创建部署和服务后，我们需要等待几分钟才能获得公开 IP 地址。我们可以通过运行以下命令来检查何时准备好：

```bash
kubectl get service streamlit-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

分配公开 IP 后，你需要在 DNS 服务中配置指向上述 IP 地址的 `A 记录`。
