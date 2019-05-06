---
layout: post
---


### 1. Qt图形视图框架（The QGraphics View Framework）

GraphicView框架特点：

1. 利用QT绘图系统的反锯齿，OPENGL
2. 支持事件传播体系，提高 图元的交互能力。
3. 通过二元空间划分树（BSP）提高查找图元速度。


主要有三个类组成：场景类（QGraphicsScene）、视图类（QGraphicView）和图元类（QGraphicItem）。

**坐标体系**：

1. QGraphicsScene，坐标原点为中心（0，0），右为x正，下为y正
2. QGraphicView，坐标原点为左上角（0，0），右为x正，下为y正
3. QGraphicItem，图元中心为原点。

场景增加图元，默认放置位置为原点（0，0），即从原点开始的第四象限内，可以用图片做实验，也可实际打印出来坐标。

>
scene(场景)坐标，属于逻辑坐标 logical coordinates（与QPainter相同），以场景中心为原点，正方向x朝右，y朝下。图元嵌入场景中，默认场景原点与图元原点对齐。**1、如果scene的大小不超过view可显示的最大值，那么scene在view中的默认对齐方式为居中对齐，这个中指的不是原点，而是所有item的Rect的中心点，是计算出来的；2、如果scene的大小超过view的可显示最大值，此时scene将在view中改成左上角对齐显示，左上角点也不一定是场景坐标原点**

>
显示时，默认场景scene的左上角顶点(一般肯定不是secene的(0,0)坐标点)与视图坐标原点对齐。又由于显示时默认中心对齐，当场景大小小于视图大小的时候，将中心对齐，此中指的仍然是整个图元的中心，同时，图元原点与场景原点对齐，场景左上角顶点与视图原点对齐，视图左上角顶点不一定是原点，此时也将出现视图坐标有正值有负值。

视图的坐标与图元坐标都是固定的，不用太多考虑。

**图层**：

图层有三个默认的，背景、图元、前景，绘制顺序也是从后往前，或者叫从下往上。

### 2.qt5中乱码

	VS2015 中如果源代码是 utf-8的，执行字符集默认是本地 Locale 字符集，
	对于简体中文的 windows 系统来说，这个 本地Locale字符集是 gb18030。
	所以直接显示汉字会全是乱码。解决这个乱码有三个办法，第一个办法是编译时加
	入命令行参数，在 Qt 的 pro 文件中可以这样：
	
	msvc:QMAKE_CXXFLAGS += -execution-charset:utf-8

	第二个办法是在源文件中加入：
	
	#pragma execution_character_set("utf-8")

	更好的办法是源代码写为：
	
	QString  str(u8"我是中文");


1. 使用QString::fromLocal8Bit

		QString tip = QString::fromLocal8Bit("视图坐标（%1，%2），场景坐标（%3，%4）")
			.arg(view.x()).arg(view.y()).arg(scene.x()).arg(scene.y());
		_tip->setText(tip);
2. 使用QStringLiteral

		QString tip = QStringLiteral("视图坐标（%1，%2），场景坐标（%3，%4）")
				.arg(view.x()).arg(view.y()).arg(scene.x()).arg(scene.y());
		_tip->setText(tip);

### 3. 使用

1. **鼠标中轮滚动事件**

		void MapView::wheelEvent( QWheelEvent * event )
		{
			// 滚轮的滚动量
			QPoint scrollAmount = event->angleDelta();
			// 正值表示滚轮远离使用者（放大），负值表示朝向使用者（缩小）
			scrollAmount.y() > 0 ? scale(1.1, 1.1) : scale(1/1.1, 1/1.1);
		}
2. **去滚动条**：
3. 
		// 去掉滚动条
		setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
		setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);


### 4.QT坐标转换

+ . QTransform 

QTransform 用于指定坐标系的 2D 转换 - 平移、缩放、扭曲（剪切）、旋转或投影坐标系。绘制图形时，通常会使用。

QTransform 与 QMatrix 不同之处在于，它是一个真正的 3x3 矩阵，允许视角转换，QTransform 的 toAffine() 方法允许将 QTransform 转换到 QMatrix。如果视角转换已在矩阵指定，则转换将导致数据丢失。

![](https://img-blog.csdn.net/20160529194454425)

QPainter中使用
	
	void CombinedTransformation::paintEvent(QPaintEvent *)
	{
	    QPainter painter(this);
	    painter.setPen(QPen(Qt::blue, 1, Qt::DashLine));
	    painter.drawRect(0, 0, 100, 100);
	
	    QTransform transform;
	    transform.translate(50, 50);
	    transform.rotate(45);
	    transform.scale(0.5, 1.0);
	    painter.setTransform(transform);
	
	    painter.setFont(QFont("Helvetica", 24));
	    painter.setPen(QPen(Qt::black, 1));
	    painter.drawText(20, 10, "QTransform");
	}

常用接口

    translate(qreal dx, qreal dy)：平移 - 对坐标系沿着 x 轴移动 dx、沿 y 轴移动 dy
    scale(qreal sx, qreal sy)：缩放 - 通过水平的 sx 和垂直的 sy 缩放坐标系
    rotate(qreal angle, Qt::Axis axis = Qt::ZAxis)：旋转 - 对指定的轴用给定的角度反时针旋转坐标系统
    shear(qreal sh, qreal sv)：扭曲 - 通过水平的 sh 和垂直的 sv 扭曲坐标系
    reset()：重置为单位矩阵


+ . **ViewportAnchor** 

		ViewportAnchor transformationAnchor () const
		void  setTransformationAnchor ( ViewportAnchor anchor )

ViewportAnchor这个属性控制着当转换时候view应该如何摆放场景的位置

QGraphicsView使用这个属性来决定当转换矩阵修改和坐标系统修改时候如何摆放场景的在viewport中的位置，默认的是 AnchorViewCenter,这样使场景点在变换时候保持在view中心点不变（例如：当旋转时候，场景将会围绕着view中心点来旋转）

只有场景中的一部分可见时候这个属性才显而易见的。例如：当view中有滚动条时候，否则整个场景都在view中，场景将会使用QGraphicsView::aligenment来摆放它的位置

下面代码，可以达到，**鼠标在哪就以哪里为中心的浏览效果**。

	//view 根据鼠标下的点作为锚点来定位 scene
	setTransformationAnchor(QGraphicsView::AnchorUnderMouse);
	centerOn(mapToScene(event->pos()));
	//scene 在 view 的中心点作为锚点
	setTransformationAnchor(QGraphicsView::AnchorViewCenter);

+ 地图漫游实现：

		void MapView::mousePressEvent( QMouseEvent * event )
		{
			if (event->button() == Qt::LeftButton)
			{
				setDragMode(QGraphicsView::ScrollHandDrag);
			}
		
			QGraphicsView::mousePressEvent(event);
		}
		
		void MapView::mouseReleaseEvent( QMouseEvent * event )
		{
			if (event->button() == Qt::LeftButton)
			{
				setDragMode(QGraphicsView::NoDrag);
			}
			QGraphicsView::mouseReleaseEvent(event);
		}


参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [定义]({{site.baseurl}}/assets/2018-10-16/3.bmp)
3. [https://www.cnblogs.com/-wang-cheng/p/4973021.html](https://www.cnblogs.com/-wang-cheng/p/4973021.html)
4. [https://blog.csdn.net/liyuanbhu/article/details/72596952](https://blog.csdn.net/liyuanbhu/article/details/72596952)
5. [https://blog.csdn.net/liang19890820/article/details/53543017](https://blog.csdn.net/liang19890820/article/details/53543017)
6. [https://blog.csdn.net/founderznd/article/details/51533777](https://blog.csdn.net/founderznd/article/details/51533777)



