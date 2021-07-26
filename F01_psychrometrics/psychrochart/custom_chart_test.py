import matplotlib.pyplot as plt
from psychrochart import PsychroChart, load_config
import matplotlib.pyplot as plt

#preconfigured style
#chart('ashrae').plot(ax=plt.gca())
#plt.show()

# Get a preconfigured style dict
config_minimal = load_config("minimal")

# Customize it
config_minimal['figure']['x_label'] = None
config_minimal['figure']['y_label'] = None
config_minimal['saturation']['linewidth'] = 3
config_minimal['chart_params']['with_constant_dry_temp'] = False
config_minimal['chart_params']['with_constant_humidity'] = False
config_minimal['chart_params']['with_constant_wet_temp'] = False
config_minimal['chart_params']['with_constant_h'] = False

print("** Customized style from preconfigured `minimal` style:")

minimal = PsychroChart(config_minimal)
chart_custom = PsychroChart('minimal').plot(ax=plt.gca())
plt.show()