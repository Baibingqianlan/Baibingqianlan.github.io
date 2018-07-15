---
layout: post
---

## 1.SQLAlchemy 

SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射（ORM）进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。使用MIT许可证发行。

![SQLAlchemy](https://images2015.cnblogs.com/blog/952555/201607/952555-20160729110817044-661804168.jpg)

SQLAlchemy本身无法操作数据库，其必须以来pymsql等第三方插件，Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作。底层使用 Engine/ConnectionPooling/Dialect 进行数据库操作，Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。如：

	
	MySQL-Python
	    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
	  
	pymysql
	    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
	  
	MySQL-Connector
	    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
	  
	cx_Oracle
	    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]

  
	更多详见：http://docs.sqlalchemy.org/en/latest/dialects/index.html

	*Engine*:
	from sqlalchemy import create_engine
	
	#创建引擎
	engine = create_engine("mysql+pymysql://fuzj:123123@127.0.0.1:3306/fuzj", max_overflow=5)
	#执行sql语句
	engine.execute("INSERT INTO user (name) VALUES ('dadadadad')")
	
	result = engine.execute('select * from user')
	res = result.fetchall()
	print(res)

在构建在 WSGI 规范上的下一代 Python Web 框架中得到了广泛应用，它是由 Mike Bayer 和他的核心开发人员团队开发的一个单独的项目。使用 SQLAlchemy等独立 ORM 的一个优势就是它允许开发人员首先考虑数据模型，并能决定稍后可视化数据的方式（采用命令行工具、Web 框架还是 GUI 框架）。这与先决定使用 Web 框架或 GUI 框架，然后再决定如何在框架允许的范围内使用数据模型的开发方法极为不同。

	ORM解决中文编码问题 sqlalchemy 默认使用latin-1进行编码。所以当出现中文时就会报如下错误：

	UnicodeEncodeError: 'latin-1' codec can't encode characters in position 39-41: ordinal not in range(256)
	 
	解决方法：
	在连接数据库的时候直接指定字符编码：
	
	#engine = create_engine("mysql+pymysql://fuzj:123.com@127.0.0.1:3306/fuzj?charset=utf8", max_overflow=5,encoding='utf-8')

使用`__repr__`定义返回的数据

	class User(Base):
	    __tablename__ = 'user'
	    nid = Column(Integer,primary_key=True,autoincrement=True)
	    name = Column(String(10),nullable=False)
	    role = Column(Integer,ForeignKey('role.rid'))
	    group = relationship("Role",backref='uuu')    #Role为类名
	
	    def __repr__(self):
	        output = "(%s,%s,%s)" %(self.nid,self.name,self.role)
	        return output
	        
	res = session.query(User).all()
	print(res)
	
	输出：
	[(1,fuzj,1), (2,jie,2), (3,张三,2), (4,李四,1), (5,王五,3)]



## 2.对象关系映射器（Object Relational Mappers，ORM）
ORM 全称 Object Relational Mapping, 翻译过来叫对象关系映射。简单的说，ORM 将数据库中的表与面向对象语言中的类建立了一种对应关系。这样，我们要操作数据库，数据库中的表或者表中的一条记录就可以直接通过操作类或者类实例来完成。


对象关系映射（英语：Object Relational Mapping，简称ORM，或O/RM，或O/R mapping），是一种程序技术，用于实现面向对象编程语言里不同类型系统的数据之间的转换。从效果上说，它其实是创建了一个可在编程语言里使用的“虚拟对象数据库”。
面向对象是从软件工程基本原则（如耦合、聚合、封装）的基础上发展起来的，而关系数据库则是从数学理论发展而来的，两套理论存在显著的区别。为了解决这个不匹配的现象，对象关系映射技术应运而生。

对象关系映射（Object-Relational Mapping）提供了概念性的、易于理解的模型化数据的方法。

ORM方法论基于三个核心原则： 简单：以最基本的形式建模数据。 传达性：数据库结构被任何人都能理解的语言文档化。 精确性：基于数据模型创建正确标准化的结构。 典型地，建模者通过收集来自那些熟悉应用程序但不熟练的数据建模者的人的信息开发信息模型。建模者必须能够用非技术企业专家可以理解的术语在概念层次上与数据结构进行通讯。建模者也必须能以简单的单元分析信息，对样本数据进行处理。ORM专门被设计为改进这种联系。

一般的ORM包括以下四部分：
一个对持久类对象进行CRUD操作的API；
一个语言或API用来规定与类和类属性相关的查询；
一个规定MAPPING METADATA的工具；
一种技术可以让ORM的实现同事务对象一起进行DIRTYCHECKING, LAZY ASSOCIATION FETCHING以及其他的优化操作。

### 产品

**JAVA系列**：

	APACHE OJB
	CAYENNE
	JAXOR
	**HIBERNATE**
	IBATIS
	JRELATIONALFRAMEWORK
	SMYLE
	TOPLINK

其中 TOPLINK 是 ORACLE 的商业产品，其他均为开源项目。

**.NET系列**：

	ENTITYSCODEGENERATE
	LINQ TOSQL （.NET FRAMEWORK 3.5）
	GROVE
	RUNGOO.ENTERPRISEORM
	FIRECODE CREATOR
	MYGENERATION
	CODESMITH PRO
	CODEAUTO ...

### 映射模式
从《公共仓库元模型：开发指南》一书第8章CWM元仓库中摘录出来的内容：

采用方法：将UML模型中的各种元素通过转换，保存为数据库模式。由于CWM是一种元模型，因此模型的实例也是一种模型，将这种实例以数据库数据的形式保存。使用数据库中比较成熟的存储过程技术提高开发和执行效率。

1、 数据类型映射模式

	1.1简单数据类型模式：建立UML和关系型数据库中简单数据类型的映射表以指导映射。
	
	1.2枚举数据类型模式：每种枚举类型对应一个表，只有一个列(_ENUMLITERAL)表示枚举值。
	
	1.3基于类的数据类型模式：使用外键约束，将基础列与基于类的类型实例相关联。

2、类映射模型

每个类对应一个表。单值属性、多值属性、继承关系可以用下述方法映射，而引用属性将在关联映射模式中提到。

	2.1单值属性模式：是CARDINALITY的上界为1的属性，映射到类所对应的表的列上。若其下界也为1（必须有的属性），列属性为NOT NULL。
	
	2.2多值属性模式：每个多值属性映射成一个独立的表，使用外键连接到类所对应的表上。
	
	2.3继承模式：每加入一个类的实例时，根据其继承关系自顶向下生成每个类的对象，这些对象具有相同的ID（根对象对应记录的主键）。删除对象实例时，自底向上删除数据。遇到从中间删的情况怎么办？多重继承怎么处理？

3、关联映射模式

	3.1一对一关联模式：在关联两端各加一列。
	3.2一对多关联模式：和3.1一样。如果多这端是有序的，还需加入一列表示序号。
	3.3多对多关联模式：将关联单独作一个表。
	3.4组合关联模式：注意级联式删除。
	3.5反演关联模式：关联两端指向相关的类型，和普通关联一样。
	3.6成对关联模式：关联记录两个类间的关系，用交集类表示关联，表示成一个单独的表，每个关联对应一个表，用外键表示它们间的关系。
	3.7关联上的OCL需要分析成对应的存储过程代码。
	3.8保证关联的CARDINALITY也需要分析成对应的存储过程代码。

4、引用映射模式

在UML中不存在的MOF特征，指属性是声明为引用类型的实例。用存储过程实现。
OPERATIONAL RISK MANAGEMENT

## 3.faker库
	
	from faker import Faker
	
	f=Faker(locale='zh_CN')
	f.name()  #生成姓名
	f.address() #生成地址

ssn()：生成身份证号

chrome()：随机生成Chrome的浏览器user_agent信息

firefox()：随机生成FireFox的浏览器user_agent信息

internet_explorer()：随机生成IE的浏览器user_agent信息

opera()：随机生成Opera的浏览器user_agent信息

safari()：随机生成Safari的浏览器user_agent信息

linux_platform_token()：随机Linux信息

user_agent()：随机user_agent信息

url()：随机URL地址

geo_coordinate()：地理坐标

latitude()：地理坐标(纬度)

longitude()：地理坐标(经度)



参考：

1. [SQLAlchemy](https://baike.baidu.com/item/SQLAlchemy/1269830)
2. [Web前端技术栈](https://blog.csdn.net/yongxiaokang1/article/details/49175311)
3. [python对Mysql操作和使用ORM框架（SQLAlchemy）](https://www.cnblogs.com/pycode/p/mysql-orm.html)
4. [SQLAlchemy 教程 —— 基础入门篇](https://www.cnblogs.com/mrchige/p/6389588.html)
5. [对象关系映射ORM](https://www.cnblogs.com/dirgo/p/5054444.html)
6. [Python Faker的使用(1)](https://www.jianshu.com/p/6bd6869631d9)