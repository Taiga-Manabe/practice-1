#オイラー法で常微分方程式を解く　
# FitzHugh–Nagumo model

import math
import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ

h = 0.5

v = 0.0
w = 0.0
I = 0.5
a = 0.7
b = 0.8
τ = 12.5
x1 = []
y1 = []

for t in np.arange(0, 100, h):
    print("t=", t, " v=", v," w=", w)
    v += h * (v - pow(v, 3) / 3 - w + I)
    w += (h * (v + a - b * w) /τ )
    x1.append(t)
    y1.append(v)


plt.plot(x1, y1)
plt.show()

