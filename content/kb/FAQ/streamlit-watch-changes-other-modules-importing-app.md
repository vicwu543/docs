---
title: 如何让 Streamlit 监视我在应用中导入的其他模块中的更改？
slug: /knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app
---

# 如何让 Streamlit 监视我在应用中导入的其他模块中的更改？

默认情况下，Streamlit 仅监视包含在主应用模块当前目录中的模块。您可以通过将每个模块的父目录添加到 `PYTHONPATH` 来跟踪其他模块。

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/module
streamlit run your_script.py
```
