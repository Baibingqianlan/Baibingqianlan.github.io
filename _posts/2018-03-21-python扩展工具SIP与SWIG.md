---
layout: post
---

## 1.python 扩展包工具 SIP

+ SIP是PYTHON扩展模块生成器，可以用来进行C/C++库绑定。专为PYQT而生，完善支持QT的信号与槽机制。
+ 支持的C++特性比较全。
+ QGIS使用了SIP进行接口封装，如下图：

![QGIS接口]({{site.baseurl}}/assets/2018-03-21/qgis-python.png)

+ 绑定实例应该提供了实现接口。


## 2. swig and c++ and Python

swig 和SIP的功能类似，但是更强大，支持很多中语言之间的转换包装。

+ 只读属性，写在**%immutable** and **%mutable** 之间
>
	class List {
	public:
	...
	%immutable;
	int length;
	%mutable;
	...
	};

or
>
	%immutable List::length;
	...
	class List {
	   ...
	   int length;         // Immutable by above directive
	   ...
	};

+ swig C++ 类中想用其它类成员，默认情况会包装成这种类型的指针，若想定用原来的类可以用 **%naturalvar** 宏
>
	// All List variables will use const List& typemaps
	%naturalvar List;
	// Only Foo::myList will use const List& typemaps
	%naturalvar Foo::myList;
	struct Foo {
  	List myList;
	};
	// All non-primitive types will use const reference typemaps
	%naturalvar;`

+ 默认参数，默认会生成参数个数+1个重载函数，可以用**compactdefaultargs**
>
	%feature("compactdefaultargs") Foo::bar;
	class Foo {
	public:
	    void bar(int x, int y = 3, int z = 4);
	};

+ 操作符重载，可以用**%rename**来解决,eg: operator+()
>%rename(`__add__`) Complex::operator+;
>
>in python you can use '+',因为`__add__`就是‘+’


+ 类扩展，用**%extend**，eg:
> 
	%module vector
	%{
	#include "vector.h"
	%}
> 	
	class Vector {
	public:
		double x,y,z;
		Vector();
		~Vector();
		... bunch of C++ methods ...
		%extend {
			char *__str__() {
				static char temp[256];
				sprintf(temp,"[ %g, %g, %g ]", $self->x,$self->y,$self->z);
				return &temp[0];
			}
		}
	};
 In Python, such a method（`__str__`） would allow us to print the value of an object using the print command. 
> 
 **$self** 相当于C++中的 'this'指针，且只能访问公有成员或函数。
>	
	struct Base {
	  virtual void method(int v) {
	    ...
	  }
	  int value;
	};
	struct Derived : Base {
	};
	%extend Derived {
	  virtual void method(int v) {
	    $self->Base::method(v); // akin to this->Base::method(v);
	    $self->value = v;       // akin to this->value = v;
	    ...
	  }
	}

+ 模板，用**%template**
> 
	/* Instantiate a few different versions of the template */
	%template(intList) List<int>;
	%template(doubleList) List<double>;

+ STL/C++ Library, 智能指针
> 
The following table shows which C++ classes are supported and the equivalent SWIG interface library file for the C++ library. 

	C++ class 	C++ Library file SWIG Interface library file 
	std::auto_ptr 	memory 		std_auto_ptr.i 
	std::deque 		deque 		std_deque.i 
	std::list 		list 		std_list.i 
	std::map 		map 		std_map.i 
	std::pair 		utility 	std_pair.i 
	std::set 		set 		std_set.i 
	std::string 	string 		std_string.i 
	std::vector 	vector 		std_vector.i 
	std::shared_ptr shared_ptr 	std_shared_ptr.i 


> eg:
> 
	module example
	%include "std_string.i"
	std::string foo();
	void        bar(const std::string &x);

> eg:
> 
	%module example
	%{
	#include "example.h"
	%}	
	%include "std_vector.i"
	// Instantiate templates used by example
	namespace std {
	   %template(IntVector) vector<int>;
	   %template(DoubleVector) vector<double>;
	}	
	// Include the header file with above prototypes
	%include "example.h"

> eg: boost/shared_ptr
> 
	%module example
	%include <boost_shared_ptr.i>
	%shared_ptr(IntValue)
>	
	%inline %{
	#include <boost/shared_ptr.hpp>
>	
	struct IntValue {
	  int value;
	  IntValue(int v) : value(v) {}
	};
>	
	static int extractValue(const IntValue &t) {
	  return t.value;
	}
>	
	static int extractValueSmart(boost::shared_ptr<IntValue> t) {
	  return t->value;
	}
	%}

参考：

1. [What is SIP?](https://pypi.python.org/pypi/SIP)
2. [ python/c++接口库比较（SWIG，boost.python, pycxx, py++, sip, Weave, Pyrex ）]( https://blog.csdn.net/LaineGates/article/details/19565823)
3. [SIP官网](https://www.riverbankcomputing.com/software/sip/intro)
4. [用Boost.Python将C++代码封装为Python模块](https://www.cnblogs.com/xuyuan77/p/8419482.html)
5. [用c++和python写GUI程序（python嵌入方式）](https://www.cnblogs.com/Shiren-Y/archive/2011/04/05/2005832.html)
