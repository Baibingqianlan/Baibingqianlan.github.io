---
layout: post
---

### Min-in类
Mix-in类，中文称为混合类、混搭类，可用于多重继承，使逻辑清楚。Mix-in类类只实现单个小功能，只定义了其它类可能需要的一套附加方法，而不定义自己的实例属性，不要求使用者调用其`__init__`构造器。

只在Mix-in类制作工具类时，使用多重继承，可以使单个小功能，构成复杂功能。达到增加一些额外功能，又避免复杂的继承层次结构污染代码。

java, C++可以通过定义接口类，来实现同样的功能。

Mix-in 技术按一下规则来限制多重继承：

+ 继承用单一继承；
+ 第二个及两个以上的父类必须是 Mix-in 的抽象类
+ 不能单独生成实例，属于抽象类。

### 类继承用super,初始化父类

在子类里调用`__init__`构造器的顺序是不固定的，优其在多继承时有顺序要求时，这点更重要。

用super初始化父类，可以保证类以MRO(method resolution order)标准的顺序来初始化类，如深度优先，从左至右，同时保证公共基类的`__init__`方法，只执行一次。

MRO顺序，可以用**mro**的类方法来查询。








参考：

2. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
3. [学习Python：Mix-in技术介绍](https://blog.csdn.net/piaoyidage/article/details/41985061)
4. [Mix-in 类](https://blog.csdn.net/rommi/article/details/51067757)
5. [python学习笔记-多重继承和Mixin](https://segmentfault.com/a/1190000007985656)

