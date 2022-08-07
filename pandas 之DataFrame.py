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
