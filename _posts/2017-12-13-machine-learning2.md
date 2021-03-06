---
layout: post
---
## ML note 1 ##

**机器学习的分类**

学习斯坦福大学的吴恩达《机器学习1》

1. 监督学习：回归问题，分类问题（支持向量机）
2. 无监督学习：聚类问题（ICA算法）
2. 强化学习：直升机训练（回报函数）

**PYTHON大数据分析准备：各个库的介绍（一句话）**

1. numpy 数组运算
2. pandas 数组、电子表格,关系数据库
3. matplotlib 图表绘制
4. Ipython 增强的Python shell
5. Scipy 标准问题域包集合，积分/微分/矩阵，函数优化器，信号处理

运行环境：EPDFree(现在叫Canopy)安装包+pandas

## 梯度下降 ##

 梯度是一个向量；既有大小，也有方向。
[梯度定义](http://blog.csdn.net/myarrow/article/details/51332421)

**几何意义**

函数z=f(x,y)在点P0处的梯度方向是函数变化率(即方向导数)最大的方向（对角线）。梯度的方向就是函数f(x,y)在这点增长最快的方向，梯度的模为方向导数的最大值


## 线性回归 ##

1. y = a0 + a1*x

对于房价欠拟合

1. y = a0 + a1*x +a2*x^2
对于房价拟合


最小二乘法
矩阵的迹
矩阵的偏导数

## 局部加权回归 （非参数学习算法）##
对某一值，选其附近的区域，局部拟合

## Python 机器学习 ##

简单例子：

需要的库：numpy, pandas, scikit-learn, matplotlib, seaborn

安装Anaconda可以解决。




参考：

1. [使用 Python 开始机器学习](http://python.jobbole.com/88705/)
2. [An example machine learning notebook](http://nbviewer.jupyter.org/github/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/example-data-science-notebook/Example%20Machine%20Learning%20Notebook.ipynb#Introduction)
3. [Python数据可视化—seaborn简介和实例](https://blog.csdn.net/qq_34264472/article/details/53814653)
4. [只需十四步：从零开始掌握 Python 机器学习（附资源）](https://www.cnblogs.com/aabbcc/p/8683042.html)