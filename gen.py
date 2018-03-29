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
wref = 314.15
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
sita0 = 36.1 / 180 * pi
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


def uqud(eqq, p, s):
    def fx(x):
        ud = x[0]
        uq = x[1]
        id = x[2]
        iq = x[3]
        return [uq - eqq + xdd * id + ra * iq, ud - xq * iq + ra * id, ud * id + uq * iq - p,
                np.sqrt(uq ** 2 + ud ** 2) * np.sqrt(id ** 2 + iq ** 2) - s]

    result = fsolve(fx, [1, 1, 1, 1])
    return result


def gen(n, h, pload, sload):
    # region 初始值设定
    sita = [sita0] * (n + 1)
    t = [h] * (n + 1)
    i0 = s / (3 * uref / math.sqrt(3))
    i00 = abs(i0) * math.sqrt(2)
    fu = 0
    fi = fu - math.acos(pref / sref)
    ia = [i00 / iB * cos(fi)] * (n + 1)
    ib = [i00 / iB * cos(fi - pi / 3 * 2)] * (n + 1)
    ic = [i00 / iB * cos(fi + pi / 3 * 2)] * (n + 1)
    u0 = uref / math.sqrt(3) * math.sqrt(2)

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

    eqq10 = uq0 + xdd * id0 + ra * iq0
    eqq0 = eqq10 * uB
    eqq1 = [eqq10] * (n + 1)
    eqq = [eqq0] * (n + 1)
    eq0 = eqq0 + (xd - xdd) * id0
    eq = [eqq0] * (n + 1)
    betaw = [0] * (n + 1)
    pt = [0] * (n + 1)
    pe = [0] * (n + 1)
    pt1 = [0] * (n + 1)
    pe1 = [0] * (n + 1)
    ef0 = eq0
    print(uq0, ud0)
    ef = [ef0] * (n + 1)
    # ud1=xq*iq1-ra*id1
    # uq1=eqq-xdd*id1-ra*iq1

    # pe1=ud1*id+uq1*iq
    uq = [uq0 * uB] * (n + 1)
    ud = [ud0 * uB] * (n + 1)
    iq = [iq0 * iB] * (n + 1)
    id = [id0 * iB] * (n + 1)
    pm = [750000000] * (n + 1)
    u = [math.sqrt(uq[0] ** 2 + ud[0] ** 2)] * (n + 1)

    # yuandognjicanshu
    yuan_y1 = [np.mat([750000000])] * (n + 1)
    yuan_y2 = [np.mat([[750000000], [750000000]])] * (n + 1)
    # liciji
    li_y = [np.mat([[0], [0], [ef0]])] * (n + 1)
    li_y1 = [np.mat([[0], [0], [ef0 / uB]])] * (n + 1)

    dian_y = [np.mat([[eqq10], [wref], [sita0]])] * (n + 1)

    # endregion

    for i in range(n):
        pt1[i] = ud1[i] * id1[i] + uq1[i] * iq1[i]
        pe1[i] = ud1[i] * id1[i] + uq1[i] * iq1[i] + ra * (id1[i] ** 2 + iq1[i] ** 2)
        pt[i] = (ud1[i] * id1[i] + uq1[i] * iq1[i]) * sref
        pe[i] = (ud1[i] * id1[i] + uq1[i] * iq1[i] + ra * (id1[i] ** 2 + iq1[i] ** 2)) * sref
        t[i] = i * h
        u[i] = math.sqrt(ud[i] ** 2 + uq[i] ** 2)
        betaw[i] = w[i] - wref
        betap = pe[i] - k * betaw[i]
        yuan_y1[i + 1], yuan_y2[i + 1] = yuandong(betap, yuan_y1[i], yuan_y2[i], h)
        pm[i + 1] = float(0.33 * yuan_y2[i + 1][0] + 0.67 * yuan_y2[i + 1][1])
        li_y[i + 1] = lici(u0, u[i], li_y[i], h)
        print(u[i])
        print(li_y[i])
        li_y1[i + 1] = li_y[i + 1] / uB
        ef[i + 1] = float(li_y1[i + 1][2])
        print(ef[i])

        a = np.mat([[-1 / 8, 0, 0], [0, 0, 0], [0, 1, 0]])
        b = np.mat([[ef[i] - (xd - xdd) * id1[i]], [(pm[i] - pe[i]) / 13 / w[i]], [-wref]])
        c = 1
        dian_y[i+1]=fang(a,b,dian_y[i],c,h)

        eqq1[i + 1] = float(dian_y[i + 1][0])
        w[i+1]=float(dian_y[i+1][1])

        print(pm[i],pe[i])

        result = uqud(eqq1[i + 1], pload[i + 1] / sref, sload[i + 1] / sref)
        ud1[i + 1] = result[0]
        uq1[i + 1] = result[1]
        id1[i + 1] = result[2]
        iq1[i + 1] = result[3]
        ud[i + 1] = ud1[i + 1] * uB
        uq[i + 1] = uq1[i + 1] * uB
        id[i + 1] = id1[i + 1] * uB
        iq[i + 1] = iq1[i + 1] * uB
    print(ud1, uq1)
    return ef



gen(10, 0.001, [750000000] * 11, [900000000] * 11)
