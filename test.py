import numpy as np
import matplotlib.pyplot as plt
def fxy(x,y):
   out=np.dot(a, y) + np.dot(b, np.array([31, 95, 70, 1200*x, 23]))
   return out

for i in range(10):
    c_ew = np.random.normal(1.875, 0.1875) * 100000  # 外墙的热容量
    c_in = np.random.normal(1.2, 0.12) * 100000  # 室内空气的热容量
    c_iw = np.random.normal(3.1, 0.31) * 100000  # 内墙的热容量
    r_cew = np.random.normal(0.005, 0.0005)  # 外部环境
    r_ew = np.random.normal(0.014, 0.0014)  # 外墙表面之间的热阻
    r_iw = np.random.normal(0.005, 0.0005)  # 室内墙壁等效热阻的一半
    r_gs = np.random.normal(0.08, 0.008)  # 玻璃表面的等效热阻

    x_ext = np.random.uniform(31, 32)  # 外界温度
    x_adj = np.random.uniform(23, 30)  # 相邻房间的温度
    i_eq = np.random.uniform(45, 55) + np.random.uniform(30, 35)  # 太阳通过玻璃表面以及室内家具的辐射量
    i_ew = np.random.uniform(95, 105)  # 太阳通过外墙表面的辐射量
    a = np.array(
        [[(1 / c_ew) * ((r_cew / (r_ew * (r_ew + r_cew)) - (2 / r_ew))), 1 / (c_ew * r_ew), 0],
         [1 / (c_in * r_ew), -(1 / c_in) * (1 / r_ew + 1 / r_iw + 1 / r_gs), 1 / (c_in * r_iw)],
         [0, 1 / (c_iw * r_iw), -2 / (c_iw * r_iw)]]
    )

    b = np.array(
        [[(1 / c_ew) * (1 / (r_cew + r_ew)), r_cew / (c_ew * (r_ew + r_cew)), 0, 0, 0],
         [1 / (c_in * r_gs), 0, 1 / c_in, -1 / c_in, 0],
         [0, 0, 0, 0, 1 / (c_iw * r_iw)]])


    def fun(t1, t2, t0):
        y = [np.array([30, t0, 24])]
        h = 1
        t = [0] * 1001
        w = [0] * 1001
        out = [t0] * 1001
        for i in range(1000):
            t[i + 1] = t[i] + h / 60
            if y[i][1] > t2:
                w[i + 1] = 1
            elif y[i][1] < t1:
                w[i + 1] = 0
            else:
                w[i + 1] = w[i]
            y.append(y[i] + fxy(w[i], y[i]) * h)
            y[i + 1] = y[i] + (fxy(w[i + 1], y[i + 1]) + fxy(w[i], y[i])) * (h / 2)
            out[i + 1] = y[i + 1][1]
        print(y)
        plt.plot(t, out)
        plt.show()


    fun(22, 23, 22.5)

    print(c_ew,i_ew,c_iw)