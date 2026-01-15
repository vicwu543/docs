---
title: 共享预览
slug: /deploy/streamlit-community-cloud/share-your-app/share-previews
description: 了解如何为社交媒体创建吸引人的共享预览，具有Streamlit应用的自定义标题和描述。
keywords: 共享预览, 社交媒体, 标题, 描述, 预览图像, twitter, facebook, linkedin, 共享, 优化
---

# 共享预览

当你分享链接时，社交媒体网站会生成一张带有标题、预览图像和描述的卡片。此功能称为"共享预览"。同样，当你在社交媒体上分享公开Streamlit应用的链接时，也会生成共享预览。以下是在Twitter上发布的公开Streamlit应用的共享预览示例：

<Note>

共享预览仅为部署在Streamlit Community Cloud上的公开应用生成。

</Note>

## 标题

标题是显示在共享预览顶部的文本。访问应用时，文本也出现在浏览器选项卡中。你应该将标题设置为对应用受众有意义并描述应用功能的内容。最佳做法是保持标题简洁，理想情况下少于60个字符。

有两种方法可以设置共享预览的标题：

1. 将[`st.set_page_config()`](/develop/api-reference/configuration/st.set_page_config)中的`page_title`参数设置为你想要的标题。例如：

   ```python
   import streamlit as st

   st.set_page_config(page_title="My App")

   # ... rest of your app
   ```

2. 如果不设置`page_title`参数，共享预览的标题将是应用GitHub仓库的名称。例如，对于托管在GitHub上的应用的默认标题为"traingenerator"。

## 描述

描述是显示在共享预览标题下方的文本。描述应该总结应用功能，理想情况下应少于100个字符。

Streamlit从应用的GitHub仓库的README中提取描述。如果没有README，描述将默认为：

"此应用在Streamlit中构建！查看它并访问https://streamlit.io以获取更多精彩社区应用。🎈"

如果你想让共享预览看起来很好，并希望用户分享你的应用并点击你的链接，你应该在应用的GitHub仓库的README中写一个很好的描述。

## 预览图像

Streamlit Community Cloud每天对应用进行一次屏幕截图，并将其用作预览图像，不像从应用代码或GitHub仓库直接提取的标题和描述。此屏幕截图可能需要长达24小时才能更新。

### 将应用从公开转换为私有

如果你最初将应用设为公开，后来决定将其设为私有，我们将停止为应用生成共享预览。但是，共享预览可能需要长达24小时才能停止出现。
