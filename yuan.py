import numpy as np
import matplotlib.pyplot as plt
import math
from load import Conditioner


def jiefangcheng(a,b,y,c,n,h):  #a，b 数组, y,c 可为列表，a为 n行 n列，b为n行 m列 c为m行
    for i in range(len(y)-1):
        y[i+1]=(np.dot(a, y[i]) + np.dot(b, c[i]))*h
        y[i+1]=(np.dot(a, y[i+1]) + np.dot(b, c[i+1])+np.dot(a, y[i]) + np.dot(b, c[i]))*h/2
    return y




def yuandong(p0,betaw,n):
    c=np.array([p0]*n)-np.array(betaw)
    y1=[p0]*n
    y2=[[p0/3,2*p0/3]]*n
    y1=jiefangcheng(-2,2,y1,c,n,1)
    print(len(y1))
    print(y1)

yuandong(100,[0]*1000,1000)


