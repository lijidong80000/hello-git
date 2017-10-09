#!/home/yuchun/anaconda2/bin/python
# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(2,7)
print "===============\ndata\n============="
print data

print "===============\nnames\n============="
names = np.array([['Bob', 'Joe', 'Will', 'Bob', 'Will', 'pipi', 'Joe'],\
                  [ 'Joe', 'Will', 'Bob','Bob', 'Will', 'jack', 'Joe']])
print "===============\nmask\n============="
print names=='Bob'
print "\n"
mask = (names=="Bob")|(names=="Joe")
print mask
print "===============\nindex of data --mask功能\n============="
print data[names=='Bob']
print "===============\nindex of data根据另一个矩阵抽取数据(取反）\n============="
print data[names!='Bob']

print "===============\nFancy索引\n============="
arr=np.empty((8,4),dtype=int)
print arr
print arr.T

print "===============\n通用函数\n============="
arr=np.arange(10)
print arr


points = np.arange(-5, 5, 0.01) # 1000个等间隔点
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
