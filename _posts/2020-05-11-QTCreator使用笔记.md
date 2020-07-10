---
layout: post
---

使用QT编译WINDOWS上的动态库，有诸多坑要踩：

### 1. 配置环境

可以用QTCREATOR自己带的编译环境检测，也可以配置其它版本QT的编译环境。

**Qtcreator中选择Qtversion时总是提示qmake没有被正确安装**

配置其它版本QT环境时，要在bin目录下加入qt.conf的配置文件，内容如下：

	[Paths]
	Prefix = /some/path
	Plugins=plugins
	Translations = i18n

说明：

	项					默认值
	Prefix				QCoreApplication::applicationDirPath()
	Documentation		doc
	Headers				include
	Libraries			lib
	Binaries			bin
	Plugins				plugins
	Data				.
	Translations		translations
	Settings			.
	Examples			.
	Demos				.

Prefix应该是一个绝对路径（也可以用相对路径），其他的设定都是相对于Prefix的相对路径。
在这个文件里还可以给不同版本的Qt设定不同Paths， 方法是使用Paths/x.y.z的形式， 这里的x是主版本号，y是次版本号，z是补丁级别号， 如：
	
	Paths
	Paths/4
	Paths/4.1
	Paths/4.2.5

其中的y和z可以忽略，并且系统会选择版本上最接近的设定，如Qt4.5这里会匹配Paths/4.2.5. 而在找不到匹配的版本号时，会使用Paths的设定， 如Qt5.0匹配Paths。

**加载插件plugins时一定要加上子目录。例如：支持图片显示的插件必须放到/plugins/imageformats里面，否则不能显示图片**

### 2. 工程配置

qt使用QMAKE进行编译，QMAKE的作用生成相应平台的MAKEFILE文件，最后进行编译。这也是QT跨平台的原因。

#### 2.1 qmake典型语法：

+ 获取内建变量、内建属性和环境变量的值

**自定义变量**：
	
	MYVAR1 = test
	MYVAR2 = "test t"
 
**取变量值使用：$$...**

	message($$MYVAR1)             #自定义变量
	message($$PWD)                #内建变量
	message($$QMAKE_DIR_SEP)      #内建变量标记正反斜杠
 
**取属性值使用$$[...]**

	message($$[QT_INSTALL_BINS])  #内建属性
	message($$[QT_INSTALL_QML])   #内建属性
 
**取系统环境变量：**

	message($$(QTDIR))            #取环境变量为QTDIR的值
	message($$(windir))           #取环境变量为windir的值

+ 常用变量

**PWD**
本变量指定指向当前文件被解析的目录的全路径。为了支持影子构建，编写工程文件时在源码树引用文件时会有用。

**OUT_PWD**
本变量包含指向生成MakeFile文件的目录的全路径

**QT**
变量中存储的值用于控制工程中使用的Qt模块。

	core：默认包含，QtCore模块
	gui：默认包含，QtGui模块
	network：QtNetwork模块
	opengl：QtOpenGl模块
	phonon：Phonon多媒体框架
	sql：QtSql模块
	svg：QtSvg模块
	xml：QtXml模块
	webkit：QtWebkit模块
默认，QT包含core和gui模块，在没有进一步配置的情况下确保构建一个GUI应用程序。
如果想要构建一个没有QtGui模块的工程，需要使用“-=”将gui排除。如：
QT -= gui # Only the core module is used

**QTPLUGIN**
本变量包含静态插件的名字列表

**QT_VERSION**
本变量包含当前Qt的版本

**RESOURCES**
本变量包含资源集合文件的名称（qrc）

**SUBDIRS**
此变量与subdirs模板一起使用时，指定包含需要构建的工程部分的所有子目录或工程文件的名称。使用此变量指定的每个子目录必须包含其自己的工程文件（.pro）。

+ 生成目标类型：

TARGET = app

	app－－可执行程序
	lib－－库



+ 生成目录

DESTDIR = $$PWD/../bin

+ 预编译头 
 
PRECOMPILED_HEADER = stdafx.h


+ 源文件

		HEADERS += mainwindow.h \
			 paintwidget.h
		SOURCES += main.cpp mainwindow.cpp \
		          paintwidget.cpp

+ 三方库，头文件，库目录
	
		# 包含目录
		INCLUDEPATH += $$(SUBDIR)
		# －L表示库目录，－l表示链接到的具体库文件
		LIBS += -L/usr/local/lib \
				-lmath

+ Debug，Release配置

		CONFIG(debug,debug|release):{
			TargetFile = $$TargetFile/debug/$$TARGET".exe"	
			...
		}
		
		CONFIG(release,debug|release):{
			TargetFile = $$TargetFile/release/$$TARGET".exe"
			...
		}


#### 2.2 使用三方库

+ 对于使用BOOST的处理：

QT与BOOST有定义上的冲突，所以使用QT进行编译时，在头文件的BOOST头文件包含中要加上

	#ifndef Q_MOC_RUN
	
		#include <boost/..>
		…

	#endif


moc 全称是 Meta-Object Compiler，也就是“元对象编译器”。Qt 程序在交由标准编译器编译之前，先要使用 moc 分析 C++ 源文件。如果它发现在一个头文件中包含了宏 Q_OBJECT，则会生成另外一个 C++ 源文件。这个源文件中包含了 Q_OBJECT 宏的实现代码。这个新的文件名字将会是原文件名前面加上 moc_ 构成。这个新的文件同样将进入编译系统，最终被链接到二进制代码中去。

+ Q_ENUM宏

使用Q_ENUM注册过的枚举类型，可以不加修饰直接被qDebug()打印出来，另外通过静态函数QMetaEnum::fromType()可以获得一个QMetaEnum 对象，以此作为中介，能够轻松完成枚举量和字符串之间的相互转化。

	#include <QObject>
	#include <QDebug>
	#include <QMetaEnum>
	
	class TestEnum : public QObject
	{
	    Q_OBJECT
	public:
	    explicit TestEnum(QObject *parent = nullptr);
	
	    enum Level{
	        first, second, third};
	    Q_ENUM(Level)
	    Q_DECLARE_FLAGS(LevelesFlags, Level)
	
	    void OutPut()
	    {
	        qDebug()<< first;
	        QMetaEnum m = QMetaEnum::fromType<TestEnum::Level>();  //since Qt5.5
	        qDebug()<< m.name() << ": " << m.key(2);
	    }
	
	signals:
	
	};

输出是

	TestEnum::first
	Level :  third



参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [我的GITHUB](https://baibingqianlan.github.io/)
3. [Qt中的枚举变量,Q_ENUM,Q_FLAG,Q_NAMESPACE,Q_ENUM_NS,Q_FLAG_NS以及其他](https://blog.csdn.net/qq_36179504/article/details/100895133?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase)
4. [https://www.cnblogs.com/iriczhao/p/11274598.html](https://www.cnblogs.com/iriczhao/p/11274598.html)
5. [https://blog.csdn.net/qq_37309849/article/details/88848802](https://blog.csdn.net/qq_37309849/article/details/88848802)

