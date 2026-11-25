# --------------------------------------------------------------------------- #
# Imported Libraries
# --------------------------------------------------------------------------- #

import math
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- #
# Defined values and flight condition evaluation system class
# --------------------------------------------------------------------------- #

h = [0,1000,2000,3000,4000,5000,6000] # Meters
Velocities = [0,100,300,500,700,900,1100] # Meters per Second

class FlightConditionEvaluationSystem:
    def __init__(self,V, Alt):
        self.V = V
        self.h = Alt
        self.a = 340
        self.P = 101325
        self.T = self.temperature()
        self.va = math.sqrt(1.4*287*self.T) #287 J/KgKelvin
        self.M = self.compute_mach()
        self.VM = self.compute_variablemach()
    
    def temperature(self):
        return 288.15 - (0.0065 * self.h)
    
    def compute_mach(self):
        return self.V / self.a
    
    def compute_variablemach(self):
        return self.V / self.va
        
    def pressure(self):
        T_kelvin = self.temperature()
        return self.P * (T_kelvin / 288.15) ** 5.256
    
    def classify_regime(self):
        if self.M<0.8:
            regime = "Subsonic"
        elif self.M<=1.2:
            regime = "Transonic"
        else:
            regime = "Supersonic"
        return self.M, regime
    
# --------------------------------------------------------------------------- #
# Printing Mach and Variable Mach comparison
# --------------------------------------------------------------------------- #

print(f"{'Altitude (m)'}, {'Velocity (m/s)'}, {'Mach (M)'}, {'Var Mach (VM)'}, {'Regime'}")

for alt, vel in zip(h, Velocities):
    system = FlightConditionEvaluationSystem(vel, alt)
    mach_val, regime = system.classify_regime()
    
    print(f"Alt: {alt}, Vel: {vel}, M: {mach_val:<1.2f}, VM: {system.VM:<1.2f}, Regime: {regime}")

# --------------------------------------------------------------------------- #
# Plotting Values
# --------------------------------------------------------------------------- #

T_result = []
va_result = []
VM_result = []
M_result = []
# Lists created in preparation for graphing

for alt, vel in zip(h, Velocities):
    system = FlightConditionEvaluationSystem(vel, alt)
    T_result.append(system.T)
    va_result.append(system.va)
    M_result.append(system.M)
    VM_result.append(system.VM)
# Making the arrays graphable 

# Plot 1: Alt vs T
plt.figure()
plt.plot(h, T_result, marker='o')
plt.xlabel("Altitude (m)")
plt.ylabel("Temperature (K)")
plt.title("Altitude vs. Temperature")
plt.grid(True)

# Plot 2: Alt vs a
plt.figure()
plt.plot(h, va_result, marker='o')
plt.xlabel("Altitude (m)")
plt.ylabel("Speed of Sound (m/s)")
plt.title("Altitude vs. Speed of Sound")
plt.grid(True)

# Plot 3: Alt vs M
plt.figure()
plt.plot(h, M_result, marker='o', label="Constant a (340 m/s)")
plt.plot(h, VM_result, marker='s', label="Variable a (Temperature-dependent)")
plt.xlabel("Altitude (m)")
plt.ylabel("Mach Number (M)")
plt.title("Altitude vs. Mach Number")
plt.legend()
plt.grid(True)

plt.show() # Show plots