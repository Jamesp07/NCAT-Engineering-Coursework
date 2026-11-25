import numpy as np                          # Imports NumPy, a library designed for computing, shortened to np

h = np.array([0, 2000, 4000, 6000, 8000]) # altitude in meters
T = np.array([288.15, 275.15, 262.15, 249.15, 236.15]) # temperature in kelvin



# Temperature at 4000 meters

T_4000 = T[h == 4000]                       # h when T = 4000
print(f"Temperature at 4000m: {T_4000}K")
# Printing text with the value in the bracket replaced by the defined value



# Change in temperature from 0 meters to 8000 meters

T_0 = T[h == 0]                             # h when T = 0
T_8000 = T[h == 8000]                       # h when T = 8000

T_Change = T_8000 - T_0                     # defining difference

print(f"Temperature change from 0m to 8000m: {T_Change}K")
# Same explanation as original print value but this time its printing a calculation



# Mean Calculation
import statistics                           # Imports Python's Statistics Module

mean_1 = statistics.mean(T)                 # Defining the mean of the temperature array

print(f"Mean temperature: {mean_1}K")
# This time its printing the statistic mean



# Step B1 - Velocity Array



V = np.array([150,200,250,300,400]) # Velocity in m/s
a = 340                   # Velocity in m/s (Speed of Sound)

M = V / a                                   # Mach number of all values

print( )                                    # Printing a space for better readability
print("Mach numbers of array values:")      # Printing text to explain values
print(M)                                    # Printing values



# Classifications
print("Classifcations:")                    # Category
conditions = [ M < 0.8,                     # Rule for Subsonic, Conditions command initiates classification
              (M >= 0.8) & (M <=1.2),       # Rule for Transonic
              M > 1.2]                      # Rule for Supersonic

labels = ["Subsonic", "Transonic", "Supersonic"] # Matching each rule with its text classification

classifications = np.select(conditions, labels, default="Unkown") # Uses NumPy to automatically match values and defines fallback as unkown

for mach_val, category in zip(M, classifications): #Line1
    print(f"Mach: {mach_val:.2f} -> {category}")   #Line2
# In order of function, Line1 groups together the M array output and the classification output
# while Line2 sets the parameters for each printed value as the mach number shortened to 2 decimals -> printed classification



# Acknowledgement
# AI was used in the creation of this script, and all code was physically typed by me.
# I have taken precaution to use AI responsibly by asking it to explain each part of
# an example line's function, where I would then replace values and titles as needed for my
# own code. I have created comments for each line as a sort of note taking system in case I
# planned to reuse some of these functions in the future.
# In this acknowledgement, I verify that I possess the knowledge to explain all of the code
# typed prior and I verify that I will continue to practice ethical AI usage.
print("Thank You.")