# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:17:00 2026

@author: pjpri
"""
import numpy as np
import matplotlib.pyplot as plt
import math

# Compute Mach Equations

A = 1000 # meters
γ = 1.4
R = 287.05 # J/kg * K
T = 288.15 - 0.0065 * A
V = np.array([340,1020,2040,3060,3400])

M1 = V / 340
M2 = V / math.sqrt(γ * R * T)

for vel, m1, m2 in zip(V, M1, M2):
    print(f"Velocity: {vel}, Mach(con): {m1:.2f}, Mach(var): {m2:.2f}")

plt.plot(V,M1)
plt.xlabel("Velocity(V)")
plt.ylabel("Mach Number(M)")
plt.grid(True)
plt.show

plt.plot(V,M2)
plt.xlabel("Velocity(V)")
plt.ylabel("Mach Number(M)")
plt.grid(True)
plt.show

#   I believe the variable model is better for operating scenarios.
#   In terms of rough calculations, the linear model is fine since it is a
#   few decimals off of the variable within the subsonic, transonic and
#   supersonic range. In operating aircraft those decimals become more
#   significant which is why I think the variable model is better
#   since it represents the actual value.