---
layout: post
---

### 1.json格式介绍

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。 JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C、C++、C#、Java、JavaScript、Perl、Python等）。这些特性使JSON成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成(一般用于提升网络传输速率)。

JSON是在2001年，由Douglas Crockford创建的，并且被IETF(Internet Engineering Task Force)定义为RFC 4627标准。JSON的媒体类型被定义为 application/json，而文件的后缀为.json。在2005年-2006年正式成为主流的数据格式，雅虎和谷歌就在那时候开始广泛地使用JSON格式。

**与 XML 相同之处**

+ JSON 是纯文本
+ JSON 具有"自我描述性"（人类可读）
+ JSON 具有层级结构（值中存在值）
+ JSON 可通过 JavaScript 进行解析
+ JSON 数据可使用 AJAX 进行传输

**与 XML 不同之处**

+ 没有结束标签
+ 更短
+ 读写的速度更快
+ 能够使用内建的 JavaScript eval() 方法进行解析
+ 使用数组
+ 不使用保留字

**JSON 语法**

+ 数据使用名/值（key/value）对表示。
+ 使用大括号保存对象，每个名称后面跟着一个 ':'（冒号），名/值对使用 ,（逗号）分割。
+ 使用方括号保存数组，数组值使用 ,（逗号）分割。
>	
	{
	    "book": [
	        {
	            "id":"01",
	            "language": "Java",
	            "edition": "third",
	            "author": "Herbert Schildt"
	        },
	        {
	            "id":"07",
	            "language": "C++",
	            "edition": "second"
	            "author": "E.Balagurusamy"
	    }]
	}

JSON 值可以是：

+ 数字（整数或浮点数）
+ 字符串（在双引号中）
+ 逻辑值（true 或 false）
+ 数组（在方括号中）
+ 对象（在花括号中）
+ null

由于 JSON 语法是 JavaScript 语法的子集，JavaScript 函数 eval() 可用于将 JSON 文本转换为 JavaScript 对象。

eval() 函数使用的是 JavaScript 编译器，可解析 JSON 文本，然后生成 JavaScript 对象。必须把文本包围在括号中，这样才能避免语法错误：
  
	var obj = eval ("(" + txt + ")");

 eval() 函数可编译并执行任何 JavaScript 代码。这隐藏了一个潜在的安全问题。**使用 JSON 解析器将 JSON 转换为 JavaScript 对象是更安全的做法。**JSON 解析器只能识别 JSON 文本，而不会编译脚本。

### 2.MYSQL中对json的支持

从MySQL5.7.8开始，Mysql提供了一个原生的Json类型，Json值将不再以字符串的形式存储，而是采用二进制（internal binary）格式，每次读写都会自动校验，大大提高了效率。

 创建带JSON类型的表格：

	CREATE TABLE table_name (
	    id INT NOT NULL AUTO_INCREMENT, 
	    json_col JSON,
	    PRIMARY KEY(id)
	);

插入JSON格式的数据到表格中：

	INSERT INTO
	    table_name (json_col) 
	VALUES
	    ('{"City": "Galle", "Description": "Best damn city in the world"}');

MySQL5.7.8 还提供了一些基于Json的函数，包括：

	JSON_ARRAY 生成json数组
	JSON_OBJECT 生成json对象
	JSON_QUOTE 加"号
	JSON_CONTAINS 指定数据是否存在
	JSON_CONTAINS_PATH 指定路径是否存在
	JSON_EXTRACT 查找所有指定数据
	JSON_KEYS 查找所有指定键值
	JSON_SEARCH 查找所有指定值的位置
	JSON_ARRAY_APPEND  指定位置追加数组元素
	JSON_ARRAY_INSERT 指定位置插入数组元素
	JSON_INSERT 指定位置插入
	JSON_REPLACE 指定位置替换
	JSON_SET 指定位置设置
	JSON_MERGE 合并
	JSON_REMOVE 指定位置移除
	JSON_UNQUOTE 去"号
	JSON_DEPTH 深度
	JSON_LENGTH 长度
	JSON_TYPE 类型
	JSON_VALID 是否有效json格式



参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [定义]({{site.baseurl}}/assets/2018-10-16/3.bmp)
3. [https://www.w3cschool.cn/json/](https://www.w3cschool.cn/json/)
4. [https://vimsky.com/article/3213.html](https://vimsky.com/article/3213.html)
5. [https://www.cnblogs.com/ooo0/p/9309277.html](https://www.cnblogs.com/ooo0/p/9309277.html)

