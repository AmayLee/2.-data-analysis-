# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 21:49:33 2022

@author: HUOQINGHAI
"""
'''DataFrame对象既有行索引，又有列索引
行索引，表明不同行，横向索引，叫index，0轴，axis=0
列索引，表明不同列，纵向索引，叫columns,1轴，axis=1'''
import numpy as np
import pandas as pd
df=pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('WXYZ'))
print(df)

d1={"name":["xiaohong","xiaogang"],"age":[13,32],"tel":[10000,10086]}
t1=pd.DataFrame(d1)
print(t1)
type(t1)#pandas.core.frame.DataFrame"

d2=[{"name":"xiaohong","age":32,"tel":10086},{"name":"xiaoming"},{"age":32}]
t2=pd.DataFrame(d2)
print(t2)
print("_"*30)


'''（一）常用的属性'''
print(t2.shape)#(3, 3)
print(t2.dtypes)
'''age     float64
name     object
tel     float64'''
print(t2.ndim)#2 维度
print(t2.index)#RangeIndex(start=0, stop=3, step=1)

print(t2.columns)#Index(['age', 'name', 'tel'], dtype='object')
print(t2.values)
print("_"*30)



'''(二）常用的方法'''

'''显示头几行（默认前五行）'''
print(t2.head(1))
'''显示后几行'''
print(t2.tail(2))
print("_"*30)

'''相关信息概览：行数、列数、列索引、列非空值个数、列类型、内存占用'''
print(t2.info())
print("_"*30)
'''快速统计数据列的最大值最小值 均值 个数 标准差 百分位'''
print(t2.describe())
print("_"*30)

'''DataFrame中排序的方法'''
df=t1.sort_values(by='age')
print(df)
print("_"*30)

df=t1.sort_values(by='age',ascending=False)
print(df)