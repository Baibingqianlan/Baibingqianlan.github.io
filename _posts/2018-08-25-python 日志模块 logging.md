---
layout: post
---

### 1.logging基本类说明

+ Loggers 类，提供实际应用中的直接调用接口
+ Handlers 类，将日志内容送到合适的地方，如控制台，文件等
+ Filters 类，提供过滤比日志级别更细致的过滤，如从内容字段等.
+ Formatters 类，提供输出的格式.


		import logging

		# 创建一个logger
		logger = logging.getLogger('simple_example')
		logger.setLevel(logging.DEBUG) #最低的日志级别，大于此级别的都记录，下同
	
		# 创建一个handler，用于写入日志文件
		fh = logging.FileHandler('spam.log')
		fh.setLevel(logging.DEBUG)
		
		 # 再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.ERROR)
		
		# 定义handler的输出格式
		formatter = logging.Formatter(
			'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		ch.setFormatter(formatter)
		fh.setFormatter(formatter)
		
		# 给logger添加handler
		logger.addHandler(ch)
		logger.addHandler(fh)
		
		# 记录日志
		logger.debug('debug message')
		logger.info('info message')
		logger.warn('warn message')
		logger.error('error message')
		logger.critical('critical message')

### 2.日志的级别

日志的级别：

	Level	Numeric value
	CRITICAL	50
	ERROR		40
	WARNING		30
	INFO		20
	DEBUG		10
	NOTSET		0

### 3.日志格式

默认是：'%(message)s'

有两种格式化方式：

+ {}类型，三种特殊的标志: '!s' 代表求值后调用 str(), '!r' 调用 repr()，'!a' 调用ascii().

		"First, thou shalt count to {0}"  # References first positional argument
		"Bring me a {}"                   # Implicitly references the first positional argument
		"From {} to {}"                   # Same as "From {0} to {1}"
		"My quest is {name}"              # References keyword argument 'name'
		"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
		"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

		"Harold's a clever {0!s}"        # Calls str() on the argument first
		"Bring out the holy {name!r}"    # Calls repr() on the argument first
		"More {!a}"                      # Calls ascii() on the argument first
	
		示例：
		>>"The sum of 1 + 2 is {0}".format(1+2)
		'The sum of 1 + 2 is 3'


+ 模板

		>>> from string import Template
		>>> s = Template('$who likes $what')
		>>> s.substitute(who='tim', what='kung pao')
		'tim likes kung pao'
		>>> d = dict(who='tim')
		>>> Template('Give $who $100').substitute(d)
		Traceback (most recent call last):
		...
		ValueError: Invalid placeholder in string: line 1, col 11
		>>> Template('$who likes $what').substitute(d)
		Traceback (most recent call last):
		...
		KeyError: 'what'
		>>> Template('$who likes $what').safe_substitute(d)
		'tim likes $what'

所有可用的属性字段：
![](https://images0.cnblogs.com/blog/282719/201310/07155407-7d1416d0262e4fbab4e376c047aab8a6.jpg)






参考：

2. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
3. [python标准日志模块logging及日志系统设计](https://www.cnblogs.com/goodhacker/p/3355660.html)
