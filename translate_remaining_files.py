#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""翻译剩余的英文MD文件到中文"""

import os

# Define all translations for remaining files
translations = {
    "content/kb/FAQ/sanity-checks.md": {
        "title: Sanity checks": "title: 健全性检查",
        "# Sanity checks": "# 健全性检查",
        "If you're having problems running your Streamlit app, here are a few things to try out.": "如果您在运行 Streamlit 应用时遇到问题，这里有一些需要尝试的事情。",
        "## Check #0: Are you using a Streamlit-supported version of Python?": "## 检查 #0：您使用的是 Streamlit 支持的 Python 版本吗？",
        "Streamlit will maintain backwards-compatibility with earlier Python versions as practical,\nguaranteeing compatibility with _at least_ the last three minor versions of Python 3.": "Streamlit 将在实际可行的情况下保持与较早 Python 版本的向后兼容性，\n保证与 _至少_ Python 3 的最后三个次要版本兼容。",
        "As new versions of Python are released, we will try to be compatible with the new version as soon\nas possible, though frequently we are at the mercy of other Python packages to support these new versions as well.": "随着新的 Python 版本的发布，我们会尽快尝试与新版本兼容，尽管通常我们受到其他 Python 包支持这些新版本的能力的限制。",
        "Streamlit currently supports versions 3.9, 3.10, 3.11, 3.12, and 3.13 of Python.": "Streamlit 目前支持 Python 的 3.9、3.10、3.11、3.12 和 3.13 版本。",
        "## Check #1: Is Streamlit running?": "## 检查 #1：Streamlit 正在运行吗？",
        "On a Mac or Linux machine, type this on the terminal:": "在 Mac 或 Linux 机器上，在终端上输入以下内容：",
        "If you don't see `streamlit run` in the output (or `streamlit hello`, if that's\nthe command you ran) then the Streamlit server is not running. So re-run your command and see if the bug goes away.": "如果您在输出中看不到 `streamlit run`（或 `streamlit hello`，如果这是您运行的命令），则 Streamlit 服务器未运行。所以请重新运行您的命令，看看错误是否消失。",
        "## Check #2: Is this an already-fixed Streamlit bug?": "## 检查 #2：这是已修复的 Streamlit 错误吗？",
        "We try to fix bugs quickly, so many times a problem will go away when you\nupgrade Streamlit. So the first thing to try when having an issue is upgrading\nto the latest version of Streamlit:": "我们会尽快修复错误，因此当您升级 Streamlit 时，很多问题都会消失。因此，在遇到问题时首先尝试的是升级到最新版本的 Streamlit：",
        "...and then verify that the version number printed corresponds to the version number displayed on [PyPI](https://pypi.org/project/streamlit/).": "...然后验证打印的版本号是否与 [PyPI](https://pypi.org/project/streamlit/) 上显示的版本号相对应。",
        "**Try reproducing the issue now.** If not fixed, keep reading on.": "**现在尝试重现问题。** 如果未修复，请继续阅读。",
        "## Check #3: Are you running the correct Streamlit binary?": "## 检查 #3：您运行的是正确的 Streamlit 二进制文件吗？",
        "Let's check whether your Python environment is set up correctly. Edit the\nStreamlit script where you're experiencing your issue, **comment everything\nout, and add these lines instead:**": "让我们检查一下您的 Python 环境是否设置正确。编辑 Streamlit 脚本，其中您遇到问题，**注释掉所有内容，并改为添加以下行：**",
        "...then call `streamlit run` on your script and make sure it says the same\nversion as above. If not the same version, check out [these\ninstructions](/get-started/installation) for some sure-fire ways to set up your\nenvironment.": "...然后对您的脚本调用 `streamlit run`，确保它显示与上述相同的版本。如果版本不同，请查看 [这些说明](/get-started/installation) 以了解一些可靠的方法来设置您的环境。",
        "## Check #4: Is your browser caching your app too aggressively?": "## 检查 #4：您的浏览器是否过度缓存您的应用？",
        "There are two easy ways to check this:": "有两种简单的方法来检查这一点：",
        "1. Load your app in a browser then press `Ctrl-Shift-R` or `⌘-Shift-R` to do a\n   hard refresh (Chrome/Firefox).": "1. 在浏览器中加载您的应用，然后按 `Ctrl-Shift-R` 或 `⌘-Shift-R` 进行硬刷新（Chrome/Firefox）。",
        "2. As a test, run Streamlit on another port. This way the browser starts the\n   page with a brand new cache. For that, pass the `--server.port`\n   argument to Streamlit on the command line:": "2. 作为测试，在另一个端口上运行 Streamlit。这样浏览器就会使用全新的缓存启动页面。为此，将 `--server.port` 参数传递给命令行上的 Streamlit：",
        "## Check #5: Is this a Streamlit regression?": "## 检查 #5：这是 Streamlit 回归吗？",
        "If you've upgraded to the latest version of Streamlit and things aren't\nworking, you can downgrade at any time using this command:": "如果您已升级到最新版本的 Streamlit，但事情不起作用，您可以随时使用以下命令进行降级：",
        "...where `1.0.0` is the version you'd like to downgrade to. See\n[Release notes](/develop/quick-reference/release-notes) for a complete list of Streamlit versions.": "...其中 `1.0.0` 是您想要降级到的版本。有关 Streamlit 版本的完整列表，请参阅 [发行说明](/develop/quick-reference/release-notes)。",
        "## Check #6 [Windows]: Is Python added to your PATH?": "## 检查 #6 [Windows]：Python 是否添加到您的 PATH？",
        "When installed by downloading from [python.org](https://www.python.org/downloads/), Python is\nnot automatically added to the [Windows system PATH](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access). Because of this, you may get error messages\nlike the following:": "当通过从 [python.org](https://www.python.org/downloads/) 下载安装 Python 时，Python 不会自动添加到 [Windows 系统 PATH](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access)。因此，您可能会收到如下错误消息：",
        "Command Prompt:": "命令提示符：",
        "PowerShell:": "PowerShell：",
        "To resolve this issue, add [Python to the Windows system PATH](https://datatofish.com/add-python-to-windows-path/).": "要解决此问题，请 [将 Python 添加到 Windows 系统 PATH](https://datatofish.com/add-python-to-windows-path/)。",
        "After adding Python to your Windows PATH, you should then be able to follow the instructions in our [Get Started](/get-started) section.": "将 Python 添加到您的 Windows PATH 后，您应该能够按照我们的 [入门](/get-started) 部分中的说明进行操作。",
        "## Check #7 [Windows]: Do you need Build Tools for Visual Studio installed?": "## 检查 #7 [Windows]：您需要安装 Visual Studio 的生成工具吗？",
        "Streamlit includes [pyarrow](https://arrow.apache.org/docs/python/) as an install dependency. Occasionally, when trying to install Streamlit from PyPI, you may see errors such as the following:": "Streamlit 包含 [pyarrow](https://arrow.apache.org/docs/python/) 作为安装依赖项。有时，当尝试从 PyPI 安装 Streamlit 时，您可能会看到如下错误：",
        "This error indicates that Python is trying to compile certain libraries during install, but it cannot find the proper compilers on your system,\nas reflected by the line `error: Microsoft Visual C++ 14.0 is required. Get it with \"Build Tools for Visual Studio\"`.": "此错误表明 Python 在安装期间尝试编译某些库，但无法在系统上找到正确的编译器，如 `error: Microsoft Visual C++ 14.0 is required. Get it with \"Build Tools for Visual Studio\"` 行所反映的。",
        "Installing [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/) should resolve this issue.": "安装 [Visual Studio 的生成工具](https://visualstudio.microsoft.com/downloads/) 应该可以解决此问题。",
    },
    "content/kb/_index.md": {
        "title: Knowledge Base": "title: 知识库",
        "slug: /knowledge-base": "slug: /knowledge-base",
        "# Knowledge Base": "# 知识库",
        "The Knowledge Base is a self-help library of tips, step-by-step tutorials, and articles to answer your questions about creating and deploying Streamlit apps.": "知识库是一个自助式的技巧、分步教程和文章库，可以回答您关于创建和部署 Streamlit 应用的问题。",
        "bold=\"FAQs\"": "bold=\"常见问题\"",
        "bold=\"Installing dependencies\"": "bold=\"安装依赖项\"",
        "bold=\"Deployment issues\"": "bold=\"部署问题\"",
        ">Below are some frequently asked questions about using Streamlit.</InlineCallout>": ">以下是关于使用 Streamlit 的一些常见问题。</InlineCallout>",
        ">If you are running into issues installing dependencies for your Streamlit app, we can help.": ">如果您在为 Streamlit 应用安装依赖项时遇到问题，我们可以帮助您。",
        ">Have questions about deploying your Streamlit app to the cloud? This section covers deployment-related issues.</InlineCallout>": ">对将 Streamlit 应用部署到云有疑问？本部分涵盖部署相关的问题。</InlineCallout>",
    },
    "content/get-started/fundamentals/summary.md": {
        "title: App model summary": "title: 应用模型摘要",
        "description: A summary of Streamlit's app model including execution flow, data handling, and state management.": "description: Streamlit 应用模型的摘要，包括执行流程、数据处理和状态管理。",
        "# App model summary": "# 应用模型摘要",
        "Now that you know a little more about all the individual pieces, let's close\nthe loop and review how it works together:": "现在您对所有各个部分了解得更多了，让我们总结一下它是如何一起工作的：",
        "1. Streamlit apps are Python scripts that run from top to bottom.": "1. Streamlit 应用是从上到下运行的 Python 脚本。",
        "1. Every time a user opens a browser tab pointing to your app, the script is executed and a new session starts.": "1. 每次用户打开指向您的应用的浏览器选项卡时，脚本都会执行并启动一个新会话。",
        "1. As the script executes, Streamlit draws its output live in a browser.": "1. 当脚本执行时，Streamlit 会在浏览器中实时绘制其输出。",
        "1. Every time a user interacts with a widget, your script is re-executed and Streamlit redraws its output in the browser.": "1. 每次用户与小部件交互时，您的脚本都会重新执行，并且 Streamlit 会在浏览器中重新绘制其输出。",
        "   - The output value of that widget matches the new value during that rerun.": "   - 该小部件的输出值在重新运行期间与新值相匹配。",
        "1. Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast.": "1. 脚本使用 Streamlit 缓存来避免重新计算昂贵的函数，因此更新发生得非常快。",
        "1. Session State lets you save information that persists between reruns when you need more than a simple widget.": "1. 会话状态让您保存在重新运行之间持续存在的信息，当您需要超过简单小部件时。",
        "1. Streamlit apps can contain multiple pages, which are defined in separate `.py` files in a `pages` folder.": "1. Streamlit 应用可以包含多个页面，这些页面在 `pages` 文件夹中的单独 `.py` 文件中定义。",
    }
}

# Apply translations
for file_path, replacements in translations.items():
    full_path = os.path.join("d:\\github_st\\docs", file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old_text, new_text in replacements.items():
            if old_text in content:
                content = content.replace(old_text, new_text)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path}")
    else:
        print(f"✗ {file_path} - File not found")

print("\nDone!")
