---
title: 如何使 st.pydeck_chart 使用自定义 Mapbox 样式？
slug: /knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles
---

# 如何使 st.pydeck_chart 使用自定义 Mapbox 样式？

如果您提供了 Mapbox 令牌，但生成的 `pydeck_chart` 没有显示您的自定义 Mapbox 样式，请检查您是否将 Mapbox 令牌添加到 Streamlit `config.toml` 配置文件中。Streamlit 不从 PyDeck 规范内部（即从 Streamlit 应用内部）读取 Mapbox 令牌。有关更多信息，请参阅此 [论坛讨论](https://discuss.streamlit.io/t/deprecation-warning-deckgl-pydeck-maps-to-require-mapbox-token-for-production-usage/2982/10)。
