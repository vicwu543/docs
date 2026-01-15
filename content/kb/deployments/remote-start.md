---
title: 远程运行时应用未加载
slug: /knowledge-base/deploy/remote-start
---

# 远程运行时应用未加载

以下是用户自行设置解决方案来远程托管Streamlit应用时发生的一些常见错误。

要了解一个欺骗性简单的方式来托管Streamlit应用，避免下面的所有问题，请查看[Streamlit Community Cloud](https://streamlit.io/cloud)。

### 症状#1：应用从不加载

当你在浏览器中输入应用URL时，只看到**空白页面、"Page not found"错误、"Connection refused"错误**或类似的东西，首先检查Streamlit是否确实在远程服务器上运行。在Linux服务器上，你可以通过SSH连接到它，然后运行：

```bash
ps -Al | grep streamlit
```

如果你看到Streamlit正在运行，最可能的原因是Streamlit端口未暴露。修复取决于你的确切设置。以下是三个示例修复：

- **尝试端口80：**某些主机默认暴露端口80。要将Streamlit设置为使用该端口，请使用`--server.port`选项启动Streamlit：

  ```bash
  streamlit run my_app.py --server.port=80
  ```

- **AWS EC2服务器**：首先，在[AWS控制台](https://us-west-2.console.aws.amazon.com/ec2/v2/home)中单击你的实例。然后向下滚动并单击_Security Groups_ → _Inbound_ → _Edit_。接下来，添加允许_Port Range_`8501`且_Source_为`0.0.0.0/0`的_Custom TCP_规则。

- **其他类型的服务器**：检查防火墙设置。

如果这仍然无法解决问题，请尝试运行一个简单的HTTP服务器而不是Streamlit，并查看_是否_能正常工作。如果确实有效，那么你就知道问题出在你的Streamlit应用或配置的某个地方(在这种情况下，你应该在我们的[论坛](https://discuss.streamlit.io)中寻求帮助！)如果没有，那么它肯定与Streamlit无关。

如何启动简单的HTTP服务器：

```bash
python -m http.server [port]
```

### 症状#2：应用显示"Please wait..."或永远显示骨架元素

从1.29.0版本开始，此症状显示不同。对于Streamlit的早期版本，加载应用在页面中央显示带有"Please wait..."消息的蓝色框。从1.29.0版本开始，加载应用显示骨架元素。如果此加载屏幕不消失，潜在原因可能是以下之一：

- 使用为内部开发保留的端口3000。
- 配置错误的[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)保护。
- 服务器从Websocket连接中剥离标头，从而破坏压缩。

要诊断此问题，首先确保你没有使用端口3000。如有疑问，请尝试如上所述的端口80。

接下来，尝试通过使用`--server.enableCORS`标志设置为`false`运行Streamlit来暂时禁用CORS保护：

```bash
streamlit run my_app.py --server.enableCORS=false
```

如果这解决了你的问题，**你应该重新启用CORS保护**，然后将`browser.serverAddress`设置为你的Streamlit应用的URL。

如果问题仍然存在，尝试通过使用`--server.enableWebsocketCompression`标志设置为`false`运行Streamlit来禁用websocket压缩

```bash
streamlit run my_app.py --server.enableWebsocketCompression=false
```

如果这解决了你的问题，你的服务器设置可能会剥离用于协商Websocket压缩的`Sec-WebSocket-Extensions` HTTP标头。

压缩对于Streamlit工作不是必需的，但强烈建议，因为它改进性能。如果你想重新打开它，你需要找出基础设施的哪一部分在剥离`Sec-WebSocket-Extensions` HTTP标头，并更改该行为。

### 症状#3：在多个副本中运行时无法上传文件

If the file uploader widget returns an error with status code 403, this is probably
due to a misconfiguration in your app's
[XSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) protection logic.

To diagnose the issue, try temporarily disabling XSRF protection by running Streamlit
with the `--server.enableXsrfProtection` flag set to `false`:

```bash
streamlit run my_app.py --server.enableXsrfProtection=false
```

If this fixes your issue, **you should re-enable XSRF protection** and try one
or both of the following:

- Set `browser.serverAddress` and `browser.serverPort` to the URL and port of
  your Streamlit app.
- Configure your app to use the same secret across every replica by setting the
  `server.cookieSecret` config option to the same hard-to-guess string everywhere.
