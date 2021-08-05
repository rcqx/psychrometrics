# Moist air cooling and dehumidification 

import psychrolib as psy 
import psychrochart as chart
psy.SetUnitSystem(psy.SI)

# Moist air at 30°C dry-bulb temperature and 50% rh enters a cooling coil 
# at 5 m3/s and is procesed to a final saturation condition at 10°C. 
# Find the kW of refrigeration required

# mw = mda ( W 1 – W 2 )
# 1 q 2 = mda [ ( h 1 – h 2 ) – ( W 1 – W 2 ) hw2 ]
# mix flow rate = 5 m3/s
mass_f = 5.0

# Values at t1; 30°C @50rh
W1_Kgw = psy.GetHumRatioFromRelHum(30.0, 0.5, 101325.0) # W value on kgw / kgda
W1 = W1_Kgw * 1000.0

h1_kg = psy.GetMoistAirEnthalpy(30.0, W1_Kgw) # j kgda
h1_g = h1_kg / 1000.0 # g kgda

# Values at t2; 10°C Sat
W2_Kgw = psy.GetHumRatioFromRelHum(10.0, 1.0, 101325.0) 
W2 = W2_Kgw * 1000.0

h2_kg = psy.GetSatAirEnthalpy(10.0, 101325.0)
h2_g = h2_kg / 1000.0

# mass flow rate of dry air = volume flow / specific dry air volume
v1 = psy.GetDryAirVolume(30.0, 101325.0)

# mass of dry air
mda = mass_f / v1

# specific enthalpy of water at saturation at 10°C (hw2) kJ/kg w
hw2 = 40.02 

h = h1_g- h2_g
w = W1 - W2
hw = w * hw2

print(mda)
print( h1_g)
print(h2_g)
print(W1)
print(W2)
print(hw2)

# the rate of heat removal from the air  stream is:
# 1q2 = mda [(h1-h2)-(w1-w2)hw2]
# 1q2 = 