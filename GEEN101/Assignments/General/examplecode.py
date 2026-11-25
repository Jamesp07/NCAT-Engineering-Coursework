import math as mat
# h = 5000

# if h < 11000:
#    T = 15.04 - 0.00649*h 
# elif h < 25000:
#    T = -56.46
# else:
#    T = -131.21 + 0.00299*h

# print(T)

import numpy as np
h = np.array([0, 5000, 10000, 150000, 30000])

if h < 11000:
    T = 15.04 - 0.00649*h 
    p = 101.29 * ((T + 273.1)/288.08)**5.256
elif h < 25000:
    T = -56.46
    p = 22.65 * mat.exp(1.73 - 0.000157*h)
else:
    T = -131.21 + 0.00299*h 
    p = 2.488 * ((T + 273.1)/216.6)**(-11.388)
    
print(f"Temperature at altitude: {T}")
print(f"Pressure at altitude: {p}")

