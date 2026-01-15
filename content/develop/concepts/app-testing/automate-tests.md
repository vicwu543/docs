---
title: 使用 CI 自动化测试
slug: /develop/concepts/app-testing/automate-tests
description: 了解如何将 Streamlit 应用测试与持续集成系统（如 GitHub Actions）集成以实现自动化测试工作流。
keywords: automated testing, ci testing, continuous integration, github actions, jenkins, gitlab ci, automated workflows, test automation, ci cd, deployment testing
---

# 使用 CI 自动化测试

应用测试的一个关键好处是可以使用持续集成（CI）来自动化测试。通过在开发过程中自动运行测试，您可以验证对应用的更改不会破坏现有功能。您可以在提交代码时验证应用代码，及早发现错误，并在部署前防止意外中断。

有许多流行的 CI 工具，包括 GitHub Actions、Jenkins、GitLab CI、Azure DevOps 和 Circle CI。Streamlit 应用测试可以轻松集成到其中任何一个工具中，类似于其他 Python 测试。

## GitHub Actions

由于许多 Streamlit 应用（以及所有社区云应用）都在 GitHub 中构建，本页面使用 [GitHub Actions](https://docs.github.com/en/actions) 的示例。有关 GitHub Actions 的更多信息，请参见：

- [GitHub Actions 快速入门](https://docs.github.com/en/actions/quickstart)
- [GitHub Actions：关于持续集成](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration)
- [GitHub Actions：构建和测试 Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

## Streamlit 应用 Action

[Streamlit 应用 Action](https://github.com/marketplace/actions/streamlit-app-action) 提供了一种简单的方法，将自动化测试添加到您在 GitHub 中的应用仓库中。它还包括对应用每个页面的基本冒烟测试，而无需您编写任何测试代码。

要安装 Streamlit 应用 Action，请在仓库的 `.github/workflows/` 文件夹中添加一个工作流 `.yml` 文件。例如：

```yaml
# .github/workflows/streamlit-app.yml
name: Streamlit 应用

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - uses: streamlit/streamlit-app-action@v0.0.3
        with:
          app-path: streamlit_app.py
```

让我们更详细地看看这个动作工作流在做什么。

### 触发工作流

```yaml
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
```

当针对 `main` 分支发起拉取请求时，以及推送到 `main` 分支的任何新提交时，将触发并执行此工作流。请注意，它还将对任何开放的拉取请求的后续提交执行测试。有关更多信息和示例，请参见 [GitHub Actions：触发工作流](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow)。

### 设置测试环境

```yaml
jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
```

工作流有一个执行一系列步骤的 `streamlit` 作业。该作业在使用 `ubuntu-latest` 镜像的 Docker 容器上运行。

- `actions/checkout@v4` 从 GitHub 检出当前仓库代码，并将代码复制到作业环境中。
- `actions/setup-python@v5` 安装 Python 3.11 版本。

### 运行应用测试

```yaml
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
```

Streamlit 应用 Action 执行以下操作：

- 安装 `pytest` 并安装 `requirements.txt` 中指定的任何依赖项。
- 运行内置的应用冒烟测试。
- 运行在仓库中找到的任何其他 Python 测试。

<Tip>

如果您的应用仓库根目录中不包含 `requirements.txt`，您需要添加一个步骤，使用您选择的包管理器安装依赖项，然后再运行 Streamlit 应用 Action。

</Tip>

内置冒烟测试具有以下行为：

- 在 AppTest 中运行 `app-path` 指定的应用。
- 验证它能成功完成且不会导致未捕获的异常。
- 对相对于 `app-path` 的应用任何附加 `pages/` 执行相同的操作。

如果您想在不使用冒烟测试的情况下运行 Streamlit 应用 Action，可以设置 `skip-smoke: true`。

### 检查应用代码

Linting 是对源代码进行程序性和风格错误的自动检查。这是通过使用 lint 工具（也称为 linter）完成的。Linting 对减少错误和提高代码的整体质量很重要，特别是对于有多个开发者的仓库或公共仓库。

您可以通过向 Streamlit 应用 Action 传递 `ruff: true` 来使用 [Ruff](https://docs.astral.sh/ruff/) 添加自动 linting。

```yaml
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
    ruff: true
```

<Tip>

您可能希望在本地开发环境中添加像 [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit) 这样的预提交钩子，在到达 CI 之前修复 linting 错误。

</Tip>

### 查看结果

如果测试失败，CI 工作流将失败，您将在 GitHub 中看到结果。通过点击工作流运行可以获取控制台日志，[如这里所述](https://docs.github.com/en/actions/using-workflows/about-workflows#viewing-the-activity-for-a-workflow-run)。

![](/images/test-results-logs.png)

对于更高级别的测试结果，您可以使用 [pytest-results-action](https://github.com/marketplace/actions/pytest-results-actions)。您可以将此与 Streamlit 应用 Action 结合使用，如下所示：

```yaml
# ... 如上设置 ...
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
    # 添加 pytest-args 以输出 junit xml
    pytest-args: -v --junit-xml=test-results.xml
- if: always()
  uses: pmeier/pytest-results-action@v0.6.0
  with:
    path: test-results.xml
    summary: true
    display-options: fEX
```

![](/images/test-results-summary.png)

## 编写自己的 Actions

以上只是一个示例。Streamlit 应用 Action 是一个快速入门的方法。一旦您学会了所选 CI 工具的基础知识，就很容易构建和自定义自己的自动化工作流。这对于提高开发者整体生产力和应用质量是非常好的方法。

## 工作示例

作为最终的工作示例，看看我们的 [`streamlit/llm-examples` Actions](https://github.com/streamlit/llm-examples/actions)，在[这个工作流文件](https://github.com/streamlit/llm-examples/blob/main/.github/workflows/app-testing.yml)中定义。