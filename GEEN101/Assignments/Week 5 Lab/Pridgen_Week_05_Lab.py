import numpy as np

# Part A1
class MachCalculator:
    def __init__(self,V,a):
        self.V = V
        self.a = a
    def compute_mach(self):
        return self.V / self.a


# Part A2
V = np.array([200,300,500])
a = 340

mc = MachCalculator(V,a)
mach_values = mc.compute_mach()

print("----- Part A2 Outputs -----")
for velocity, mach in zip(mc.V, mach_values):       # Zip pairs V values with mach values
    print(f"| Velo: {velocity:<3} m/s | Mach: {mach:.2f} |")


# Part B1
class FlightRegime:
    def __init__(self,M):
        self.M = M
    def classify_regime(self):
        regime = []                     # Line created from debugging by AI
        for m in self.M:
            if m < 0.8:
                regime.append("Subsonic  ")
            elif m <= 1.2:
                regime.append("Transonic ")
            else:
                regime.append("Supersonic")
        return regime


# Part B2
M = [0.55,0.95,1.35]

fr = FlightRegime(M)
regime_values = fr.classify_regime()

print("----- Part B2 Outputs -----")
for mach, regime in zip(fr.M, regime_values):
    print(f"| Mach: {mach:<3} | Regime: {regime} |")


# Part C1
class FlightConditionEvaluator:
    def __init__(self, V, a):
        self.V = V
        self.a = a
    def evaluate_conditions(self):
        calculator = MachCalculator(self.V, self.a)
        mach_array = calculator.compute_mach()
        regime_classifier = FlightRegime(mach_array)
        regimes = regime_classifier.classify_regime()
        return mach_array, regimes                         # Setting up final print values


# Part C2
V = np.array([150,250,350,450,600])
a = 340

ev = FlightConditionEvaluator(V,a)
mach_values, regime_values = ev.evaluate_conditions()

print("----- Part C2 Outputs -----")
for velo, mach, regi in zip(V, mach_values, regime_values):  # Flattens created from debugging by AI
    print(f"| V = {velo} -> Mach = {mach:.2f} -> Regime = {regi} |")
