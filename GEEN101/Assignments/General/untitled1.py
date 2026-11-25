# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:19:47 2026

@author: pjpri
"""

import numpy as np
import matplotlib.pyplot as plt

h = np.array([0,1000,2000,3000])
T = np.array([288.15,281.65,275.15,268.65])

plt.plot(h,T)
plt.xlabel("Altitude(m)")
plt.ylabel("Temperature(K)")
plt.grid(True)
plt.show