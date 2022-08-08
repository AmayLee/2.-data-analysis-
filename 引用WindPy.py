# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 10:51:42 2022

@author: HUOQINGHAI
"""

import numpy as np
from WindPy import *
from numpy import *
import pandas as pd

w.start()
data1=w.wsd("SC2207.INE","close","2022-04-14","2022-05-20","Fill=previous")
data2=w.wsd("SC2208.INE","close","2022-05-21","2022-06-20","Fill=previous")
Time=data1.Times
print('_'*30)
Data=data1.Data
print(len(Time))

print('_'*30)
for i in range(len(Time)):
    print(Time[i])
    print(Data[i])

    
    