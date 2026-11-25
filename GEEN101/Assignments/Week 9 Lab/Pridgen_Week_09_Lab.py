# Using the class from our group assignment,

import math
import matplotlib.pyplot as plt


class FlightConditionEvaluationSystem:

  def __init__(self, V, Alt):
    self.V = V
    self.h = Alt
    self.a = 340
    self.P = 101325
    self.T = self.temperature()
    self.va = math.sqrt(1.4 * 287 * self.T)
    self.M = self.compute_mach()
    self.VM = self.compute_variablemach()

  def temperature(self):
    return 288.15 - (0.0065 * self.h)

  def compute_mach(self):
    return self.V / self.a

  def compute_variablemach(self):
    return self.V / self.va


h = list(range(0, 15100, 100))
velocities = [250, 300, 320, 350]

plt.figure(figsize=(9, 5))

for v in velocities:
  vm_values = []
  crossing_alt = None
  for alt in h:
    system = FlightConditionEvaluationSystem(v, alt)
    vm_values.append(system.VM)
    if crossing_alt is None and system.VM >= 1.0:
      crossing_alt = alt
      crossing_mach = system.VM
  plt.plot(h, vm_values, label=f"V = {v} m/s")
  if crossing_alt is not None:
    print(f"V = {v} m/s crosses Mach 1 at approximately {crossing_alt} m")
    plt.plot(crossing_alt, crossing_mach, marker="o", markersize=8, color="red")
    plt.annotate(
        f"Mach 1 @ {crossing_alt} m",
        xy=(crossing_alt, crossing_mach),
        xytext=(crossing_alt + 400, crossing_mach - 0.05),
    )


plt.axhline(1.0, color="black", linestyle="--", label="Mach = 1.0 (Sonic)")

plt.title("Variable Mach vs. Altitude & Mach 1 Transition")
plt.xlabel("Altitude (m)")
plt.ylabel("Variable Mach Number (VM)")
plt.legend()
plt.grid(True)
plt.show()