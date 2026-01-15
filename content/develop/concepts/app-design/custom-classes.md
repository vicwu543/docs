---
title: 在 Streamlit 应用中使用自定义 Python 类
slug: /develop/concepts/design/custom-classes
description: 学习在 Streamlit 应用中使用自定义 Python 类、数据类和枚举的最佳实践，包括处理类重定义和跨重新运行的比较问题。
keywords: 自定义类, python 类, dataclass, enum, 类重定义, streamlit 重新运行, 类比较, 实例比较, 自定义接口, 类模式
---

# 在 Streamlit 应用中使用自定义 Python 类

如果你正在构建一个复杂的 Streamlit 应用或使用现有代码，你可能在脚本中定义了自定义 Python 类。常见的例子包括以下内容：

- 定义 `@dataclass` 来在应用中存储相关数据。
- 定义 `Enum` 类来表示一组固定的选项或值。
- 定义自定义接口到外部服务或 [`st.connection`](/develop/api-reference/connections/st.connection) 未覆盖的数据库。

因为 Streamlit 在每次用户交互后重新运行你的脚本，自定义类可能在同一 Streamlit 会话内多次重定义。这可能导致不期望的效果，特别是在类和实例比较中。继续阅读以了解这个常见陷阱以及如何避免它。

我们首先介绍一些通用模式，你可以将其用于不同类型的自定义类，然后介绍一些更多技术细节，说明为什么这很重要。最后，我们详细介绍[使用 `Enum` 类](#using-enum-classes-in-streamlit)，并描述一个可以使其更方便的配置选项。

## 定义自定义类的模式

### 模式 1：在单独的模块中定义你的类

这是推荐的通用解决方案。如果可能，将类定义移到它们自己的模块文件中并将其导入到应用脚本中。只要你不编辑定义应用的文件，Streamlit 就不会在每次重新运行时重新导入那些类。因此，如果一个类在外部文件中定义并导入到你的脚本中，该类在会话期间不会被重定义，除非你正在主动编辑你的应用。

#### 示例：移动你的类定义

尝试运行以下 Streamlit 应用，其中 `MyClass` 在页面的脚本中定义。`isinstance()` 将在第一个脚本运行时返回 `True`，然后在之后的每次重新运行时返回 `False`。

```python
# app.py
import streamlit as st

# MyClass gets redefined every time app.py reruns
class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

if "my_instance" not in st.session_state:
  st.session_state.my_instance = MyClass("foo", "bar")

# Displays True on the first run then False on every rerun
st.write(isinstance(st.session_state.my_instance, MyClass))

st.button("Rerun")
```

如果你将类定义移出 `app.py` 到另一个文件中，你可以使 `isinstance()` 一致地返回 `True`。考虑以下文件结构：

```
myproject/
├── my_class.py
└── app.py
```

```python
# my_class.py
class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
```

```python
# app.py
import streamlit as st
from my_class import MyClass # MyClass doesn't get redefined with each rerun

if "my_instance" not in st.session_state:
  st.session_state.my_instance = MyClass("foo", "bar")

# Displays True on every rerun
st.write(isinstance(st.session_state.my_instance, MyClass))

st.button("Rerun")
```

Streamlit 仅在检测到代码已更改时重新加载导入模块中的代码。因此，如果你正在主动编辑应用代码，你可能需要启动新的会话或重新启动 Streamlit 服务器以避免不期望的类重定义。

### 模式 2：强制你的类比较内部值

对于存储数据的类（如[数据类](https://docs.python.org/3/library/dataclasses.html)），你可能更感兴趣的是比较内部存储的值而不是类本身。如果你定义自定义的 `__eq__` 方法，你可以强制在内部存储的值上进行比较。

#### 示例：定义 `__eq__`

尝试运行以下 Streamlit 应用，并观察比较如何在第一次运行时为 `True`，然后在之后的每次重新运行时为 `False`。

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5)

# Displays True on the first run the False on every rerun
st.session_state.my_dataclass == MyDataclass(1, 5.5)

st.button("Rerun")
```

由于 `MyDataclass` 在每次重新运行时被重定义，存储在会话状态中的实例将不等于在稍后脚本运行中定义的任何实例。你可以通过强制比较内部值来修复此问题，如下所示：

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

    def __eq__(self, other):
        # An instance of MyDataclass is equal to another object if the object
        # contains the same fields with the same values
        return (self.var1, self.var2) == (other.var1, other.var2)

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5)

# Displays True on every rerun
st.session_state.my_dataclass == MyDataclass(1, 5.5)

st.button("Rerun")
```

对于常规类或 `@dataclass` 的默认 Python `__eq__` 实现取决于类或类实例的内存中 ID。为了避免 Streamlit 中的问题，你的自定义 `__eq__` 方法不应依赖 `self` 和 `other` 的 `type()`。

### 模式 3：将你的类存储为序列化数据

存储数据的类的另一个选项是为你的类定义序列化和反序列化方法，如 `to_str` 和 `from_str`。你可以使用这些在 `st.session_state` 中存储类实例数据而不是存储类实例本身。与模式 2 相似，这是一种强制比较内部数据并绕过不断变化的内存中 ID 的方式。

#### 示例：将你的类实例保存为字符串

使用与模式 2 相同的示例，这可以按如下方式完成：

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

    def to_str(self):
        return f"{self.var1},{self.var2}"

    @classmethod
    def from_str(cls, serial_str):
        values = serial_str.split(",")
        var1 = int(values[0])
        var2 = float(values[1])
        return cls(var1, var2)

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5).to_str()

# Displays True on every rerun
MyDataclass.from_str(st.session_state.my_dataclass) == MyDataclass(1, 5.5)

st.button("Rerun")
```

### 模式 4：使用缓存来保留你的类

对于用作资源的类（数据库连接、状态管理器、API），请考虑使用缓存单例模式。使用 `@st.cache_resource` 来装饰你类的 `@staticmethod` 以生成该类的单个缓存实例。例如：

```python
import streamlit as st

class MyResource:
    def __init__(self, api_url: str):
        self._url = api_url

    @st.cache_resource(ttl=300)
    @staticmethod
    def get_resource_manager(api_url: str):
        return MyResource(api_url)

# This is cached until Session State is cleared or 5 minutes has elapsed.
resource_manager = MyResource.get_resource_manager("http://example.com/api/")
```

当你在函数上使用 Streamlit 的缓存装饰器之一时，Streamlit 不使用函数对象来查找缓存的值。相反，Streamlit 的缓存装饰器使用函数的限定名称和模块来索引返回值。因此，即使 Streamlit 在每次脚本运行时都重定义了 `MyResource`，`st.cache_resource` 也不受此影响。`get_resource_manager()` 将在每次重新运行时返回其缓存值，直到该值过期。

## 理解 Python 如何定义和比较类

那么这里真正发生了什么？我们将考虑一个简单的例子来说明为什么这是一个陷阱。如果你不想处理更多细节，可以随时跳过本部分。你可以跳到前面以了解[使用 `Enum` 类](#using-enum-classes-in-streamlit)。

### 示例：定义同一个类两次时会发生什么？

暂时搁置 Streamlit，思考这个简单的 Python 脚本：

```python
from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    name: str

Marshall_A = Student(1, "Marshall")
Marshall_B = Student(1, "Marshall")

# This is True (because a dataclass will compare two of its instances by value)
Marshall_A == Marshall_B

# Redefine the class
@dataclass
class Student:
    student_id: int
    name: str

Marshall_C = Student(1, "Marshall")

# This is False
Marshall_A == Marshall_C
```

在此示例中，数据类 `Student` 定义了两次。所有三个 Marshall 都有相同的内部值。如果你比较 `Marshall_A` 和 `Marshall_B`，它们将相等，因为它们都是从 `Student` 的第一个定义创建的。但是，如果你比较 `Marshall_A` 和 `Marshall_C`，它们将不相等，因为 `Marshall_C` 是从 `Student` 的第二个定义创建的。即使两个 `Student` 数据类的定义完全相同，它们有不同的内存中 ID，因此是不同的。

### Streamlit 中发生了什么？

在 Streamlit 中，你可能在页面脚本中没有两次写同一个类。但是，Streamlit 的重新运行逻辑产生了相同的效果。让我们使用上面的示例作为类比。如果你在一个脚本运行中定义一个类并在会话状态中保存一个实例，那么稍后的重新运行将重定义该类，你最终可能会将重新运行中的 `Marshall_C` 与会话状态中的 `Marshall_A` 进行比较。由于小部件在底层依赖会话状态，这是事情变得混乱的地方。

## Streamlit 小部件如何存储选项

多个 Streamlit UI 元素，如 `st.selectbox` 或 `st.radio`，通过 `options` 参数接受多选选项。应用的用户通常可以选择其中一个或多个选项。小部件函数返回选定的值。例如：

```python
number = st.selectbox("Pick a number, any number", options=[1, 2, 3])
# number == whatever value the user has selected from the UI.
```

当你调用函数（如 `st.selectbox`）并向 `options` 传递 `Iterable` 时，`Iterable` 和当前选择被保存到[会话状态](/develop/concepts/architecture/session-state)的隐藏部分，称为小部件元数据。

当应用的用户与 `st.selectbox` 小部件交互时，浏览器将其选择的索引发送到 Streamlit 服务器。该索引用于确定从原始 `options` 列表返回到应用的值，该列表保存在上一个页面执行的小部件元数据中。

关键细节是 `st.selectbox`（或类似的小部件函数）返回的值来自在页面的先前执行期间保存在会话状态中的 `Iterable`，而不是在当前执行中传递给 `options` 的值。Streamlit 以这种方式设计的有许多架构原因，我们不会在这里讨论。但是，**这**是我们最终比较不同类的实例的方式，而我们认为我们在比较同一类的实例。

### 一个病理性示例

上面的解释可能有点令人困惑，所以这里有一个病理性的例子来说明这个想法。

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    name: str

Marshall_A = Student(1, "Marshall")
if "B" not in st.session_state:
    st.session_state.B = Student(1, "Marshall")
Marshall_B = st.session_state.B

options = [Marshall_A,Marshall_B]
selected = st.selectbox("Pick", options)

# This comparison does not return expected results:
selected == Marshall_A
# This comparison evaluates as expected:
selected == Marshall_B
```

最后的说明是，我们在这一部分的示例中使用了 `@dataclass` 来说明一点，但实际上，一般来说，可能会遇到这些相同的类问题。任何在比较运算符（如 `__eq__` 或 `__gt__`）中检查类身份的类都可以展示这些问题。

## 在 Streamlit 中使用 `Enum` 类

Python 标准库中的 [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum) 类是定义自定义符号名称的强大方式，这些名称可以代替 `str` 值用作 `st.multiselect` 或 `st.selectbox` 的选项。

例如，你可能向 streamlit 页面添加以下内容：

```python
from enum import Enum
import streamlit as st

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

selected_colors = set(st.multiselect("Pick colors", options=Color))

if selected_colors == {Color.RED, Color.GREEN}:
    st.write("Hooray, you found the color YELLOW!")
```

如果你使用的是最新版本的 Streamlit，此 Streamlit 页面将按其应该的方式工作。当用户同时选择 `Color.RED` 和 `Color.GREEN` 时，他们会看到特殊消息。

但是，如果你已经读过本页的其余部分，你可能会注意到一些棘手的地方。具体来说，`Enum` 类 `Color` 在每次运行此脚本时都会被重定义。在 Python 中，如果你使用相同的类名、成员和值定义两个 `Enum` 类，这些类及其成员仍然被认为彼此是唯一的。这应该导致上面的 `if` 条件始终计算为 `False`。在任何脚本重新运行中，`st.multiselect` 返回的 `Color` 值将是与该脚本运行中定义的 `Color` 的不同类。

如果你使用 Streamlit 版本 1.28.0 或更早版本运行上面的代码片段，你将无法看到特殊消息。幸运的是，从版本 1.29.0 起，Streamlit 引入了一个配置选项来大大简化问题。这就是启用的默认 `enumCoercion` 配置选项的用武之地。

### 理解 `enumCoercion` 配置选项

启用 `enumCoercion` 后，Streamlit 会尝试识别你何时使用元素（如 `st.multiselect` 或 `st.selectbox`），且以一组 `Enum` 成员为选项。

如果 Streamlit 检测到这一点，它会将小部件的返回值转换为最新脚本运行中定义的 `Enum` 类的成员。这是我们称之为自动 `Enum` 强制转换的东西。

此行为可通过你的 Streamlit `config.toml` 文件中的 `enumCoercion` 设置进行[配置](/develop/concepts/configuration)。它默认启用，并可能被禁用或设置为一组更严格的匹配条件。

如果你发现在启用 `enumCoercion` 的情况下仍然遇到问题，请考虑使用上面描述的[自定义类模式](#patterns-to-define-your-custom-classes)，例如将你的 `Enum` 类定义移到单独的模块文件中。
