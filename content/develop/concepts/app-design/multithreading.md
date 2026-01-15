---
title: Streamlit 中的线程处理
slug: /develop/concepts/design/multithreading
description: 了解 Streamlit 应用中的多线程处理，包括限制、最佳实践和安全实现并发过程的技术。
keywords: 多线程处理, 线程, 并发, streamlit 线程处理, 并发过程, 线程安全, 异步编程, 后台任务, 并行处理
---

# Streamlit 中的多线程处理

多线程处理是一种并发类型，可以提高计算机程序的效率。这是处理器执行多任务的一种方式。Streamlit 在其架构中使用线程，这可能使应用开发人员难以包含他们自己的多线程过程。Streamlit 不正式支持应用代码中的多线程处理，但本指南提供了有关如何实现的信息。

## 前置条件

- 你应该对 Streamlit 的[架构](/develop/concepts/architecture/architecture)有基本的理解。

## 何时使用多线程处理

多线程处理只是并发的一种类型。多处理和协程是并发的其他形式。你需要理解代码如何被限制以选择正确的并发类型。

多处理本质上是并行的，意味着资源被分割并且多个任务同时执行。因此，多处理对于计算密集型操作很有帮助。相比之下，多线程处理和协程本质上不是并行的，而是允许资源切换。这使得它们是一个不错的选择，当你的代码被困在等待某些东西时，例如 IO 操作。AsyncIO 使用协程，可能对于非常慢的 IO 操作更可取。线程处理可能对于更快的 IO 操作更可取。有关将 AsyncIO 与 Streamlit 一起使用的有用指南，请参阅[Sehmi-Conscious Thoughts 的这篇 Medium 文章](https://sehmi-conscious.medium.com/got-that-asyncio-feeling-f1a7c37cab8b)。

别忘了 Streamlit 也有[片段](/develop/concepts/architecture/fragments)和[缓存](/develop/concepts/architecture/caching)！使用缓存来避免不必要地重复计算或 IO 操作。使用片段来隔离你想从应用的其余部分单独更新的一段代码。你可以将片段设置为以指定的间隔重新运行，这样它们可以用于流式更新图表或表格。

## Streamlit 创建的线程

Streamlit creates two types of threads in Python:

- The **server thread** runs the Tornado web (HTTP + WebSocket) server.
- A **script thread** runs page code &mdash; one thread for each script run in a session.
## Streamlit 创建的线程

Streamlit 在 Python 中创建两种类型的线程：

- **服务器线程**运行 Tornado web（HTTP + WebSocket）服务器。
- **脚本线程**运行页面代码 — 每个会话中的脚本运行一个线程。

当用户连接到你的应用时，这会创建一个新的会话并运行脚本线程来为该用户初始化应用。当脚本线程运行时，它在用户的浏览器标签中呈现元素并向服务器报告状态。当用户与应用交互时，另一个脚本线程运行，重新呈现浏览器标签中的元素并更新服务器上的状态。

这是一个简化的图示，显示 Streamlit 如何工作：

![每个用户会话都使用脚本线程在用户的前端和 Streamlit 服务器之间进行通信。](/images/concepts/Streamlit-threading.svg)

## `streamlit.errors.NoSessionContext`

许多 Streamlit 命令，包括 `st.session_state`，期望从脚本线程调用。当 Streamlit 按预期运行时，此类命令使用附加到脚本线程的 `ScriptRunContext` 来确保它们在预期的会话中工作并更新正确的用户视图。当那些 Streamlit 命令找不到任何 `ScriptRunContext` 时，它们会引发 `streamlit.errors.NoSessionContext` 异常。根据你的记录器设置，你也可能看到一个控制台消息，按名称标识线程并警告"缺少 ScriptRunContext！"

## 创建自定义线程

当你使用 IO 密集操作（如远程查询或数据加载）时，你可能需要减少延迟。一般编程策略是创建线程并让它们并发工作。但是，如果你在 Streamlit 应用中执行此操作，这些自定义线程可能在与 Streamlit 服务器交互时遇到困难。

本部分介绍两种模式，让你在 Streamlit 应用中创建自定义线程。这些只是提供起点而不是完整解决方案的模式。

### 选项 1：不在自定义线程内使用 Streamlit 命令

如果你不从自定义线程调用 Streamlit 命令，你可以完全避免该问题。幸运的是，Python 线程处理提供了启动线程并从另一个线程收集其结果的方法。

在以下示例中，从脚本线程创建五个自定义线程。线程完成运行后，它们的结果显示在应用中。

```python
import streamlit as st
import time
from threading import Thread


class WorkerThread(Thread):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.return_value = None

    def run(self):
        start_time = time.time()
        time.sleep(self.delay)
        end_time = time.time()
        self.return_value = f"start: {start_time}, end: {end_time}"


delays = [5, 4, 3, 2, 1]
threads = [WorkerThread(delay) for delay in delays]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
for i, thread in enumerate(threads):
    st.header(f"Thread {i}")
    st.write(thread.return_value)

st.button("Rerun")
```

<Cloud name="doc-multithreading-no-st-commands-batched" height="700px" />

如果你想在应用中显示结果，当各种自定义线程完成运行时，使用容器。在以下示例中，五个自定义线程的创建方式与之前的示例类似。但是，在运行自定义线程之前初始化五个容器，并使用 `while` 循环在结果可用时显示它们。由于 Streamlit `write` 命令是在自定义线程外部调用的，这不会引发异常。

```python
import streamlit as st
import time
from threading import Thread


class WorkerThread(Thread):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.return_value = None

    def run(self):
        start_time = time.time()
        time.sleep(self.delay)
        end_time = time.time()
        self.return_value = f"start: {start_time}, end: {end_time}"


delays = [5, 4, 3, 2, 1]
result_containers = []
for i, delay in enumerate(delays):
    st.header(f"Thread {i}")
    result_containers.append(st.container())

threads = [WorkerThread(delay) for delay in delays]
for thread in threads:
    thread.start()
thread_lives = [True] * len(threads)

while any(thread_lives):
    for i, thread in enumerate(threads):
        if thread_lives[i] and not thread.is_alive():
            result_containers[i].write(thread.return_value)
            thread_lives[i] = False
    time.sleep(0.5)

for thread in threads:
    thread.join()

st.button("Rerun")
```

<Cloud name="doc-multithreading-no-st-commands-iterative" height="700px" />

### 选项 2：向线程暴露 `ScriptRunContext`

如果你想从自定义线程内调用 Streamlit 命令，你必须将正确的 `ScriptRunContext` 附加到线程。

<Warning>

- 这不被正式支持，并且可能在 Streamlit 的未来版本中更改。
- 这可能不适用于所有 Streamlit 命令。
- 确保自定义线程不会超过拥有 `ScriptRunContext` 的脚本线程的生命周期。`ScriptRunContext` 的泄漏可能导致安全漏洞、致命错误或意外行为。

</Warning>

在以下示例中，附加了 `ScriptRunContext` 的自定义线程可以调用 `st.write` 而不会出现警告。

```python
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
import time
from threading import Thread


class WorkerThread(Thread):
    def __init__(self, delay, target):
        super().__init__()
        self.delay = delay
        self.target = target

    def run(self):
        # 在自定义线程中运行，但可以调用 Streamlit API
        start_time = time.time()
        time.sleep(self.delay)
        end_time = time.time()
        self.target.write(f"start: {start_time}, end: {end_time}")


delays = [5, 4, 3, 2, 1]
result_containers = []
for i, delay in enumerate(delays):
    st.header(f"Thread {i}")
    result_containers.append(st.container())

threads = [
    WorkerThread(delay, container)
    for delay, container in zip(delays, result_containers)
]
for thread in threads:
    add_script_run_ctx(thread, get_script_run_ctx())
    thread.start()

for thread in threads:
    thread.join()

st.button("Rerun")
```

<Cloud name="doc-multithreading-expose-context" height="700px" />
