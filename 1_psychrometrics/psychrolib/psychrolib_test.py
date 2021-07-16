import psychrolib, psychrochart
psychrolib.SetUnitSystem(psychrolib.SI)

# psychrolib methods testing  
TDewPoint = psychrolib.GetTDewPointFromRelHum(30.0, 0.80)
Sat_deg = psychrolib.GetDegreeOfSaturation(30.0, 0.80, 101325)
Da_density = psychrolib.GetDryAirDensity(30.0, 101325)
Psy_props = psychrolib.CalcPsychrometricsFromRelHum(30.0, 0.80, 101325)

print(f'TDewPoint: {TDewPoint} C°')
print(Psy_props)



