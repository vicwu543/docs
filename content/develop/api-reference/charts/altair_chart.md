---
title: st.altair_chart
slug: /develop/api-reference/charts/st.altair_chart
description: st.altair_chart 使用 Altair 库显示交互式图表。
keywords: altair_chart, altair, chart, visualization, data, plot, graph, vega-lite, interactive, grammar of graphics
---

<Autofunction function="streamlit.altair_chart" />

## 图表选择

<Autofunction function="VegaLiteState" />

<Autofunction function="DeltaGenerator.add_rows" deprecated={true} deprecatedText="我们计划弃用 <code>.add_rows()</code>。请留下<a href='https://github.com/streamlit/streamlit/issues/13063'>反馈</a>。" />

## 主题

Altair 图表默认使用 Streamlit 主题显示。此主题时尚、用户友好，并融入 Streamlit 的调色板。额外的好处是您的图表更好地与应用的其余设计集成。

从 Streamlit 1.16.0 开始，Streamlit 主题通过 `theme="streamlit"` 关键字参数可用。要禁用它并使用 Altair 的原生主题，请改用 `theme=None`。

让我们看看使用 Streamlit 主题和原生 Altair 主题的图表示例：

```python
import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)
```

单击下面的交互式应用中的选项卡，查看启用和禁用 Streamlit 主题的图表。

<Cloud name="doc-altair-chart" height="500px" />

如果您想知道自己的自定义是否仍会被考虑，不要担心！您仍然可以对图表配置进行更改。换句话说，虽然我们现在默认启用 Streamlit 主题，但您可以用自定义颜色或字体覆盖它。例如，如果您希望图表线条为绿色而不是默认红色，您可以做到！

以下是手动传递颜色并反映的 Altair 图表示例：

<Collapse title="See the code">

```python
import altair as alt
import streamlit as st
from vega_datasets import data

source = data.seattle_weather()

scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(date):T", title="Date"),
        alt.Y(
            "temp_max:Q",
            title="Maximum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)

# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(
        width=550,
    )
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
```

</Collapse>

注意，即使启用 Streamlit 主题，自定义颜色仍反映在图表中 👇

<Cloud name="doc-altair-custom-colors" height="675px" />

有关更多使用和不使用 Streamlit 主题的 Altair 图表示例，请查看 [altair.streamlit.app](https://altair.streamlit.app)。
