# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:48:22 2022

@author: HUOQINGHAI
"""

from math import log,sqrt,exp
from scipy import stats
import pandas as pd
import numpy as np
import time
import datetime
import matplotlib.pyplot as plt

data=pd.read_excel(r'C:\Users\HUOQINGHAI\Desktop\沪深300期权隐含波动率计算及BSM定价.xlsx')
option=pd.read_excel(r'C:\Users\HUOQINGHAI\Desktop\option.xlsx')

#求沪深300近半年收益率
data['rtn']=option['沪深300'].pct_change(1)
#求沪深300近半年历史波动率(单一的值)
sigma_history = np.std(data['rtn'])


'''
#牛顿迭代法求隐含波动率
temp_t_end=str(data['最后行权日期'][1]).split('-')
temp_t_end2=datetime.datetime(int(temp_t_end[0]),int(temp_t_end[1]),int(temp_t_end[2]))
temp_t_start=data['日期'][1]
T=((temp_t_end2-temp_t_start).days)/365
r=0.015/365
K=data['行权价格'][0]
'''
#BSM定价公式计算理论价格函数
def bsm_call_value(S0,K,T,r,sigma):
    
    d1 = (log(S0/K)+(r+0.5*sigma**2)*T)/sigma*sqrt(T)
    d2 = (log(S0/K)+(r-0.5*sigma**2)*T)/sigma*sqrt(T)
    value=S0*stats.norm.cdf(d1,0.0,1.0)-K*exp(-r*T)*stats.norm.cdf(d2,0.0,1.0)
    return value


#运用以上函数求每个合约的理论价格
value_result=[]
for i in range(data.shape[0]):
    C0=data['收盘价'][i]
    temp_t_end=str(data['最后行权日期'][i]).split('-')
    temp_t_end2=datetime.datetime(int(temp_t_end[0]),int(temp_t_end[1]),int(temp_t_end[2]))
    
    temp_t_start=data['日期'][i]
    T=((temp_t_end2-temp_t_start).days)/365
    S0=float(data['沪深300'][1])
    r=0.015/365
    K=data['行权价格'][i]
    sigma=np.std(data['rtn'])
    
    value_result.append(bsm_call_value(S0,K,T,r,sigma))
print(value_result) 
print(T)
'''
'''
#将计算出的理论价格放入data表格
#data=data.drop('开盘价',axis=1)
data['value']=pd.DataFrame(value_result)
    
#Vega函数
def bsm_vega(S0,K,T,r,sigma):
    S0=float(S0)
    d1 = (log(S0/K)+(r+0.5*sigma**2)*T)/sigma*sqrt(T)
    vega=S0*stats.norm.cdf(d1,0.0,1.0)*sqrt(T)
    return vega
vega=bsm_vega(S0,K,T,r,sigma)

#隐含波动率函数
def bsm_call_imp_vol(S0,K,T,r,C0,sigma_est,it):
    for i in range(it):
        sigma_est = (bsm_call_value(S0,K,T,r,sigma_est)-C0)/bsm_vega(S0,K,T,r,sigma_est)
    return sigma_est

result=[]
for i in range(data.shape[0]):
    C0=data['收盘价'][i]
    S0=data['沪深300'][i]
    temp_t_end=data['最后行权日期'][i]
    temp_t_start=data['日期'][i]
    T=((temp_t_end-temp_t_start).days)/365
    r=0.015/365
    K=data['行权价格'][i]
    sigma_est=np.std(data['rtn'])
    imp_vol = bsm_call_imp_vol(S0,K,T,r,C0,sigma_est,it = 100)
    result.append(imp_vol)
    
data['imp_vol']=pd.DataFrame(result)
maturities = sorted(set(data['行权价格']))


#画图
plt.figure(figsize=(18,22),dpi=200)

'''
     
 


