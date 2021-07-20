# Moist air sensible heating example

import psychrolib as psy 
import psychrochart as chart
psy.SetUnitSystem(psy.SI)


# Moist air, saturated at 2°C, enters a heating coil at a rate of
# 10 m 3 /s. Air leaves the coil at 40°C. Find the required rate of heat addition.

# calculate values of t1
h = psy.GetSatAirEnthalpy(2, 101325)

print(h) 

psy.GetSatAirEnthalpy