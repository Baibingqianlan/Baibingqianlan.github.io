---
layout: post
---

blog site cannot be finded.

常用命令：

1. start project: django-admin startproject %prjName%
2. start app:  python manager.py startapp %appName%
3. run app: python manager.py runserver ip:port（0：8000）


### 模板使用

作为一个Web框架，Django需要一种动态生成HTML的便捷方法。最常用的方法依赖于模板。模板包含所需HTML输出的静态部分以及描述动态内容将被插入的一些特殊语法。有关创建带有模板的HTML页面的示例，请参阅:doc:`Tutorial 3</intro/tutorial03>

Django项目可以配置一个或多个模板引擎（或者如果不使用模板，甚至为零）。Django后端内置一个自己的模板系统，创造性地称为Django template language（DTL），和一个流行的替代品JICAN2*。后端也可以使用第三方提供其他可用的模板语言。

Django定义了一个标准的API，用于加载和渲染模板，而不用考虑后端的模板系统。加载包括查找给定标识符的模板并对其进行预处理，通常将其编译的结果保存在内存中。渲染工具将上下文数据插入模板并返回结果字符串。

1. 配置文件：setting.py中的TEMPLATES

		TEMPLATES = [
		    {
		        'BACKEND': 'django.template.backends.django.DjangoTemplates',
		        'DIRS': [],
		        'APP_DIRS': True,
		        'OPTIONS': {
		            # ... some options here ...
		        },
		    },
		]

		BACKEND:模板引擎
		DIRS：模板路径
		APP_DIRS：是否查找应用的模板路径，默认为True

2. 模板语言

主要涉及4个方面的内容：变量、标签、过滤器、注释

**变量：**

变量用 `_{_{ `和 `_}_}` 包围，用来输出内容信息，变量可以用模型信息，可以和模型进行交换信息。
>
	My first name is _{_{ first_name _}_}. My last name is _{_{ last_name _}_}.

其中first_name与last_name可以在模型中定义。模型的值、属性、列表等查看可以用点来访问，如下：
>
	_{_{ my_dict.key _}_}
	_{_{ my_object.attribute _}_}
	_{_{ my_list.0 _}_}

**标签：**

标签,可以用来输出内容，用作控制作用，如if和for循环。标签用 ``\{ % 和 \}`` 包围。


	1.CSRF 保护
	_{ _% csrf_token  _%_}  
	
	2.if,for循环，cycle
	_{ _% if user.is_authenticated  _%_}Hello, _{_{ user.username _}_}._{ _% endif  _%_}

	_{ _% for o in some_list  _%_}
    	<tr class="_{ _% cycle 'row1' 'row2' }">
        ...
    	</tr>
	_{ _% endfor  _%_}

	cycle,用来生成参数，第一次产生第一个参数，第二次产生第二个，结束后从头再来，常用在for循环中。

	3.自动转义
	_{ _% autoescape on  _%_}
	    _{_{ body _}_}
	_{ _% endautoescape  _%_}

	4.extends扩展模板
	_{ _% extends "base.html"  _%_} 用引号引用，将 "base.html" 当作父模板扩展.

	_{ _% extends variable  _%_} 使用变量值. 如果变量值为字符串,
	则当作父模板扩展. 如果是一个模板对象,则也会当作父模板扩展.

	目录：
	dir1/
    	template.html
    	base2.html
    	my/
        	base3.html
	base1.html
	
	在template.html,可以使用以下扩展：
	_{ _% extends "./base2.html"  _%_}
	_{ _% extends "../base1.html"  _%_}
	_{ _% extends "./my/base3.html"  _%_}

	5.乘法、除法widthratio
	_{ _% widthratio 5 1 100  _%_}
	note:等同于：(5 / 1) * 100 ，结果返回500，withratio需要三个参数，
	它会使用参数1/参数2*参数3的方式进行运算，进行乘法运算，使「参数2」=1

	6.with,定义变量
	_{ _% with total=business.employees.count  _%_}
    _{_{ total _}_} employee_{_{ total|pluralize _}_}
	_{ _% endwith  _%_}

**过滤器:**

过滤器，用来操作变量的值与格式。

	_{_{ var|title _}_}
	_{_{ my_date|date:"Y-m-d" _}_}

	1.add，增加
	_{_{ value|add:"2" _}_}
	_{_{ first|add:second _}_}
	first =[1, 2, 3] and second = [4, 5, 6], 结果＝ [1, 2, 3, 4, 5, 6].
	注：字符器会转成整数进行操作

	利用 add 这个filter ,可以做更疯狂的事:
	计算 A^2: _{ _% widthratio A 1 A  _%_}
	计算 (A+B)^2: _{ _% widthratio A|add:B 1 A|add:B  _%_}
	计算 (A+B) * (C+D): _{ _% widthratio A|add:B 1 C|add:D  _%_}

	2.addslashes，引号前增加转义，用CSV文件中用处多

	_{_{ value|addslashes _}_}
	If value is "I'm using Django", the output will be "I\'m using Django".

	3.capfirst，首字母大写；lower，转为小写；

	4.center，给定宽度居中；ljust，左对齐；rjust，右对齐
	"_{_{ value|center:"15" _}_}"

	5.cut，移除给定值
	_{_{ value|cut:" " _}_}
	If value is "String with spaces", the output will be "Stringwithspaces".

	6.date日期格式化，类似PHP的data()函数
	_{_{ value|date:"D d M Y" _}_} #'Wed 09 Jan 2008'.
	_{_{ value|date:"SHORT_DATE_FORMAT" _}_} #"09/01/2008"
	_{_{ value|date _}_} #9 de Enero de 2008
	_{_{ value|date:"D d M Y" _}_} _{_{ value|time:"H:i" _}_} 

	7.default，默认值 ，default_if_none，如果值为None
	_{_{ value|default:"nothing" _}_}
	_{_{ value|default_if_none:"nothing" _}_}

	8.dictsort,字典排序；dictsortreversed，反向排序，
	_{_{ value|dictsort:"name" _}_} #按name排序

	9.divisibleby，被整除
	_{_{ value|divisibleby:"3" _}_}
	If value is 21, the output would be True.

	10.filesizeformat，文件大小格式化可读， (i.e. '13 KB', '4.1 MB', '102 bytes', etc.).
	_{_{ value|filesizeformat _}_}
	If value is 123456789, the output would be 117.7 MB.

	11.first，列表第一项；last,最后一项
	_{_{ value|first _}_}
	If value is the list ['a', 'b', 'c'], the output will be 'a'.
	
	12.floatformat，浮点格式化
	34.23234	_{_{ value|floatformat _}_}	34.2
	34.00000	_{_{ value|floatformat _}_}	34
	34.26000	_{_{ value|floatformat _}_}	34.3
	
	
	value		Template					Output
	34.23234	_{_{ value|floatformat:3 _}_}	34.232
	34.00000	_{_{ value|floatformat:3 _}_}	34.000
	34.26000	_{_{ value|floatformat:3 _}_}	34.260

	自动圆整
	34.23234	_{_{ value|floatformat:"-3" _}_}	34.232
	34.00000	_{_{ value|floatformat:"-3" _}_}	34
	34.26000	_{_{ value|floatformat:"-3" _}_}	34.260

	12.force_escape,强制转义
	_{ _% autoescape off  _%_}
    _{_{ body|linebreaks|force_escape _}_}
	_{ _% endautoescape  _%_}

	13.get_digit，取数值的第几位，从右侧开始，第一个为1
	_{_{ value|get_digit:"2" _}_}
	If value is 123456789, the output will be 8.
	
	14.join，列表连接成为字符串
	_{_{ value|join:" // " _}_}
	If value is the list ['a', 'b', 'c'], the output will be the string "a // b // c".
	
	15.length，长度；length_is，长度是否为
	_{_{ value|length _}_}
	_{_{ value|length_is:"4" _}_}

	16.linebreaks，将换行（\n）替换为<br />
	_{_{ value|linebreaks _}_}
	If value is Joel\nis a slug, the output will be <p>Joel<br />is a slug</p>.

	17.linenumbers，增加行号
	_{_{ value|linenumbers _}_}

	18.make_list，生成列表

	19.phone2numeric，电话号码

	20.random，列表中随机取值

	21.pluralize，自动复数
	You have _{_{ num_walruses _}_} walrus_{_{ num_walruses|pluralize:"es" _}_}.

	22.i18n，国际化；l10n，本地化

	23.static,加载静态文件
	_{ _% load static  _%_}
	<img src="_{ _% static "images/hi.jpg"  _%_}" alt="Hi!" />

	_{ _% load static  _%_}
	_{ _% static "images/hi.jpg" as myphoto  _%_}
	<img src="_{_{ myphoto _}_}"></img>

	24.get_static_prefix，取静态路径
	_{ _% load static  _%_}
	<img src="_{ _% get_static_prefix  _%_}images/hi.jpg" alt="Hi!" />

	_{ _% load static  _%_}
	_{ _% get_static_prefix as STATIC_PREFIX  _%_}
	<img src="_{_{ STATIC_PREFIX _}_}images/hi.jpg" alt="Hi!" />
	<img src="_{_{ STATIC_PREFIX _}_}images/hi2.jpg" alt="Hello!" />

	25.get_media_prefix，
	_{ _% load static  _%_}
	<body data-media-url="_{ _% get_media_prefix  _%_}">

	26.include，包含其它模板
	_{ _% include "foo/bar.html"  _%_}

	27.now，当前日期或时间
	It is _{ _% now "jS F Y H:i"  _%_}

自定义方法：

首先定义方法在templatehelper.py文件中

	@register.filter
	def div(value, div):
	    '''
	    分转化为元，保留两位小数
	    :param value:
	    :param div:
	    :return:
	    '''
	    return round((value / div), 2)
然后在模板中可以按照如下使用，当然前提是

	_{ _% load templatehelper  _%_}：
	<td>_{_{ foo.product_amount |div:100 _}_}</td>

**注释(Comments)：**

注释(Comments)，用 `{#` 和 `#}` 包围

	_{# this won't be rendered #_}


参考：

1. [https://docs.djangoproject.com/zh-hans/2.0/ref/templates/builtins/#ref-templates-builtins-filters](https://docs.djangoproject.com/zh-hans/2.0/ref/templates/builtins/#ref-templates-builtins-filters)
2. [https://my.oschina.net/bobwei/blog/2221851](https://my.oschina.net/bobwei/blog/2221851)


