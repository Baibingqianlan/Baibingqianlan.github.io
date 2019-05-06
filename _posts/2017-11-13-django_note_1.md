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

变量用 `{{ `和 `}}` 包围，用来输出内容信息，变量可以用模型信息，可以和模型进行交换信息。

	My first name is {{ first_name }}. My last name is {{ last_name }}.

其中first_name与last_name可以在模型中定义。模型的值、属性、列表等查看可以用点来访问，如下：

	{{ my_dict.key }}
	{{ my_object.attribute }}
	{{ my_list.0 }}

**标签：**

标签,可以用来输出内容，用作控制作用，如if和for循环。标签用 `{%` 和 `%}` 包围。

	1.CSRF 保护
	{% csrf_token %}  
	
	2.if,for循环，cycle
	{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}

	{% for o in some_list %}
    	<tr class="{% cycle 'row1' 'row2' }">
        ...
    	</tr>
	{% endfor %}

	cycle,用来生成参数，第一次产生第一个参数，第二次产生第二个，结束后从头再来，常用在for循环中。

	3.自动转义
	{% autoescape on %}
	    {{ body }}
	{% endautoescape %}

	4.extends扩展模板
	{% extends "base.html" %} 用引号引用，将 "base.html" 当作父模板扩展.

	{% extends variable %} 使用变量值. 如果变量值为字符串,
	则当作父模板扩展. 如果是一个模板对象,则也会当作父模板扩展.

	目录：
	dir1/
    	template.html
    	base2.html
    	my/
        	base3.html
	base1.html
	
	在template.html,可以使用以下扩展：
	{% extends "./base2.html" %}
	{% extends "../base1.html" %}
	{% extends "./my/base3.html" %}

	5.乘法、除法widthratio
	{% widthratio 5 1 100 %}
	note:等同于：(5 / 1) * 100 ，结果返回500，withratio需要三个参数，
	它会使用参数1/参数2*参数3的方式进行运算，进行乘法运算，使「参数2」=1

	6.with,定义变量
	{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
	{% endwith %}

**过滤器:**

过滤器，用来操作变量的值与格式。

	{{ var|title }}
	{{ my_date|date:"Y-m-d" }}

	1.add，增加
	{{ value|add:"2" }}
	{{ first|add:second }}
	first =[1, 2, 3] and second = [4, 5, 6], 结果＝ [1, 2, 3, 4, 5, 6].
	注：字符器会转成整数进行操作

	利用 add 这个filter ,可以做更疯狂的事:
	计算 A^2: {% widthratio A 1 A %}
	计算 (A+B)^2: {% widthratio A|add:B 1 A|add:B %}
	计算 (A+B) * (C+D): {% widthratio A|add:B 1 C|add:D %}

	2.addslashes，引号前增加转义，用CSV文件中用处多

	{{ value|addslashes }}
	If value is "I'm using Django", the output will be "I\'m using Django".

	3.capfirst，首字母大写；lower，转为小写；

	4.center，给定宽度居中；ljust，左对齐；rjust，右对齐
	"{{ value|center:"15" }}"

	5.cut，移除给定值
	{{ value|cut:" " }}
	If value is "String with spaces", the output will be "Stringwithspaces".

	6.date日期格式化，类似PHP的data()函数
	{{ value|date:"D d M Y" }} #'Wed 09 Jan 2008'.
	{{ value|date:"SHORT_DATE_FORMAT" }} #"09/01/2008"
	{{ value|date }} #9 de Enero de 2008
	{{ value|date:"D d M Y" }} {{ value|time:"H:i" }} 

	7.default，默认值 ，default_if_none，如果值为None
	{{ value|default:"nothing" }}
	{{ value|default_if_none:"nothing" }}

	8.dictsort,字典排序；dictsortreversed，反向排序，
	{{ value|dictsort:"name" }} #按name排序

	9.divisibleby，被整除
	{{ value|divisibleby:"3" }}
	If value is 21, the output would be True.

	10.filesizeformat，文件大小格式化可读， (i.e. '13 KB', '4.1 MB', '102 bytes', etc.).
	{{ value|filesizeformat }}
	If value is 123456789, the output would be 117.7 MB.

	11.first，列表第一项；last,最后一项
	{{ value|first }}
	If value is the list ['a', 'b', 'c'], the output will be 'a'.
	
	12.floatformat，浮点格式化
	34.23234	{{ value|floatformat }}	34.2
	34.00000	{{ value|floatformat }}	34
	34.26000	{{ value|floatformat }}	34.3
	
	
	value		Template					Output
	34.23234	{{ value|floatformat:3 }}	34.232
	34.00000	{{ value|floatformat:3 }}	34.000
	34.26000	{{ value|floatformat:3 }}	34.260

	自动圆整
	34.23234	{{ value|floatformat:"-3" }}	34.232
	34.00000	{{ value|floatformat:"-3" }}	34
	34.26000	{{ value|floatformat:"-3" }}	34.260

	12.force_escape,强制转义
	{% autoescape off %}
    {{ body|linebreaks|force_escape }}
	{% endautoescape %}

	13.get_digit，取数值的第几位，从右侧开始，第一个为1
	{{ value|get_digit:"2" }}
	If value is 123456789, the output will be 8.
	
	14.join，列表连接成为字符串
	{{ value|join:" // " }}
	If value is the list ['a', 'b', 'c'], the output will be the string "a // b // c".
	
	15.length，长度；length_is，长度是否为
	{{ value|length }}
	{{ value|length_is:"4" }}

	16.linebreaks，将换行（\n）替换为<br />
	{{ value|linebreaks }}
	If value is Joel\nis a slug, the output will be <p>Joel<br />is a slug</p>.

	17.linenumbers，增加行号
	{{ value|linenumbers }}

	18.make_list，生成列表

	19.phone2numeric，电话号码

	20.random，列表中随机取值

	21.pluralize，自动复数
	You have {{ num_walruses }} walrus{{ num_walruses|pluralize:"es" }}.

	22.i18n，国际化；l10n，本地化

	23.static,加载静态文件
	{% load static %}
	<img src="{% static "images/hi.jpg" %}" alt="Hi!" />

	{% load static %}
	{% static "images/hi.jpg" as myphoto %}
	<img src="{{ myphoto }}"></img>

	24.get_static_prefix，取静态路径
	{% load static %}
	<img src="{% get_static_prefix %}images/hi.jpg" alt="Hi!" />

	{% load static %}
	{% get_static_prefix as STATIC_PREFIX %}
	<img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!" />
	<img src="{{ STATIC_PREFIX }}images/hi2.jpg" alt="Hello!" />

	25.get_media_prefix，
	{% load static %}
	<body data-media-url="{% get_media_prefix %}">

	26.include，包含其它模板
	{% include "foo/bar.html" %}

	27.now，当前日期或时间
	It is {% now "jS F Y H:i" %}

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

	{% load templatehelper %}：
	<td>{{ foo.product_amount |div:100 }}</td>

**注释(Comments)：**

注释(Comments)，用 `{#` 和 `#}` 包围

	{# this won't be rendered #}



参考：

1. [https://docs.djangoproject.com/zh-hans/2.0/ref/templates/builtins/#ref-templates-builtins-filters](https://docs.djangoproject.com/zh-hans/2.0/ref/templates/builtins/#ref-templates-builtins-filters)
2. [https://my.oschina.net/bobwei/blog/2221851](https://my.oschina.net/bobwei/blog/2221851)


