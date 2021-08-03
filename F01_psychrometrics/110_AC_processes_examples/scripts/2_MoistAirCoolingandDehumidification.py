# Moist air cooling and dehumidification 

import psychrolib as psy 
import psychrochart as chart
psy.SetUnitSystem(psy.SI)

# Moist air at 30°C dry-bulb temperature and 50% rh enters a cooling coil 
# at 5 m3/s and is procesed to a final saturation condition at 10°C. 
# Find the kW of refrigeration required

# 1 q 2 = m da [ ( h 1 – h 2 ) – ( W 1 – W 2 ) h w2 ]

# Values at t1; 30°C @50rh
W1_Kgw = psy.GetHumRatioFromRelHum(30.0, 0.5, 101325.0) # W value on kgw / kgda
W1 = W1_Kgw * 1000

h1_kg = psy.GetMoistAirEnthalpy(30.0, W1_Kgw) # j kgda
h1_g = h1_kg / 1000 # g kgda

# Values at t2; 10°C Sat

W2_Kgw = psy.GetHumRatioFromRelHum(10.0, 1.0, 101325.0)
W2 = W2_Kgw * 1000


h2_kg = psy.GetSatAirEnthalpy(10.0, 101325.0) # j kgda
h2_g = h2_kg / 1000 # g kgda


print(W2_Kgw)
print(W2)

