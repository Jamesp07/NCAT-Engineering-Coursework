# GEEN101 - Week 1 Lab
# System Model: Flight Condition Evaluator

V = 250.0 
# velocity in m/s
a = 340.0 
# speed of sound in m/s

M = V / a
# Equation

print(f"Mach number test = {M:.3f}")



# Modify The System Inputs



V = 150
a = 340.0 

X = V / a

print(f"Mach number Case 1 = {X:.3f}")
# Case 1: Subsonic



V = 250
a = 340.0

Z = V / a

print(f"Mach number Case 2 = {Z:.3f}")
# Case 2: Subsonic



V = 450
a = 340.0 

G = V / a

print(f"Mach number Case 3 = {G:.3f}")
# Case 3: Supersonic



V = 1685
a = 340.0

Y = V / a

print(f"Mach number Case 4 = {Y:.3f}")
# Case 4: Supersonic

