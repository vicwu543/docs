---
title: 使用表单
slug: /develop/concepts/architecture/forms
description: 了解如何使用 Streamlit 表单与 st.form 批量处理用户输入，控制应用重新运行，并使用提交按钮创建高效的交互界面。
keywords: streamlit forms, st.form, batch input, form submission, user input batching, form controls, submit button, form validation, interactive forms, form patterns
---

# 使用表单

当您不希望在用户每次输入时都重新运行脚本时，[`st.form`](/develop/api-reference/execution-flow/st.form) 就派上用场了！表单可以轻松地将用户输入批量处理为单次重新运行。本使用表单指南提供了示例并解释了用户如何与表单交互。

## 示例

在以下示例中，用户可以设置多个参数以更新地图。当用户更改参数时，脚本不会重新运行，地图也不会更新。当用户点击标记为"**更新地图**"的按钮提交表单时，脚本重新运行，地图更新。

如果任何时候用户点击表单外部的"**生成新点**"，脚本将重新运行。如果用户在表单内有任何未提交的更改，这些更改将_不会_随重新运行发送。对表单的所有更改只有在表单本身提交时才会发送到 Python 后端。

<Collapse title="查看源代码" expanded={false} >

```python
import streamlit as st
import pandas as pd
import numpy as np

def get_data():
    df = pd.DataFrame({
        "lat": np.random.randn(200) / 50 + 37.76,
        "lon": np.random.randn(200) / 50 + -122.4,
        "team": ['A','B']*100
    })
    return df

if st.button('生成新点'):
    st.session_state.df = get_data()
if 'df' not in st.session_state:
    st.session_state.df = get_data()
df = st.session_state.df

with st.form("my_form"):
    header = st.columns([1,2,2])
    header[0].subheader('颜色')
    header[1].subheader('透明度')
    header[2].subheader('尺寸')

    row1 = st.columns([1,2,2])
    colorA = row1[0].color_picker('团队 A', '#0000FF')
    opacityA = row1[1].slider('A 透明度', 20, 100, 50, label_visibility='hidden')
    sizeA = row1[2].slider('A 尺寸', 50, 200, 100, step=10, label_visibility='hidden')

    row2 = st.columns([1,2,2])
    colorB = row2[0].color_picker('团队 B', '#FF0000')
    opacityB = row2[1].slider('B 透明度', 20, 100, 50, label_visibility='hidden')
    sizeB = row2[2].slider('B 尺寸', 50, 200, 100, step=10, label_visibility='hidden')

    st.form_submit_button('更新地图')

alphaA = int(opacityA*255/100)
alphaB = int(opacityB*255/100)

df['color'] = np.where(df.team=='A',colorA+f'{alphaA:02x}',colorB+f'{alphaB:02x}')
df['size'] = np.where(df.team=='A',sizeA, sizeB)

st.map(df, size='size', color='color')
```

</Collapse>

<Cloud name="doc-forms-overview" height="800px"/>

## 用户交互

如果小部件不在表单中，则当用户更改其值时，该小部件将触发脚本重新运行。对于具有键控输入的小部件（`st.number_input`、`st.text_input`、`st.text_area`），当用户点击或跳出小部件时，新值会触发重新运行。用户也可以在光标处于活动状态时按 `Enter` 来提交更改。

另一方面，如果小部件在表单内部，则当用户点击或跳出该小部件时，脚本不会重新运行。对于表单内的小部件，当提交表单时脚本将重新运行，表单内的所有小部件都将向 Python 后端发送其更新的值。

![表单](/images/forms.gif)

如果用户在接收键控输入的小部件中光标处于活动状态，用户可以使用键盘上的**Enter**键提交表单。在 `st.number_input` 和 `st.text_input` 中，用户按**Enter**键提交表单。在 `st.text_area` 中，用户按**Ctrl+Enter**/**⌘+Enter**提交表单。

![键盘提交表单](/images/form-submit-keyboard.png)

## 小部件值

在提交表单之前，表单内的所有小部件都将具有默认值，就像表单外的小部件具有默认值一样。

```python
import streamlit as st

with st.form("my_form"):
   st.write("在表单内部")
   my_number = st.slider('选择一个数字', 1, 10)
   my_color = st.selectbox('选择一个颜色', ['红色','橙色','绿色','蓝色','紫色'])
   st.form_submit_button('提交我的选择')

# 这是在表单外部
st.write(my_number)
st.write(my_color)
```

<Cloud name="doc-forms-default" height="450px"/>

## 表单是容器

当调用 `st.form` 时，前端会创建一个容器。您可以像处理其他[容器元素](/develop/api-reference/layout)一样写入该容器。也就是说，您可以使用 Python 的 `with` 语句，如上面示例所示，或者您可以将表单容器分配给一个变量并直接在其上调用方法。此外，您可以将 `st.form_submit_button` 放在表单容器中的任何位置。

```python
import streamlit as st

animal = st.form('my_animal')

# 这是直接写入主主体。由于表单容器
# 在上面定义，这将出现在表单中写入的所有内容下方。
sound = st.selectbox('声音像', ['喵','汪','吱','啾'])

# 这些方法调用在表单容器上，因此它们出现在表单内部。
submit = animal.form_submit_button(f'用{sound}说它!')
sentence = animal.text_input('您的句子:', '金枪鱼在哪？')
say_it = sentence.rstrip('.,!?') + f', {sound}!'
if submit:
    animal.subheader(say_it)
else:
    animal.subheader('&nbsp;')
```

<Cloud name="doc-forms-container" height="375px"/>

## 处理表单提交

表单的目的是覆盖 Streamlit 的默认行为，即用户进行更改时立即重新运行脚本。对于表单外的小部件，逻辑流程是：

1. 用户在前端更改小部件的值。
2. `st.session_state` 中小部件的值和 Python 后端（服务器）中的值被更新。
3. 脚本重新运行开始。
4. 如果小部件有回调，它作为页面重新运行的前缀执行。
5. 在重新运行期间执行更新的小部件函数时，它输出新值。

对于表单内的小部件，用户所做的任何更改（步骤1）在提交表单之前不会传递到 Python 后端（步骤2）。此外，表单内唯一可以有回调函数的小部件是 `st.form_submit_button`。如果您需要使用新提交的值执行进程，您有三种主要模式来执行。

### 在表单后执行进程

如果您需要作为表单提交的结果执行一次性进程，您可以将该进程条件设置为 `st.form_submit_button` 并在表单后执行它。如果您需要将进程结果显示在表单上方，您可以使用容器来控制表单相对于输出的位置。

```python
import streamlit as st

col1,col2 = st.columns([1,2])
col1.title('总和:')

with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('相加')

if submit:
    col2.title(f'{a+b:.2f}')
```

<Cloud name="doc-forms-process1" height="400px"/>

### 使用带有会话状态的回调

您可以使用回调在脚本重新运行前缀执行进程。

<Important>

在回调中处理新更新的值时，不要通过 `args` 或 `kwargs` 参数直接将这些值传递给回调。您需要为回调中使用的任何小部件分配一个键。如果您在回调主体中从 `st.session_state` 查找该小部件的值，您将能够访问新提交的值。请参见下面的示例。

</Important>

```python
import streamlit as st

if 'sum' not in st.session_state:
    st.session_state.sum = ''

def sum():
    result = st.session_state.a + st.session_state.b
    st.session_state.sum = result

col1,col2 = st.columns(2)
col1.title('总和:')
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

with st.form('addition'):
    st.number_input('a', key = 'a')
    st.number_input('b', key = 'b')
    st.form_submit_button('相加', on_click=sum)
```

<Cloud name="doc-forms-process2" height="400px"/>

### 使用 `st.rerun`

如果您的进程影响表单上方的内容，另一个替代方法是使用额外的重新运行。尽管如此，这可能效率较低，可能不如上述选项理想。

```python
import streamlit as st

if 'sum' not in st.session_state:
    st.session_state.sum = ''

col1,col2 = st.columns(2)
col1.title('总和:')
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('相加')

# st.session_state.sum 的值在脚本重新运行结束时更新，
# 因此顶部 col2 中显示的值不会显示新的总和。在提交表单时触发
# 第二次重新运行以更新上方的值。
st.session_state.sum = a + b
if submit:
    st.rerun()
```

<Cloud name="doc-forms-process3" height="400px"/>

## 限制

- 每个表单必须包含一个 `st.form_submit_button`。
- `st.button` 和 `st.download_button` 不能添加到表单中。
- `st.form` 不能嵌套在另一个 `st.form` 中。
- 回调函数只能分配给表单内的 `st.form_submit_button`；表单中的其他小部件不能有回调。
- 表单内的相互依赖小部件不太可能特别有用。如果将 `widget1` 的值传递给 `widget2`，当它们都在表单内时，则 `widget2` 只有在提交表单时才会更新。