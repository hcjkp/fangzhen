import numpy as np
import matplotlib.pyplot as plt
import math

import time
from scipy.optimize import fsolve


def fx(x):
    ud = float(x[0])
    uq = float(x[1])
    id = float(x[2])
    iq = float(x[3])
    eqq = 1.09
    xdd = 0.30
    xq = 1.70
    ra = 0.0025
    p = 75 / 90
    s = 1.0
    return np.array([uq - eqq + xdd * id + ra * iq, ud - xq * iq + ra * id, ud * id + uq * iq - p,
            np.sqrt(uq ** 2 + ud ** 2) * np.sqrt(id ** 2 + iq ** 2) - s])


x0 = np.array([0.58, 0.50, 0.81, 0.577])
result = fsolve(fx, x0)
print(type([0.361, 0.50, 0.91, 0.577]))
print(np.sqrt(result[0] ** 2 + result[1] ** 2))
print(result[0] * result[2] + result[1] * result[3])
print(result)
