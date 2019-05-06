---
layout: post
title: "djangoproject note 2"
---

## 1. net address ##
using django document on the site[django document](https://docs.djangoproject.com/en/dev/intro/tutorial01/), you can learn more!

## 2. csrf *csrf_token* ##
CSRF（Cross-Site Request Forgery，跨站点伪造请求）是一种网络攻击方式，该攻击可以在受害者毫不知情的情况下以受害者名义伪造请求发送给受攻击站点，从而在未授权的情况下执行在权限保护之下的操作，具有很大的危害性。具体来讲，可以这样理解CSRF攻击：攻击者盗用了你的身份，以你的名义发送恶意请求，对服务器来说这个请求是完全合法的，但是却完成了攻击者所期望的一个操作，比如以你的名义发送邮件、发消息，盗取你的账号，添加系统管理员，甚至于购买商品、虚拟货币转账等。
 [@detail@](http://blog.csdn.net/wjtlht928/article/details/46563809)

## 3. HTTP 请求方式: GET和POST的比较 ##
- GET - 从指定的服务器中获取数据
- POST - 提交数据给指定的服务器处理


> GET方法：
使用GET方法时，查询字符串（键值对）被附加在URL地址后面一起发送到服务器：
`/test/demo_form.jsp?ame1=value1&name2=value2`

特点：

+ GET请求能够被缓存
+ GET请求会保存在浏览器的浏览记录中
+ 以GET请求的URL能够保存为浏览器书签
+ GET请求有长度限制
+ GET请求主要用以获取数据

> POST方法：
使用POST方法时，查询字符串在POST信息中单独存在，和HTTP请求一起发送到服务器：
POST /test/demo_form.jsp HTTP/1.1
Host: w3schools.com name1=value1&name2=value2

特点：

+ POST请求不能被缓存下来
+ POST请求不会保存在浏览器浏览记录中
+ 以POST请求的URL无法保存为浏览器书签
+ POST请求没有长度限制

[@detail@](https://www.cnblogs.com/igeneral/p/3641574.html )

## 4. 模型与数据库

+ 编辑 models.py 文件，改变模型。
+ 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
+ 运行 python manage.py migrate 来应用数据库迁移。

## 5.视图
django中视图编码分类：**FBV(function based view)和CBV(class based view)**.FBV用函数来实现响应请求，参数为request,CBV用类来实现响应（类要继承自View）.

	
	1. FBV是基于函数的view
	
	def add_class(request):
	    if request.method == "POST":
	        class_name = request.POST.get("class_name")
	        models.Classes.objects.create(name=class_name)
	        return redirect("/class_list/")
	    return render(request, "add_class.html")

	2. CBV是基于类的view

	from django.views import View
	
	class AddClass(View):
	
	    def get(self, request):
	        return render(request, "add_class.html")
	
	    def post(self, request):
	        class_name = request.POST.get("class_name")
	        models.Classes.objects.create(name=class_name)
	        return redirect("/class_list/")

	　　注意 : 
	
	　　　　使用CBV时, urls.py中的映射关系也要修改.
	
	url(r'^add_class/$', views.AddClass.as_view()),

一个视图函数（类），简称视图，是一个简单的Python 函数（类），它接受Web请求并且返回Web响应。响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片. . . 是任何东西都可以。无论视图本身包含什么逻辑，都要返回响应。

视图函数，一定包含两个对象： 

    requset---->用户请求相关的所有信息（对象）
    Httpresponse---->响应字符串

+ HttpRequest请求对象，是由django自动创建的，request参数承接这个对象

属性：

	HttpRequest.scheme	表示请求方案的字符串（通常为http或https）
	request.path   　　　　# 获取访问文件路径
	request.method 　　#获取请求中使用的HTTP方式（POST/GET），必须使用大写	
	request.body　　　　　　#含所有请求体信息 是bytes类型，我们还可以用 python 的类文件方法去操作它，详情参考 HttpRequest.read()
	request.GET  　　　　　　#GET请求的数据(类字典对象)  请求头中的url中?	后面拿值
	request.POST　　　　 # POST请求的数据(类字典对象) 请求体里拿值
	request.COOKIES 　　　　#包含所有cookies的标准Python字典对象；	keys和values都是字符串。
	
	request.FILES：      包含所有上传文件的类字典对象；FILES中的每一个Key都是
		<input type="file" name="" />标签中name属性的值，
		FILES中的每一个value同时也是一个标准的python字典对象，包含下面三个Keys：
	
	            　　　　 filename：      上传文件名，用字符串表示
	           　　　　  content_type:   上传文件的Content Type
	            　　　　 content：       上传文件的原始内容
	
	
	request.user：       是一个django.contrib.auth.models.User对象，代表当前登陆的用户。
		如果访问用户当前没有登陆，user将被初始化为django.contrib.auth.models.AnonymousUser
		的实例。你可以通过user的is_authenticated()方法来辨别用户是否登陆：
		 if req.user.is_authenticated();
		只有激活Django中的AuthenticationMiddleware时该属性才可用
	
	request.session：   　　 唯一可读写的属性，代表当前会话的字典对象；
		自己有激活Django中的session支持时该属性才可用
	request.META： 一个标准的Python 字典，包含所有的HTTP 首部。

实例：

request.GET.get('name') 　　 

	拿到GET请求里name的值，如果某个键对应有多个值，则不能直接用get取值，需要用getlist，如：
	request.POST.getlist("hobby")


请求url:http://127.0.0.1:8000/index.html/23?a=1
      
	request.path
	结果为:/index.html/23
	
	request.get_full_path()
	结果为:/index.html/23?a=1

+ HttpResponse，响应对象就必须我们自己创建，HttpResponse类在django.http.HttpResponse ，每个view请求处理方法必须返回一个HttpResponse响应对象。

在HttpResponse对象上扩展的常用方法：

1. **render**(request, template_name[, context]），将指定页面渲染后返回给浏览器。render方法主要是将从服务器提取的数据，填充到模板中，然后将渲染后的html静态文件返回给浏览器。这里一定要注意：render渲染的是模板。

		参数：
		request： 用于生成响应的请求对象。		
		template_name：要使用的模板的完整名称，可选的参数
		context：添加到模板上下文的一个字典。默认是一个空字典。
			如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。
		content_type：生成的文档要使用的MIME类型。
			默认为DEFAULT_CONTENT_TYPE 设置的值。
		status：响应的状态码。默认为200。

实例：

	from django.shortcuts import render

	def test(request):
   		return render(request,'index.html')   

	def show(request, id):  
	    book = BookInfo.objects.get(pk=id) 　　#从数据库中取出对应id的数据
	    herolist = book.heroinfo_set.all()  
	    context = {'list': herolist} 　　　　  # 将数据保存在list
	    return render(request, 'booktest/show.html', context) #通过render进行模板渲染

2.**redirect** 函数

	参数可以是：
	
	一个模型：将调用模型的get_absolute_url() 函数
	一个视图，可以带有参数：将使用urlresolvers.reverse 来反向解析名称
	一个绝对的或相对的URL，将原封不动的作为重定向的位置。
	默认返回一个临时的重定向；传递permanent=True 可以返回一个永久的重定向。

	传递一个对象：	
		将调用get_absolute_url() 方法来获取重定向的URL：	
		from django.shortcuts import redirect		 
		def my_view(request):
		    ...
		    object = MyModel.objects.get(...)
		    return redirect(object)

	传递一个视图的名称：
	
		可以带有位置参数和关键字参数；将使用reverse() 方法反向解析URL：　
		def my_view(request):
	    	...
	    	return redirect('some-view-name', foo='bar')

	传递要重定向的一个硬编码的URL：
		def my_view(request):
		    ...
		    return redirect('/some/url/')

	也可以是一个完整的URL：
		def my_view(request):
		    ...
		    return redirect('http://example.com/')

	永久的重定向：
		def my_view(request):
		    ...
		    object = MyModel.objects.get(...)
		    return redirect(object, permanent=True)　


总结两者区别：　　　　

第一，render返回一个登陆成功后的页面，刷新该页面将回复到跳转前页面。而redirect则不会

第二，如果页面需要模板语言渲染,需要的将数据库的数据加载到html,那么render方法则不会显示这一部分，render返回一个登陆成功页面，不会经过url路由分发系统，也就是说，不会执行跳转后url的视图函数。这样，返回的页面渲染不成功；而redirect是跳转到指定页面，当登陆成功后，会在url路由系统进行匹配，如果有存在的映射函数，就会执行对应的映射函数。

+ View类，通用视图的基类
		
		# views.py
		from django.http import HttpResponse
		from django.views.generic import View
		 
		class MyView(View):
		 
		    def get(self, request, *args, **kwargs):
		        return HttpResponse('Hello, World!')
		 
		# urls.py
		from django.conf.urls import patterns, url
		 
		from myapp.views import MyView
		 
		urlpatterns = patterns('',
		    url(r'^mine/$', MyView.as_view(), name='my-view'),
		)

+ django.views.generic.base.TemplateView

在 get_context_data() 函数中，可以传一些 额外内容 到 模板

	# views.py
	 
	from django.views.generic.base import TemplateView
	 
	from articles.models import Article
	 
	class HomePageView(TemplateView):
	 
	    template_name = "home.html"
	 
	    def get_context_data(self, **kwargs):
	        context = super(HomePageView, self).get_context_data(**kwargs)
	        context['latest_articles'] = Article.objects.all()[:5]
	        return context
	 
	 
	# urls.py
	 
	from django.conf.urls import patterns, url
	 
	from myapp.views import HomePageView
	 
	urlpatterns = patterns('',
	    url(r'^$', HomePageView.as_view(), name='home'),
	)

+ django.views.generic.base.RedirectView

		# views.py
		from django.shortcuts import get_object_or_404
		from django.views.generic.base import RedirectView
		 
		from articles.models import Article
		 
		class ArticleCounterRedirectView(RedirectView):
		 
		    url = ' # 要跳转的网址，
		    # url 可以不给，用 pattern_name 和 get_redirect_url() 函数 来解析到要跳转的网址
		     
		    permanent = False #是否为永久重定向, 默认为 True
		    query_string = True # 是否传递GET的参数到跳转网址，True时会传递，默认为 False
		    pattern_name = 'article-detail' # 用来跳转的 URL, 看下面的 get_redirect_url() 函数
		 
		     
		    # 如果url没有设定，此函数就会尝试用pattern_name和从网址中捕捉的参数来获取对应网址
		    # 即 reverse(pattern_name, args) 得到相应的网址，
		    # 在这个例子中是一个文章的点击数链接，点击后文章浏览次数加1，再跳转到真正的文章页面
		    def get_redirect_url(self, *args, **kwargs):
		        article = get_object_or_404(Article, pk=kwargs['pk'])
		        article.update_counter() # 更新文章点击数，在models.py中实现
		        return super(ArticleCounterRedirectView, self).get_redirect_url(*args, **kwargs)
		 
		 
		# urls.py
		from django.conf.urls import patterns, paths
		from django.views.generic.base import RedirectView
		 
		from article.views import ArticleCounterRedirectView, ArticleDetail
		 
		urlpatterns = patterns('',		 
		    path(r'^counter/(?P<pk>\d+)/$', 
				ArticleCounterRedirectView.as_view(), name='article-counter'),
		    path(r'^details/(?P<pk>\d+)/$', 
				ArticleDetail.as_view(), name='article-detail'),
		)

+ django.views.generic.detail.DetailView

DetailView 有以下方法：

	dispatch()	
	http_method_not_allowed()	
	get_template_names()	
	get_slug_field()
	get_queryset()	
	get_object()	
	get_context_object_name()	
	get_context_data()	
	get()	
	render_to_response()

实例：

	# views.py
	from django.views.generic.detail import DetailView
	from django.utils import timezone
	 
	from articles.models import Article
	 
	class ArticleDetailView(DetailView):
	 
	    model = Article # 要显示详情内容的类
	     
	    template_name = 'article_detail.html' 
	    # 模板名称，默认为 应用名/类名_detail.html（即 app/modelname_detail.html）
	 
	    # 在 get_context_data() 函数中可以用于传递一些额外的内容到网页
	    def get_context_data(self, **kwargs):
	        context = super(ArticleDetailView, self).get_context_data(**kwargs)
	        context['now'] = timezone.now()
	        return context
	         
	         
	# urls.py
	from django.conf.urls import path 
	from article.views import ArticleDetailView
	 
	urlpatterns = [
	    path(r'^(?P<slug>[-_\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
	]
	
页面	article_detail.html
	
	<h1>标题：{{ object.title }}</h1>
	<p>内容：{{ object.content }}</p>
	<p>发表人: {{ object.reporter }}</p>
	<p>发表于: {{ object.pub_date|date }}</p>
	<p>日期: {{ now|date }}</p>

实例2：

	from django.utils import timezone
	from django.views.generic import DetailView
	from books.models import Author
	
	class AuthorDetailView(DetailView):
	
	    queryset = Author.objects.all()
	
	    def get_object(self):
	        # Call the superclass
	        object = super().get_object()
	        # Record the last accessed date
	        object.last_accessed = timezone.now()
	        object.save()
	        # Return the object
	        return object


+  django.views.generic.list.ListView

ListView 有以下方法：

	dispatch()	
	http_method_not_allowed()	
	get_template_names()	
	get_queryset()	
	get_context_object_name()
	get_context_data()	
	get()	
	render_to_response()

实例

	# views.py
	from django.views.generic.list import ListView
	from django.utils import timezone
	 
	from articles.models import Article
	 
	class ArticleListView(ListView):
	 
	    model = Article
	 
	    def get_context_data(self, **kwargs):
	        context = super(ArticleListView, self).get_context_data(**kwargs)
	        context['now'] = timezone.now()
	        return context
	 
	 
	 
	# urls.py:	 
	from django.conf.urls import path	 
	from article.views import ArticleListView
	 
	urlpatterns = [
	    path(r'^$', ArticleListView.as_view(), name='article-list'),
	]

页面article_list.html

	<h1>文章列表</h1>
	<ul>
	_{_% for article in object_list _%_}
	    <li>_{_{ article.pub_date|date _}_} - _{_{ article.headline _}_}</li>
	_{_% empty _%_}
	    <li>抱歉，目前还没有文章。</li>
	_{_% endfor _%_}
	</ul>

**心得**：

同一个视图，可以通过不同的函数重写，来增加附加内容，如，可以通过get_context_data（）来返回一些其它模型的数据。不需要为一个网页建立多套视图地址。如下实例：

	class IndexView(generic.ListView):
	    template_name='timeblog/index.html'
	    context_object_name='blogs'
	
	    def get_queryset(self):
	        """Return the last five published questions."""
	        return BlogPost.objects.order_by('-pub_date')[:5]
	
	    def get_context_data(self,**kwargs):
	        """Return the last five published questions."""
	        context = super(IndexView, self).get_context_data(**kwargs)
	        context['site'] = Site.objects.first()
	        return context

safe标签 

我们在发布的文章用markdown之后，是一堆乱码一样的 HTML 标签，这些标签本应该在浏览器显示它本身的格式，但是 Django 出于安全方面的考虑，任何的 HTML 代码在 Django 的模板中都会被转义（即显示原始的 HTML 代码，而不是经浏览器渲染后的格式）。为了解除转义，只需在模板标签使用 safe 过滤器即可，告诉 Django，这段文本是安全的，你什么也不用做。

在模板中找到展示博客文章主体的 {{ post.body }} 部分，为其加上 safe 过滤器，{{ post.body|safe }}，这下看到预期效果了。

	class DetailView(generic.DetailView):
	    model = BlogPost
	    template_name = 'timeblog/detail.html'
	
	    def get_context_data(self,**kwargs):
	        """Return the last five published questions."""
	        context = super(DetailView, self).get_context_data(**kwargs)
	        context['site'] = Site.objects.first()
	
	        self.object.content = markdown.markdown( self.object.content,
	                              extensions=[
	                                 'markdown.extensions.extra',
	                                 'markdown.extensions.codehilite',
	                                 'markdown.extensions.toc',
	                              ])
	        obj_name =self.get_context_object_name(self.object)
	        context[obj_name] = self.object
	        return context

### 测试视图

+ Django 测试工具之 Client

Django 提供了一个供测试使用的 Client 来模拟用户和视图层代码的交互。我们能在 tests.py 甚至是 shell 中使用它。

我们依照惯例从 shell 开始，首先我们要做一些在 tests.py 里不是必须的准备工作。第一步是在 shell 中配置测试环境:

	>>> from django.test.utils import setup_test_environment
	>>> setup_test_environment()

setup_test_environment() 提供了一个模板渲染器，允许我们为 responses 添加一些额外的属性，例如 response.context，未安装此 app 无法使用此功能。注意，这个方法并 不会 配置测试数据库，所以接下来的代码将会在当前存在的数据库上运行，输出的内容可能由于数据库内容的不同而不同。如果你的 settings.py 中关于 TIME_ZONE 的设置不对，你可能无法获取到期望的结果。如果你之前忘了设置，在继续之前检查一下。

然后我们需要导入 django.test.TestCase 类（在后续 tests.py 的实例中我们将会使用 django.test.TestCase 类，这个类里包含了自己的 client 实例，所以不需要这一步）:

	>>> from django.test import Client
	>>> # create an instance of the client for our use
	>>> client = Client()
	
	>>> # get a response from '/'
	>>> response = client.get('/')
	Not Found: /
	>>> # we should expect a 404 from that address; if you instead see an
	>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
	>>> # omitted the setup_test_environment() call described earlier.
	>>> response.status_code
	404
	>>> # on the other hand we should expect to find something at '/polls/'
	>>> # we'll use 'reverse()' rather than a hardcoded URL
	>>> from django.urls import reverse
	>>> response = client.get(reverse('polls:index'))
	>>> response.status_code
	200
	>>> response.content
	b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
	>>> response.context['latest_question_list']
	<QuerySet [<Question: What's up?>]>

还是用测试用命test.py写方便，命令行太随意了

	python manage.py test timeblog

timeblog 为应用名称
	
	# test.py
	from django.test import TestCase
	from django.test import Client
	from django.urls import reverse
	
	client = Client()
	# Create your tests here.
	class IndexViewTests(TestCase):
	    def test_no_site(self):
	        """
	        If no questions exist, an appropriate message is displayed.
	        """
	        response = self.client.get(reverse('timeblog:side'))
	        self.assertEqual(response.status_code, 200)
	        print(response.context)


参考：

1. [Django - - - -视图层之视图函数(views)](https://www.cnblogs.com/huchong/p/7718393.html)
2. [http://www.360doc.com/content/18/1003/16/13328254_791631195.shtml](http://www.360doc.com/content/18/1003/16/13328254_791631195.shtml)
3. [Django视图系统(view)](https://www.cnblogs.com/dong-/p/9763236.html)
4. [https://code.ziqiangxuetang.com/django/django-generic-views.html](https://code.ziqiangxuetang.com/django/django-generic-views.html)

