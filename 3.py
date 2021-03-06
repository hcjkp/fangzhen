import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

from load import Conditioner

# region 定义数学函数
e = math.e
pi = math.pi


def fang(a, b, y, c, h):
    out = y + (a * y + b * c) * h
    out2 = y + (a * y + b * c + b * c + a * out) * h / 2
    return out2


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def pq_abc(x, ia, ib, ic):
    pq = 2 / 3 * np.array([
        [cos(x), cos(x - 2 * pi / 3), cos(x + 2 * pi / 3)],
        [-sin(x), -sin(x - 2 * pi / 3), -sin(x + 2 * pi / 3)]
    ])
    return np.dot(pq, [ia, ib, ic])


def xiang(x, y):
    return x * sin(y) + 1j * cos(y)


# endregion


# region 发电机初始参数
k = 20
wref = 50
wrefb = 1
uref = 20000
urefb = 1
sref = 900000000
pref = 750000000
s = pref - 1j * math.sqrt(sref ** 2 - pref ** 2)


xd = 1.8
xq = 1.7
x1 = 0.2
xdd = 0.3
xqq = 0.55
ra = 0.0025
td0 = 0.03
def iiiii(t):
    sita0 = t/ 180 * pi
    uB = math.sqrt(2) * uref / math.sqrt(3)
    iB = sref / 3 / (uref / math.sqrt(3)) * math.sqrt(2)

    n=10
    i0 = s / (3 * uref / math.sqrt(3))

    i00 = abs(i0) * math.sqrt(2)

    fu = 0
    fi = fu - math.acos(pref / sref)
    ia = [i00 / iB * cos(fi)] * (n + 1)
    ib = [i00 / iB * cos(fi - pi / 3 * 2)] * (n + 1)
    ic = [i00 / iB * cos(fi + pi / 3 * 2)] * (n + 1)
    u0 = uref / math.sqrt(3)*math.sqrt(2)

    ua = [u0 / uB * cos(0)] * (n + 1)
    ub = [u0 / uB * cos(-pi / 3 * 2)] * (n + 1)
    uc = [u0 / uB * cos(pi / 3 * 2)] * (n + 1)
    [id0, iq0] = pq_abc(sita0 - pi / 2, ia[0], ib[0], ic[0])
    [ud0, uq0] = pq_abc(sita0 - pi / 2, ua[0], ub[0], uc[0])
    eqq0 = uq0 + xdd * id0 + ra * iq0
    eqq = [eqq0] * (n + 1)
    eq0 = eqq0 + (xd - xdd) * id0
    eq = [eqq0] * (n + 1)
    betaw = [0] * (n + 1)
    pt = [0] * (n + 1)
    pe = [0] * (n + 1)
    ef0 = eq0
    ef = [ef0] * (n + 1)
    ud11 = xq * iq0 -ra* id0
    return ud0,ud11
for i in range(1800):
    out0,out1=iiiii(i/10)
    if out1-out0<0.001 and out1-out0>-0.001:
        print(i)
    else:
        pass
print(iiiii(36.1))


