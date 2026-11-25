# GEEN101 James Pridgen 10/1

#Step A1
def compute_mach(V,a):
    M = V / a
    return M

#Step A2
#print(compute_mach(V,a))
print("A. Mach Calculations")
print(f"V = 200 m/s | M = {compute_mach(200,340):.2f}")
print(f"V = 300 m/s | M = {compute_mach(300,340):.2f}") 
print(f"V = 450 m/s | M = {compute_mach(450,340):.2f}")

print("-----------------------")

#Step B1
def classify_regime(M):
    if M < 0.8:
        return "Subsonic"
    elif M <= 1.2:
        return "Transonic"
    else:
        return "Supersonic"

#Step B2
print("B. Regime Calculations")
print(f"M = 0.55 | Regime = {classify_regime(0.55)}")
print(f"M = 0.95 | Regime = {classify_regime(0.95)}")
print(f"M = 1.35 | Regime = {classify_regime(1.35)}")

print("-----------------------")

#Step C1
def evaluate_flight_condition(V,a):
    M = compute_mach(V,a)
    regime = classify_regime(M)
    return M,regime                 # 

#Step C2
print("C. Flight Conditions")

velocities = [150,250,350,450,600]
a = 340

for V in velocities: 
    mach_val, regime_val = evaluate_flight_condition(V, a)
    print(f"V = {V} -> Mach = {mach_val:.3f} -> {regime_val}")
# Take each value in the list, temporarily name it V, calculate, print, then move to next
# then name the first value from the output mach value and the second value regime value






