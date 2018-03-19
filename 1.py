import numpy as np
import matplotlib.pyplot as plt
import math


e = math.e
pi = math.pi
def sin(x):
    return  math.sinh(x)


def cos(x):
    return math.cos(x)


def xiang(x,y):
    return x*sin(y)+1j*cos(y)

def d2(t):
    d2 = 0.01692*e ^ (-0.1*t) + 0.03*e ^ (-2.5*t) - 0.99429*e ^ (-5.0*t) + 0.94737*e ^ (-2.0*t)
    return d2


def d3(t):
    d3 = 2666.66667 * e ^ (-43.83333 * t) * (math.cosh(43.75722 * t) - 0.97889 * math.sinh(43.75722 * t))
    return d3


def d4(t):

    d4 = 75.65851 * e^(-0.1 * t) -30.440121 * e^(-0.33333 * t) + 824.461674 * e^(-21.27660 * t) + 1214.12056* e^(-43.8333 * t) * (
            math.cosh(43.75722 * t) - 1.11300 * math.sinh(43.75722 * t))
    return d4

k = 20
wref= 50
wrefb=1
uref=20000
urefb=1
sref = 900000000
pref = 750000000
s=pref+1j*(sref-pref)
prefb = 1
xd=1.8
xq=1.7
x1=0.2
xdd=0.3
xqq=0.55
ra=0.0025
td0=0.03

sita0=pi/6

sita=[sita0]*100001
h=1
t=[h]*100001
i0=s/uref
i0=s/(3*uref)
ia=[i0]*100001
ib=[i0*xiang(1,-pi/6*5)]*100001
ic=[i0*xiang(1,pi/6*5)]*100001
print(i0,ia,ib,ic)