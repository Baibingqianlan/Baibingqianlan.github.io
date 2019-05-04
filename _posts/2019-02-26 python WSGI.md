---
layout: post
---

### 0. python Web服务器模块

这里的“Web服务器模块”有如下三种：

+ BaseHTTPServer: 提供基本的Web服务和处理器类，分别是HTTPServer和BaseHTTPRequestHandler。
+ SimpleHTTPServer: 包含执行GET和HEAD请求的SimpleHTTPRequestHandler类。
+ CGIHTTPServer: 包含处理POST请求和执行CGIHTTPRequestHandler类。

#### web服务器、应用服务器、web应用框架的关系
下面的博客文章解释的比较清楚：
[https://blog.csdn.net/feit2417/article/details/81387377](https://blog.csdn.net/feit2417/article/details/81387377)

+ web服务器：负责处理http请求，响应静态文件，常见的有Apache，Nginx以及微软的IIS.
+ 应用服务器：负责处理逻辑的服务器。比如php、python的代码，是不能直接通过nginx这种web服务器来处理的，只能通过应用服务器来处理，常见的应用服务器有uwsgi、tomcat等。
+ web应用框架：一般使用某种语言，封装了常用的web功能的框架就是web应用框架，flask、Django以及Java中的SSH(Structs2+Spring3+Hibernate3)框架都是web应用框架
![](https://img-blog.csdn.net/20180803144914215?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2ZlaXQyNDE3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 1. WSGI

Python Web服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI）是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。自从WSGI被开发出来以后，许多其它语言中也出现了类似接口。

+ 2003年： 原初的Python版本
+ 2007年： Rack，Ruby版本
+ 2008年： Lua WSAPI，Lua版本
+ 2009年： JSGI，Java版本
+ 2009年： PSGI，Perl版本

WSGI区分为两个部份：一为“服务器”或“网关”，另一为“应用程序”或“应用框架”。在处理一个WSGI请求时，服务器会为应用程序提供环境上下文及一个回调函数（Callback Function）。当应用程序完成处理请求后，透过先前的回调函数，将结果回传给服务器。所谓的 WSGI 中间件同时实现了API的两方，因此可以在WSGI服务和WSGI应用之间起调解作用：从WSGI服务器的角度来说，中间件扮演应用程序，而从应用程序的角度来说，中间件扮演服务器。“中间件”组件可以执行以下功能：

1. 重写环境变量后，根据目标URL，将请求消息路由到不同的应用对象。
2. 允许在一个进程中同时运行多个应用程序或应用框架。
3. 负载均衡和远程处理，通过在网络上转发请求和响应消息。
4. 进行内容后处理，例如应用XSLT样式表。

WSGI没有官方的实现, 因为WSGI更像一个协议。只要遵照这些协议,WSGI应用(Application)都可以在任何服务器(Server)上运行, 反之亦然。WSGI就是Python的CGI包装，相对于Fastcgi是PHP的CGI包装。

WSGI将 web 组件分为三类： web服务器，web中间件,web应用程序， wsgi基本处理模式为 ： 

browser -> WSGI Server -> (WSGI Middleware)* -> WSGI Application 

![](https://www.biaodianfu.com/wp-content/uploads/2014/08/wsgi.png)
![](https://img-blog.csdn.net/20180626101119515?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTg2OTUyNg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 2. uwsgi：

要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。

+ WSGI是一种通信协议。
+ uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
+ 而uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。

>
uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型（type of information），每一个uwsgi packet前4byte为传输信息类型描述，它与WSGI相比是两样东西。据称其效率是fcgi的10倍。具体的协议内容请参考：the uwsgi protocol


uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。uWSGI项目旨在为部署分布式集群的网络应用开发一套完整的解决方案。uWSGI主要面向web及其标准服务，已经成功的应用于多种不同的语言。由于uWSGI的可扩展架构，它能够被无限制的扩展用来支持更多的平台和语言。

目前，你可以使用C，C++和Objective-C来编写插件。项目名称中的“WSGI”是为了向同名的Python Web标准表示感谢，因为WSGI为该项目开发了第一个插件。uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。

　　uWSGI的主要特点如下：

+ 超快的性能。
+ 低内存占用（实测为apache2的mod_wsgi的一半左右）。
+ 多app管理。
+ 详尽的日志功能（可以用来分析app性能和瓶颈）。
+ 高度可定制（内存大小限制，服务一定次数后重启等）。

### 3. Gunicorn：

　　和uWSGi类似的工具，从rails的部署工具(Unicorn)移植过来的。但是它使用的协议是前文所讲的WSGI，这是python2.5时定义的官方标准(PEP 333 )，根红苗正，而且部署比较简单，详细的使用教程请点击这里。Gunicorn采用prefork模式，Gunicorn 服务器与各种 Web 框架兼容，只需非常简单的执行，轻量级的资源消耗，以及相当迅速。它的特点是与 Django 结合紧密，部署特别方便。 缺点也很多，不支持 HTTP 1.1，并发访问性能不高，与 uWSGI，Gevent 等有一定的性能差距。

### 4. Tornado：

　　Tornado即使一款python 的开发框架，也是一个异步非阻塞的http服务器，它本身的数据产出实现没有遵从上文所说的一些通用协议，因为自身就是web服务器，所以动态请求就直接通过内部的机制，输出成用户所请求的动态内容。如果把它作为一个单独服务器，想用它来配合其他的框架如Flask来部署，则需要采用WSGI协议，Tornado内置了该协议，tornado.wsgi.WSGIContainer。

### 5. wsgiref：

　　Python自带的实现了WSGI协议的的wsgi server。wsgi server可以理解为一个符合wsgi规范的web server，接收request请求，封装一系列环境变量，按照wsgi规范调用注册的wsgi app，最后将response返回给客户端。Django的自带服务器就是它了。

### 6. 借鉴
+ Django项目用Nginx+uWSGI方式部署，Tornado项目用Nginx+Gunicorn方式部署
+ Nginx都作为负载均衡以及静态内容转发。Tornado项目用supervisord来管理Gunicorn，用Gunicorn管理Tornado。众所周知，由于Python的GIL存在，所以Python的并发都采用多进程模式，所以我们部署的方式是一个核心两个进程。

### 7. web前端
+ Bootstrap– 最流行的Web前端UI框架

Bootstrap是由twitter公司推出的Web前端UI框架，由Twitter的设计师Mark Otto和Jacob Thornton合作开发的，是一个CSS/HTML框架，常用语php等后端开发中。这个框架使用了最新的浏览器技术，Bootstrap提供了时尚的排版样式，表单，buttons，表格，网格系统等等。（关于Bootstrap的具体运用，大家可以看看《Bootstrap视频教程》）

+ jQuery UI - 基于jQuery的开源Javascript框架
+ jQuery UI Bootstrap，样式是Bootstrap的，外观比较漂亮，同时拥有jQuery UI的控件功能，开发者快速地创建网页控件。
+ BootMetro- Metro风格的CSS框架，BootMetro是一款基于Bootstrap的前端UI框架，其特点是可以很方便地构建类似Windonws 8扁平化风格的网页界面，效果非常不错。
+ Flat UI- 扁平风格 UI 工具包，Flat UI是一套精美的扁平风格 UI 工具包，基于 Twitter Bootstrap 实现。这套界面工具包含许多基本的和复杂的 UI 部件，例如按钮，输入框，组合按钮，复选框，单选按钮，标签，菜单，进度条和滑块，导航元素等等。
+ 网易CSS框架 NEC，NEC是网易推出的开源前端CSS框架，提供了丰富UI代码库和插件，可以极大的帮助开发人员提高开发效率。即使你并非前端专业开发人员，利用NEC你也可以快速地构建属于自己的网页应用。
+ Alloy UI – 功能强大的CSS UI框架，Alloy UI是基于YUI 3的前端UI框架，包含一套丰富的UI 部件，如图片库，对话框，树形结构，面板，自动完成，按钮，日历控件，工具条等。
+ Cardinal – 移动端的CSS UI框架，小型的移动优先的 CSS 框架，提供很多有用的默认样式、可缩放排版、可重用模块和一个简单的响应式表格系统。
+ CSScaffold框架，
CSScaffold不同于许多CSS框架，它必须依靠PHP与Apache的mod_rewrite来执行，也正是由于其执行环境的特殊性，让CSScaffold变得很神奇、很方便，写起CSS来又快又轻松！



参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [定义]({{site.baseurl}}/assets/2018-10-16/3.bmp)
3. [Python Web部署方式总结](https://www.cnblogs.com/titanjf/p/python-web-deploy.html)
4. [部署python web 的几种方式](https://www.cnblogs.com/xiaopai501/p/3303086.html)
5. [https://www.airpair.com/python/posts/django-flask-pyramid](https://www.airpair.com/python/posts/django-flask-pyramid)
6. [如何把本地的Django项目部署到服务器（亲测）](https://blog.csdn.net/qq_30501975/article/details/80423547)
7. [Django Nginx+uwsgi 安装配置](http://www.runoob.com/django/django-nginx-uwsgi.html)
8. [https://uwsgi-docs-cn.readthedocs.io/zh_CN/latest/WSGIquickstart.html](https://uwsgi-docs-cn.readthedocs.io/zh_CN/latest/WSGIquickstart.html)
9. [Windows 下 python 安装 uwsgi](https://xiexianbin.cn/python/2018/04/11/python-uwsgi-for-windows)
10. [web前端开发常用的10个高端CSS UI开源框架](https://www.cnblogs.com/good10001/p/4708580.html)
11. [如何将本地的Django项目部署到云服务器](https://blog.csdn.net/qq_30501975/article/details/80423547)