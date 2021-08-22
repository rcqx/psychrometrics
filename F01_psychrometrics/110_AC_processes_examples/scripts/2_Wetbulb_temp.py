import psychrolib as psy
psy.SetUnitSystem(psy.SI)

wb = psy.GetTWetBulbFromRelHum(30.0, 0.5, 101325.0)


print(wb)

