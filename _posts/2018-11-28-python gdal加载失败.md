---
layout: post
---

### 1.生成 gdal python 加载库

GDAL_HOME/swig/python目录下，运行


	  $ python setup.py build
	  $ python setup.py install

设置环境变量：

1. PATH变量化增加
  
     	C:\gdalwin32-1.7\bin

2. 新建GDAL_DATA变量

	     Name : GDAL_DATA
	     Path : C:\gdalwin32-1.7\data

### 2.加载 gdal python 库 过程中的问题

+ 库加载
		
		import gdal
		import ogr
		import osr
		import gdalnumeric
		import gdalconst

+ 数据加载

		ReadAsArray expects to make an entire copy of a raster band or dataset unless 
		the data are explicitly subsetted as part of the function call. For large 
		data, this approach is expected to be prohibitively memory intensive.
		
		.. _GDAL API Tutorial: http://www.gdal.org/gdal_tutorial.html
		.. _GDAL Windows Binaries: http://gisinternals.com/sdk/
		.. _Microsoft Knowledge Base doc: http://support.microsoft.com/kb/310519
		.. _Python Cheeseshop: http://pypi.python.org/pypi/GDAL/
		.. _val_repl.py: http://trac.osgeo.org/gdal/browser/trunk/gdal/swig/python/samples/val_repl.py
		.. _GDAL: http://www.gdal.org
		.. _SWIG: http://www.swig.org

+ 加载gdalnumeric库失败

我在使用过程中，发现这个库加载失败，跟踪时，发现在下面这句没有返回成功：

 	_mod = imp.load_module('_gdal_array', fp, pathname, description)

后来发现，可能是我编译过程有问题，我电脑上有3个版本的VS: VC6,VS2010,VS2015.动态库是VS2010编的，PYTHON库是默认编译的（VS2015）
。

统一编译器，问题解决。

参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [定义]({{site.baseurl}}/assets/2018-10-16/3.bmp)
3. [https://baike.baidu.com/item/TIFF/2106?fr=aladdin](https://baike.baidu.com/item/TIFF/2106?fr=aladdin)
4. [tiff和geotiff格式分析](https://www.cnblogs.com/arxive/p/6746570.html)
5. [GDAL 综合整理](https://www.xuebuyuan.com/3221812.html)
6. [Python的地形三维可视化Matplotlib和gdal使用实例](https://www.jb51.net/article/130172.htm)
7. [GDAL python教程（4）——用GDAL读取栅格数据【转】](http://blog.sina.com.cn/s/blog_777d52410101qxp3.html)

