#オイラー法で常微分方程式を解く　演習１

import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ

h=0.1
T=1.0

x=0.0
y=1.0

x1 = []
y1 = []

while x<T:
    print("x=",x," y=",y)
    f=2*x
    x=x+h
    y=y+h*f
    x1.append(x)
    y1.append(y)

plt.plot(x1, y1)
plt.show()





