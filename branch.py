#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 18:27:06 2019

@author: lg
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin,pi


#pi=3.1415926

def logstic(k,x):
    
#    x1=0.6*x*(1-x)
    x1=k*sin(pi*x)
#    x1=λ*sin(pi*x)
    return x1

def gg(k,x):
    x1=1-k*x**2
    return x1


plt.figure(figsize=(20, 12))
for k in np.arange(0.5,2,0.005):
    print(k)
#for k=0.5:0.01:2;
    x=[0]
    for i in range(300):
#    for i=1:300
        temp=x[i]
#        p=logstic(k,temp)
        p=gg(k,temp)
        x.append(p)
    for t in range(150,300):
        plt.plot(k,x[t],'.b') 
        
        
        
plt.figure(figsize=(20, 12))
for k in np.arange(0.5,2,0.01):
    print(k)
#for k=0.5:0.01:2;
    x=[0.3]
    for i in range(300):
#    for i=1:300
        temp=x[i]
        p=logstic(k,temp)
#        p=gg(k,temp)
        x.append(p)
    for t in range(150,300):
        plt.plot(k,x[t],'.b') 

'''
for k in np.arange(0.5,1,0.01):
    print(k)
#for k=0.5:0.01:2;
    for i in range(300):
#    for i=1:300
        temp=x0[i]
        p=logstic(k,temp)
        x0.append(p)
        if i>150:
            plt.plot(k,p,'.b')
'''            
            

           
'''

b=[0.3]
for i in range(30):
     
    temp=b[i]
     
#    p=lorence(temp)
    p=logstic(temp)
    b.append(p)
     
b=np.array(b)
#plt.figure(figsize=(20, 12))
#ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程


plt.plot(list(range(len(b))), b)


ax = plt.subplot(111)  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(list(range(len(b))), b, c='y')  # 绘制数据点
 
#ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
'''