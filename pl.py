import numpy as np
import math
# dy/dt=y    y(0)=1
h=0.01
t=[0]*10001
y=[1]*10001
e=[1]*10001
for i in range(10000):
    y[i+1]=y[i]+h*y[i]
    y[i+1]=y[i]+(h/2)*(y[i+1]+y[i])
    t[i+1]=t[i]+h
    e[i+1]=math.e**t[i+1]-1
import matplotlib.pyplot as plt

plt.plot(t[0:10],y[0:10])
plt.plot(t[0:10],e[0:10])

plt.show()

