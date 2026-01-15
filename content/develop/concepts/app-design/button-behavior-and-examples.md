---
title: 按钮行为和示例
slug: /develop/concepts/design/buttons
description: 了解 Streamlit 按钮行为、状态管理以及使用 st.button 与 st.session_state 的实际示例用于交互式应用。
keywords: 按钮行为, st.button, streamlit 按钮, 会话状态, 按钮状态, 按钮示例, 交互式按钮, 按钮模式, 按钮反模式, 状态管理
---

# 按钮行为和示例

## 摘要

使用 [`st.button`](/develop/api-reference/widgets/st.button) 创建的按钮不保留状态。它们在由其点击导致的脚本重新运行时返回 `True`，并在下一个脚本重新运行时立即返回 `False`。如果显示的元素嵌套在 `if st.button('Click me'):` 内，该元素将在单击按钮时可见，并在用户采取下一步操作后立即消失。这是因为脚本重新运行，按钮返回值变为 `False`。

在本指南中，我们将说明按钮的使用并解释常见的误解。继续阅读以查看各种示例，这些示例使用 [`st.session_state`](/develop/api-reference/caching-and-state/st.session_state) 扩展 `st.button`。[反模式](#anti-patterns)包含在最后。继续并拿起你喜欢的代码编辑器，这样当你阅读时可以 `streamlit run` 示例。如果你还没有运行过自己的 Streamlit 脚本，请查看 Streamlit 的[基本概念](/get-started/fundamentals/main-concepts)。

## 何时使用 `if st.button()`

当代码以按钮的值为条件时，它将一次执行以响应按钮被单击，并且不会再次执行（直到再次单击按钮）。

适合在按钮内嵌套：

- 立即消失的临时消息。
- 每次单击一次的过程，将数据保存到会话状态、文件或数据库。

不适合在按钮内嵌套：

- 应在用户继续时保持的显示项。
- 使用时导致脚本重新运行的其他小部件。
- 既不修改会话状态也不写入文件/数据库的过程。\*

\* 当需要一次性结果时，这可能是合适的。如果你有一个"验证"按钮，它可能是直接以按钮为条件的过程。它可以用来创建一个警报来说"有效"或"无效"，无需保留该信息。

## 按钮的常见逻辑

### 使用按钮显示临时消息

如果你想给用户一个快速按钮来检查条目是否有效，但在用户继续时不保留该检查显示。

在此示例中，用户可以单击按钮来检查其 `animal` 字符串是否在 `animal_shelter` 列表中。当用户单击"**检查可用性**"时，他们将看到"我们有那个动物！"或"我们没有那个动物。"如果他们在 [`st.text_input`](/develop/api-reference/widgets/st.text_input) 中更改动物，脚本会重新运行，消息会消失，直到他们再次单击"**检查可用性**"。

```python
import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'
```

注意：上面的示例使用[魔法](/develop/api-reference/write-magic/magic)在前端渲染消息。

### 有状态按钮

如果你希望单击的按钮继续为 `True`，请在 `st.session_state` 中创建一个值，并使用按钮通过回调将该值设置为 `True`。

```python
import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')
```

### 切换按钮

如果你希望按钮像切换开关一样工作，请考虑使用 [`st.checkbox`](/develop/api-reference/widgets/st.checkbox)。否则，你可以使用带有回调函数的按钮来反转保存在 `st.session_state` 中的布尔值。

在此示例中，我们使用 `st.button` 来打开和关闭另一个小部件。通过在 `st.session_state` 中的值上有条件地显示 [`st.slider`](/develop/api-reference/widgets/st.slider)，用户可以与滑块交互而不会使其消失。

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')
```

或者，你可以在滑块的 `disabled` 参数上使用 `st.session_state` 中的值。

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

st.slider('Select a value', disabled=st.session_state.button)
```

### 按钮用于继续或控制过程的阶段

另一种替代在按钮内嵌套内容的方法是在 `st.session_state` 中使用指定过程的"步骤"或"阶段"的值。在此示例中，我们的脚本中有四个阶段：

0. 用户开始之前。
1. 用户输入他们的名字。
2. 用户选择颜色。
3. 用户获得感谢消息。

开始处的按钮将阶段从 0 推进到 1。末尾的按钮将阶段从 3 重置为 0。阶段 1 和 2 中使用的其他小部件有回调来设置阶段。如果你有一个依赖步骤的过程，并希望保持之前的阶段可见，这样的回调会强制用户在更改早期小部件时重新追踪后续阶段。

```python
import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    name = st.text_input('Name', on_change=set_state, args=[2])

if st.session_state.stage >= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write(f':{color}[Thank you!]')
    st.button('Start Over', on_click=set_state, args=[0])
```

### 按钮修改 `st.session_state`

如果你在按钮内修改 `st.session_state`，你必须考虑该按钮在脚本中的位置。

#### 一个小问题

在此示例中，我们在修改它的按钮之前和之后访问 `st.session_state.name`。单击按钮（"**Jane**"或"**John**"）时，脚本会重新运行。按钮之前显示的信息滞后于按钮之后写入的信息。按钮之前的 `st.session_state` 中的数据未更新。当脚本执行按钮函数时，这是有条件代码更新 `st.session_state` 的创建更改的时候。因此，此更改在按钮之后反映。

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'

if st.button('John'):
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])
```

#### 回调中使用的逻辑

回调是修改 `st.session_state` 的干净方法。回调作为脚本重新运行的前缀执行，因此按钮相对于访问数据的位置并不重要。

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

def change_name(name):
    st.session_state['name'] = name

st.header(st.session_state['name'])

st.button('Jane', on_click=change_name, args=['Jane Doe'])
st.button('John', on_click=change_name, args=['John Doe'])

st.header(st.session_state['name'])
```

#### 按钮内嵌套的逻辑和重新运行

虽然回调通常优先于避免额外重新运行，但我们的第一个"John Doe"/"Jane Doe"示例可以通过添加 [`st.rerun`](/develop/api-reference/execution-flow/st.rerun) 来修改。如果你需要在修改它的按钮之前访问 `st.session_state` 中的数据，你可以包含 `st.rerun` 来在进行更改后重新运行脚本。这意味着单击按钮时脚本将重新运行两次。

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'
    st.rerun()

if st.button('John'):
    st.session_state['name'] = 'John Doe'
    st.rerun()

st.header(st.session_state['name'])
```

### 按钮修改或重置其他小部件

当使用按钮来修改或重置另一个小部件时，它与上述修改 `st.session_state` 的示例相同。但是，存在一个额外的考虑：如果小部件的小部件已经为当前脚本运行呈现在页面上，你不能修改 `st.session_state` 中的键值对。

<Important>

不要这样做！

```python
import streamlit as st

st.text_input('Name', key='name')

# These buttons will error because their nested code changes
# a widget's state after that widget within the script.
if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    st.session_state.name = ('Streamlit')
```

</Important>

#### 选项 1：为按钮使用键并将逻辑放在小部件之前

如果你为按钮分配了一个键，你可以通过在 `st.session_state` 中使用其值来根据按钮的状态来条件化代码。这意味着取决于你的按钮的逻辑可以在你的脚本中的该按钮之前。在以下示例中，我们在 `st.session_state` 上使用 `.get()` 方法，因为按钮的键在脚本首次运行时不会存在。`.get()` 方法如果找不到密钥，将返回 `False`。否则，它将返回密钥的值。

```python
import streamlit as st

# Use the get method since the keys won't be in session_state
# on the first script run
if st.session_state.get('clear'):
    st.session_state['name'] = ''
if st.session_state.get('streamlit'):
    st.session_state['name'] = 'Streamlit'

st.text_input('Name', key='name')

st.button('Clear name', key='clear')
st.button('Streamlit!', key='streamlit')
```

#### 选项 2：使用回调

```python
import streamlit as st

st.text_input('Name', key='name')

def set_name(name):
    st.session_state.name = name

st.button('Clear name', on_click=set_name, args=[''])
st.button('Streamlit!', on_click=set_name, args=['Streamlit'])
```

#### 选项 3：使用容器

通过使用 [`st.container`](/develop/api-reference/layout/st.container)，你可以在脚本和前端视图（网页）中以不同的顺序显示小部件。

```python
import streamlit as st

begin = st.container()

if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    st.session_state.name = ('Streamlit')

# The widget is second in logic, but first in display
begin.text_input('Name', key='name')
```

### 按钮动态添加其他小部件

动态向页面添加小部件时，请确保使用索引来保持键唯一并避免 `DuplicateWidgetID` 错误。在此示例中，我们定义一个函数 `display_input_row`，它呈现一行小部件。该函数接受 `index` 作为参数。`display_input_row` 呈现的小部件在其键中使用 `index`，以便可以在单个脚本重新运行上多次执行 `display_input_row` 而不重复任何小部件键。

```python
import streamlit as st

def display_input_row(index):
    left, middle, right = st.columns(3)
    left.text_input('First', key=f'first_{index}')
    middle.text_input('Middle', key=f'middle_{index}')
    right.text_input('Last', key=f'last_{index}')

if 'rows' not in st.session_state:
    st.session_state['rows'] = 0

def increase_rows():
    st.session_state['rows'] += 1

st.button('Add person', on_click=increase_rows)

for i in range(st.session_state['rows']):
    display_input_row(i)

# Show the results
st.subheader('People')
for i in range(st.session_state['rows']):
    st.write(
        f'Person {i+1}:',
        st.session_state[f'first_{i}'],
        st.session_state[f'middle_{i}'],
        st.session_state[f'last_{i}']
    )
```

### 按钮处理昂贵或文件写入的过程

当你有昂贵的过程时，将其设置为在单击按钮时运行，并将结果保存到 `st.session_state`。这允许你继续访问过程的结果而无需不必要地重新执行它。这对于保存到磁盘或写入数据库的过程特别有帮助。在此示例中，我们有一个 `expensive_process`，取决于两个参数：`option` 和 `add`。从功能上讲，`add` 改变输出，但 `option` 不改变 — `option` 的存在是为了提供参数

```python
import streamlit as st
import pandas as pd
import time

def expensive_process(option, add):
    with st.spinner('Processing...'):
        time.sleep(5)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C':[7, 8, 9]}) + add
    return (df, add)

cols = st.columns(2)
option = cols[0].selectbox('Select a number', options=['1', '2', '3'])
add = cols[1].number_input('Add a number', min_value=0, max_value=10)

if 'processed' not in st.session_state:
    st.session_state.processed = {}

# Process and save results
if st.button('Process'):
    result = expensive_process(option, add)
    st.session_state.processed[option] = result
    st.write(f'Option {option} processed with add {add}')
    result[0]
```

敏锐的观察者可能会想，"这感觉有点像缓存。"我们只保存与一个参数相关的结果，但该模式可以轻松扩展以保存与两个参数都相关的结果。从这个意义上讲，是的，它与缓存有一些相似之处，但也有一些重要的区别。当你在 `st.session_state` 中保存结果时，这些结果仅可用于其当前会话中的当前用户。如果你改为使用 [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data)，这些结果将对所有会话中的所有用户可用。此外，如果要更新保存的结果，你必须清除该函数的所有保存结果才能这样做。

## 反模式

以下是按钮如何出错的一些简化示例。请注意这些常见错误。

### 嵌套在按钮内的按钮

```python
import streamlit as st

if st.button('Button 1'):
    st.write('Button 1 was clicked')
    if st.button('Button 2'):
        # This will never be executed.
        st.write('Button 2 was clicked')
```

### 嵌套在按钮内的其他小部件

```python
import streamlit as st

if st.button('Sign up'):
    name = st.text_input('Name')

    if name:
        # This will never be executed.
        st.success(f'Welcome {name}')
```

### 在按钮内嵌套过程而不保存到会话状态

```python
import streamlit as st
import pandas as pd

file = st.file_uploader("Upload a file", type="csv")

if st.button('Get data'):
    df = pd.read_csv(file)
    # This display will go away with the user's next action.
    st.write(df)

if st.button('Save'):
    # This will always error.
    df.to_csv('data.csv')
```
