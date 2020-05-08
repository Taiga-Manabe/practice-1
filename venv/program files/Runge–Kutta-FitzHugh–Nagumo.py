#ルンゲ＝クッタ法で常微分方程式を解く　
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
    v_calc = v
    w_calc = w
    k_1 = v_calc - pow(v_calc, 3) / 3 - w_calc + I
    l_1 = ((v_calc + a - b * w_calc) / τ)

    v_calc = v_calc + h * k_1 / 2
    w_calc = w_calc + h * l_1 / 2
    k_2 = v_calc - pow(v_calc, 3) / 3 - w_calc + I
    l_2 = ((v_calc + a - b * w_calc) / τ)

    v_calc = v_calc + h * k_2 / 2
    w_calc = w_calc + h * l_2 / 2
    k_3 = v_calc - pow(v_calc, 3) / 3 - w_calc + I
    l_3 = ((v_calc + a - b * w_calc) / τ)

    v_calc = v_calc + h * k_3
    w_calc = w_calc + h * l_3
    k_4 = v_calc - pow(v_calc, 3) / 3 - w_calc + I
    l_4 = ((v_calc + a - b * w_calc) / τ)

    v += h * (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
    w += h * (l_1 + 2 * l_2 + 2 * l_3 + l_4) / 6
    x1.append(t)
    y1.append(v)


plt.plot(x1, y1)
plt.show()

