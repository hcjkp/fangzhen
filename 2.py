import numpy as np
import matplotlib.pyplot as plt
import math

import time

from scipy.optimize import fsolve


def fx(x):
    ud = x[0]
    uq = x[1]
    id = x[2]
    iq = x[3]
    eqq = 0.87
    xdd = 0.3
    xq = 1.7
    ra = 0.0025
    p = 0.27
    s = 1
    return [uq - eqq + xdd * id + ra * iq, ud - xq * iq + ra * id, ud * id + uq * iq - p,
            np.sqrt(uq ** 2 + ud ** 2) * np.sqrt(id ** 2 + iq ** 2) - s/2]


result = fsolve(fx, [0.255707185749,0.659252482101,0.690724533639,0.151326199416])
print(result)
