#!/home/yuchun/anaconda2/bin/python
# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(2,7)
print "===============\ndata\n============="


obj=pd.Series([4,5,9,2,5,73,8,2,8,2,83])
print obj
print obj.index

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas'] 
obj4 = pd.Series(sdata, index=states) 
print obj4 
#California NaN Ohio 35000 Oregon 16000 Texas 71000
