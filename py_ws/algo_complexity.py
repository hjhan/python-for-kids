
import numpy as np
import matplotlib.pyplot as plt
""" def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)


x = np.arange(0, 5, 0.000002)  # 曲线要光滑,步长尽可能小
# 该图在上半部分
plt.subplot(2, 1, 1)
plt.plot(x, f(x))
# 该图在下半部分
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(2*np.pi*x), 'r--')  # ‘r--’:r表示红色，--表示控制曲线格式的字符 """
x = np.arange(0, 100)
plt.plot(x, x * x)
plt.plot(x, x)
plt.plot(x, x*x*x, 'r--')

plt.show()
