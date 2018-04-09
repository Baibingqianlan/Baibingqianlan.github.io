---
layout: post
---

## 1.OSG系列化数据

+ **osg 自定义类（从原节点继承的），可以系列化成原生的文件格式如osg,ive,osgt,osgb,osgx**
> 
测试了一下wrapper自己的类，结果表明，只能系列化成osgt,osgb,osgx格式之一，才可以保存到文件中，其它两种不可以。猜测可以是只有二代系列化可以支持。
自定义系列化`ADD_USER_SERIALIZER`，只需要写三个静态函数来进行流中数据的读写，就可实现。

+ **setUserValue函数设置的值，也可以保存到文件中。缺点是，太多属性时太繁琐。**

+ OSG的分页加载注意几个点：子节点文件名，显示方式（距离还是相素），注册到osgDB,设置距离或相素数。加载的数据精度好像只有6位有效数字（FLOAT），还不清楚在哪设置为DOUBLE。


参考：

1. [OSG Saving and Loading Files](http://osg3.readthedocs.io/en/latest/ch10.html)

##2.应用程序中数据库与文件的存储选择

对应用程序中存储的选择，通常有数据库与文件两种方式。各有特点，需要分别对待。

数据库：
> 
本身就是一个大型程序，系统稳定，支持多进程多线程，数据分库分表存取，查询方便，支持聚合，合并，分表等标准数据操作。支持备份、日志、灾难恢复、事务管理，安全性高。
少量数据速度快效率高。

文件系统：
> 
支持大数据存储，单次可读数据容量大，效率高。数据查询相对单一，安全性不高，不支持数据备份与灾难恢复。没有事务处理功能，不支持日志。

建议少量数据，安全要求高，需要数据库功能依赖的用数据库；大数据文件，实时性要求高，安全性要求低的，可以文件存取；也可以二者结合起来使用。

##3. osgEarth 资料

osgEarth2.9 编译过程

环境： VS2010 + OSG3.4 + OSGEARTH2.9 + CMAKE

遇到的问题：

1. GDAL库，用命令行编译不过去。原因有个函数返回类型不正确。
2. 用到的库很多：GDAL, GEOS, ZLIB, Protobuffer, rocksdb, gflags等。每一种都有自己的特长。
3. google flags,命令行解析与配置工具。[google gflags 库完全使用](https://blog.csdn.net/jcjc918/article/details/50876613)， [gflags下载](http://gflags.github.io/gflags/#download)

4. RocksDB 是一个来自 facebook 的可嵌入式的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，但主要目的还是嵌入式。RocksDB 基于 LevelDB 构建。可以不用管
5. protobuf的版本，最新的不支持，试了好几个，都在osgEarthFeatures编译失败，最后找protobuf－2.6.1才成功。



参考：

1. [OSGEARTH三维地形开源项目](https://www.cnblogs.com/rainbow70626/p/5575797.html)
2. [osgEarth - a C++ Geospatial SDK](http://docs.osgearth.org/en/latest/)
3. [osgEarth2.7+vs2010+win7编译方法](http://blog.csdn.net/sunxiaoju/article/details/50396838)


