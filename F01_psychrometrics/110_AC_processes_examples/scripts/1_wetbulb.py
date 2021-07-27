import psychrolib as psy 
import psychrochart as chart
psy.SetUnitSystem(psy.SI)

Wt40 = psy.GetHumRatioFromEnthalpyAndTDryBulb(60000.0, 40.0)

W = Wt40 * 1000

Wb2 = psy.GetTWetBulbFromHumRatio(2.0, 0.004363635463664969, 101325.0)

Wb40 = psy.GetTWetBulbFromHumRatio(40.0, 0.004363635463664969, 101325.0)

rh40 = psy.GetRelHumFromTWetBulb(40.0, 18.403213500323155, 101325.0)

print(W)

print(Wb2, Wb40, rh40)