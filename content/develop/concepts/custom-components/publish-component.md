---
title: 发布组件
slug: /develop/concepts/custom-components/publish
description: 了解如何将 Streamlit 自定义组件发布到 PyPI，使其可被全球 Python 社区和 Streamlit 用户访问。
keywords: publish component, PyPI publishing, component distribution, package publishing, component sharing, public components, Python package distribution
---

# 发布组件

## 发布到 PyPI

将您的 Streamlit 组件发布到 [PyPI](https://pypi.org/) 可以让全世界的 Python 用户轻松访问。这一步完全是可选的，如果您不打算公开发布组件，可以跳过此部分！

<Note>

对于[静态 Streamlit 组件](/develop/concepts/custom-components/intro#create-a-static-component)，将 Python 包发布到 PyPI 遵循与[核心 PyPI 打包说明](https://packaging.python.org/tutorials/packaging-projects/)相同的步骤。静态组件可能只包含 Python 代码，因此一旦您的[setup.py](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py) 文件正确并且[生成了分发文件](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives)，您就可以准备[上传到 PyPI](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives)。

[双向 Streamlit 组件](/develop/concepts/custom-components/intro#create-a-bi-directional-component) 至少包含 Python 和 JavaScript 代码，因此在可以发布到 PyPI 之前需要稍作准备。本页面的其余部分重点介绍双向组件的准备工作。

</Note>

### 准备您的组件

双向 Streamlit 组件与纯 Python 库略有不同，因为它必须包含预编译的前端代码。这也是基础 Streamlit 的工作方式；当您 `pip install streamlit` 时，您得到的是一个 Python 库，其中包含的 HTML 和前端代码已编译为静态资源。

[component-template](https://github.com/streamlit/component-template) GitHub 仓库提供了发布到 PyPI 所需的文件夹结构。但在发布之前，您需要做一些整理工作：

1. 给您的组件命名（如果尚未命名）
   - 将 `template/my_component/` 文件夹重命名为 `template/<组件名称>/`
   - 将组件名称作为第一个参数传递给 `declare_component()`
2. 编辑 `MANIFEST.in`，将 `recursive-include` 的路径从 `package/frontend/build *` 更改为 `<组件名称>/frontend/build *`
3. 编辑 `setup.py`，添加组件名称和其他相关信息
4. 创建前端代码的发布构建。这将添加一个新目录 `frontend/build/`，其中包含已编译的前端：

   ```bash
   cd frontend
   npm run build
   ```

5. 将构建文件夹的路径作为 `path` 参数传递给 `declare_component`。（如果您使用模板 Python 文件，可以在文件顶部设置 `_RELEASE = True`）：

   ```python
      import streamlit.components.v1 as components

      # 将这个:
      # component = components.declare_component("my_component", url="http://localhost:3001")

      # 改为:
      parent_dir = os.path.dirname(os.path.abspath(__file__))
      build_dir = os.path.join(parent_dir, "frontend/build")
      component = components.declare_component("new_component_name", path=build_dir)
   ```

### 构建 Python wheel

更改默认的 `my_component` 引用，编译 HTML 和 JavaScript 代码并在 `components.declare_component()` 中设置新的组件名称后，您就可以构建 Python wheel：

1. 确保您拥有最新版本的 setuptools、wheel 和 twine

2. 从源代码构建 wheel：

   ```bash
    # 从组件的顶级目录运行此命令；即，
    # 包含 `setup.py` 的目录
    python setup.py sdist bdist_wheel
   ```

### 将 wheel 上传到 PyPI

创建 wheel 后，最后一步是上传到 PyPI。此处的说明重点介绍如何上传到 [Test PyPI](https://test.pypi.org/)，以便您可以在不用担心搞砸任何东西的情况下学习此过程的机制。上传到 PyPI 遵循相同的基本过程。

1. 如果还没有，请在 [Test PyPI](https://test.pypi.org/) 上创建一个账户
   - 访问 [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) 并完成步骤

   - 访问 [https://test.pypi.org/manage/account/#api-tokens](https://test.pypi.org/manage/account/#api-tokens) 并创建一个新的 API 令牌。不要将令牌作用域限制为特定项目，因为您正在创建一个新项目。在关闭页面之前复制您的令牌，因为您将无法再次检索它。

2. 将 wheel 上传到 Test PyPI。`twine` 将提示您输入用户名和密码。对于用户名，使用 **\_\_token\_\_**。对于密码，使用您上一步的令牌值，包括 `pypi-` 前缀：

   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

3. 在新 Python 项目中安装您刚刚上传的包以确保它能正常工作：

   ```bash
    python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
   ```

如果一切顺利，您就可以按照 [https://packaging.python.org/tutorials/packaging-projects/#next-steps](https://packaging.python.org/tutorials/packaging-projects/#next-steps) 上的说明将您的库上传到 PyPI。

恭喜，您已经创建了一个公开可用的 Streamlit 组件！

## 推广您的组件！

我们很高兴帮助您与 Streamlit 社区分享您的组件！要分享它：

1. 如果您的代码托管在 GitHub 上，请添加 `streamlit-component` 标签，以便它被列入 [GitHub **streamlit-component** 主题](https://github.com/topics/streamlit-component) 中：

   <Image caption="将 streamlit-component 标签添加到您的 GitHub 仓库" src="/images/component-tag.gif" />

2. 在 Streamlit 论坛的 [展示社区！](https://discuss.streamlit.io/c/streamlit-examples/9) 中发帖。使用类似"新组件：`<您的组件名称>`，一种实现 X 的新方式"的帖子标题。
3. 将您的组件添加到 [社区组件跟踪器](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)。
4. 在 Twitter 上 @[@streamlit](https://twitter.com/streamlit) 发帖，以便我们可以转发您的公告。

我们的[组件库](https://streamlit.io/components) 大约每月更新一次。遵循以上建议以最大化您的组件进入我们组件库的可能性。我们文档中的社区组件是不定期手工策划的。受欢迎的、有很多星标和良好文档的组件更有可能被选中。