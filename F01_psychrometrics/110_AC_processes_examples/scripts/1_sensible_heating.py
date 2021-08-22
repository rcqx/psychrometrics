# Moist air sensible heating example
# Moist air, saturated at 2°C, enters heating coil at 10 m 3 /s rate 
# Air leaves the coil at 40°C. Find required rate of heat addition (1q2)
# 1q2 = m da (h2 - h1)

import psychrolib as psy 
import psychrochart as chart
psy.SetUnitSystem(psy.SI)

# Mass flow air is given in cubic meters over secs (m3/s)
mass_f = 10.0 

# Calculate initial values of t1 (2°C)   
# Enthalpy 
h_J1 = psy.GetSatAirEnthalpy(2.0, 101325.0)

# Value is given in Joules (J), kJ conversion  
h_kJ1 = h_J1 / 1000

# Humidity ratio of t1
W_Kg1 = psy.GetHumRatioFromEnthalpyAndTDryBulb(h_J1, 2.0)

# Value is given in Kg w / Kg da, g w/ kg da conversion
W_g1 = W_Kg1 * 1000

# Specific volume of dry air 
v1 = psy.GetDryAirVolume(2.0, 101325)

# Initial values for t2 (40°C)
h_J2 = psy.GetMoistAirEnthalpy(40.0, W_Kg1)

# Return value is in J kg, conversion to Kj/kg da 
h_kJ2 = h_J2 / 1000

# Mass of dry air in Kg da / s 
mda = mass_f / v1

# q = Rate of heat needed to increase air temp from 2°C to 40°C with constant W
# q = mda ( h2 -h1) in kW
q = mda * (h_kJ2 - h_kJ1) 

print(q)



