---
title: Streamlit信任和安全
slug: /deploy/streamlit-community-cloud/get-started/trust-and-security
description: 了解Streamlit Community Cloud的安全模型，包括认证、数据保护、加密和合规措施。
keywords: 安全, 信任, 认证, 数据保护, 加密, 合规, vpc, https, tls, 漏洞管理, 渗透测试
---

# Streamlit信任和安全

Streamlit是一个将Python脚本转化为交互式应用的框架，给数据科学家快速为整个公司创建基于数据和模型的应用的能力。

一个简单的Streamlit应用是：

```python
import streamlit as st
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
```

当你执行`streamlit run my_app.py`时，你启动一个在本地计算机上以`http://localhost:8501`运行交互式应用的web服务器。这对本地开发很好。当你想与同事分享时，Streamlit Community Cloud让你在云中部署和运行这些应用。Streamlit Community Cloud处理容器化的细节，并为你提供一个用于轻松管理部署应用的界面。

本文档提供了我们实施的安全保障措施的概述，以保护你和你的数据。但是，安全是共同责任，你最终负责适当使用Streamlit和Streamlit Community Cloud，包括实施适当的用户可配置的安全保障措施和最佳做法。

## 产品安全

### 认证

你必须通过GitHub进行认证以部署或管理应用。当你在关联的GitHub仓库上没有推送或管理员权限时，通过Google或单次使用电子邮件链接的认证是查看私有应用所必需的。单次使用电子邮件链接在请求后有效期为15分钟。

### 权限

Streamlit Community Cloud继承你在GitHub中分配的权限。对给定应用的GitHub仓库有写入权限的用户将能够在Streamlit管理控制台中进行更改。但是，只有拥有仓库**管理员访问权限**的用户能够**部署和删除应用**。

## 网络和应用安全

### 数据托管

我们的物理基础设施托管和管理在由基础设施即服务云提供商维护的安全数据中心内。Streamlit利用这些平台的许多内置安全、隐私和冗余功能。我们的云提供商持续监控其数据中心以寻求风险，并进行评估以确保符合行业标准。

### 数据删除

Community Cloud用户可以选择删除他们部署的任何应用以及整个账户。

当用户从管理控制台删除应用时，我们删除其源代码，包括从其GitHub仓库复制的任何文件或从运行应用在我们系统中创建的文件。但是，我们在数据库中保留表示应用的记录。此记录包含应用的坐标：GitHub组织或用户、GitHub仓库、分支和主模块文件的路径。

当用户删除其账户时，我们对其数据进行硬删除，并对与其账户相关联的GitHub身份所属的所有应用进行硬删除。在这种情况下，我们不保留上述应用坐标的记录。删除账户时，我们也删除与Community Cloud账户相关联的任何HubSpot联系人。

### 虚拟专用云

我们的所有服务器都在虚拟专用云（VPC）内，带有防火墙和网络访问控制列表（ACL），允许外部访问选定的少数API端点；所有其他内部服务仅在VPC内可访问。

### 加密

Streamlit应用完全通过HTTPS提供。我们只使用强密码套件和HTTP严格传输安全（HSTS）来确保浏览器与Streamlit应用通过HTTPS交互。

所有通过公网发送到或来自Streamlit的数据都使用256位加密进行传输加密。我们的API和应用端点使用传输层安全（TLS）1.2（或更好）。我们也使用AES-256对磁盘上的静止数据进行加密。

### 权限和认证

对Community Cloud用户账户数据的访问仅限于授权人员。我们运行零信任企业网络，利用单点登录和多因素认证（MFA），并强制执行强密码策略以确保对云相关服务的访问受到保护。

### 事件响应

我们处理安全事件的内部协议包括检测、分析、响应、升级和缓解。安全公告可在[https://streamlit.io/advisories](https://streamlit.io/advisories)获得。

### 渗透测试

Streamlit使用第三方安全工具定期扫描漏洞。我们的安全团队对Streamlit平台进行定期、密集的渗透测试。我们的产品开发团队对任何已识别的问题或潜在漏洞进行响应，以确保Streamlit应用的质量、安全和可用性。

### 漏洞管理

我们使我们的系统保持最新的最新安全补丁，并持续监控新漏洞。这包括对我们代码仓库的自动扫描，以寻找易受攻击的依赖。

如果你在我们的一个产品或网站中发现漏洞，请向[HackerOne](https://hackerone.com/snowflake?type=team)报告问题。
