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
    d2 = (56*e**(-2*t))/57 - (155*e**(-5*t))/147 + (67*e**(-t/10))/931
    return d2


def d3(t):
    d3 = 20000*e**(-100*t)
    return d3


def d4(t):

    d4 = (118580000000*e**(-100*t))/11051937 - (918068000*e**(-t/10))/69601329 - (476640000*e**(-t/3))/6180629 + (278356000000000*e**(-(1000*t)/47))/51111312451 - 2000000*t*e**(-100*t)
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
print(ua[1]*ia[1])
[id0,iq0]=pq_abc(sita0-pi/2,ia[0],ib[0],ic[0])
[ud0,uq0]=pq_abc(sita0-pi/2,ua[0],ub[0],uc[0])
iq1=[iq0]*100001
id1=[id0]*100001
uq1=[uq0]*100001
ud1=[ud0]*100001
w=[314.15]*100001
print(np.sqrt(uq0**2+ud0**2))
eqq0=uq0+xdd*id0+ra*iq0
eqq=[eqq0]*100001
eq0=eqq0+(xd-xdd)*id0
eq=[eqq0]*100001
betaw=[0]*100001
pt=[0]*100001
pe=[0]*100001
ef0=eq0
#ud1=xq*iq1-ra*id1
#uq1=eqq-xdd*id1-ra*iq1

print(ud0,uq0,id0,iq0)
print(ud0*id0+uq0*iq0)














