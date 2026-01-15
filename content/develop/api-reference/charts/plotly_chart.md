---
title: st.plotly_chart
slug: /develop/api-reference/charts/st.plotly_chart
description: st.plotly_chart 显示交互式 Plotly 图表。
keywords: plotly_chart, plotly, chart, visualization, data, plot, graph, interactive, dashboard, web-based
---

<Autofunction function="streamlit.plotly_chart" />

## Chart selections

<Autofunction function="PlotlyState" />

<Autofunction function="PlotlySelectionState" />

## Theming

Plotly 图表默认使用 Streamlit 主题显示。这个主题简洁、用户友好，并包含 Streamlit 的调色板。额外的好处是您的图表能更好地与应用的其余设计集成。

从 Streamlit 1.16.0 开始，可以通过 `theme="streamlit"` 关键字参数使用 Streamlit 主题。要禁用它并使用 Plotly 的原生主题，请改用 `theme=None`。

让我们看看使用 Streamlit 主题和原生 Plotly 主题的图表示例：

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

点击下方交互式应用中的选项卡，查看启用和禁用 Streamlit 主题的图表。

<Cloud name="doc-plotly-chart-theme" height="525px" />

如果您想知道自己的自定义设置是否仍会被考虑，不要担心！您仍然可以对图表配置进行更改。换句话说，虽然我们现在默认启用 Streamlit 主题，但您可以用自定义颜色或字体覆盖它。例如，如果您希望图表线条是绿色而不是默认的红色，您可以这样做！

以下是一个定义了自定义颜色比例并反映在图表中的 Plotly 图表示例：

```python
import plotly.express as px
import streamlit as st

st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

注意，即使启用 Streamlit 主题，自定义颜色比例仍会反映在图表中 👇

<Cloud name="doc-plotly-custom-colors" height="650px" />

有关更多使用和不使用 Streamlit 主题的 Plotly 图表示例，请查看 [plotly.streamlit.app](https://plotly.streamlit.app)。
