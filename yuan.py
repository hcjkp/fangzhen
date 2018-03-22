import numpy as np
import matplotlib.pyplot as plt
import math
from load import Conditioner

def fangc(a,b,y,c,h):
    out=y+(a*y+b*c)*h
    out2=y+(a*y+b*c+b*c+a*out)*h/2
    return out2

def lici(uref,n,h): #ut为标幺值
    a=np.mat([[-50,0,0],
              [249.6,-250.2667,-1.25],
              [6240,-6240,-31.25]])
    b=np.mat([[50],[0],[0]])
    t = [0] * 10001
    ut = [0] * 10001
    y=[np.mat([[1],[0],[0]])]*10001
    for i in range(10000):
        ut[i+1]=ut[i]+h*(y[i][2]/5.36-ut[i]/5.36/0.8)
        c =uref - ut[i]
        y[i+1] = y[i] + (a * y[i] + b * c) * h
        y[i + 1] = y[i] + (a * y[i] + b * c + b * c + a * y[i + 1]) * h / 2


    return y
print(lici(1,1000,0.001))

def jiefangcheng(a,b,y,c,n,h):  #a，b 数组, y,c 可为列表，a为 n行 n列，b为n行 m列 c为m行
    for i in range(n-1):
        y[i+1]=y[i]+(a*y[i]+b*c[i])*h
        y[i+1]=y[i]+(a*y[i+1]+b*c[i+1]+a*y[i]+b*c[i])*h/2


    return y

def yuandong(p0,betaw,n):
    c=np.array([p0]*n)-np.array(betaw)
    y1=[np.mat(p0)]*n
    y2=[np.mat([[p0],[p0]])]*n
    y1=jiefangcheng(-2,2,y1,c,n,1)
    a=np.mat([[-5,0],[0.1,-0.1]])
    b=np.mat([[5],[0]])
    y2=jiefangcheng(a,b,y2,y1,n,1)
    return y2