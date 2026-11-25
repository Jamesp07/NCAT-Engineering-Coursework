# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:31:39 2026

@author: pjpri
"""
import matplotlib.pyplot as plt


altitudes = [0, 2000, 4000, 6000, 8000, 10000]
temperatures = []
pressures = []

class Atmosphere:
    def __init__(self, altitude):
        self.h = altitude
        self.P = 101325 # Sea-level pressure (Pa)
    def temperature(self):
        return 288.15 - (0.0065 * self.h)
    def pressure(self):
        T_kelvin = self.temperature()
        return self.P * (T_kelvin / 288.15) ** 5.256

for h in altitudes:
    atm = Atmosphere(h)
    
    T = atm.temperature()
    temperatures.append(T)
    
    P = atm.pressure()
    pressures.append(P)
    

# plot 1
plt.figure()
plt.plot(temperatures,altitudes)
plt.xlabel("Temperature (C)")
plt.ylabel("Altitude (m)")
plt.title("Temperature vs Altitude")
plt.grid()

# plot 2
plt.figure()
plt.plot(pressures, altitudes)
plt.xlabel("Pressure (Pa)")
plt.ylabel("Altitude (m)")
plt.title("Pressure vs Altitude")
plt.grid()

plt.show()