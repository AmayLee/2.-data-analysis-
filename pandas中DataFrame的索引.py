# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:08:04 2022

@author: HUOQINGHAI
"""

import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\HUOQINGHAI\Desktop\profits.xlsx')
df=df.sort_values(by='IO2207-C-4100.CFE')
print(df[:10])
print(type(df[:10]))
'''这是dataframe类型'''

print(df[:10]['IO2207-C-4100.CFE'])
print(df['IO2207-C-4050.CFE'])
print('_'*30)
'''pandas取行或列的注意事项:
    方括号写数组，表示取行，对行进行索引
    方括号写字符串，表示取列索引，对列进行操作'''
    

'''还有更多的经过pandas优化过的选择方式”
1、df.loc通过标签索引行数据
2、df.iloc通过位置索引行数据'''

d1=pd.DataFrame(np.arange(12).reshape(3,4),index=list('ABC'),columns=list('WXYZ'))
print(d1)
print('*'*20)
d2=d1.loc["A","W"]
print(d2)
d2=d1.loc["A":,["W","Z"]]
print(d2)
print('*'*20)
'''选择间隔的多行多列'''

d2=d1.loc["A":"C",["W","Y"]]
print(d2)
print('*'*20)
'''冒号是闭合的，会选择到冒号后面的数据'''
d2=d1.loc["A":"C",["W","Z"]]
print('_'*30)

'''df.iloc通过位置获取行数据'''
print(d1.iloc[1,:])
print('*'*20)
'''取第一行'''

'''取第三列'''
print(d1.iloc[:,2])
print('*'*20)
'''取不连续的多列，取第二列和第一列'''
print(d1.iloc[:,[2,1]])
print('*'*20)
'''取第二三行和第二三列'''
print(d1.iloc[1:3,[1,2]])
print(d1.iloc[[0,2],[2,1]])


'''赋值更改数据'''
d1.loc["A","W"]=100
print(d1)