---
title: SEO和搜索可索引性
slug: /deploy/streamlit-community-cloud/share-your-app/indexability
description: 了解如何通过自定义子域、描述性标题和元描述为搜索引擎优化Streamlit应用。
keywords: seo, 搜索, 可索引性, google, bing, 子域, 标题, 元描述, 优化, 可发现性
---

# SEO和搜索可索引性

当你将公开应用部署到Streamlit Community Cloud时，它会每周自动被Google和Bing等搜索引擎索引。这意味着任何人都可以通过搜索其自定义子域（例如"traingenerator.streamlit.app"）或搜索应用标题来找到你的应用。

## 充分利用应用可索引性

这里有一些提示可以帮助你充分利用应用可索引性：

1. 确保你的应用是公开的
2. 尽早选择自定义子域
3. 选择描述性应用标题
4. 自定义应用的元描述

### 确保你的应用是公开的

Community Cloud上托管的所有公开应用都被搜索引擎索引。如果你的应用是私有的，它将不被搜索引擎索引。要使私有应用公开，请阅读"共享你的应用"。

### 尽早选择自定义子域

如果你不选择子域，Community Cloud会自动为应用生成子域。但是，你可以随时更改子域！自定义子域会修改应用URL以反映应用内容、个人品牌或任何你想要的内容。要了解如何更改应用子域，请参阅"查看或更改应用URL"。

通过选择自定义子域，你可以使用它来帮助人们找到你的应用。例如，如果你部署生成训练数据的应用，你可能会选择像`traingenerator.streamlit.app`这样的子域。这使人们可以通过搜索"training generator"或"train generator streamlit app"来轻松找到你的应用。

我们建议在部署应用时选择自定义子域。这确保应用使用自定义子域而不是自动生成的子域被搜索引擎索引。如果稍后选择自定义子域，应用可能会被索引多次——一次使用默认子域，一次使用自定义子域。在这种情况下，旧URL将导致404错误，这可能会困惑正在搜索应用的用户。

### 选择描述性应用标题

应用的元标题是显示在搜索引擎结果中的文本。它也是应用打开时显示在浏览器选项卡中的文本。默认情况下，应用的元标题与应用标题相同。但是，你可以通过将`st.set_page_config`参数`page_title`设置为自定义字符串来自定义应用的元标题。例如：

```python
st.set_page_config(page_title="Traingenerator")
```

这会将应用的元标题更改为"Traingenerator"。这使人们可以通过搜索"Traingenerator"或"train generator streamlit app"更轻松地找到你的应用。

### 自定义应用的元描述

元描述是显示在搜索引擎结果中的短描述。搜索引擎使用元描述来帮助用户理解应用的内容。

从我们的观察来看，搜索引擎似乎比`st.title`更喜欢`st.header`和`st.text`中的内容。如果你在应用顶部在`st.header`或`st.text`下放置描述，搜索引擎很可能会将其用于元描述。

## 我的索引应用看起来怎样？

如果你对应用在搜索引擎结果中的样子感到好奇，你可以在Google搜索中输入以下内容：

```
site:<your-custom-subdomain>.streamlit.app
```

示例：`site:traingenerator.streamlit.app`

## 如果我不想要索引应用怎么办？

如果你不想让应用被搜索引擎索引，你可以将其设为私有。阅读"共享你的应用"以了解更多关于使应用私有的信息。注意：每个工作空间只能有一个私有应用。如果你想使应用私有，你必须首先删除工作空间中的任何其他私有应用或使其成为公开。

也就是说，Community Cloud是一个开放且免费的平台，供社区部署、发现和彼此分享Streamlit应用和代码。因此，我们鼓励你使应用成为公开，以便可以被搜索引擎索引并被其他Streamlit用户和社区成员发现。
