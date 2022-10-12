# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 20:39:56 2022

@author: HUOQINGHAI
"""

'''假设现在有一组从2006年到2016年1000部最流行的电影数据，我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？
数据来源：https://www.kaggle.com/damianpanek/sunday-eda/data'''

#导演的人数
#print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))

#获取演员的人数
import numpy as np
import pandas as pd
temp_actors_list=df["actor]
temp_actors_list=np.array(temp_actors_list).flatten()
actors_num=len(set(actors_list))
print(actors_num)
