# A stream of 2 m 3 /s of outdoor air at 4°C dry-bulb temperature and 2°C thermodynamic wet-bulb
# temperature is adiabatically mixed with 6.25 m 3 /s of recirculated air at 25°C dry-bulb
# temperature and 50% rh. Find the dry-bulb temperature and thermodynamic wet-bulb temperature 
# of the resulting mixture.

import psychrolib as psy
psy.SetUnitSystem(psy.SI)

# OA --> 4°C drybulb, 2°C wetbulb
# RA --> 25°C drybulb, 50% rh
# MIX --> drybulb and wetbulb temperatures????

# L3-2/1-3 = mda1/mda2 or L1-3/1-2 = mda2/mda3

#t1 4°C DB, 2°C WB, 2m3/s
v1 = psy.GetDryAirVolume(4.0, 101325.0)
mda1 = 2.0 / v1
print(mda1)
#t2 25°C DB, 50% rh, 6.25 m3/s
v2 = psy.GetDryAirVolume(25.0, 101325.0)
mda2 = 6.25 / v2
print(mda2)
#t3
mda3 = mda1 + mda2
print(mda3)
# L1-3/1-2 = mda2/mda3
Line3 = mda2 / mda3
print(Line3)

#Line1-2 = 21 units
#Point 3 = 21 * 0.743
point3 = 21 * 0.743
print(point3)
