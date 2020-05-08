#オイラー法で常微分方程式を解く　
# Hindmarsh–Rose model

import math
import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ

h=0.1

x = 0
y = 0
z = 0

a = 1
b = 3
c = 1
d = 5

s = 4
xr = -8 / 5
r = 1 / 2000

I = 3




x1 = []
y1 = []

for t in np.arange(0, 10, h):
    print("t=", t, " x=", x," y=", y," z", z)
    phi = (-a * pow(x, 3)) + (b * pow(x, 2))
    psi = c - (d * pow(x, 2))
    x += h * (y + phi - z + I)
    y += h * (psi - y)
    z += h * (r * (s *(x - xr) - z))

    x1.append(t)
    y1.append(x)


plt.plot(x1, y1)
plt.show()

