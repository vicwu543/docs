---
title: 健全性检查
slug: /knowledge-base/using-streamlit/sanity-checks
---

# 健全性检查

如果您在运行 Streamlit 应用时遇到问题，这里有一些需要尝试的事情。

## 检查 #0：您使用的是 Streamlit 支持的 Python 版本吗？

Streamlit 将在实际可行的情况下保持与较早 Python 版本的向后兼容性，
保证与 _至少_ Python 3 的最后三个次要版本兼容。

随着新的 Python 版本的发布，我们会尽快尝试与新版本兼容，尽管通常我们受到其他 Python 包支持这些新版本的能力的限制。

Streamlit 目前支持 Python 的 3.9、3.10、3.11、3.12 和 3.13 版本。

## 检查 #1：Streamlit 正在运行吗？

在 Mac 或 Linux 机器上，在终端上输入以下内容：

```bash
ps -Al | grep streamlit
```

如果您在输出中看不到 `streamlit run`（或 `streamlit hello`，如果这是您运行的命令），则 Streamlit 服务器未运行。所以请重新运行您的命令，看看错误是否消失。

## 检查 #2：这是已修复的 Streamlit 错误吗？

我们会尽快修复错误，因此当您升级 Streamlit 时，很多问题都会消失。因此，在遇到问题时首先尝试的是升级到最新版本的 Streamlit：

```bash
pip install --upgrade streamlit
streamlit version
```

...然后验证打印的版本号是否与 [PyPI](https://pypi.org/project/streamlit/) 上显示的版本号相对应。

**现在尝试重现问题。** 如果未修复，请继续阅读。

## 检查 #3：您运行的是正确的 Streamlit 二进制文件吗？

让我们检查一下您的 Python 环境是否设置正确。编辑 Streamlit 脚本，其中您遇到问题，**注释掉所有内容，并改为添加以下行：**

```python
import streamlit as st
st.write(st.__version__)
```

...然后对您的脚本调用 `streamlit run`，确保它显示与上述相同的版本。如果版本不同，请查看 [这些说明](/get-started/installation) 以了解一些可靠的方法来设置您的环境。

## 检查 #4：您的浏览器是否过度缓存您的应用？

有两种简单的方法来检查这一点：

1. 在浏览器中加载您的应用，然后按 `Ctrl-Shift-R` 或 `⌘-Shift-R` 进行硬刷新（Chrome/Firefox）。

2. 作为测试，在另一个端口上运行 Streamlit。这样浏览器就会使用全新的缓存启动页面。为此，将 `--server.port` 参数传递给命令行上的 Streamlit：

   ```bash
   streamlit run my_app.py --server.port=9876
   ```

## 检查 #5：这是 Streamlit 回归吗？

如果您已升级到最新版本的 Streamlit，但事情不起作用，您可以随时使用以下命令进行降级：

```bash
pip install --upgrade streamlit==1.0.0
```

...其中 `1.0.0` 是您想要降级到的版本。有关 Streamlit 版本的完整列表，请参阅 [发行说明](/develop/quick-reference/release-notes)。

## 检查 #6 [Windows]：Python 是否添加到您的 PATH？

当通过从 [python.org](https://www.python.org/downloads/) 下载安装 Python 时，Python 不会自动添加到 [Windows 系统 PATH](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access)。因此，您可能会收到如下错误消息：

命令提示符：

```bash
C:\Users\streamlit> streamlit hello
'streamlit' is not recognized as an internal or external command,
operable program or batch file.
```

PowerShell：

```bash
PS C:\Users\streamlit> streamlit hello
streamlit : The term 'streamlit' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that
the path is correct and try again.
At line:1 char:1
+ streamlit hello
+ ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (streamlit:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

要解决此问题，请 [将 Python 添加到 Windows 系统 PATH](https://datatofish.com/add-python-to-windows-path/)。

将 Python 添加到您的 Windows PATH 后，您应该能够按照我们的 [入门](/get-started) 部分中的说明进行操作。

## 检查 #7 [Windows]：您需要安装 Visual Studio 的生成工具吗？

Streamlit 包含 [pyarrow](https://arrow.apache.org/docs/python/) 作为安装依赖项。有时，当尝试从 PyPI 安装 Streamlit 时，您可能会看到如下错误：

```bash
Using cached pyarrow-1.0.1.tar.gz (1.3 MB)
  Installing build dependencies ... error
  ERROR: Command errored out with exit status 1:
   command: 'c:\users\streamlit\appdata\local\programs\python\python38-32\python.exe' 'c:\users\streamlit\appdata\local\programs\python\python38-32\lib\site-packages\pip' install --ignore-installed --no-user --prefix 'C:\Users\streamlit\AppData\Local\Temp\pip-build-env-s7owjrle\overlay' --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- 'cython >= 0.29' 'numpy==1.14.5; python_version<'"'"'3.9'"'"'' 'numpy==1.16.0; python_version>='"'"'3.9'"'"'' setuptools setuptools_scm wheel
       cwd: None

  Complete output (319 lines):

      Running setup.py install for numpy: finished with status 'error'
      ERROR: Command errored out with exit status 1:

      # <truncated for brevity> #

      building library "npymath" sources
      No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
      error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": https://visualstudio.microsoft.com/downloads/
      ----------------------------------------
  ERROR: Command errored out with exit status 1: 'c:\users\streamlit\appdata\local\programs\python\python38-32\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\streamlit\\AppData\\Local\\Temp\\pip-install-0jwfwx_u\\numpy\\setup.py'"'"'; __file__='"'"'C:\\Users\\streamlit\\AppData\\Local\\Temp\\pip-install-0jwfwx_u\\numpy\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\streamlit\AppData\Local\Temp\pip-record-eys4l2gc\install-record.txt' --single-version-externally-managed --prefix 'C:\Users\streamlit\AppData\Local\Temp\pip-build-env-s7owjrle\overlay' --compile --install-headers 'C:\Users\streamlit\AppData\Local\Temp\pip-build-env-s7owjrle\overlay\Include\numpy' Check the logs for full command output.
  ----------------------------------------
```

此错误表明 Python 在安装期间尝试编译某些库，但无法在系统上找到正确的编译器，如 `error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio"` 行所反映的。

安装 [Visual Studio 的生成工具](https://visualstudio.microsoft.com/downloads/) 应该可以解决此问题。
