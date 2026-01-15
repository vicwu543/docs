---
title: st.pyplot
slug: /develop/api-reference/charts/st.pyplot
description: st.pyplot 显示 matplotlib.pyplot 图表。
keywords: pyplot, matplotlib, chart, visualization, data, plot, graph, figure, scientific, custom
---

<Autofunction function="streamlit.pyplot" />

<Warning>
    Matplotlib [不支持线程](https://matplotlib.org/3.3.2/faq/howto_faq.html#working-with-threads)。因此，如果您使用 Matplotlib，您应该用锁包装您的代码。当您部署和共享应用时，这个 Matplotlib 错误会更加突出，因为您更有可能获得并发用户。以下示例使用 `threading` 模块的 [`Rlock`](https://docs.python.org/3/library/threading.html#rlock-objects)。

    ```python
    import streamlit as st
    import matplotlib.pyplot as plt
    import numpy as np
    from threading import RLock

    _lock = RLock()

    x = np.random.normal(1, 1, 100)
    y = np.random.normal(1, 1, 100)

    with _lock:
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        st.pyplot(fig)
    ```

</Warning>
