# 1. PSYCHROMETRICS
Psychrometrics are the study of physical and thermodynamic properties of moist air, i.e.,
the use of thermodynamic properties to analyse conditions and processes involving moist air.

## 1.1 Dry and moist air composition
**Atmospheric air**  --->  Contains gaseous components as well as water vapor and miscellaneous contaminants

**Dry air**  --->  Atmospheric air with all water vapor and contaminants removed. 

**Moist air**  --->  Mixture of dry air and water vapor. The amount of water vapor varies from zero (dry air) to a maximum that 
depends on temperature and pressure. 

**Saturation**  --->  State of equilibrium between moist air and condensed water phase (liquid or solid).  

## 1.2 Standard atmosphere
Temperature and barometric pressure of air varies with altitude and with local geographic and weather conditions.
The standard atmosphere allows to estimate properties at various altitudes.

**Standard values**

Temperature  --->  15C°

Barometric pressure  --->  101.325 kPa

Gravity  --->  9.80665 m/s2

Lower atmophere is assumed to consist of dry air that behaves as a perfect gas

![image info](./static/table_1.png)

## 1.3 Moist air thermodynamic properties
Based on International Temperature Scale (ITS-90). Thermodynamic Properties of Moist Air at Standard Atmospheric Pressure, 101.325kPa

* Humidity ratio at saturation **( Ws )**   

* Specific volume of dry air **( Vda )**

* Specific volume difference of Vs - Vda **( Vas )**

* Specific volume of moist air at saturation **( Vs )**
 
* Specific enthalpy of dry air **( Vda )**

* Specific enthalpy difference of Hs - Hda **( has )** 

* Specific enthalpy of moist air at saturation **( hs )**

* Specific entropy of dry air **( Sda )**

* Specific entropy of moist air at saturation **( Ss )** 

![image info](./static/table_2.png)

## 1.4 Thermodynamic properties of water at saturation (saturated liquid)
Based on ITS-90. For detailed formulas refered to ASHRAE fundamentals, 2017.

The water vapor saturation pressure ( pws ) is required to determine
a number of moist air properties, principally the saturation humidity ratio ( Ws )

* Absolute pressure (saturation pressure)  **( Pws )**
* Vapor pressure ( ps ) can be used in equations in place of pws with very little error: 

		ps = Xws P 

where x ws is the mole fraction of water vapor in saturated moist air
at temperature t and pressure p, and p is the total barometric pressure
of moist air.

![image info](./static/table_3.png)

## 1.5 Humidity parameters

### Basic parameters

1. **Humidity ratio _W_ (or mixing ratio)**

Ratio of the mass of water vapor to the mass of dry air:

	W = M w /M da

Where equals the mole fraction ratio x w /x da multiplied by the ratio of
molecular masses:

	W = 0.621945 ( xw / xda ) 

2. **Specific humidity**

Ratio of the mass of water vapor to total mass of moist air sample 

	Y = M w /(M w + M da )

In terms of humidity ratio:

	Y =  W / (1 + W)

3. **Absolute humidity (water vapor density)** 

Ratio of the mass of water vapor to total volume sample 

	d v = M w / V

4. **Density** (of a moist air mixture) 

Ratio of total mass to total volume

	p = ( M da + M w ) / V = ( 1/v )( 1 + W )

Where v is the moist air specific volume, m3/kgda

### Humidity parameters involving saturation (moist air saturation)

1. **Saturation humidity ratio _W s ( t, p )_**

Humidity ratio of moist air saturated to water at a same temperature and pressure 

2. **Relative humidity _RH_**

Ratio of water vapor partial pressure in moist air at dew-point pressure and temperature to 
the reference saturation water vapor partial pressure ar dry-bulb pressure and temperature.

In layman's terms, tells us how much water vapor is in the air, compared to how much it could hold at that temperature. It is shown as a percent

	( phi ) = ( p wv _ enh /p wvs _ ref | p,t ) = [ f ( p, t dp ) e (t dp ) ] / [ f ( p, t db ) e ( t db )]

3. **Dew-point temperature _(td)_**

Temperature of moist air saturated at pressure, with same humidity ratio W as that of the
given sample of moist air.  

Put simply, is the temperature the air needs to be cooled to (at constant pressure) in order to achieve a relative humidity (RH) of 100%.

	W s ( p, t d ) = W

4. **Thermodynamic wet-bulb temperature _(t)_** 

Temperature at which water, by evaporating into moist air at dry-bulb temperature and humidity ratio,
can bring air to saturation adiabatically at the same temperture while total pressure is constant. 

## 1.6 Perfect gas relationships for dry and moist air

When moist air is considered a mixture of independent perfect gases (dry air and water vapor), perfect gas equation (pV=nRT)  can be 
assumed for each.

### Dry Air

	p ( da ) V = n ( da ) RT

### Water vapor
 
	p ( w ) V = n ( w ) RT

### The mixture also obeys the perfect gas equation:

	( pda + pw ) V = ( nda + nw ) RT

###  Humidity ratio (_W_) (p = pda + pw)

	W = 0.621945 ( pw / p - pw )

### Saturation humidity ration (_Ws_) is:

	Ws = 0.621945 ( pws / p - pws )

Where:

pda = Partial pressure of dry air

pw = Partial pressure of water vapor

V = Total mixture volume

nda  = Number of moles of dry air

nw = Number of moles of water vapor

R = Universal gas constant, 8314.472 (kmol.K) 

T = Absolute temperature, K 

The enthalpy _(h)_ of a mixture of perfect gases equals the sum of the
individual partial enthalpies of the components. Specific enthalpy of moist air equals:

	h = h da + W hg

Where h da = Specific h for dry air in kJ /kgda and hg is the specific enthalpy for saturated
water vapor un kg / kgw at the mixture's temperature. As an aprox: 

	h da =  1.006t
	h g  =  2501 + 1.86t

where _t_ = dry-bul temperature in C°. The moist air specific
enthalpy in kJ / kg da then becomes:

	h = 1.006t + W ( 2501 +  1.86t )

## 1.7 Thermodynamic wet-bulb and dew-point temperature

For any moist air, a temperature _t_ exist at which liquid water evaporates into the air to bring it 
to saturation at the same _t_ and total pressure (Harrison, 1965). During this adiabatic saturation, 
saturated air is expelled at a _t_ = to that of the injected water. 

In this constant-pressure process:

* _W_ = increases from initial _W_ to _Ws_
* _h_ = increases from _h_ to hs
* Energy conservation (h) requires: 

	
	h + (W s * – W)h w * = h s 


The value of _t_ that satifies _h_, _W_, and _p_ is the **thermodynamic wet-bulb temperature**

 







