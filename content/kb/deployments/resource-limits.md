---
title: 呃。此应用已超过其资源限制
slug: /knowledge-base/deploy/resource-limits
---

# 呃。此应用已超过其资源限制

遗憾！这意味着你已达到[Streamlit Community Cloud](https://streamlit.io/cloud)账户的[资源限制](/deploy/streamlit-community-cloud/manage-your-app#app-resources-and-limits)。

你可以在应用中进行一些更改以使其占用更少资源：

- 重启应用(临时修复)
- 使用`st.cache_data`或`st.cache_resource`仅加载模型或数据一次
- 使用`ttl`或`max_entries`限制缓存大小
- 将大型数据集移到数据库
- 分析应用的内存使用情况

查看我们关于["常见应用问题：资源限制"](https://blog.streamlit.io/common-app-problems-resource-limits/)的[博客文章](https://blog.streamlit.io/common-app-problems-resource-limits/)，了解更多深入的提示以防止你的应用达到Streamlit Community Cloud的[资源限制](/deploy/streamlit-community-cloud/manage-your-app#app-resources-and-limits)。

相关论坛帖子：

- [https://discuss.streamlit.io/t/common-app-problems-resource-limits/16969](https://discuss.streamlit.io/t/common-app-problems-resource-limits/16969)
- [https://blog.streamlit.io/common-app-problems-resource-limits/](https://blog.streamlit.io/common-app-problems-resource-limits/)

我们仅在逐案例基础上向非营利组织或教育组织提供免费资源增加。如果你是非营利组织或教育组织，请填写[此表单](https://info.snowflake.com/streamlit-resource-increase-request.html)，我们将尽快审查你的提交。

增加完成后，你将收到来自Streamlit市场营销团队的电子邮件，确认增加已应用。
