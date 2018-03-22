import numpy as np
import matplotlib.pyplot as plt
import math
from load import Conditioner

a = np.mat([[-50, 0, 0],
            [249.6, -250.2667, -1.25],
            [6240, -6240, -31.25]])
y=np.mat([[1],[0],[0]])
print(a*y)