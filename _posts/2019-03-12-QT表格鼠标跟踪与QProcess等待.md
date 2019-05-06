---
layout: post
---


### 1. QT表格鼠标跟踪

使用样式表时，可以不用设置鼠标跟踪，就得到鼠标移动时颜色改变的效果。

	QTableWidget
	{
		border-top: 0.5px solid #8F8F91;
		background-color: transparent;
	}
	QTableWidget::item:hover
	{
		background-color: #00f000;
	}
	QTableWidget::item:selected
	{
		background-color: #00f000;
		color:rgb(0,0,255); /*文字颜色*/
	}

### 2. 与QProcess等待执行完成

2种方法：

1. waitForFinished(-1);//默认等待，最多30秒
2. 用excute(),这个方法会等到执行完成才不阻塞。

以上两种方法，都会阻塞GUI，使程序“卡死”一段时间。

### 3. qt的QCombox增加提示tooltip

	QAbstractItemModel m* = ui.combox->model();
	if(m)
	{
		for(int i=0; i<ui.combox->count(); i++)
		{
			QModelIndex index = m->index(i,0);
			QString data = index.data().toString();
			m->setData(index, data, Qt::ToolTipRole);
		}
	}





参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [定义]({{site.baseurl}}/assets/2018-10-16/3.bmp)
3. [boost.any实现任意类型存储](https://blog.csdn.net/pngynghay/article/details/42774813)
