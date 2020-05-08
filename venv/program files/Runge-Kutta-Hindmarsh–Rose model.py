#ルンゲ＝クッタ法で常微分方程式を解く　
# Hindmarsh–Rose model


import math
import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ

h = 0.01

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

for t in np.arange(0, 2000, 1):

    x_calc = x
    y_calc = y
    z_calc = z

    k_1 = (y_calc + (-a * x_calc * x_calc * x_calc) + (b * x_calc * x_calc) - z_calc + I)
    l_1 = (c - (d * x_calc * x_calc) - y_calc)
    m_1 = (r * (s *(x_calc - xr) - z_calc))

    x_calc = x_calc + h * k_1 / 2
    y_calc = y_calc + h * l_1 / 2
    z_calc = z_calc + h * l_1 / 2
    k_2 =  (y_calc + (-a * x_calc * x_calc * x_calc) + (b * x_calc * x_calc) - z_calc + I)
    l_2 =  (c - (d * x_calc * x_calc) - y_calc)
    m_2 =  (r * (s *(x_calc - xr) - z_calc))

    x_calc = x_calc + h * k_2 / 2
    y_calc = y_calc + h * l_2 / 2
    z_calc = z_calc + h * l_2 / 2
    k_3 = (y_calc + (-a * x_calc * x_calc * x_calc) + (b * x_calc * x_calc) - z_calc + I)
    l_3 = (c - (d * x_calc * x_calc) - y_calc)
    m_3 = (r * (s * (x_calc - xr) - z_calc))

    x_calc = x_calc + h * k_3
    y_calc = y_calc + h * l_3
    z_calc = z_calc + h * l_3
    k_4 = (y_calc + (-a * x_calc * x_calc * x_calc) + (b * x_calc * x_calc) - z_calc + I)
    l_4 = (c - (d * x_calc * x_calc) - y_calc)
    m_4 = (r * (s * (x_calc - xr) - z_calc))

    x += h * (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    y += h * (l_1 + 2 * l_2 + 2 * l_3 + l_4) / 6
    z += h * (m_1 + 2 * m_2 + 2 * m_3 + m_4) / 6

    x1.append(t)
    y1.append(x)


plt.plot(x1, y1)
plt.show()
