---
title: st.vega_lite_chart
slug: /develop/api-reference/charts/st.vega_lite_chart
description: st.vega_lite_chart 使用 Vega-Lite 库显示交互式图表。
keywords: vega_lite_chart, vega-lite, chart, visualization, data, plot, graph, interactive, json, grammar of graphics
---

<Autofunction function="streamlit.vega_lite_chart" />

## Chart selections

<Autofunction function="VegaLiteState" />

<Autofunction function="DeltaGenerator.add_rows" deprecated={true} deprecatedText="We plan to deprecate <code>.add_rows()</code>. Please leave <a href='https://github.com/streamlit/streamlit/issues/13063'>feedback</a>." />

## Theming

Vega-Lite 图表默认使用 Streamlit 主题显示。这个主题简洁、用户友好，并包含 Streamlit 的调色板。额外的好处是您的图表能更好地与应用的其余设计集成。

从 Streamlit 1.16.0 开始，可以通过 `theme="streamlit"` 关键字参数使用 Streamlit 主题。要禁用它并使用 Vega-Lite 的原生主题，请改用 `theme=None`。

让我们看看使用 Streamlit 主题和原生 Vega-Lite 主题的图表示例：

```python
import streamlit as st
from vega_datasets import data

source = data.cars()

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        source, chart, theme=None, use_container_width=True
    )
```

点击下方交互式应用中的选项卡，查看启用和禁用 Streamlit 主题的图表。

<Cloud name="doc-vega-lite-theme" height="500px" />

如果您想知道自己的自定义设置是否仍会被考虑，不要担心！您仍然可以对图表配置进行更改。换句话说，虽然我们现在默认启用 Streamlit 主题，但您可以用自定义颜色或字体覆盖它。例如，如果您希望图表线条是绿色而不是默认的红色，您可以这样做！
