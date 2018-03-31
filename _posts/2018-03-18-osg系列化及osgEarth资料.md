---
layout: post
---

## 1.OSG系列化数据

+ **osg 自定义类（从原节点继承的），可以系列化成原生的文件格式如osg,ive,osgt,osgb,osgx**


	测试了一下wrapper自己的类，结果表明，只能系列化成osgt,osgb,osgx格式之一，才可以保存到文件中，其它两种不可以。猜测可以是只有二代系列化可以支持。

	自定义插件暂未测试

+ **setUserValue函数设置的值，也可以保存到文件中。缺点是，太多属性时太繁琐。**

参考：

1. [OSG Saving and Loading Files](http://osg3.readthedocs.io/en/latest/ch10.html)


## osgEarth 资料

osgEarth2.9 编译过程

环境： VS2010 + OSG3.4 + OSGEARTH2.9 + CMAKE

遇到的问题：

1. GDAL库，用命令行编译不过去。原因有个函数返回类型不正确。
2. 用到的库很多：GDAL, GEOS, ZLIB, Protobuffer, rocksdb, gflags等。每一种都有自己的特长。
3. google flags,命令行解析与配置工具。[google gflags 库完全使用](https://blog.csdn.net/jcjc918/article/details/50876613)， [gflags下载](http://gflags.github.io/gflags/#download)

4. RocksDB 是一个来自 facebook 的可嵌入式的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，但主要目的还是嵌入式。RocksDB 基于 LevelDB 构建。
5. protobuf的版本，最新的不支持，试了好几个，都在osgEarthFeatures编译失败，最后找protobuf－2.6.1才成功。



参考：

1. [OSGEARTH三维地形开源项目](https://www.cnblogs.com/rainbow70626/p/5575797.html)
2. [osgEarth - a C++ Geospatial SDK](http://docs.osgearth.org/en/latest/)
3. [osgEarth2.7+vs2010+win7编译方法](http://blog.csdn.net/sunxiaoju/article/details/50396838)


