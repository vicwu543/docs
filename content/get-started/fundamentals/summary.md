---
title: 应用模型摘要
slug: /get-started/fundamentals/summary
description: Streamlit 应用模型的摘要，包括执行流程、数据处理和状态管理。
keywords: app model, execution flow, data handling, state management, streamlit architecture, app summary, fundamentals recap
---

# 应用模型摘要

现在您对所有各个部分了解得更多了，让我们总结一下它是如何一起工作的：

1. Streamlit 应用是从上到下运行的 Python 脚本。
1. 每次用户打开指向您的应用的浏览器选项卡时，脚本都会执行并启动一个新会话。
1. 当脚本执行时，Streamlit 会在浏览器中实时绘制其输出。
1. 每次用户与小部件交互时，您的脚本都会重新执行，并且 Streamlit 会在浏览器中重新绘制其输出。
   - 该小部件的输出值在重新运行期间与新值相匹配。
1. 脚本使用 Streamlit 缓存来避免重新计算昂贵的函数，因此更新发生得非常快。
1. 会话状态让您保存在重新运行之间持续存在的信息，当您需要超过简单小部件时。
1. Streamlit 应用可以包含多个页面，这些页面在 `pages` 文件夹中的单独 `.py` 文件中定义。

![The Streamlit app model](/images/app_model.png)
