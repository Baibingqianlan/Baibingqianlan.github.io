---
layout: post
---

## 一、网页中的javascript
JavaScript 是世界上最流行的编程语言。
这门语言可用于 HTML 和 web，更可广泛用于服务器、PC、笔记本电脑、平板电脑和智能手机等设备。

### 1.位置
HTML 中的脚本必须位于 `<script> 与 </script> `标签之间。
脚本可被放置在 HTML 页面的 `<body> 和 <head> `部分中

`<head>` 或 `<body>` 中的 JavaScript
您可以在 HTML 文档中放入不限数量的脚本。
脚本可位于 HTML 的 <body> 或 <head> 部分中，或者同时存在于两个部分中。
通常的做法是把函数放入 <head> 部分中，或者放在页面底部。这样就可以把它们安置到同一处位置，不会干扰页面的内容。

### 2.JavaScript 输出
JavaScript 通常用于操作 HTML 元素。

	document.getElementById("demo").innerHTML="我的第一段 JavaScript";
	document.write("<p>我的第一段 JavaScript</p>");

请使用 document.write() 仅仅向文档输出写内容。
如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖：

### 3.语法
1. 分号 ;

分号用于分隔 JavaScript 语句。
通常我们在每条可执行的语句结尾添加分号。在 JavaScript 中，用分号来结束语句是可选的。

2. 变量使用 var 关键词来声明，变量必须以字母开头。对大小写敏感，与C++相同
3. 对代码行进行折行"\"，与C++相同
4. 单行注释以 // 开头，多行注释以 /* 开始，以 */ 结尾，与C++相同
5. JavaScript 拥有动态类型。这意味着相同的变量可用作不同的类型

    	for (var i=0;i<cars.length;i++)
    	{
    		document.write(cars[i] + "<br>");
    	}



### 4.数据类型
1. JavaScript 字符串，使用单引号或双引号
2. JavaScript 数字，只有一种数字类型。数字可以带小数点，也可以不带，可用科学计数法
3. JavaScript 布尔，只能有两个值：true 或 false
4. JavaScript 数组,如下
5. JavaScript 对象,对象由花括号分隔，json形式 (name : value) 来定义,与PYTHON的字典很像 

>
>   数组：
>   
> 	var cars=new Array();
> 	cars[0]="Audi";
> 	cars[1]="BMW";
> 	cars[2]="Volvo";
> 
> 	var cars=new Array("Audi","BMW","Volvo");
> 	var cars=["Audi","BMW","Volvo"];
> 	
>对象：
>   var person={firstname:"Bill", lastname:"Gates", id:5566};
> 	


当您声明新变量时，可以使用关键词 "new" 来声明其类型：

	var carname=new String;
	var x=      new Number;
	var y=      new Boolean;
	var cars=   new Array;
	var person= new Object;

JavaScript 中的所有事物都是对象：字符串、数字、数组、日期，等等。
在 JavaScript 中，对象是拥有属性和方法的数据。
本例创建名为 "person" 的对象，并为其添加了四个属性：

	person=new Object();
	person.firstname="Bill";
	person.lastname="Gates";
	person.age=56;
	person.eyecolor="blue";

### 5.JavaScript 事件

	onabort	图像加载被中断	1	3	4
	onblur	元素失去焦点	1	2	3
	onchange	用户改变域的内容	1	2	3
	onclick	鼠标点击某个对象	1	2	3
	ondblclick	鼠标双击某个对象	1	4	4
	onerror	当加载文档或图像时发生某个错误	1	3	4
	onfocus	元素获得焦点	1	2	3
	onkeydown	某个键盘的键被按下	1	4	3
	onkeypress	某个键盘的键被按下或按住	1	4	3
	onkeyup	某个键盘的键被松开	1	4	3
	onload	某个页面或图像被完成加载	1	2	3
	onmousedown	某个鼠标按键被按下	1	4	4
	onmousemove	鼠标被移动	1	6	3
	onmouseout	鼠标从某元素移开	1	4	4
	onmouseover	鼠标被移到某元素之上	1	2	3
	onmouseup	某个鼠标按键被松开	1	4	4
	onreset	重置按钮被点击	1	3	4
	onresize	窗口或框架被调整尺寸	1	4	4
	onselect	文本被选定	1	2	3
	onsubmit	提交按钮被点击	1	2	3
	onunload	用户退出页面	1	2	3


## 二、JavaScript中Browser 对象
BOM(Browser Object Model) 是指浏览器对象模型，是用于描述这种对象与对象之间层次关系的模型，浏览器对象模型提供了独立于内容的、可以与浏览器窗口进行互动的对象结构。BOM由多个对象组成，其中代表浏览器窗口的Window对象是BOM的顶层对象，其他对象都是该对象的子对象。
### 1.Window 对象
Window 对象表示浏览器中打开的窗口。
如果文档包含框架`（<frame> 或 <iframe> 标签）`，浏览器会为 HTML 文档创建一个 window 对象，并为每个框架创建一个额外的 window 对象。

Note注意： 没有应用于 window 对象的公开标准，不过所有浏览器都支持该对象。

Window 对象属性

	closed	返回窗口是否已被关闭。
	defaultStatus	设置或返回窗口状态栏中的默认文本。
	document	对 Document 对象的只读引用。(请参阅对象)
	frames	返回窗口中所有命名的框架。该集合是 Window 对象的数组，每个 Window 对象在窗口中含有一个框架。
	history	对 History 对象的只读引用。请参数 History 对象。
	innerHeight	返回窗口的文档显示区的高度。
	innerWidth	返回窗口的文档显示区的宽度。
	localStorage	在浏览器中存储 key/value 对。没有过期时间。
	length	设置或返回窗口中的框架数量。
	location	用于窗口或框架的 Location 对象。请参阅 Location 对象。
	name	设置或返回窗口的名称。
	navigator	对 Navigator 对象的只读引用。请参数 Navigator 对象。
	opener	返回对创建此窗口的窗口的引用。
	outerHeight	返回窗口的外部高度，包含工具条与滚动条。
	outerWidth	返回窗口的外部宽度，包含工具条与滚动条。
	pageXOffset	设置或返回当前页面相对于窗口显示区左上角的 X 位置。
	pageYOffset	设置或返回当前页面相对于窗口显示区左上角的 Y 位置。
	parent	返回父窗口。
	screen	对 Screen 对象的只读引用。请参数 Screen 对象。
	screenLeft	返回相对于屏幕窗口的x坐标
	screenTop	返回相对于屏幕窗口的y坐标
	screenX	返回相对于屏幕窗口的x坐标
	sessionStorage	在浏览器中存储 key/value 对。 在关闭窗口或标签页之后将会删除这些数据。
	screenY	返回相对于屏幕窗口的y坐标
	self	返回对当前窗口的引用。等价于 Window 属性。
	status	设置窗口状态栏的文本。
	top	返回最顶层的父窗口。

Window 对象方法
 
	alert()	显示带有一段消息和一个确认按钮的警告框。
	atob()	解码一个 base-64 编码的字符串。
	btoa()	创建一个 base-64 编码的字符串。
	blur()	把键盘焦点从顶层窗口移开。
	clearInterval()	取消由 setInterval() 设置的 timeout。
	clearTimeout()	取消由 setTimeout() 方法设置的 timeout。
	close()	关闭浏览器窗口。
	confirm()	显示带有一段消息以及确认按钮和取消按钮的对话框。
	createPopup()	创建一个 pop-up 窗口。
	focus()	把键盘焦点给予一个窗口。
	getSelection()	返回一个 Selection 对象，表示用户选择的文本范围或光标的当前位置。
	getComputedStyle()	获取指定元素的 CSS 样式。
	matchMedia()	该方法用来检查 media query 语句，它返回一个 MediaQueryList对象。
	moveBy()	可相对窗口的当前坐标把它移动指定的像素。
	moveTo()	把窗口的左上角移动到一个指定的坐标。
	open()	打开一个新的浏览器窗口或查找一个已命名的窗口。
	print()	打印当前窗口的内容。
	prompt()	显示可提示用户输入的对话框。
	resizeBy()	按照指定的像素调整窗口的大小。
	resizeTo()	把窗口的大小调整到指定的宽度和高度。
	scroll()	已废弃。 该方法已经使用了 scrollTo() 方法来替代。
	scrollBy()	按照指定的像素值来滚动内容。
	scrollTo()	把内容滚动到指定的坐标。
	setInterval()	按照指定的周期（以毫秒计）来调用函数或计算表达式。
	setTimeout()	在指定的毫秒数后调用函数或计算表达式。
	stop()	停止页面载入。
### 2.Navigator 对象
Navigator 对象包含有关浏览器的信息。

Navigator 对象属性

	appCodeName	返回浏览器的代码名
	appName	返回浏览器的名称
	appVersion	返回浏览器的平台和版本信息
	cookieEnabled	返回指明浏览器中是否启用 cookie 的布尔值
	platform	返回运行浏览器的操作系统平台
	userAgent	返回由客户机发送服务器的user-agent 头部的值
Navigator 对象方法

	javaEnabled()	指定是否在浏览器中启用Java
	taintEnabled()	规定浏览器是否启用数据污点(data tainting)

### 3.Screen 对象
Screen 对象包含有关客户端显示屏幕的信息。
Screen 对象属性

	availHeight	返回屏幕的高度（不包括Windows任务栏）
	availWidth	返回屏幕的宽度（不包括Windows任务栏）
	colorDepth	返回目标设备或缓冲器上的调色板的比特深度
	height	返回屏幕的总高度
	pixelDepth	返回屏幕的颜色分辨率（每象素的位数）
	width	返回屏幕的总宽度
### 4.History 对象
History 对象包含用户（在浏览器窗口中）访问过的 URL。
History 对象是 window 对象的一部分，可通过 window.history 属性对其进行访问。

History 对象属性

	length	返回历史列表中的网址数
	History 对象方法

方法	

	back()	加载 history 列表中的前一个 URL
	forward()	加载 history 列表中的下一个 URL
	go()	加载 history 列表中的某个具体页面

### 5.Location 对象
Location 对象包含有关当前 URL 的信息。
Location 对象是 window 对象的一部分，可通过 window.Location 属性对其进行访问。

![host url]({{site.url}}/assets/2018-07-05/host.png)

Location 对象属性

	hash	返回一个URL的锚部分
	host	返回一个URL的主机名和端口
	hostname	返回URL的主机名
	href	返回完整的URL
	pathname	返回的URL路径名。
	port	返回一个URL服务器使用的端口号
	protocol	返回一个URL协议
	search	返回一个URL的查询部分
Location 对象方法

	assign()	载入一个新的文档
	reload()	重新载入当前文档
	replace()	用新的文档替换当前文档

### 6.window.Document 对象
每个载入浏览器的 HTML 文档都会成为 Document 对象。

Document 对象使我们可以从脚本中对 HTML 页面中的所有元素进行访问。

提示：Document 对象是 Window 对象的一部分，可通过 window.document 属性对其进行访问。

Document 对象集合

	all[]	提供对文档中所有 HTML 元素的访问。
	anchors[]	返回对文档中所有 Anchor 对象的引用。
	applets	返回对文档中所有 Applet 对象的引用。
	forms[]	返回对文档中所有 Form 对象引用。
	images[]	返回对文档中所有 Image 对象引用。
	links[]	返回对文档中所有 Area 和 Link 对象引用。

Document 对象属性

	body	提供对 <body> 元素的直接访问。	对于定义了框架集的文档，该属性引用最外层的 <frameset>。
	cookie	设置或返回与当前文档有关的所有 cookie。
	domain	返回当前文档的域名。
	lastModified	返回文档被最后修改的日期和时间。
	referrer	返回载入当前文档的文档的 URL。
	title	返回当前文档的标题。
	URL	返回当前文档的 URL。

Document 对象方法

	close()	关闭用 document.open() 方法打开的输出流，并显示选定的数据。
	getElementById()	返回对拥有指定 id 的第一个对象的引用。
	getElementsByName()	返回带有指定名称的对象集合。
	getElementsByTagName()	返回带有指定标签名的对象集合。
	open()	打开一个流，以收集来自任何 document.write() 或 document.writeln() 方法的输出。
	write()	向文档写 HTML 表达式 或 JavaScript 代码。
	writeln()	等同于 write() 方法，不同的是在每个表达式之后写一个换行符。

HTML DOM 节点
在 HTML DOM （文档对象模型）中，每个部分都是节点：

	文档本身是文档节点
	所有 HTML 元素是元素节点
	所有 HTML 属性是属性节点
	HTML 元素内的文本是文本节点
	注释是注释节点

Element 对象

	在 HTML DOM 中，Element 对象表示 HTML 元素。
	Element 对象可以拥有类型为元素节点、文本节点、注释节点的子节点。
	NodeList 对象表示节点列表，比如 HTML 元素的子节点集合。
	元素也可以拥有属性。属性是属性节点。
属性和方法
下面的属性和方法可用于所有 HTML 元素上：

	element.accessKey	设置或返回元素的快捷键。
	element.appendChild()	向元素添加新的子节点，作为最后一个子节点。
	element.attributes	返回元素属性的 NamedNodeMap。
	element.childNodes	返回元素子节点的 NodeList。
	element.className	设置或返回元素的 class 属性。
	element.clientHeight	返回元素的可见高度。
	element.clientWidth	返回元素的可见宽度。
	element.cloneNode()	克隆元素。
	element.compareDocumentPosition()	比较两个元素的文档位置。
	element.contentEditable	设置或返回元素的文本方向。
	element.dir	设置或返回元素的内容是否可编辑。
	element.firstChild	返回元素的首个子。
	element.getAttribute()	返回元素节点的指定属性值。
	element.getAttributeNode()	返回指定的属性节点。
	element.getElementsByTagName()	返回拥有指定标签名的所有子元素的集合。
	element.getFeature()	返回实现了指定特性的 API 的某个对象。
	element.getUserData()	返回关联元素上键的对象。
	element.hasAttribute()	如果元素拥有指定属性，则返回true，否则返回 false。
	element.hasAttributes()	如果元素拥有属性，则返回 true，否则返回 false。
	element.hasChildNodes()	如果元素拥有子节点，则返回 true，否则 false。
	element.id	设置或返回元素的 id。
	element.innerHTML	设置或返回元素的内容。
	element.insertBefore()	在指定的已有的子节点之前插入新节点。
	element.isContentEditable	设置或返回元素的内容。
	element.isDefaultNamespace()	如果指定的 namespaceURI 是默认的，则返回 true，否则返回 false。
	element.isEqualNode()	检查两个元素是否相等。
	element.isSameNode()	检查两个元素是否是相同的节点。
	element.isSupported()	如果元素支持指定特性，则返回 true。
	element.lang	设置或返回元素的语言代码。
	element.lastChild	返回元素的最后一个子元素。
	element.namespaceURI	返回元素的 namespace URI。
	element.nextSibling	返回位于相同节点树层级的下一个节点。
	element.nodeName	返回元素的名称。
	element.nodeType	返回元素的节点类型。
	element.nodeValue	设置或返回元素值。
	element.normalize()	合并元素中相邻的文本节点，并移除空的文本节点。
	element.offsetHeight	返回元素的高度。
	element.offsetWidth	返回元素的宽度。
	element.offsetLeft	返回元素的水平偏移位置。
	element.offsetParent	返回元素的偏移容器。
	element.offsetTop	返回元素的垂直偏移位置。
	element.ownerDocument	返回元素的根元素（文档对象）。
	element.parentNode	返回元素的父节点。
	element.previousSibling	返回位于相同节点树层级的前一个元素。
	element.removeAttribute()	从元素中移除指定属性。
	element.removeAttributeNode()	移除指定的属性节点，并返回被移除的节点。
	element.removeChild()	从元素中移除子节点。
	element.replaceChild()	替换元素中的子节点。
	element.scrollHeight	返回元素的整体高度。
	element.scrollLeft	返回元素左边缘与视图之间的距离。
	element.scrollTop	返回元素上边缘与视图之间的距离。
	element.scrollWidth	返回元素的整体宽度。
	element.setAttribute()	把指定属性设置或更改为指定值。
	element.setAttributeNode()	设置或更改指定属性节点。
	element.setIdAttribute()	
	element.setIdAttributeNode()	
	element.setUserData()	把对象关联到元素上的键。
	element.style	设置或返回元素的 style 属性。
	element.tabIndex	设置或返回元素的 tab 键控制次序。
	element.tagName	返回元素的标签名。
	element.textContent	设置或返回节点及其后代的文本内容。
	element.title	设置或返回元素的 title 属性。
	element.toString()	把元素转换为字符串。
	nodelist.item()	返回 NodeList 中位于指定下标的节点。
	nodelist.length	返回 NodeList 中的节点数。

HTML DOM Event 对象

Event 对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。
事件通常与函数结合使用，函数不会在事件发生前被执行！

事件句柄　(Event Handlers)

HTML 4.0 的新特性之一是能够使 HTML 事件触发浏览器中的行为，比如当用户点击某个 HTML 元素时启动一段 JavaScript。下面是一个属性列表，可将之插入 HTML 标签以定义事件的行为。

	onabort	图像的加载被中断。
	onblur	元素失去焦点。
	onchange	域的内容被改变。
	onclick	当用户点击某个对象时调用的事件句柄。
	ondblclick	当用户双击某个对象时调用的事件句柄。
	onerror	在加载文档或图像时发生错误。
	onfocus	元素获得焦点。
	onkeydown	某个键盘按键被按下。
	onkeypress	某个键盘按键被按下并松开。
	onkeyup	某个键盘按键被松开。
	onload	一张页面或一幅图像完成加载。
	onmousedown	鼠标按钮被按下。
	onmousemove	鼠标被移动。
	onmouseout	鼠标从某元素移开。
	onmouseover	鼠标移到某元素之上。
	onmouseup	鼠标按键被松开。
	onreset	重置按钮被点击。
	onresize	窗口或框架被重新调整大小。
	onselect	文本被选中。
	onsubmit	确认按钮被点击。
	onunload	用户退出页面。

鼠标 / 键盘属性

	altKey	返回当事件被触发时，"ALT" 是否被按下。
	button	返回当事件被触发时，哪个鼠标按钮被点击。
	clientX	返回当事件被触发时，鼠标指针的水平坐标。
	clientY	返回当事件被触发时，鼠标指针的垂直坐标。
	ctrlKey	返回当事件被触发时，"CTRL" 键是否被按下。
	metaKey	返回当事件被触发时，"meta" 键是否被按下。
	relatedTarget	返回与事件的目标节点相关的节点。
	screenX	返回当某个事件被触发时，鼠标指针的水平坐标。
	screenY	返回当某个事件被触发时，鼠标指针的垂直坐标。
	shiftKey	返回当事件被触发时，"SHIFT" 键是否被按下。








参考：

1. [JavaScript 简介](http://www.w3school.com.cn/js/js_intro.asp)
