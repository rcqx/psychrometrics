# Moist air at 20°C dry-bulb and 8°C thermodynamic wet-bulb temperature is to be processed to a 
# final dew-point temperature of 13°C by adiabatic injection of saturated steam at 110°C. 
# The rate of dry air-flow m · da is 2 kg da /s. Find the final dry-bulb temperature of the moist
# air and the rate of steam flow.

import psychrolib as psy
psy.SetUnitSystem(psy.SI)

# Find final dry bulb temperature of moist air  DBt 
# Find steam flow (mass fo water)

# formulas 
# h2 - h1 / W2 - w1 = hw
# mdw = mda (W2 - W1) =

# t1 = 20°C DB, 8°C WB
w1_kg = psy.GetHumRatioFromTWetBulb(20.0, 8.0, 101325.0)
w1 = w1_kg * 1000
h1_j = psy.GetMoistAirEnthalpy(20.0, w1_kg)
h1 = h1_j / 1000

# mw =  
# hw = 2691.07 Kg/kgw
# @ 110°C 

# t2 = 21°C
# h2 = 44.72 Kj/kgda
# w2 = 9.28 gw/kgda

w2_Kg = psy.GetHumRatioFromTWetBulb(21.0, 16.0, 101325.0)
w2 = w2_Kg * 1000.0
print(w2)
h2_J = psy.GetMoistAirEnthalpy(21.0, w2_Kg)
h2 = h2_J / 1000

# deltas
delta_h = h2 - h1 
delta_w = w2 - w1

hw = delta_h / delta_w

print(h2, h1)
print(w2_Kg, w1_kg)
print (delta_h, delta_w)
print(hw)