---
title: Streamlit 原生应用测试框架
slug: /develop/concepts/app-testing
description: 探索有关 Streamlit 原生应用测试框架的综合指南，包括设置、示例和 CI/CD 集成的最佳实践。
keywords: 应用测试, streamlit 测试, AppTest, 自动化测试, 测试框架, pytest, 单元测试, 集成测试, ci 测试, 测试自动化, 测试最佳实践
---

# Streamlit 原生应用测试框架

Streamlit 应用测试使开发者能够构建和运行自动化测试。带上你喜欢的测试自动化软件，享受简单的语法来模拟用户输入并检查渲染输出。

提供的类 AppTest 模拟运行的应用，并提供方法来通过 API（而不是浏览器 UI）设置、操纵和检查应用内容。AppTest 提供与浏览器自动化工具（如 Selenium 或 Playwright）类似的功能，但编写和执行测试的开销更少。将我们的测试框架与 [pytest](https://docs.pytest.org/) 之类的工具一起使用来执行或自动化你的测试。典型的模式是为应用构建一套测试，以确保应用随着发展的一致功能。测试在本地和/或 CI 环境（如 GitHub Actions）中运行。

<InlineCalloutContainer>
    <InlineCallout
        color="indigo-70"
        icon="science"
        bold="入门"
        href="/develop/concepts/app-testing/get-started"
    >向你介绍应用测试框架以及如何使用 <code>pytest</code> 执行测试。了解如何初始化和运行模拟的应用，包括如何检索、操纵和检查应用元素。</InlineCallout>
    <InlineCallout
        color="indigo-70"
        icon="password"
        bold="超越基础知识"
        href="/develop/concepts/app-testing/beyond-the-basics"
    >解释如何在应用测试中使用 secrets 和 Session State，包括如何测试多页应用。</InlineCallout>
    <InlineCallout
        color="indigo-70"
        icon="play_circle"
        bold="自动化你的测试"
        href="/develop/concepts/app-testing/automate-tests"
    >使用持续集成 (CI) 随时间验证应用更改。</InlineCallout>
    <InlineCallout
        color="indigo-70"
        icon="quiz"
        bold="示例"
        href="/develop/concepts/app-testing/examples"
    >将上面解释的概念放在一起。查看已实施多个测试的应用。</InlineCallout>
    <InlineCallout
        color="indigo-70"
        icon="saved_search"
        bold="速查表"
        href="/develop/concepts/app-testing/cheat-sheet"
    >是总结可用语法的紧凑参考。</InlineCallout>
</InlineCalloutContainer>
