# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 12:37:13 2022

@author: HUOQINGHAI
"""

#数据的拼接
#首先相加肯定不可以，将导致里面的数据加起来

np.vstack((t1,t2)) #竖直拼接
np.hstack(t1,t2)) #水平拼接

#数据的行列变换
t[[1,2],:]=t[[2,1],:]#行变换
t[:,[0,1]]=t[:,[1,0]]#列变换

