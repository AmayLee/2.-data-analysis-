# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 10:49:07 2022

@author: HUOQINGHAI
"""



import numpy as np
#file_path=r'C:\Users\HUOQINGHAI\Desktop\profits.xlsx'
#t1=np.loadtxt(file_path)
#mport pandas as pd
#df=pd.read_excel(r'C:\Users\HUOQINGHAI\Desktop\profits.xlsx')
#print(df)


t1=np.array([[1,2,3],[4,5,6],[7,8,9],[9,10,11]])
print(t1.shape)
print('*'*10)
#取第三行
print(t1[2])
print('*'*10)
#取连续的多行
print(t1[0:2])
print('*'*10)

#取不连续的多行
print(t1[[0,1,3],])

#取第二行的所有列
print(t1[1,:])
print('*'*10)

#取第三行之后的所有行的所有列
print(t1[2:,:])
print('*'*10)

#取第三行及之后的的所有行，及第2列所有列
print(t1[2:,1:])

#取不连续的多列
print(t1[:,[0,2]])

#取交叉行列的位置
print(t1[1:3,0:2])

#取行和列，取第三行第四列的数值（交叉点）
a=t1[0,1]
print(a)
print('*'*10)

#取多个不相邻的点

print(t1[[0,0],[1,2]])