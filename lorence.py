
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:23:53 2019
 
@author: luogantt
"""
 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
sigma=10.0
r=28.0
bb=8/3
 
h=0.004
 
#洛伦茨混沌系统
def lorence(tp):
     
    x=tp[0]
    y=tp[1]
    z=tp[2]
    x1=x+h*(sigma*(y-x))
    y1=y+h*(x*(r-z)-y)
    z1=z+h*(x*y-bb*z)
     
    return [x1,y1,z1]
     
b=[[15.34,13.68,37.91]]
for i in range(3000):
     
    temp=b[i]
     
    p=lorence(temp)
    b.append(p)
     
b=np.array(b)
plt.figure(figsize=(20, 12))
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(b[:,0], b[:,1], b[:,2], c='y')  # 绘制数据点
 
ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()