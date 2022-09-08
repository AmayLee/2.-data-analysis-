# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 12:02:07 2022

@author: HUOQINGHAI
"""

#修改行列的值，修改某一部分的值为零；
import numpy as np
t=np.arange(24).reshape(4,6)
t[:,2:4]=0
print(t)
    

#把t中小于10的数字替换为3
print(t<10)#输出的是bool值

t[t<10]=5
print(t)

t[t>20]=10
print(t)


#numpy中的三元运算符
#where用法：和if else一样，如果t<10，那么输出0，如果不小于10,那么输出10
t1=np.where(t<10,0,10)
print(t1)



#numpy中的clip(裁剪)
t2=t.clip(10,18) #小于10的数值设置为10 大于18的数值设置为18
print(t2)

#将数值替换为nan
t3=np.array([[12,3,4],[7,9,6]])
t3=t3.astype(float)
print(t3)
t3[0,0]=np.nan  #第一行和第一列数值设置为零
print(t3)
