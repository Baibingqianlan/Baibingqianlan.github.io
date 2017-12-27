---
layout: post
---

## python and c++ integration ##

reference:

> - [c++中嵌入python](https://www.cnblogs.com/earvin/p/5423868.html)

> 1. [Python实例浅谈之三Python与C/C++相互调用](http://blog.csdn.net/taiyang1987912/article/details/44779719)

> 1. [FFPYTHON Github项目地址：https://github.com/fanchy/ffpython](https://www.cnblogs.com/zhiranok/archive/2013/05/09/ffpython_cn.html)

1. C++代码可以用**SWIG库**、**Boost.Python库**转为PYTHON代码

2. C++如何与PYTHON同时修改同一个内存？

	参考QGIS调用PYTHON的代码，初始化时初始化了PYTHON解释器，再执行接口初始化。

3. 怎样将一个C++对象传递到PYTHON中

	 很多办法都可以 如果你的c++对象是已有的代码，可以用cpython包装成Python对象，这些cpython包装的对象有一个指针是指向你要包装的c++对象的，然后提供访问c++对象的方法。比如你一颗树可以包装成Python对象，树节点也包装成Python对象，只要是复杂一点的c++对象都可以包装成Python对象。如果c++部分的代码还没写，可以用cython直接来写，这样自动扩展成Python模块，这样的模块通常是对性能要求很高的才需要专门用c扩展也可以用Python自带的ctypes模块直接定义c++  对象，这种对象是可以直接导到Python使用的。

	方法二：消息传递，如JSON格式的消息
	[http://blog.csdn.net/szchtx/article/details/22320671](http://blog.csdn.net/szchtx/article/details/22320671)



