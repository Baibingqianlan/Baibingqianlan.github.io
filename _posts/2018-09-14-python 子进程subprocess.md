---
layout: post
---

python与系统交互，可以用命令行工具，但是命令行中的越写会越复杂，且多子进程的管理太麻烦，可以用subprocess模块来处理。此外也有其它运行子进程的方式，如popen、popen2、os.exex*等，在此只说subprocess。

### 1.subprocess模块常用函数

subprocess可以生成子进程，可以连接管道，将标准输入输出串在一起，方便使用。

+ **run**(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, env=None)

可以用来运行命令行，返回子进程实例。3.5版本开始加入，旧版本用call().
返回值是一个subprocess.CompletedProcess。

args,用一个列表，输入参数

window系统，要加shell参数，才能运行命令行。输出时编码格式要正确。


    c = subprocess.run(['dir'], shell = True, stdout=subprocess.PIPE)
    out = str(c.stdout, encoding='gb2312' )
    print(out)

	 驱动器 D 中的卷没有标签。
	 卷的序列号是 A66A-075E
	
	 D:\MyDocuments\python_works\untitled 的目录
	
	2018/09/14  22:05    <DIR>          .
	2018/09/14  22:05    <DIR>          ..
	2018/09/14  22:03    <DIR>          .idea
	2018/09/01  21:54             1,143 propertyBindTest.py
	2018/08/31  22:24             1,200 serialize.py
	2018/09/14  22:05               197 subprocessTest.py
               3 个文件          2,540 字节
               3 个目录 37,198,790,656 可用字节

+ Popen 构造器

Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None)

为了方便使用，可以用**Popen 构造器**来启动进程。

	with subprocess.Popen(["dir"], shell = True, stdout=subprocess.PIPE) as proc:
	        print(proc.stdout.read().decode('gb2312' ))


+ Popen实例函数

1.Popen.poll()，检查子进程是否终止。返回None,表示进程未终止。

2.Popen.wait(timeout=None)

3.Popen.communicate(input=None, timeout=None)，返回元组
(stdout_data, stderr_data). 

	用于与子进程交互，input用来输入数据，如果流用文本模式打开，则输入字符串，否则输入数据为字节流。

4.Popen.send_signal(signal)，发送信号给子进程

5.Popen.terminate()、Popen.kill()，终止进程

	proc = subprocess.Popen(...)
	try:
	    outs, errs = proc.communicate(timeout=15)
	except TimeoutExpired:
	    proc.kill()
	    outs, errs = proc.communicate()

+ 经典命令行调用方式

不考虑安全与异常

1.subprocess.getstatusoutput(cmd)，返回 (exitcode, output).

	>>> subprocess.getstatusoutput('ls /bin/ls')
	(0, '/bin/ls')
	>>> subprocess.getstatusoutput('cat /bin/junk')
	(1, 'cat: /bin/junk: No such file or directory')

2.subprocess.getoutput(cmd)，返回(stdout and stderr) 

	>>> subprocess.getoutput('ls /bin/ls')
	'/bin/ls'

### 2.字节流与字符串之间的转换
	 # bytes object
	  b = b"example"
	
	  # str object
	  s = "example"
		
	  # str to bytes
	  byte_code = s.encode("utf－8")
	
	  # bytes to str
	  str_code = b.decode('gb2312')




参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [Python之系统交互（subprocess）](https://www.cnblogs.com/sunshine-1/p/7290468.html)
