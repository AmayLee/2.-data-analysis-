# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:04:20 2022

@author: HUOQINGHAI
"""

'''numpy可以帮助我们处理数值信息，不过pandas除了数值外，还可以处理其他类型的数据'''

'''pandas常用数据类型有两种
1、Series一维，带标签数组；
2、DataFrame二维，'''
import pandas as pd
t1=pd.Series([1,23,4,56,1])
print(t1)

'''指定索引'''
t2=pd.Series([1,2,3,4,5],index=list('abcde'))#list字符串转列表
print(t2)

'''通过字典创建Series'''
temp_dict={'name':'yidong','age':18,'tel':10086}
t3=pd.Series(temp_dict)
print(t3.age)

'''常见的切片即索引'''
print(t3[0])
print(t3[0:3])
print(t3['age'])
print(t3[['age','name']])
print('_'*30)

'''series具有两个常见的属性 分别是index 和values'''
print(t3.index)
print(type(t3.index))
'''<class 'pandas.core.indexes.base.Index'>单纯的index类型'''
print(len(t3.index))
print(list(t3.index))
print(list(t3.index)[:2])

print('_'*30)
'''强制转化为列表形式'''
print(t3.values)
print(type(t3.values))

print(len(t3.values))
print(list(t3.values))
print('_'*30)

'''注意，pandas也有where功能，但是结果和ndarray不同，其他numpy中的方法和pandas几乎一致'''