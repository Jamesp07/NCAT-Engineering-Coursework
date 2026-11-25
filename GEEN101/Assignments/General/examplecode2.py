"""
Created on Tue Oct  20 13:09:34 2026

@author: pjpri
"""

import numpy as np
import matplotlib.pyplot as plt

xstart = -10
xstop = 10
increment = 0.1

x = np.arange(xstart, xstop, increment)

y = x ** 2

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show

