---
layout: post
---

### 1.django's generic view ##

1. Convert the URLconf.
1. inherite from django.views
> from django.views import generic.
 
	 class IndexView(generic.ListView):
    	template_name='blog/index.html'
    	context_object_name='latest_question_list'#overide'question_list'

     def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

	class DetailView(generic.DetailView):
    	model = Question
    	template_name = 'polls/detail.html'


	class ResultsView(generic.DetailView):
    	model = Question
    	template_name = 'polls/results.html'



[generic view document](https://docs.djangoproject.com/en/dev/topics/class-based-views/ "generic view")


### 2. HTML跳转到指定页面

有三种方法：

1> 用锚点,链接地址为“#”+id(或name)

	<a href="#ct1">跳转到词条1</a>
	 
	<a href="#ct2">跳转到词条2</a>
	<br>
	<div id="ct1" style="height:1000px;">词条1</div>
	<div id="ct2">词条2</div>

2> 用JS

		<script>
	    function onClick() {
	         window.location.hash = "#abc";
	       }
	    </script>
	    <input  type="button" name="Submit" 
			value="提交"  onclick="javascript:onClick();" />
	
	    <div id="abc">跳转到的位置</div>


3> JS中animate的方法

 	<ul>
        <li>
            <a href="#toc0" class="aaa">点击文字跳转</a>
            <!--herf的值一定要带#号，并且要和相对应要跳转的值一致-->
        </li>
    </ul>
    <div class="chapter" style="margin-top: 850px;">
        <a name="toc0" class="aaa1">文字跳转到这里</a>
        <!--这里的a标签可以用name也可以用id-->
        <p>。。。</p>
    </div>

	Js代码

	$(".aaa").click(function () {
	    $('html,body').animate({
	        scrollTop:$(".aaa1").offset().top},{duration:500,easing:'swing'});
	    return false;
	})

### 3. ECMAScript与JavaScript
一个完整的 JavaScript 实现是由以下 3 个不同部分组成的：

+ 核心（ECMAScript）
+ 文档对象模型（DOM）
+ 浏览器对象模型（BOM）

核心 ECMAScript 描述了该语言的语法和基本对象；

DOM 描述了处理网页内容的方法和接口；

BOM 描述了与浏览器进行交互的方法和接口。

#### ECMAScript
简单地说，ECMAScript 描述了以下内容：语法、类型、语句、关键字、保留字、运算符、对象。ECMAScript 仅仅是一个描述，定义了脚本语言的所有属性、方法和对象。

在 ECMA-262 中，ECMAScript 符合性（conformance）有明确的定义。一个脚本语言必须满足以下四项基本原则：

1. 符合的实现必须按照 ECMA-262 中所描述的支持所有的“类型、值、对象、属性、函数和程序语言及语义”（ECMA-262，第一页）
2. 符合的实现必须支持 Unicode 字符标准（UCS）
3. 符合的实现可以增加没有在 ECMA-262 中指定的“额外类型、值、对象、属性和函数”。ECMA-262 将这些增加描述为规范中未给定的新对象或对象的新属性
4. 符合的实现可以支持没有在 ECMA-262 中定义的“程序和正则表达式语法”（意思是可以替换或者扩展内建的正则表达式支持）

#### DOM
DOM（文档对象模型）是 HTML 和 XML 的应用程序接口（API）。DOM 将把整个页面规划成由节点层级构成的文档。HTML 或 XML 页面的每个部分都是一个节点的衍生物。

DOM Level 1 是 W3C 于 1998 年 10 月提出的。它由两个模块组成，即 DOM Core 和 DOM HTML。DOM 不是 JavaScript 专有的，事实上许多其他语言都实现了它。不过，Web 浏览器中的 DOM 已经用 ECMAScript 实现了，现在是 JavaScript 语言的一个很大组成部分。在 Level 3 中，DOM Core 被扩展为支持所有的 XML 1.0 特性，包括 XML Infoset、XPath 和 XML Base。

除了 DOM Core 和 DOM HTML 外，还有其他几种语言发布了自己的 DOM 标准。这些语言都是基于 XML 的，每种 DOM 都给对应语言添加了特有的方法和接口：
+ 可缩放矢量语言（SVG）1.0
+ 数字标记语言（MathML）1.0
+ 同步多媒体集成语言（SMIL）

#### BOM

BOM 主要处理浏览器窗口和框架，不过通常浏览器特定的 JavaScript 扩展都被看做 BOM 的一部分。这些扩展包括：

+ 弹出新的浏览器窗口
+ 移动、关闭浏览器窗口以及调整窗口大小
+ 提供 Web 浏览器详细信息的定位对象
+ 提供用户屏幕分辨率详细信息的屏幕对象
+ 对 cookie 的支持
+ IE 扩展了 BOM，加入了 ActiveXObject 类，可以通过 JavaScript 实例化 ActiveX 对象




