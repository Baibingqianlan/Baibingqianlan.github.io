---
layout: post
---

windows下的WEB服务器安装环境。

+ 环境：WIN7
+ 开发语言： Python
+ 后台框架：Django/Flask
+ 前端框架：bootstrap
+ web服务器：apache
+ wsgi服务器：mod_wsgi

### 1. apache下载
下载源码地址：[http://httpd.apache.org/download.cgi](http://httpd.apache.org/download.cgi)

apache本身不提供已编译的安装包，只提供源码，如果你自己无法编译，可以选择下面这些官方推荐的第三方提供编译的网站：[https://mirrors.tuna.tsinghua.edu.cn/apache//httpd/binaries/win32/README.html](https://mirrors.tuna.tsinghua.edu.cn/apache//httpd/binaries/win32/README.html)

我们从[ApacheHaus](https://www.apachehaus.com/cgi-bin/download.plx)上下载编译好的安装包：Apache 2.4.38

安装：

1. 解压到安装目录，进入\bin目录下
2. 安装目录有使用说明：地址栏输入CMD
3. 管理员身份执行：httpd -k install
4. 执行：httpd -k start或者httpd
5. 在浏览器输入本地地址加端口号，显示默认网页：it works!

命令：

	Stop Apache	 	httpd -k stop
	Restart Apache	httpd -k restart
	Uninstall Apache Service	httpd -k uninstall
	Test Config Syntax			httpd -t
	Version Details				httpd -V
	Command Line Options List	httpd -h

问题：

+ 安装前设置服务的根目录：Define SRVROOT "E:***/Apache24"，用来放置服务日志等,设置到服务程序的目录，否则会出现配置上的问题，如找不到动态库了等。
+ 将Apache24\htdocs文件夹下面的 index.html 文件删除，我们刚才看到的 It works! 页面就是这个文件的作用，然后将我们的文件及文件夹放到 Apache24\htdocs 下面，浏览器就可以下载了。

### 2. mod_wsgi

找到Mod_wsgi，下载对应位数和python的版本:
[http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil)

我下载：mod_wsgi‑4.6.5+ap24vc14‑cp36‑cp36m‑win32.whl

下载好之后安装到python目录下，在安装成功后在python的安装目录的\scripts文件夹下运行

	mod_wsgi-express module-config
输出如下三行结果：

	D:\anaconda3\Scripts>mod_wsgi-express module-config
	LoadFile "d:/anaconda3/python36.dll"
	LoadModule wsgi_module "d:/anaconda3/lib/site-packages/mod_wsgi/server/mod_wsgi.cp36-win32.pyd"
	WSGIPythonHome "d:/anaconda3"

也可以输入mod_wsgi-express module-config > myconfig.txt ，将信息重定向到了Scripts文件夹下的myconfig.txt，打开这个txt文件，将里面的信息复制到httpd.conf文件夹中。
把这三行内容复制到http.cnf文件下的其他LoadModule命令后面。

### 3.测试网页

修改配置文件httpd.conf ，配置好应用的位置：
	
	# my app
	Define appDir "D:/MyDocuments/python_works/mysite"
	WSGIPythonPath  ${appDir}
	WSGIScriptAlias /mysite ${appDir}/mysite/wsgi.py
	
	ServerAdmin 444129199@qq.com   
	DocumentRoot ${appDir} 
	<VirtualHost *:8088>
	<Directory "${appDir}/mysite">
	#	<Files wsgi.py>   
		  Require all granted
		  Require host ip
	#	</Files> 
	</Directory>  
	</VirtualHost>  

我电脑上原来有一个测试django的应用，所以配置了一下。

+ 其中WSGIScriptAlias /mysite ${appDir}/mysite/wsgi.py，设置了一个下级的别名，不加的话，WSGIScriptAlias / ${appDir}/mysite/wsgi.py，输入网址会直接进入网站。
+ Directory 目录，要指向wsgi.py的目录
+ VirtualHost，是一个虚拟主机的配置，加不加不影响测试






参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [定义]({{site.baseurl}}/assets/2018-10-16/3.bmp)
3. [Python Web部署方式总结](https://www.cnblogs.com/titanjf/p/python-web-deploy.html)
4. [部署python web 的几种方式](https://www.cnblogs.com/xiaopai501/p/3303086.html)
5. [https://www.airpair.com/python/posts/django-flask-pyramid](https://www.airpair.com/python/posts/django-flask-pyramid)
6. [如何把本地的Django项目部署到服务器（亲测）](https://blog.csdn.net/qq_30501975/article/details/80423547)
7. [Django Nginx+uwsgi 安装配置](http://www.runoob.com/django/django-nginx-uwsgi.html)
10. [web前端开发常用的10个高端CSS UI开源框架](https://www.cnblogs.com/good10001/p/4708580.html)
11. [如何将本地的Django项目部署到云服务器](https://blog.csdn.net/qq_30501975/article/details/80423547)
12. [Windows7 64位 上搭建Python+Django+Apache+wsgi](https://www.jianshu.com/p/528aa5327174)
13. [在Windows下用Apache+wsgi部署python+flask项目](https://blog.csdn.net/sunroyi666/article/details/82454523)
14. [Windows+Apache+mod_wsgi+Flask完全配置攻略](https://www.jianshu.com/p/0aa1c7097976)