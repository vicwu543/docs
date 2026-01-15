#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量翻译KB目录下所有英文MD文件"""

import os

# Dependencies and Deployments translations
files_content = {
    "content/kb/dependencies/_index.md": """---
title: 安装依赖
slug: /knowledge-base/dependencies
description: 探索常见的依赖和环境问题，并查看可能的解决方案。
---

# 安装依赖

- [ModuleNotFoundError: No module named](/knowledge-base/dependencies/module-not-found-error)
- [ImportError: libGL.so.1: cannot open shared object file: No such file or directory](/knowledge-base/dependencies/libgl)
- [ERROR: No matching distribution found for](/knowledge-base/dependencies/no-matching-distribution)
- [如何安装不在PyPI/Conda上但可在GitHub上获得的包](/knowledge-base/dependencies/install-package-not-pypi-conda-available-github)
""",
    "content/kb/deployments/_index.md": """---
title: 部署相关问题和错误
slug: /knowledge-base/deploy
description: 探索常见的部署问题和解决方案。
---

# 部署相关问题和错误

- [如何在域上部署Streamlit应用以使其显示为在常规端口(即端口80)上运行？](/knowledge-base/deploy/deploy-streamlit-domain-port-80)
- [如何在不同子域上部署多个Streamlit应用？](/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains)
- [在部署的Streamlit应用中调用Python子进程](/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app)
- [Streamlit支持WSGI协议吗？(又名我可以用gunicorn部署Streamlit吗？)](/knowledge-base/deploy/does-streamlit-support-wsgi-protocol)
- [呃。此应用已超过其资源限制。](/knowledge-base/deploy/resource-limits)
- [远程运行时应用未加载](/knowledge-base/deploy/remote-start)
- [无SSO身份验证](/knowledge-base/deploy/authentication-without-sso)
- [如何增加Streamlit Community Cloud上st.file_uploader的上传限制？](/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud)
- [登录时出现"呃。这不应该发生"消息](/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in)
- [登录Streamlit Community Cloud失败，错误403](/knowledge-base/deploy/login-attempt-to-streamlit-community-cloud-fails-with-error-403)
- [如何为Streamlit Community Cloud提交支持案例](/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud)
""",
}

# Write files with their complete translated content
for filepath, content in files_content.items():
    full_path = os.path.join("d:\\github_st\\docs", filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

print("\nIndex files updated!")
