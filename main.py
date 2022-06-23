#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


""" #Zapis logarifma
x = np.array([1, 10, 100, 1000])
print("Значения x: \n", x)
y = np.log(1 / np.e ** np.sin(x + 1) / (5 / 4 + 1 / x**15)) / np.log(1 + x**2)
print(y) """

""" #Grafiki
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x) = \sin(x),\ f_2(x) = \cos(x), f_3(x) = -x$')
plt.grid(True)
plt.show() """


""" #podpisi k grafikam
x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show() """


""" #variant razdelnih grafikov
x = np.arange(-10, 10.01, 0.01)
t = np.arange(-10, 11, 1)

#subplot 1
sp = plt.subplot(221)
plt.plot(x, np.sin(x))
plt.title(r'$\sin(x)$')
plt.grid(True)
#subplot 2
sp = plt.subplot(222)
plt.plot(x, np.cos(x), 'g')
plt.axis('equal')
plt.grid(True)
plt.title(r'$\cos(x)$')
#subplot 3
sp = plt.subplot(223)
plt.plot(x, x**2, t, t**2, 'ro')
plt.title(r'$x^2$')

#subplot 4
sp = plt.subplot(224)
plt.plot(x, x)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.title(r'$x$')
plt.show() """


""" #krugovaya diagramma
plt.subplot(111, polar=True)
phi = np.arange(0, 2*np.pi, 0.01)
rho = 2*phi
plt.plot(phi, rho, lw=2)
plt.show() """

# Drugie varianty diagramm   http://cs.mipt.ru/python/lessons/lab1.html#section-2


