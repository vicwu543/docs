---
title: Snowflake 中的 Streamlit
slug: /deploy/snowflake
description: 在 Snowflake 中部署 Streamlit 应用，为企业级安全性和与原生应用和容器服务的数据集成。
keywords: snowflake, enterprise, security, data, native apps, container services, deployment
---

# 在 Snowflake 中部署 Streamlit 应用

在单个全球平台中与您的数据一起托管您的应用。Snowflake 提供行业领先的功能，为您的账户、用户、数据和应用提供最高级别的安全性。如果您正在寻找企业托管解决方案，请尝试 Snowflake！

<TileContainer>
    <Tile
        icon="rocket_launch"
        title="Snowflake 中的 Streamlit 快速入门"
        text="创建免费试用账户并使用 Snowflake 中的 Streamlit 部署应用。"
        link="/get-started/installation/streamlit-in-snowflake"
        background="lightBlue-70"
    />
    <Tile
        icon="code"
        title="示例"
        text="在 Snowflake Labs 的 snowflake-demo-streamlit 存储库中探索各种示例应用。"
        link="https://github.com/Snowflake-Labs/snowflake-demo-streamlit"
        background="lightBlue-70"
    />
    <Tile
        icon="book"
        title="Snowflake 入门"
        text="了解更多 Snowflake 的文档。"
        link="https://docs.snowflake.com/user-guide-getting-started"
        background="lightBlue-70"
    />
</TileContainer>

在 Snowflake 中有三种方式来托管 Streamlit 应用：

<InlineCalloutContainer>
    <InlineCallout
        color="lightBlue-70"
        icon="bolt"
        bold="Snowflake 中的 Streamlit。"
        href="https://docs.snowflake.com/developer-guide/streamlit/about-streamlit"
    >以 Snowflake 中的原生对象运行您的 Streamlit 应用。享受浏览器内编辑器和最少的环境配置工作。通过基于角色的访问控制 (RBAC) 与 Snowflake 账户中的其他用户共享您的应用。这是为您的业务内部部署应用的好方式。查看 Snowflake 文档！</InlineCallout>
    <InlineCallout
        color="lightBlue-70"
        icon="ac_unit"
        bold="Snowflake 原生应用。"
        href="https://docs.snowflake.com/en/developer-guide/native-apps/adding-streamlit"
    >将您的应用与数据打包并与其他 Snowflake 账户共享。这是与使用 Snowflake 的其他组织共享应用及其底层数据的好方式。查看 Snowflake 文档！</InlineCallout>
    <InlineCallout
        color="lightBlue-70"
        icon="web_asset"
        bold="Snowpark 容器服务。"
        href="https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview"
    >在针对 Snowflake 运行进行了优化的容器中部署您的应用。这是最灵活的选项，您可以使用任何库并为应用分配公共 URL。通过您的 Snowflake 账户管理您的允许查看者。查看 Snowflake 文档！</InlineCallout>
</InlineCalloutContainer>

<Note>

    使用 Snowpark 容器服务部署 Streamlit 应用需要计算池，目前在试用账户中不可用。

</Note>
