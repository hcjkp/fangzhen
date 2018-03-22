
import numpy as np
import matplotlib.pyplot as plt
import math
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
# endregion


def yuandong(betap, y1, y2, h):
    y1 = fang(-2, 2, y1, betap, h)
    a = np.mat([[-5, 0], [0.1, -0.1]])
    b = np.mat([[5], [0]])
    y2 = fang(a, b, y2, y1, h)
    return y1, y2


def lici(uref, ut, y, h):  #
    a = np.mat([[-50, 0, 0],
                [249.6, -250.2667, -1.25],
                [6240, -6240, -31.25]])
    b = np.mat([[50], [0], [0]])
    c = uref - ut
    y = fang(a, b, y, c, h)
    return y


def gen(n, h):
    # region 初始值设定
    sita = [sita0] * (n + 1)
    t = [h] * (n + 1)
    i0 = s / (3 * uref / math.sqrt(3))
    i00 = abs(i0)
    ia = [i00 / iB * cos(fi)] * (n + 1)
    ib = [i00 / iB * cos(fi - pi / 3 * 2)] * (n + 1)
    ic = [i00 / iB * cos(fi + pi / 3 * 2)] * (n + 1)
    u0 = uref / math.sqrt(3)
    ua = [u0 / uB * cos(0)] * (n + 1)
    ub = [u0 / uB * cos(-pi / 3 * 2)] * (n + 1)
    uc = [u0 / uB * cos(pi / 3 * 2)] * (n + 1)
    [id0, iq0] = pq_abc(sita0 - pi / 2, ia[0], ib[0], ic[0])
    [ud0, uq0] = pq_abc(sita0 - pi / 2, ua[0], ub[0], uc[0])
    iq1 = [iq0] * (n + 1)
    id1 = [id0] * (n + 1)
    uq1 = [uq0] * (n + 1)
    ud1 = [ud0] * (n + 1)
    w = [314.15] * (n + 1)

    eqq0 = uq0 + xdd * id0 + ra * iq0
    eqq = [eqq0] * (n + 1)
    eq0 = eqq0 + (xd - xdd) * id0
    eq = [eqq0] * (n + 1)
    betaw = [0] * (n + 1)
    pt = [0] * (n + 1)
    pe = [0] * (n + 1)
    ef0 = eq0
    ef=[ef0]*(n+1)
    # ud1=xq*iq1-ra*id1
    # uq1=eqq-xdd*id1-ra*iq1

    # pe1=ud1*id+uq1*iq
    uq = [uq0 * uB] * (n + 1)
    ud = [ud0 * uB] * (n + 1)
    iq = [iq0 * iB] * (n + 1)
    id = [id0 * iB] * (n + 1)
    pm = [750000000] * (n + 1)
    u = [math.sqrt(uq[0]**2 + ud[0]**2)]

    # yuandognjicanshu
    yuan_y1 = [np.mat([750000000])] * (n + 1)
    yuan_y2 = [np.mat([[750000000], [750000000]])] * (n + 1)
    # liciji
    li_y = [np.mat([[0], [0], [ef0]])] * (n + 1)

# endregion

    for i in range(n):
        pt[i] = ud[0] * id[0] + uq[0] * iq[0]
        pe[i] = ud[0] * id[0] + uq[0] * iq[0] + ra * (id[i] ** 2 + iq[i] ** 2)
        t[i] = i * h
        u[i] = math.sqrt(ud[i]**2 + uq[i]**2)
        betaw[i] = w[i] - wref
        betap = pt[i] - k * betaw[i]
        yuan_y1[i + 1], yuan_y2[i + 1] = yuandong(betap, yuan_y1[i], yuan_y2[i], h)
        pm[i + 1] = 0.33 * yuan_y1[i + 1] + 0.67 * yuan_y2[i + 1]
        li_y[i+1]=lici(u0,u[i],li_y[i],h)
        ef[i+1]=li_y[i+1][2]


