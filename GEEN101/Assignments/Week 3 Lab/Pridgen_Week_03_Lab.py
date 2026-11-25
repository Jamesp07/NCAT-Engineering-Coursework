#GEEN101 James Pridgen 9/29

print("Part A")
V = 300.0 # Velocity (m/s)
a = 340.0 # Speed of Sound (m/s)
M = V / a # Mach Number
if M < 0.8: 
    regime = "Subsonic"
elif M <= 1.2: 
    regime = "Transonic"
else: 
    regime = "Supersonic"
print(f"Mach = {M:.3f} | Regime = {regime}")



print("Part B")
V_values = [150,250,300,400,500] # m/s
a = 340.0 # m/s

for V in V_values:
    M = V / a
    if M < 0.8: 
        regime = "Subsonic"
    elif M <= 1.2: 
        regime = "Transonic"
    else: 
        regime = "Supersonic"
    print(f"V = {V:.1f} m/s | Mach = {M:.3f} | Regime = {regime}")
# Print velocity to one decimal point, Mach number to 3
# decimal points, and print regime