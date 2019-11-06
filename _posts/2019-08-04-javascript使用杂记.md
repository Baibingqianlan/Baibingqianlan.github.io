---
layout: post
---

### 1. js对象增加属性与方法

有时，您希望向所有给定类型的已有对象添加新属性（或方法）。

有时，您希望向对象构造器添加新属性（或方法）。

使用 prototype 属性:
JavaScript **prototype** 属性允许您为对象构造器添加新属性：

实例:
	
	function Person(first, last, age, eyecolor) {
	    this.firstName = first;
	    this.lastName = last;
	    this.age = age;
	    this.eyeColor = eyecolor;
	}
	Person.prototype.nationality = "English";
	Person.prototype.name = function() {
	    return this.firstName + " " + this.lastName;
	};
	
	var myFriend = new Person("Bill", "Gates", 62, "blue");
	document.getElementById("demo").innerHTML =
	"My friend is " + myFriend.name(); 


+ ES5 新的对象方法:

####　更改属性值

	语法
	Object.defineProperty(object, property, {value : value})
本例更改了属性值：

	实例
	var person = {
	  firstName: "Bill",
	  lastName : "Gates",
	  language : "EN" 
	};
	
	// 更改属性
	Object.defineProperty(person, "language", {value : "ZH"});

ES5 允许更改以下属性元数据：

	writable : true      // 属性值可修改
	enumerable : true    // 属性可枚举
	configurable : true  // 属性可重新配置
	writable : false     // 属性值不可修改
	enumerable : false   // 属性不可枚举
	configurable : false // 属性不可重新配置
ES5 允许更改 getter 和 setter：

	// 定义 getter
	get: function() { return language }
	// 定义 setter
	set: function(value) { language = value }

此例使语言为只读：

	Object.defineProperty(person, "language", {writable:false});
此例使语言不可枚举：

	Object.defineProperty(person, "language", {enumerable:false});


列出可枚举的属性，此例只列出对象的所有可枚举属性：

	实例
	var person = {
	  firstName: "Bill",
	  lastName : "Gates"
	  language : "EN" 
	};
	
	Object.defineProperty(person, "language", {enumerable:false});
	Object.keys(person);  // 返回可枚举属性的数组


添加属性，此例向对象添加新属性：

	实例
	// 创建对象
	var person = {
	  firstName: "Bill",
	  lastName : "Gates",
	  language : "EN"
	};
	
	// 添加属性
	Object.defineProperty(person, "year", {value:"2008"});

###　２.js面向对象设计之class类

ES6提供了更接近传统语言的写法，引入了Class（类）这个概念，作为对象的模板。通过class关键字，可以定义类．


1、class 写法更加简洁、含义更加明确、代码结构更加清晰。

2、class 尽管也是函数，却无法直接调用（不存在防御性代码了）。

3、class 不存在变量提升。

4、class 为污染 window 等全局变量（这点很赞啊）。

5、class 函数体中的代码始终以严格模式执行（新手写的代码可靠性也必须上来了）

6、可直接使用 set 和 get 函数。这比 function 要好用多了。
据我所知，vue 中的数据绑定是通过 set 和 get 来实现，而这里 class 可以使用便捷的如同普通的函数的写法。
function 中则需要通过 Object.defineProperty 的方式来设置 set 和 get，繁琐且代码可读性差。

	class Class01{
	    constructor() { }
	    get name(){
	        console.log( 'getter' );
	        return this._name;
	    }
	    set name( v ){
	        this._name = v;
	        console.log( 'setter' );
	        return this;
	    }
	}
	var ins01 = new Class01();
	ins01.name; /* getter */
	ins01.name = 2; /* setter */

7、class 内部方法中若涉及到 this，则一定要注意。class 中的 this 永远都不会指向 window。

8、class 可以从 javascript 中著名的几大类中进行继承：Array、number、string....，显然 function 是做不到的。

在一个类中只能有一个名为 “constructor” 的特殊方法。

在一个构造方法中可以使用super关键字来调用一个父类的构造方法

如果没有显式指定构造方法，则会添加默认的 constructor 方法。

	默认构造方法节	
	如前所述，如果不指定构造方法，则使用默认构造函数。对于基类，默认构造函数是：
	
	constructor() {}
	对于派生类，默认构造函数是：
	
	constructor(...args) {
	  super(...args);
	}


extends关键字用来创建一个普通类或者内建对象的子类。继承的.prototype必须是一个Object 或者 null。
下面给一个简单的示例：

	
	class Square extends Polygon {
	  constructor(length) {
	    // Here, it calls the parent class' constructor with lengths
	    // provided for the Polygon's width and height
	    super(length, length);
	    // Note: In derived classes, super() must be called before you
	    // can use 'this'. Leaving this out will cause a reference error.
	    this.name = 'Square';
	  }
	
	  get area() {
	    return this.height * this.width;
	  }
	}

9.类（class）通过 static 关键字定义静态方法。不能在类的实例上调用静态方法，而应该通过类本身调用。

	静态方法调用同一个类中的其他静态方法，可使用 this 关键字。
	
	class StaticMethodCall {
	    static staticMethod() {
	        return 'Static method has been called';
	    }
	    static anotherStaticMethod() {
	        return this.staticMethod() + ' from another static method';
	    }
	}
	StaticMethodCall.staticMethod();
	// 'Static method has been called'

10.let

使用 let 语句声明一个变量，该变量的范围限于声明它的块中。  可以在声明变量时为变量赋值，也可以稍后在脚本中给变量赋值。  

使用 let 声明的变量，在声明前无法使用，否则将会导致错误。

如果未在 let 语句中初始化您的变量，则将自动为其分配 JavaScript 值 undefined


参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [https://www.w3school.com.cn/js/js_object_es5.asp](https://www.w3school.com.cn/js/js_object_es5.asp)
3. [js面向对象设计之class类](https://www.cnblogs.com/ndos/p/8127597.html)
4. [https://developer.mozilla.org/zh-CN/docs/Web/JavaScript](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)
4. [https://googlechrome.github.io/samples/classes-es6/index.html](https://googlechrome.github.io/samples/classes-es6/index.html)

