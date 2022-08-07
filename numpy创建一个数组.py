# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:27:35 2022

@author: HUOQINGHAI
"""
#numpy创建一个数组
import numpy as np
t1=np.array([1,2,3])
print(t1)

t2=np.array(range(10))
print(t2)

t3=np.arange(10)
print(t3)

print(type(t2))
print(type(t3))

t4=np.arange(4,10,2)
print(t4)
print(t4.dtype) #dtype属性（名词就是属性，动词就是方法）

#手动指定numpy中的数据类型
t5=np.array(range(1,10),dtype='float32')
print(t5)
print(t5.dtype)

#numpy中的bool类型
t6=np.array([1,1,0,0,1],dtype='bool')
print(t6)
print(t6.dtype)

#调整数据类型
t7=t6.astype('int8')  #astype方法
print(t7)
print(t7.dtype)

#numpy中的小数
t8=np.array([random.random() for i in range(10)])
print(t8)
print(t8.dtype)

t9=np.round(t8,2)
print(t9)
print(t9.dtype)