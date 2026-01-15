---
title: Chart elements
slug: /develop/api-reference/charts
description: 使用 Streamlit 的图表功能创建交互式数据可视化，包括简单图表、高级可视化库和社区组件。
keywords: charts, visualization, matplotlib, vega-lite, deck.gl, altair, plotly, bokeh, pydeck, graphviz, maps, line chart, bar chart, area chart, scatter chart
---

# Chart elements

Streamlit 支持多种不同的图表库，我们的目标是不断添加更多支持。现在，我们武器库中最基本的库是 [Matplotlib](https://matplotlib.org/)。然后还有像 [Vega Lite](https://vega.github.io/vega-lite/)（2D 图表）和 [deck.gl](https://github.com/uber/deck.gl)（地图和 3D 图表）这样的交互式图表库。最后，我们还提供了一些"原生"于 Streamlit 的图表类型，如 `st.line_chart` 和 `st.area_chart`。

## Simple chart elements

<TileContainer>
<RefCard href="/develop/api-reference/charts/st.area_chart">
<Image pure alt="screenshot" src="/images/api/area_chart.jpg" />

<h4>Simple area charts</h4>

显示面积图。

```python
st.area_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bar_chart">
<Image pure alt="screenshot" src="/images/api/bar_chart.jpg" />

<h4>Simple bar charts</h4>

显示条形图。

```python
st.bar_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.line_chart">
<Image pure alt="screenshot" src="/images/api/line_chart.jpg" />

<h4>Simple line charts</h4>

显示线图。

```python
st.line_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.scatter_chart">
<Image pure alt="screenshot" src="/images/api/scatter_chart.svg" />

<h4>Simple scatter charts</h4>

显示散点图。

```python
st.scatter_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.map">
<Image pure alt="screenshot" src="/images/api/map.jpg" />

<h4>Scatterplots on maps</h4>

显示带有点的地图。

```python
st.map(my_data_frame)
```

</RefCard>
</TileContainer>

## Advanced chart elements

<TileContainer>
<RefCard href="/develop/api-reference/charts/st.pyplot">
<Image pure alt="screenshot" src="/images/api/pyplot.jpg" />

<h4>Matplotlib</h4>

显示 matplotlib.pyplot 图表。

```python
st.pyplot(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.altair_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Altair</h4>

使用 Altair 库显示图表。

```python
st.altair_chart(my_altair_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.vega_lite_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Vega-Lite</h4>

使用 Vega-Lite 库显示图表。

```python
st.vega_lite_chart(my_vega_lite_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.plotly_chart">
<Image pure alt="screenshot" src="/images/api/plotly_chart.jpg" />

<h4>Plotly</h4>

显示交互式 Plotly 图表。

```python
st.plotly_chart(my_plotly_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bokeh_chart">
<Image pure alt="screenshot" src="/images/api/bokeh_chart.jpg" />

<h4>Bokeh</h4>

显示交互式 Bokeh 图表。

```python
st.bokeh_chart(my_bokeh_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.pydeck_chart">
<Image pure alt="screenshot" src="/images/api/pydeck_chart.jpg" />

<h4>PyDeck</h4>

使用 PyDeck 库显示图表。

```python
st.pydeck_chart(my_pydeck_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.graphviz_chart">
<Image pure alt="screenshot" src="/images/api/graphviz_chart.jpg" />

<h4>GraphViz</h4>

使用 dagre-d3 库显示图表。

```python
st.graphviz_chart(my_graphviz_spec)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/tvst/plost">

<Image pure alt="screenshot" src="/images/api/components/plost.jpg" />

<h4>Plost</h4>

一个看似简单的 Streamlit 绘图库。由 [@tvst](https://github.com/tvst) 创建。

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

</ComponentCard>

<ComponentCard href="https://github.com/facebookresearch/hiplot">

<Image pure alt="screenshot" src="/images/api/components/hiplot.jpg" />

<h4>HiPlot</h4>

高维交互式绘图。由 [@facebookresearch](https://github.com/facebookresearch) 创建。

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-echarts">

<Image pure alt="screenshot" src="/images/api/components/echarts.jpg" />

<h4>ECharts</h4>

Streamlit 的 ECharts 组件。由 [@andfanilo](https://github.com/andfanilo) 创建。

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

<h4>Streamlit Folium</h4>

用于渲染 Folium 地图的 Streamlit 组件。由 [@randyzwitch](https://github.com/randyzwitch) 创建。

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/explosion/spacy-streamlit">

<Image pure alt="screenshot" src="/images/api/components/spacy.jpg" />

<h4>Spacy-Streamlit</h4>

Streamlit 应用的 spaCy 构建块和可视化工具。由 [@explosion](https://github.com/explosion) 创建。

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

</ComponentCard>

<ComponentCard href="https://github.com/ChrisDelClea/streamlit-agraph">

<Image pure alt="screenshot" src="/images/api/components/agraph.jpg" />

<h4>Streamlit Agraph</h4>

基于 [react-grah-vis](https://github.com/crubier/react-graph-vis) 的 Streamlit 图可视化。由 [@ChrisDelClea](https://github.com/ChrisDelClea) 创建。

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

<h4>Streamlit Lottie</h4>

在您的 Streamlit 应用中集成 [Lottie](https://lottiefiles.com/) 动画。由 [@andfanilo](https://github.com/andfanilo) 创建。

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

<h4>Plotly Events</h4>

让 Plotly 图表具有交互性！由 [@null-jones](https://github.com/null-jones/) 创建。

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-chart-annotations.jpg" />

<h4>Streamlit Extras</h4>

一个包含有用 Streamlit 扩展的库。由 [@arnaudmiribel](https://github.com/arnaudmiribel/) 创建。

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

</ComponentCard>

</ComponentSlider>
