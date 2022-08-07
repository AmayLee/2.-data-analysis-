# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 13:40:46 2022

@author: HUOQINGHAI
"""


import numpy as np
from matplotlib import pyplot as plt
#创建一个全为零的数组
t1=np.zeros((2,3))
print(t1)

#创建一个全为1的数组
t1=np.ones((2,3))
print(t1)

#获取最大值和最小值的位置
np.argmax(t1,axis=0)#行方向上的最大值，即每一列的最大值
np.argmin(t1,axis=1)#列方向上的最大值，即每一行的最大值

#创建一个对角线为1的正方形数组（方阵）：
np.eye(3)
print(np.eye(3))
print("_"*30)

#numpy生成随机数

#创建 n维的 均匀分布的随机数数组，浮点数，范围从0-1

t=np.random.rand(2,4)
#print(t)
plt.subplot(2,1,1)
plt.scatter(range(2*4),t)

#创建正太分布 创建n维度的标准正太分布随机数，浮点数，平均数0，标准差1
t1=np.random.randn(23)
print(t1)
plt.subplot(2,1,2)
plt.bar(range(23),t1) 

t2=np.random.randint(10,20,(4,5))
print(t2)