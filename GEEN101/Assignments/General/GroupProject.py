# Subsystem Class 1 - Atmosphere Temperature

def compute_temperature(m):
    T = 288.15 - 0.0065 * m
    return T

# Subsytem Class 2 - Mach Calculator

def compute_mach(V,a):
    M = V / a
    return M

# Subsystem Class 3 - Flight Regime

def classify_regime(M):
    if M < 0.8:
        return "Subsonic"
    elif M <= 1.2:
        return "Transonic"
    else:
        return "Supersonic"

# Main System CLass - FLight Condition Evaluator

def evaluate_flight_condition(V,a,m,T):
    M = compute_mach(V,a)
    regime = classify_regime(M)
    T = compute_temperature(m)
    m
    return m,T,M,regime

    # inputs
m = 1000
V = 500


    # given
a = 340
T = 288.15 - 0.0065 * m

    # print values
alt_val,temp_val, mach_val, regime_val = evaluate_flight_condition(V,a,m,T)
print(f"Altitude = {alt_val} meters, Temperature = {temp_val}°K, Mach = {mach_val:.3f}, Regime = {regime_val}")

