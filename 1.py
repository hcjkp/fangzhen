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
sita0 = 36.1 / 180 * pi
print(sita0)
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


def uqud(ef,p,s):
    def fx(x):
        ud = x[0]
        uq = x[1]
        id = x[2]
        iq = x[3]
        xdd = 0.3
        xq = 1.7
        ra = 0.0025
        return [uq - ef - xdd * id - ra * iq, ud - xq * iq - ra * id, ud * id + uq * iq - p,
                np.sqrt(uq ** 2 + ud ** 2) * np.sqrt(id ** 2 + iq ** 2) - s]

    result = fsolve(fx, [1,1,1,1])
    return result


def gen(n, h):
    # region 初始值设定
    sita = [sita0] * (n + 1)
    t = [h] * (n + 1)
    i0 = s / (3 * uref / math.sqrt(3))
    i00 = abs(i0) * math.sqrt(2)
    fu = 0
    fi = fu - math.acos(pref / sref)
    print(math.acos(pref / sref))
    ia = [i00 / iB * cos(fi)] * (n + 1)
    ib = [i00 / iB * cos(fi - pi / 3 * 2)] * (n + 1)
    ic = [i00 / iB * cos(fi + pi / 3 * 2)] * (n + 1)
    u0 = uref / math.sqrt(3)*math.sqrt(2)

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
    ud11 = xq * iq0 - ra * id0
    betaw = [0] * (n + 1)
    pt = [0] * (n + 1)
    pe = [0] * (n + 1)
    ef0 = eq0
    ef = [ef0] * (n + 1)
    uq = [uq0 * uB] * (n + 1)
    ud = [ud0 * uB] * (n + 1)
    iq = [iq0 * iB] * (n + 1)
    id = [id0 * iB] * (n + 1)
    pm = [750000000] * (n + 1)
    return ud11,iq0,id0,uq0,eqq0
print(gen(10,0.01))

