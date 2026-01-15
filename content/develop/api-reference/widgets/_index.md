---
title: Input widgets
slug: /develop/api-reference/widgets
description: 使用输入小部件为 Streamlit 应用添加交互性，包括按钮、滑块、文本输入、选择框、文件上传器和更多交互式组件。
keywords: input widgets, interactive widgets, buttons, sliders, text input, selectbox, checkbox, radio, file upload, user input, form controls, interactive elements
---

# Input widgets

使用小部件，Streamlit 允许您使用按钮、滑块、文本输入等直接为您的应用添加交互性。

## Button elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.button">

<Image pure alt="screenshot" src="/images/api/button.svg" />

<h4>Button</h4>

显示按钮小部件。

```python
clicked = st.button("Click me")
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.download_button">

<Image pure alt="screenshot" src="/images/api/download_button.svg" />

<h4>Download button</h4>

显示下载按钮小部件。

```python
st.download_button("Download file", file)
```

</RefCard>

<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button">

<Image pure alt="screenshot" src="/images/api/form_submit_button.svg" />

<h4>Form button</h4>

显示表单提交按钮。与 `st.form` 一起使用。

```python
st.form_submit_button("Sign up")
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.link_button">

<Image pure alt="screenshot" src="/images/api/link_button.svg" />

<h4>Link button</h4>

显示链接按钮。

```python
st.link_button("Go to gallery", url)
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.page_link">

<Image pure alt="screenshot" src="/images/api/page_link.jpg" />

<h4>Page link</h4>

显示指向多页应用中另一页的链接。

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

</RefCard>

</TileContainer>

## Selection elements

<TileContainer>

<RefCard href="/develop/api-reference/widgets/st.checkbox">

<Image pure alt="screenshot" src="/images/api/checkbox.jpg" />

<h4>Checkbox</h4>

显示复选框小部件。

```python
selected = st.checkbox("I agree")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.color_picker">

<Image pure alt="screenshot" src="/images/api/color_picker.jpg" />

<h4>Color picker</h4>

显示颜色选择器小部件。

```python
color = st.color_picker("Pick a color")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.feedback">

<Image pure alt="screenshot" src="/images/api/feedback.jpg" />

<h4>Feedback</h4>

显示评分或情感按钮组。

```python
st.feedback("stars")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.multiselect">

<Image pure alt="screenshot" src="/images/api/multiselect.jpg" />

<h4>Multiselect</h4>

显示多选小部件。多选小部件初始为空。

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.pills">

<Image pure alt="screenshot" src="/images/api/pills.jpg" />

<h4>Pills</h4>

显示药丸按钮选择小部件。

```python
st.pills("Tags", ["Sports", "AI", "Politics"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.radio">

<Image pure alt="screenshot" src="/images/api/radio.jpg" />

<h4>Radio</h4>

显示单选按钮小部件。

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.segmented_control">

<Image pure alt="screenshot" src="/images/api/segmented_control.jpg" />

<h4>Segmented control</h4>

显示分段按钮选择小部件。

```python
st.segmented_control("Filter", ["Open", "Closed", "All"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.select_slider">

<Image pure alt="screenshot" src="/images/api/select_slider.jpg" />

<h4>Select slider</h4>

显示滑块小部件以从列表中选择项目。

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.selectbox">

<Image pure alt="screenshot" src="/images/api/selectbox.jpg" />

<h4>Selectbox</h4>

显示选择小部件。

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.toggle">

<Image pure alt="screenshot" src="/images/api/toggle.jpg" />

<h4>Toggle</h4>

显示切换小部件。

```python
activated = st.toggle("Activate")
```

</RefCard>

</TileContainer>

## Numeric input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.number_input">

<Image pure alt="screenshot" src="/images/api/number_input.jpg" />

<h4>Number input</h4>

显示数字输入小部件。

```python
choice = st.number_input("Pick a number", 0, 10)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.slider">

<Image pure alt="screenshot" src="/images/api/slider.jpg" />

<h4>Slider</h4>

显示滑块小部件。

```python
number = st.slider("Pick a number", 0, 100)
```

</RefCard>

</TileContainer>

## Date and time input elements

<TileContainer>

<RefCard href="/develop/api-reference/widgets/st.date_input">

<Image pure alt="screenshot" src="/images/api/date_input.jpg" />

<h4>Date input</h4>

显示日期输入小部件。

```python
date = st.date_input("Your birthday")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.datetime_input">

<Image pure alt="screenshot" src="/images/api/datetime_input.jpg" />

<h4>Datetime input</h4>

显示日期时间输入小部件。

```python
datetime = st.datetime_input("Schedule your event")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.time_input">

<Image pure alt="screenshot" src="/images/api/time_input.jpg" />

<h4>Time input</h4>

显示时间输入小部件。

```python
time = st.time_input("Meeting time")
```

</RefCard>

</TileContainer>

## Text input elements

<TileContainer>

<RefCard href="/develop/api-reference/widgets/st.text_input">

<Image pure alt="screenshot" src="/images/api/text_input.jpg" />

<h4>Text input</h4>

显示单行文本输入小部件。

```python
name = st.text_input("First name")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_area">

<Image pure alt="screenshot" src="/images/api/text_area.jpg" />

<h4>Text area</h4>

显示多行文本输入小部件。

```python
text = st.text_area("Text to translate")
```

</RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

<h4>Chat input</h4>

显示聊天输入小部件。

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>

</TileContainer>

## Other input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.audio_input">

<Image pure alt="screenshot" src="/images/api/audio_input.jpg" />

<h4>Audio input</h4>

显示允许用户使用麦克风录制的窗口小部件。

```python
speech = st.audio_input("Record a voice message")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

<h4>Data editor</h4>

显示数据编辑器小部件。

```python
edited = st.data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.file_uploader">

<Image pure alt="screenshot" src="/images/api/file_uploader.jpg" />

<h4>File uploader</h4>

显示文件上传器小部件。

```python
data = st.file_uploader("Upload a CSV")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.camera_input">

<Image pure alt="screenshot" src="/images/api/camera_input.jpg" />

<h4>Camera input</h4>

显示允许用户直接从相机上传图像的小部件。

```python
image = st.camera_input("Take a picture")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

<h4>Streamlit Elements</h4>

在 Streamlit 中创建可拖拽和可调整大小的仪表板。由 [@okls](https://github.com/okls) 创建。

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

<h4>Tags</h4>

为您的 Streamlit 应用添加标签。由 [@gagan3012](https://github.com/gagan3012) 创建。

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

<h4>Stqdm</h4>

在 Streamlit 应用中处理进度条的最简单方法。由 [@Wirg](https://github.com/Wirg) 创建。

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/innerdoc/streamlit-timeline">

<Image pure alt="screenshot" src="/images/api/components/timeline.jpg" />

<h4>Timeline</h4>

使用 [TimelineJS](https://timeline.knightlab.com/) 在 Streamlit 应用中显示时间线。由 [@innerdoc](https://github.com/innerdoc) 创建。

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
  timeline(f.read(), height=800)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-camera-input-live">

<Image pure alt="screenshot" src="/images/api/components/camera-live.jpg" />

<h4>Camera input live</h4>

st.camera_input 的替代方案，可实时返回网络摄像头图像。由 [@blackary](https://github.com/blackary) 创建。

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

<h4>Streamlit Ace</h4>

Streamlit 的 Ace 编辑器组件。由 [@okld](https://github.com/okld) 创建。

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/AI-Yash/st-chat">

<Image pure alt="screenshot" src="/images/api/components/chat.jpg" />

<h4>Streamlit Chat</h4>

聊天机器人 UI 的 Streamlit 组件。由 [@AI-Yash](https://github.com/AI-Yash) 创建。

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```

</ComponentCard>

<ComponentCard href="https://github.com/victoryhb/streamlit-option-menu">

<Image pure alt="screenshot" src="/images/api/components/option-menu.jpg" />

<h4>Streamlit Option Menu</h4>

从菜单中的选项列表中选择单个项目。由 [@victoryhb](https://github.com/victoryhb) 创建。

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'],
  icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-toggle.jpg" />

<h4>Streamlit Extras</h4>

一个包含有用 Streamlit 扩展的库。由 [@arnaudmiribel](https://github.com/arnaudmiribel/) 创建。

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!", """🥷 Surprise! Here's some additional content""",)
```

</ComponentCard>

</ComponentSlider>
