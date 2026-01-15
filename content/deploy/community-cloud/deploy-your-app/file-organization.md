---
title: Community Cloud应用的文件组织
slug: /deploy/streamlit-community-cloud/deploy-your-app/file-organization
description: 了解如何组织文件、依赖和配置以成功部署Community Cloud，包括子目录和多个应用。
keywords: 文件组织, 仓库结构, 入口文件, 依赖, 配置, 子目录, 多个应用, git lfs
---

# Community Cloud应用的文件组织

Streamlit Community Cloud复制仓库中的所有文件并从其根目录执行`streamlit run`。因为Community Cloud正在创建一个新的Python环境来运行你的应用，你需要包括对任何[应用依赖](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)的声明，以及任何[配置](/develop/concepts/configuration)选项。

你可以在你的仓库中有多个应用，其入口文件可以在仓库的任何位置。但是，你只能有一个配置文件。本页解释如何正确组织你的应用、配置和依赖文件。以下示例假设你使用`requirements.txt`来声明依赖，因为这是最常见的方式。如前一页所述，Community Cloud支持其他格式来配置你的Python环境。

## 基础示例

在以下示例中，入口文件（`your_app.py`）位于项目目录的根目录，与`requirements.txt`文件并排，以声明应用的依赖。

```
your_repository/
├── requirements.txt
└── your_app.py
```

如果你包括自定义配置，你的配置文件必须位于仓库内的`.streamlit/config.toml`。

```
your_repository/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── your_app.py
```

此外，应用需要本地可用的任何文件都应包括在仓库中。

<Tip>

如果你有非常大或二进制的数据，你经常更改，git运行缓慢，你可能想看看[Git Large File Store (LFS)](https://git-lfs.github.com/)作为在GitHub中存储大文件的更好方式。你不需要对应用做任何更改来开始使用它。如果你的GitHub仓库使用LFS，它将_正常工作_与Streamlit Community Cloud。

</Tip>

## 在子目录中使用入口文件

当入口文件在子目录中时，配置文件必须保留在根目录。但是，依赖文件可以在根目录或入口文件旁边。

你的依赖文件可以在仓库根目录，而入口文件在子目录中。

```
your_repository/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── subdirectory
    └── your_app.py
```

或者，你的依赖文件可以在与入口文件相同的子目录中。

```
your_repository/
├── .streamlit/
│   └── config.toml
└── subdirectory
    ├── requirements.txt
    └── your_app.py
```

虽然大多数Streamlit命令相对于入口文件解释路径，但某些命令相对于工作目录解释路径。在Community Cloud上，工作目录始终是仓库的根目录。因此，在本地开发和测试应用时，从仓库根目录执行`streamlit run`。这确保路径在本地环境和Community Cloud之间的解释一致。

在前面的示例中，这将看起来像这样：

```bash
cd your_repository
streamlit run subdirectory/your_app.py
```

<Tip>
    记住总是在你的路径中使用正斜杠路径分隔符。Community Cloud无法使用反斜杠分隔的路径。
</Tip>

## 仓库中的多个应用

当你在一个仓库中有多个应用时，它们共享仓库根目录的同一个配置文件（`.streamlit/config.toml`）。依赖文件可能为这些多个应用共享或单独配置。要为应用定义单独的依赖文件，将每个入口文件放在其自己的子目录中，以及其自己的依赖文件。要了解更多关于Community Cloud如何优先级和解析依赖文件，请参阅[应用依赖](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)。
