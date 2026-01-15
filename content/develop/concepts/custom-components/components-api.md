---
title: 自定义组件简介
slug: /develop/concepts/custom-components/intro
description: 了解如何使用 Python 和 JavaScript 之间的静态和双向通信开发 Streamlit 自定义组件以扩展功能。
keywords: custom component development, static components, bi-directional components, Python JavaScript communication, component API, component development
---

# 自定义组件简介

开发 Streamlit 组件的第一步是决定创建静态组件（即仅渲染一次，由 Python 控制）还是创建可以实现 Python 到 JavaScript 及返回的双向通信的组件。

## 创建静态组件

如果创建 Streamlit 组件的目标仅仅是显示 HTML 代码或从 Python 可视化库渲染图表，Streamlit 提供了两种大大简化此过程的方法：`components.html()` 和 `components.iframe()`。

如果您不确定是否需要双向通信，**请先从这里开始**！

### 渲染 HTML 字符串

虽然 [`st.text`](/develop/api-reference/text/st.text)、[`st.markdown`](/develop/api-reference/text/st.markdown) 和 [`st.write`](/develop/api-reference/write-magic/st.write) 可以轻松将文本写入 Streamlit 应用，但有时您可能更愿意实现自定义 HTML 片段。同样，虽然 Streamlit 本地支持[许多图表库](/develop/api-reference/charts#chart-elements)，但您可能希望为新的图表库实现特定的 HTML/JavaScript 模板。[`components.html`](/develop/api-reference/custom-components/st.components.v1.html) 通过为您提供在 Streamlit 应用中嵌入包含所需输出的 iframe 的能力来工作。

**示例**

```python
import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 折叠示例
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            可折叠组项目 #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            可折叠组项目 #1 内容
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            可折叠组项目 #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            可折叠组项目 #2 内容
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
```

### 渲染 iframe URL

[`components.iframe`](/develop/api-reference/custom-components/st.components.v1.iframe) 在功能上与 `components.html` 类似，区别在于 `components.iframe` 以 URL 作为输入。这用于您想在 Streamlit 应用中包含整个页面的情况。

**示例**

```python
import streamlit as st
import streamlit.components.v1 as components

# 在 streamlit 应用中嵌入 streamlit 文档
components.iframe("https://example.com", height=500)
```

## 创建双向组件

双向 Streamlit 组件有两个部分：

1. 一个**前端**，由 HTML 和您喜欢的任何其他网络技术（JavaScript、React、Vue 等）构建，并通过 iframe 标签在 Streamlit 应用中渲染。
2. 一个**Python API**，Streamlit 应用使用它来实例化并与前端通信

为了使创建双向 Streamlit 组件的过程更容易，我们在 [Streamlit Component-template GitHub 仓库](https://github.com/streamlit/component-template) 中创建了一个 React 模板和一个仅 TypeScript 模板。我们还在同一个仓库中提供了一些[示例组件](https://github.com/streamlit/component-template/tree/master/examples)。

### 开发环境设置

要构建 Streamlit 组件，您需要在开发环境中安装以下内容：

- Python 3.9 - Python 3.13
- Streamlit
- [nodejs](https://nodejs.org/en/)
- [npm](https://www.npmjs.com/) 或 [yarn](https://yarnpkg.com/)

克隆 [component-template GitHub 仓库](https://github.com/streamlit/component-template)，然后决定是否要使用 React.js (["template"](https://github.com/streamlit/component-template/tree/master/template)) 或纯 TypeScript (["template-reactless"](https://github.com/streamlit/component-template/tree/master/template-reactless)) 模板。

1. 从终端初始化并构建组件模板前端：

   ```bash
   # React 模板
   template/my_component/frontend
   npm install    # 初始化项目并安装 npm 依赖项
   npm run start  # 启动 Vite 开发服务器

   # 或

   # 仅 TypeScript 模板
   template-reactless/my_component/frontend
   npm install    # 初始化项目并安装 npm 依赖项
   npm run start  # 启动 Vite 开发服务器
   ```

2. _从另一个终端_，运行声明和使用组件的 Streamlit 应用（Python）：

   ```bash
   # React 模板
   cd template
   . venv/bin/activate # 或类似命令激活安装了 Streamlit 的 venv/conda 环境
   pip install -e . # 将模板安装为可编辑包
   streamlit run my_component/example.py # 运行示例

   # 或

   # 仅 TypeScript 模板
   cd template-reactless
   . venv/bin/activate # 或类似命令激活安装了 Streamlit 的 venv/conda 环境
   pip install -e . # 将模板安装为可编辑包
   streamlit run my_component/example.py # 运行示例
   ```

运行上述步骤后，您应该在浏览器中看到一个 Streamlit 应用，如下所示：

![Streamlit 组件示例应用](/images/component_demo_example.png)

模板中的示例应用展示了双向通信是如何实现的。Streamlit 组件显示一个按钮（`Python → JavaScript`），终端用户可以点击该按钮。每次点击按钮时，JavaScript 前端都会递增计数器值并将其传回 Python（`JavaScript → Python`），然后由 Streamlit 显示（`Python → JavaScript`）。

### 前端

由于每个 Streamlit 组件都是一个独立的网页，通过 `iframe` 渲染到应用中，您可以使用几乎任何网络技术来创建该网页。我们在 Streamlit [Components-template GitHub 仓库](https://github.com/streamlit/component-template/) 中提供了两个模板来开始；其中一个模板使用 [React](https://reactjs.org/)，另一个不使用。

<Note>

即使您还不熟悉 React，您可能仍想查看基于 React 的模板。它处理了从 Streamlit 发送和接收数据所需的大部分样板代码，您可以随着进展学习所需的 React 知识。

如果您不想使用 React，请无论如何阅读此部分！它解释了 Streamlit ↔ 组件通信的基础知识。
</Note>

#### React

基于 React 的模板位于 `template/my_component/frontend/src/MyComponent.tsx`。

- 当组件需要重新渲染时（就像在任何 React 应用中一样），会自动调用 `MyComponent.render()`
- 从 Python 脚本传递的参数可通过 `this.props.args` 字典获得：

```python
# 在 Python 中发送参数:
result = my_component(greeting="Hello", name="Streamlit")
```

```javascript
// 在前端接收参数:
let greeting = this.props.args["greeting"]; // greeting = "Hello"
let name = this.props.args["name"]; // name = "Streamlit"
```

- 使用 `Streamlit.setComponentValue()` 将数据从前端返回到 Python 脚本：

```javascript
// 在前端设置值:
Streamlit.setComponentValue(3.14);
```

```python
# 在 Python 中访问值:
result = my_component(greeting="Hello", name="Streamlit")
st.write("result = ", result) # result = 3.14
```

当您调用 `Streamlit.setComponentValue(new_value)` 时，该新值会被发送到 Streamlit，然后 _从头到尾重新执行 Python 脚本_。当脚本重新执行时，对 `my_component(...)` 的调用将返回新值。

从 _代码流_ 的角度来看，似乎您正在与前端同步传输数据：Python 将参数发送给 JavaScript，JavaScript 将值返回给 Python，全部在单个函数调用中！但实际上这一切都是 _异步_ 发生的，正是 Python 脚本的重新执行实现了这种巧妙的手法。

- 使用 `Streamlit.setFrameHeight()` 控制组件的高度。默认情况下，React 模板会自动调用此函数（请参见 `StreamlitComponentBase.componentDidUpdate()`）。如果您需要更多控制，可以覆盖此行为。
- 文件的最后一行有一个小技巧：`export default withStreamlitConnection(MyComponent)` - 这会与 Streamlit 进行一些握手，并建立双向数据通信机制。

#### 仅 TypeScript

仅 TypeScript 模板位于 `template-reactless/my_component/frontend/src/MyComponent.tsx`。

此模板比其 React 对应版本有更多的代码，因为握手、设置事件监听器和更新组件框架高度的所有机制都是手动完成的。React 版本的模板自动处理大部分这些细节。

- 在源文件底部附近，模板调用 `Streamlit.setComponentReady()` 告诉 Streamlit 它已准备好开始接收数据。（通常在创建和加载组件依赖的所有内容后执行此操作。）
- 它订阅 `Streamlit.RENDER_EVENT` 以获知何时重绘。（在调用 `setComponentReady` 之前不会触发此事件）
- 在其 `onRender` 事件处理程序中，它通过 `event.detail.args` 访问 Python 脚本中传递的参数
- 它以与 React 模板相同的方式将数据发送回 Python 脚本——点击"Click Me!"按钮调用 `Streamlit.setComponentValue()`
- 它通过 `Streamlit.setFrameHeight()` 通知 Streamlit 其高度可能已更改

#### 使用主题

<Note>

自定义组件主题支持需要 streamlit-component-lib 版本 1.2.0 或更高版本。

</Note>

除了向组件发送 `args` 对象外，Streamlit 还发送一个定义活动主题的 `theme` 对象，以便您的组件可以以兼容的方式调整其样式。此对象与 `args` 在同一条消息中发送，因此可通过 `this.props.theme`（使用 React 模板时）或 `event.detail.theme`（使用纯 TypeScript 模板时）访问。

`theme` 对象具有以下结构：

```json
{
  "base": "lightORdark",
  "primaryColor": "someColor1",
  "backgroundColor": "someColor2",
  "secondaryBackgroundColor": "someColor3",
  "textColor": "someColor4",
  "font": "someFont"
}
```

`base` 选项允许您指定自定义主题继承的预设 Streamlit 主题。在主题设置中未定义的任何主题配置选项的值将设置为基本主题的值。`base` 的有效值为 `"light"` 和 `"dark"`。

请注意，主题对象具有与使用命令 `streamlit config show` 打印的配置选项中"theme"部分选项同名且语义相同的字段。

使用 React 模板时，还会自动设置以下 CSS 变量。

```css
--base
--primary-color
--background-color
--secondary-background-color
--text-color
--font
```

如果您不熟悉 [CSS 变量](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)，简单来说您可以这样使用它们：

```css
.mySelector {
  color: var(--text-color);
}
```

这些变量与上面 `theme` 对象中定义的字段匹配，是否在组件中使用 CSS 变量还是主题对象是个人偏好的问题。

#### 其他前端细节

- 由于您从开发服务器（通过 `npm run start`）托管组件，保存时所做的任何更改都应该自动反映在 Streamlit 应用中。
- 如果您想向组件添加更多包，请在组件的 `frontend/` 目录中运行 `npm add` 来添加它们。

```bash
npm add baseui
```

- 要构建组件的静态版本，请运行 `npm run export`。更多信息请参见 [准备您的组件](publish#prepare-your-component)

### Python API

`components.declare_component()` 是创建组件 Python API 所需的全部：

```python
  import streamlit.components.v1 as components
  my_component = components.declare_component(
    "my_component",
    url="http://localhost:3001"
  )
```

然后您可以使用返回的 `my_component` 函数与前端代码发送和接收数据：

```python
# 使用命名参数向前端发送数据。
return_value = my_component(name="Blackbeard", ship="Queen Anne's Revenge")

# `my_component` 的返回值是从前端返回的数据。
st.write("Value = ", return_value)
```

虽然以上是从 Python 方面定义工作组件所需的一切，但我们建议创建一个带有命名参数和默认值、输入验证等的"包装器"函数。这将使最终用户更容易理解您的函数接受哪些数据值，并允许定义有用的文档字符串。

请参见 [此示例](https://github.com/streamlit/component-template/blob/master/template/my_component/__init__.py#L41-L77) 了解从 Components-template 创建包装函数的示例。

### 数据序列化

#### Python → 前端

您通过向前端调用函数（即 `declare_component` 返回的函数）传递关键字参数将数据从 Python 发送到前端。您可以从前端发送以下类型的数据：

- 任何 JSON 可序列化数据
- `numpy.array`
- `pandas.DataFrame`

任何 JSON 可序列化数据都会序列化为 JSON 字符串，并反序列化为 JavaScript 等价物。`numpy.array` 和 `pandas.DataFrame` 使用 [Apache Arrow](https://arrow.apache.org/) 进行序列化，并反序列化为 `ArrowTable` 实例，这是一种包装 Arrow 结构并在其之上提供便捷 API 的自定义类型。

查看 [CustomDataframe](https://github.com/streamlit/component-template/tree/master/examples/CustomDataframe) 和 [SelectableDataTable](https://github.com/streamlit/component-template/tree/master/examples/SelectableDataTable) 组件示例代码，了解如何使用 `ArrowTable` 的更多上下文。

#### 前端 → Python

您通过 `Streamlit.setComponentValue()` API（这是模板代码的一部分）从前端将数据发送到 Python。与从 Python → 前端的参数传递不同，**此 API 接受单个值**。如果您想返回多个值，需要将它们包装在 `Array` 或 `Object` 中。

自定义组件可以从前端向 Python 发送 JSON 可序列化数据，以及 [Apache Arrow](http://arrow.apache.org/) `ArrowTable` 以表示数据框。