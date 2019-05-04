---
layout: post
---

### 1.filter()

filter(function, iterable)

高阶函数，可以用来过滤能迭代的对象。关键是可以定制自己的过滤函数。返回一个迭代对象（python3.x）

	import math
	def is_sqr(x):
	    return math.sqrt(x) % 1 == 0
	 
	tmplist = filter(is_sqr, range(1, 101))
	newlist = list(tmplist)
	print(newlist)

	输出结果 ：
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

### 2.高阶函数

一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

函数名也是变量，即函数是一个对象。函数式编程就是指这种高度抽象的编程范式。

	def add(x, y, f):
	    return f(x) + f(y)


	当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，
	根据函数定义，我们可以推导计算过程为：
	
	x ==> -5
	y ==> 6
	f ==> abs
	f(x) + f(y) ==> abs(-5) + abs(6) ==> 11

### 3.函数式编程

函数式编程中最古老的例子莫过于1958年被创造出来的LISP了，透过 LISP，可以用精简的人力。较现代的例子包括Haskell、Clean、Erlang和Miranda等。

函数编程支持函数作为第一类对象，有时称为**闭包**或者**仿函数（functor）**对象。实质上，闭包是起函数的作用并可以像对象一样操作的对象。


优点：

+ 代码简洁，开发快速
+ 接近自然语言，易于理解
+ 更方便的代码管理

	函数式编程不依赖、也不会改变外界的状态，只要给定输入参数，返回的结果必定相同。因此，每一个函数都可以被看做独立单元，很有利于进行单元测试（unit testing）和除错（debugging），以及模块化组合。

+ 易于"并发编程"
	
	函数式编程不需要考虑"死锁"（deadlock），因为它不修改变量，所以根本不存在"锁"线程的问题。不必担心一个线程的数据，被另一个线程修改，所以可以很放心地把工作分摊到多个线程，部署"并发编程"（concurrency）

+ 代码的热升级

缺点：

+ 函数式编程常被认为严重耗费在CPU和存储器资源


### 4.编程范式

编程语言主要有三种类型：

1. 命令式编程（Imperative Programming）: 专注于”如何去做”，这样不管”做什么”，都会按照你的命令去做。解决某一问题的具体算法实现。
2. 函数式编程（Functional Programming）：把运算过程尽量写成一系列嵌套的函数调用。
3. 逻辑式编程（Logical Programming）：它设定答案须符合的规则来解决问题，而非设定步骤来解决问题。过程是事实+规则=结果


### 5.闭包

要理解闭包，首先要理解python的变量作用域。

python语言中形成闭包的三个条件，缺一不可：

1. 必须有一个内嵌函数(函数里定义的函数）——这对应函数之间的嵌套
2. 内嵌函数必须引用一个定义在闭合范围内(外部函数里)的变量——内部函数引用外部变量
3. 外部函数必须返回内嵌函数——必须返回那个内部函数




参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [Python3 filter() 函数) 入门篇](http://www.runoob.com/python3/python3-func-filter.html)
3. [高阶函数](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819873910807d8c322ca74d269c9f80f747330a52000)
4. [函数式编程](https://baike.baidu.com/item/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B/4035031?fr=aladdin)
5. [函数式编程介绍](https://blog.csdn.net/u013007900/article/details/79104110)
6. [什么是闭包？闭包的优缺点？](https://www.cnblogs.com/cxying93/p/6103375.html)
7. [Python中的闭包](https://www.cnblogs.com/Khannia/p/6220384.html)
