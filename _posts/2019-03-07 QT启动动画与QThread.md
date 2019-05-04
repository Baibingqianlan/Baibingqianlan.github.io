---
layout: post
---


### 1. 启动动画实现原理

原理：用QLabel 加载一个GIF图片，设置时间来控制动画的时长，如果卡的话，可以调用QApplication::processEvents()来处理没有进入主循环时的事件。

QT主循环:指调用了app.exec()后，程序进入事件循环。对话框也有自己的事件循环，每一个线程也有自己的事件循环（调用QThread::exec()之后）。

	QCoreApplicaton::exec()
	QApplication::exec()
	QDialog::exec()
	QThread::exec()
	QDrag::exec()
	QMenu::exec()

也可以用QEventLoop，随时进入事件循环。开启了事件循环，事件循环首先是一个无限“循环”，程序在exec()里面无限循环，能让跟在exec()后面的代码得不到运行机会，直至程序从exec()跳出。从exec()跳出时，事件循环即被终止。QEventLoop::quit()能够终止事件循环。

	QEventLoop loop;
	QTimer::singleShot(1000, &loop, SLOT(quit()));
	loop.exec();

启动动画实例：

	QLabel label(&splash);
    QMovie mv(":images/danceMan.gif");
    label.setMovie(&mv);
    mv.start();

	//等一段时间
	QTime t;
     t.start();
     while(t.elapsed()<5000)
     {
         QApplication::processEvents();
     }

### 2. QThread使用方法之一

	class MyThread : public QThread
	{
		Q_OBJECT
	public:
	    MyThread(QObject * parent=0);
	 
	protected:
	    virtual void run();    
	}

例子如上所示：直接使用，这样在主程序中实例化一个MyThread的实例，

	{	
		...
		private:
			MyThread * thread;
	}

调用start(),启动线程，线程进入run()函数。若在run()函数的最后加入exec(),则线程不会退出，一直在事件循环中，否则，run运行完成则发送finished()信号。直到主线程析构时，线程完全结束。当然也可以在中间强制让线程退出。

	thread = new MyThread()
	start();
	


参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [定义]({{site.baseurl}}/assets/2018-10-16/3.bmp)
3. [https://www.cnblogs.com/-wang-cheng/p/4973021.html](https://www.cnblogs.com/-wang-cheng/p/4973021.html)



