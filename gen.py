import numpy as np
import matplotlib.pyplot as plt
import math
from load import Conditioner

# region 定义函数
e = math.e
pi = math.pi


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


k = 20
wref = 50
wrefb = 1
uref = 20000
urefb = 1
sref = 900000000
pref = 750000000
s = pref - 1j * math.sqrt(sref**2 - pref**2)
fi = -math.asin(pref / sref)
prefb = 1
xd = 1.8
xq = 1.7
x1 = 0.2
xdd = 0.3
xqq = 0.55
ra = 0.0025
td0 = 0.03
sita0 = 21.2 / 180 * pi
uB = math.sqrt(2) * uref / math.sqrt(3)
iB = sref / 3 / (uref / math.sqrt(3)) * math.sqrt(2)


sita = [sita0] * 1001
h = 1
t = [h] * 1001
i0 = s / (3 * uref / math.sqrt(3))
i00 = abs(i0)
ia = [i00 / iB * cos(fi)] * 1001
ib = [i00 / iB * cos(fi - pi / 3 * 2)] * 1001
ic = [i00 / iB * cos(fi + pi / 3 * 2)] * 1001
u0 = uref / math.sqrt(3)
ua = [u0 / uB * cos(0)] * 1001
ub = [u0 / uB * cos(-pi / 3 * 2)] * 1001
uc = [u0 / uB * cos(pi / 3 * 2)] * 1001
[id0, iq0] = pq_abc(sita0 - pi / 2, ia[0], ib[0], ic[0])
[ud0, uq0] = pq_abc(sita0 - pi / 2, ua[0], ub[0], uc[0])
iq1 = [iq0] * 1001
id1 = [id0] * 1001
uq1 = [uq0] * 1001
ud1 = [ud0] * 1001
w = [314.15] * 1001

eqq0 = uq0 + xdd * id0 + ra * iq0
eqq = [eqq0] * 1001
eq0 = eqq0 + (xd - xdd) * id0
eq = [eqq0] * 1001
betaw = [0] * 1001
pt = [0] * 1001
pe = [0] * 1001
ef0 = eq0
# ud1=xq*iq1-ra*id1
# uq1=eqq-xdd*id1-ra*iq1

# pe1=ud1*id+uq1*iq
uq = [uq0 * uB] * 1001
ud = [ud0 * uB] * 1001
iq = [iq0 * iB] * 1001
id = [id0 * iB] * 1001
pm = [750000000] * 1001
u = [math.sqrt(uq[0]**2 + ud[0]**2)]

for i in range(1000):
    pt[i] = ud[0] * id[0] + uq[0] * iq[0]
    pe[i] = ud[0] * id[0] + uq[0] * iq[0] + ra * (id[i] ** 2 + iq[i] ** 2)
    t[i] = i
    u[i] = math.sqrt(ud[i]**2 + uq[i]**2)
    betaw[i] = w[i] - wref
    betap = pt[i] - k * betaw[i]
    pm[i] = betap


