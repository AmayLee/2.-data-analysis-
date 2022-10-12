# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:50:29 2022

@author: HUOQINGHAI
"""
'''pip install package
import package as pkg

python容器
list列表，序列是python中最基本的数据结构。序列中的每个元素都分配一个数字 
它的位置或索引，第一个是0，第二个是1 以此类推

dict字典
字典中每个键值（key=value)对用冒号分割，每个对之间用逗号分割，整个字典包括在花括号中。

list基本操作
创建
添加元素 ：append,extend
删除元素：del,pop

dict基本操作
访问
添加元素
修改元素
删除元素
容器元素数量
遍历

python函数
函数是组织好，可重复使用的，实现特定功能的代码段
一些简单规则
以def关键词开头，后接函数标识符名称和圆括号（）
传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数内容以冒号起始，并且缩进。
return[表达式]结束函数，选择性第返回一个值为调用方。不带表达式的return相当与返回None
'''

#函数定义和
def func(x,y=500):
    print(x,y)
func(150)

func(100,200)
func(y=300,x=100)

'''
python期权数据处理
期权数据的特征，在同意交易时间有多个合约以及多个价格

编写函数 记录正在开仓的合约 应用了python的工具包

常用数组函数numpy
Array将输入数据（列表、元组、数组或其他序列类型）转换为ndarray.要么推断出dtype,要么显示指定dtype.默认直接复制输入数据。

Arange类似于内置的range,但返回一个ndarray而不是列表

ones，one_like根据指定形状和dtype创建一个全1数组。其中one_like以另一个数组为参数，并根据其形状和dtype创建一个全1数组。

eye,identity创建一个正方的N*N单位矩阵
'''

import numpy as np
import numpy.random as np_random

'''利用数组进行数据处理
矢量化数组运算
Where的使用：将条件逻辑变为数组运算
'''
import numpy as np
import pylab
import matplotlib.pyplot as plt

points=np.arange(-5,5,0.01)#生成100个点
xs,ys=np.meshgrid(points,points)#xs,yx互为转置
print(xs)
print(ys)
z=np.sqrt(xs**2+ys**2)

plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of s\sqrt(x^2+y^2)s for a grid of values")
pylab.show()
'''
print('通过真值选择元素')
x_arr=np.array([1.1,1.2,1.3,1.4,1.5])
y_arr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result = [x if c else y ] for x,y,c in zip(x_arr,y_arr)

'''
