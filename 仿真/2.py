import numpy as np
import matplotlib.pyplot as plt
import math


e = math.e
pi = math.pi
def sin(x):
    return  math.sin(x)


def cos(x):
    return math.cos(x)


def pq_abc(x,ia,ib,ic):
    pq=2/3*np.array([
    [cos(x),cos(x-2*pi/3),cos(x+2*pi/3)],
    [-sin(x),-sin(x-2*pi/3),-sin(x+2*pi/3)]
])
    return np.dot(pq,[ia,ib,ic])

def xiang(x,y):
    return x*sin(y)+1j*cos(y)

def d2(t):
    d2 = 0.01692*e**(-0.1*t) + 0.03*e**(-2.5*t) - 0.99429*e **(-5.0*t) + 0.94737*e**(-2.0*t)
    return d2


def d3(t):
    d3 = 2666.66667 * e**(-43.83333 * t) * (math.cosh(43.75722 * t) - 0.97889 * math.sinh(43.75722 * t))
    return d3


def d4(t):

    d4 = 75.65851 * e**(-0.1 * t) -  30.440121 * e**(-0.33333 * t) + 824.461674 * e**(-21.27660 * t) + 1214.12056* e**(-43.8333 * t) * (
            math.cosh(43.75722 * t) - 1.11300 * math.sinh(43.75722 * t))
    return d4

k = 20
wref= 50
wrefb=1
uref=20000
urefb=1
sref = 900000000
pref = 750000000
s=pref-1j*math.sqrt(sref**2-pref**2)
fi=-math.asin(pref/sref)
prefb = 1
xd=1.8
xq=1.7
x1=0.2
xdd=0.3
xqq=0.55
ra=0.0025
td0=0.03
sita0=21.2/180*pi
uB=math.sqrt(2)*uref/math.sqrt(3)
iB=sref/3/(uref/math.sqrt(3))*math.sqrt(2)


sita=[sita0]*100001
h=1
t=[h]*100001
i0=s/(3*uref/math.sqrt(3))
i00=abs(i0)
ia=[i00/iB*cos(fi)]*100001
ib=[i00/iB*cos(fi-pi/3*2)]*100001
ic=[i00/iB*cos(fi+pi/3*2)]*100001
u0=uref/math.sqrt(3)
ua=[u0/uB*cos(0)]*100001
ub=[u0/uB*cos(-pi/3*2)]*100001
uc=[u0/uB*cos(pi/3*2)]*100001
[id0,iq0]=pq_abc(sita0-pi/2,ia[0],ib[0],ic[0])
[ud0,uq0]=pq_abc(sita0-pi/2,ua[0],ub[0],uc[0])
ud11 = xq * iq0 -ra* id0
d=[]
t=[]
for i in range(1,10000):
    x=0.0001*i
    d.append(d2(x))
    t.append(x)
plt.plot(t,d)
plt.show()
