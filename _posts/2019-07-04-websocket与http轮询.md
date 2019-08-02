---
layout: post
---

![](https://www.runoob.com/wp-content/uploads/2016/03/ws.png)

### 1.websocket

WebSocket 是 HTML5 开始提供的一种在单个 TCP 连接上进行全双工通讯的协议。
WebSocket 使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。在 WebSocket API 中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。

django实现websocket大致上有两种方式，一种channels，一种是dwebsocket。channels依赖于redis，twisted等，相比之下使用dwebsocket要更为方便一些。

WebSocket 协议本质上是一个基于 TCP 的协议。

Socket 是传输控制层协议，WebSocket 是应用层协议。

### 2.http Ajax 轮询

现在，很多网站为了实现推送技术，所用的技术都是 Ajax 轮询。轮询是在特定的的时间间隔（如每1秒），由浏览器对服务器发出HTTP请求，然后由服务器返回最新的数据给客户端的浏览器。这种传统的模式带来很明显的缺点，即浏览器需要不断的向服务器发出请求，然而HTTP请求可能包含较长的头部，其中真正有效的数据可能只是很小的一部分，显然这样会浪费很多的带宽等资源。

**HTTP/2**

HTTP/2 于 2015 年标准化，主要目的是优化性能。其特性如下：

+ 二进制协议：HTTP/2 的消息头使用二进制格式，而非文本格式。并且使用专门设计的 HPack 算法压缩。

+ 多路复用（Multiplexing）：就是说 HTTP/1 可以重复使用同一个 TCP 连接，并且连接是多路的，多个请求或响应可以同时传输。

+ 服务器推送：服务端能够直接把资源推送给客户端，当客户端需要这些文件的时候，它已经在客户端了。（该推送对 Web App 是隐藏的，由浏览器处理）

HTTP/2 允许取消某个正在传输的数据流（通过发送 RST_STREAM 帧），而不关闭 TCP 连接。这正是二进制协议的好处之一，可以定义多种功能的数据帧。

### 3.websocket API

	var Socket = new WebSocket(url, [protocol] );

以上代码中的第一个参数 url, 指定连接的 URL。第二个参数 protocol 是可选的，指定了可接受的子协议。

**Websocket 使用 ws 或 wss 的统一资源标志符**

Websocket 使用 ws 或 wss 的统一资源标志符，类似于 HTTPS，其中 wss 表示在 TLS 之上的 Websocket。如：

	ws://example.com/wsapi
	wss://secure.example.com/
Websocket 使用和 HTTP 相同的 TCP 端口，可以绕过大多数防火墙的限制。默认情况下，Websocket 协议使用 80 端口；运行在 TLS 之上时，默认使用 443 端口。
一个典型的Websocket握手请求如下：

	客户端请求
	GET / HTTP/1.1
	Upgrade: websocket
	Connection: Upgrade
	Host: example.com
	Origin: http://example.com
	Sec-WebSocket-Key: sN9cRrP/n9NdMgdcy2VJFQ==
	Sec-WebSocket-Version: 13
	服务器回应
	HTTP/1.1 101 Switching Protocols
	Upgrade: websocket
	Connection: Upgrade
	Sec-WebSocket-Accept: fFBooB7FAkLlXgRSz0BT3v4hq5s=
	Sec-WebSocket-Location: ws://example.com/


**WebSocket 属性**

以下是 WebSocket 对象的属性。假定我们使用了以上代码创建了 Socket 对象：

	属性			描述
	Socket.readyState	
		只读属性 readyState 表示连接状态，可以是以下值：
		0 - 表示连接尚未建立。
		1 - 表示连接已建立，可以进行通信。
		2 - 表示连接正在进行关闭。
		3 - 表示连接已经关闭或者连接不能打开。
	Socket.bufferedAmount	
		只读属性 bufferedAmount 已被 send() 放入正在队列中等待传输，
		但是还没有发出的 UTF-8 文本字节数。

**WebSocket 事件**

以下是 WebSocket 对象的相关事件。假定我们使用了以上代码创建了 Socket 对象：

	事件	事件处理程序	描述
	open	Socket.onopen	连接建立时触发
	message	Socket.onmessage	客户端接收服务端数据时触发
	error	Socket.onerror	通信发生错误时触发
	close	Socket.onclose	连接关闭时触发

**WebSocket 方法**

以下是 WebSocket 对象的相关方法。假定我们使用了以上代码创建了 Socket 对象：

	方法				描述
	Socket.send()	使用连接发送数据	
	Socket.close()	关闭连接
	
### 4.比较
**WebSocket 与 HTTP/2 比较**

加密与否：

	WebSocket 支持明文通信 ws:// 和加密 wss://，
	而 HTTP/2 协议虽然没有规定必须加密，但是主流浏览器都只支持 HTTP/2 over TLS.

消息推送：

WebSocket是全双工通道，可以双向通信。而且消息是直接推送给 Web App.
HTTP/2 虽然也支持 Server Push，但是服务器只能主动将资源推送到客户端缓存！并不允许将数据推送到客户端里跑的 Web App 本身。服务器推送只能由浏览器处理，不会在应用程序代码中弹出服务器数据，这意味着应用程序没有 API 来获取这些事件的通知。

为了接近实时地将数据推送给 Web App， HTTP/2 可以结合 SSE（Server-Sent Event）使用。这是一种新提出的 API，用于从服务端单向将数据推送给 Web App.

WebSocket 在需要接近实时双向通信的领域，很有用武之地。而 HTTP/2 + SSE 适合用于展示实时数据。另外在客户端非浏览器的情况下，使用不加密的 HTTP/2 也是可能的。


### 5.Django通过dwebsocket实现websocket

方法1:

只需views.py文件中,将对应的视图函数添加装饰器

accept_websocket-—可以接受websocket请求和普通http请求
require_websocket----只接受websocket请求,拒绝普通http请求


方法2:
settings.py中加入以下内容

	import dwebsocket
	# 为所有的URL提供websocket，如果只是单独的视图需要可以不选
	MIDDLEWARE_CLASSES=['dwebsocket.middleware.WebSocketMiddleware']
	
	WEBSOCKET_ACCEPT_ALL=True  # 可以允许每一个单独的视图实用websockets

注意不是在MIDDLEWARE后面追加!

原因是二者之间的区别: MIDDLEWARE_CLASSES是旧的格式,新格式用 MIDDLEWARE, 

	If used with MIDDLEWARE_CLASSES, the __call__() method
	 will never be used; Django calls process_request() and 
	process_response() directly.

	
	使用MIDDLEWARE_CLASSES, 每个中间件必须有process_response方法调
	用, 即使最简单的回环方法. 使用 MIDDLEWARE, 中间件的行为更像洋葱：响
	应在退出时经过的层与在进入时看到请求的层相同。如果一个中间件发生短路，
	只有那个中间件和它之前在中间件中的中间件才能看到响应。
	
	使用MIDDLEWARE_CLASSES，进程异常应用于从中间件进程请求方法引发的异
	常。在MIDDLEWARE下，进程异常仅适用于从视图（或从TemplateResponse
	的呈现方法）引发的异常。从中间件引发的异常被转换为适当的HTTP响应，然后传递到下一个中间件。

	在MIDDLEWARE_CLASSES下，如果进程响应方法引发异常，则跳过所有早期中间件的进程响应
	方法，并始终返回500个内部服务器错误HTTP响应（即使引发的异常是
	HTTP404）。在MIDDLEWARE下，从中间件引发的异常将立即转换为适当的HTTP响
	应，然后行中的下一个中间件将看到该响应。中间件从不被跳过，因为中间件引
	发了异常。

参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [https://www.runoob.com/html/html5-websocket.html](https://www.runoob.com/html/html5-websocket.html)
3. [WebSocket 与 HTTP/2](https://www.cnblogs.com/kirito-c/p/10360309.html)
4. [Django实现websocket完成实时通讯、聊天室、在线客服等](https://www.cnblogs.com/sui776265233/p/10176275.html)
5. [Django通过dwebsocket实现websocket](https://blog.csdn.net/weixin_39726347/article/details/88045752)
6. [https://docs.djangoproject.com/en/2.2/topics/http/middleware/](https://docs.djangoproject.com/en/2.2/topics/http/middleware/)


