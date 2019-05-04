---
layout: post
---

### 1. 修改背景 ##

通过CSS可以设置背景及其它属性。

DIR:

appname/static/polls/style.css
appname/static/polls/images/background.gif

### 2. 站点地图

网站地图，又叫站点地图，它就是一个列出了你网站上所有页面地址的清单文件，一般来说分为2种，一种是给搜索引擎看的，一种是给用户看的，前者帮助搜索引擎更好地收录你的网站，后者帮助用户更好的了解你的网站整体结构、更快的找到他们想要找的内容。

一般有3种格式，txt、xml、html，绝大部分情况下都是用xml格式，百度、谷歌都是支持xml格式。下面简单介绍3种格式。

#### 2.1. txt格式
这种格式最简单，一般较少采用，示例如下：

	http://liuxianan.com/
	http://liuxianan.com/link.html
	http://liuxianan.com/msgboard.html
注意事项：

文本文件每行都必须有一个网址。网址中不能有换行。
不应包含网址列表以外的任何信息。
您必须书写完整的网址，包括 http。
每个文本文件最多可包含 50,000 个网址，并且应小于10MB（10,485,760字节）。如果网站所包含的网址超过 50,000 个，则可将列表分割成多个文本文件，然后分别添加每个文件。
文本文件需使用 UTF-8 编码或GBK编码。
#### 2.2. xml格式
示例sitemap.xml如下：

	<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
	    <url>
	        <loc>http://liuxianan.com/</loc>
	        <lastmod>2016-09-06T00:00:16+08:00</lastmod>
	        <changefreq>daily</changefreq>
	        <priority>1.0</priority>
	    </url>
	    <url>
	        <loc>http://liuxianan.com/link.html</loc>
	        <lastmod>2016-09-06T00:00:16+08:00</lastmod>
	        <changefreq>daily</changefreq>
	        <priority>0.8</priority>
	    </url>
	</urlset>
其中：

+ loc表示完整网址，必填项，长度不得超过256字节
+ lastmod表示本网页最后修改时间，必须是ISO-8601时间格式，具体这个格式是什么样的没整清楚，根据我的理解，反正就当成是：yyyy-MM-ddTHH:mm:ss+08:00，最后面的+08:00应该表示的是东八区；
+ changefreq 表示更新频率，可选值：always、hourly、daily、weekly、monthly、yearly、never
+ priority 用来指定此链接相对于其他链接的优先权比值，可选值 0.0-1.0，一般来说网站首页1.0，然后二级三级页面依次降低，具体这个属性有多重要不太清楚。
以上4项中，除了loc是必填项之外，其它3个都不是必须的，但最好都写上。

一个sitemap文件包含的网址不得超过 5 万个，且文件大小不得超过 10 MB。如果您的sitemap超过了这些限值，请将其拆分为几个小的sitemap。这些限制条件有助于确保您的网络服务器不会因提供大文件而超载。一个站点支持提交的sitemap文件个数必须小于5万个


参考：

1. [http://https://www.cnblogs.com/liuxianan/p/make-sitemap.html](http://https://www.cnblogs.com/liuxianan/p/make-sitemap.html)