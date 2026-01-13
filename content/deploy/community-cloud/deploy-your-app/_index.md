---
title: 在 Community Cloud 上准备和部署应用
slug: /deploy/streamlit-community-cloud/deploy-your-app
description: Streamlit 应用在 Community Cloud 上的部署完整指南，涵盖项目结构、依赖管理和密钥配置。
keywords: deploy, community cloud, preparation, file organization, dependencies, secrets, deployment guide
---

# 在 Community Cloud 上准备和部署应用

Streamlit Community Cloud 支持一键部署，大多数应用可在数分钟内完成部署。若无现成应用，可从 <a href="https://streamlit.io/gallery" target="_blank">应用库</a>中 fork 或克隆示例项目——涵盖机器学习、数据可视化、数据分析、A/B 测试等多种场景。你也可以[使用模板快速部署](/deploy/streamlit-community-cloud/get-started/deploy-from-a-template)。应用部署后，可[通过 GitHub Codespaces 进行在线编辑](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app#edit-your-app-with-github-codespaces)。

<Note>

如需在其他云平台部署应用，请参阅[部署指南](/deploy/tutorials)。

</Note>

## 概述

以下内容说明如何组织项目结构，为 Community Cloud 提供必要配置以确保应用正常运行。

准备就绪后，部署流程十分简洁。进入工作区，点击右上角的"**新建应用**"。按照向导完成应用信息配置，最后点击"**部署**"。

![从工作区部署新应用](/images/streamlit-community-cloud/deploy-empty-new-app.png)

## 核心步骤

<InlineCalloutContainer>
    <InlineCallout
        color="lightBlue-70"
        icon="description"
        bold="项目结构"
        href="/deploy/streamlit-community-cloud/deploy-your-app/file-organization"
    >了解 Community Cloud 应用初始化机制及路径解析规则。掌握配置文件的放置位置。</InlineCallout>
    <InlineCallout
        color="lightBlue-70"
        icon="build_circle"
        bold="依赖管理"
        href="/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies"
    >学习如何声明依赖项，将 Python 库及其他依赖安装到运行时环境。</InlineCallout>
    <InlineCallout
        color="lightBlue-70"
        icon="password"
        bold="密钥管理"
        href="/deploy/streamlit-community-cloud/deploy-your-app/secrets-management"
    >掌握 Community Cloud 提供的密钥管理接口，安全上传 <code>secrets.toml</code> 配置。</InlineCallout>
    <InlineCallout
        color="lightBlue-70"
        icon="flight_takeoff"
        bold="部署应用"
        href="/deploy/streamlit-community-cloud/deploy-your-app/deploy"
    >整合所有配置，将应用发布到生产环境。</InlineCallout>
</InlineCalloutContainer>
