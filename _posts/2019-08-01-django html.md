---
layout: post
---

### 1. html杂记

#### 1.1 for属性

for 属性规定 label 与哪个表单元素绑定。

隐式和显式的联系

标记通常以下面两种方式中的一种来和表单控件相联系：将表单控件作为标记标签的内容，这样的就是隐式形式，或者为 `<label>` 标签下的 for 属性命名一个目标表单 id，这样就是显式形式。

例如，在 XHTML 中：

	显式的联系：
	<label for="SSN">Social Security Number:</label>
	<input type="text" name="SocSecNum" id="SSN" />

	隐式的联系：
	<label>Date of Birth: <input type="text" name="DofB" /></label>

第一个标记是以显式形式将文本 "Social Security Number:" 和表单的社会安全号码的文本输入控件 ("SocSecNum") 联系起来，它的 for 属性的值和控件的 id 一样，都是 SSN。第二个标记 ("Date of Birth:") 不需要 for 属性，它的相关控件也不需要 id 属性，它们是通过在 `<label> `标签中放入` <input> `标签来隐式地连接起来的。

#### 1.2 form中的ACTION

必需的 action 属性规定当提交表单时，向何处发送表单数据。

	<form class="signin" action="{_% url 'timeblog:login' %_}" method="post">

当提交表单时，表单数据会提交到名为 "timeblog:login" 的页面来处理.


### 2. django 中重定向

1.使用绝对地址,不再说明

2.使用相对地址时,前面加"/"和不加"/"意思不完全相同.使用"/"时,地址从网站根目录开始找,不使用"/"会加上当前项目的名称.

	redirect( '/timeblog/') //http://127.0.0.1:8000/timeblog/
	redirect( 'timeblog/') //http://127.0.0.1:8000/timeblog/timeblog

### 3. django render() render_to_response() local()

#### django render()
context在Django里表现为 Context 类，在 django.template 模块里。 它的构造函数带有一个可选的参数：

一个字典映射变量和它们的值。 调用 Template 对象 的 render() 方法并传递context来填充模板：

	>>> from django.template import Context, Template  
	>>> t = Template('My name is {{ name }}.')  
	>>> c = Context({'name': 'Stephane'})  
	>>> t.render(c)  
	u'My name is Stephane.'

在views.py中:
	
	return render(request, 'blog_add.html', 
		{'blog': blog, 'form': form, 'id': id, 'tag': tag})

#### django中的`render_to_response`()
	
	 return render_to_response('blog_add.html', 
		{'blog': blog, 'form': form, 'id': id, 'tag': tag})

很明显，如果使用render_to_response就省去了render里传递的request。

#### local()

locals()可以直接将函数中所有的变量全部传给模板。当然这可能会传递一些多余的参数，有点浪费内存的嫌疑。

	return render(request, 'timeblog/register.html', locals())


参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [django 中的render和render_to_response()和locals()](https://blog.csdn.net/uwenhao2008/article/details/80675370)

