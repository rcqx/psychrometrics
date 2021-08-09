#import resources
import matplotlib.pyplot as plt
from psychrochart import PsychroChart, load_config

#preconfig chart
chart = PsychroChart()
#plot
chart.plot(ax=plt.gca())

# Add labelled points and conexions between points
points = {'exterior': {'label': 'fresh Air',
                       'style': {'color': [0.592, 0.745, 0.051, 0.9],
                                 'marker': 'o', 'markersize': 10},
                       'xy': (4.0, 70.0)},
          'Return Air': {'label': 'Return Air',
                       'style': {'color': [0.592, 0.745, 0.051, 0.9],
                                 'marker': 'o', 'markersize': 15},
                       'xy': (25.0, 50.0)},
          'Mix': {'label': 'Adiabatic mixture',
                       'style': {'color': [0.855, 0.004, 0.278, 0.8],
                                 'marker': 'X', 'markersize': 10},
                       'xy': (19.5, 58.0)}}
connectors = [{'start': 'exterior',
               'end': 'Return Air',
               'label': 'Adiabaric Process Line',
               'style': {'color': [0.573, 0.106, 0.318, 0.7],
                         "linewidth": 2, "linestyle": "-."}}]

chart.plot_points_dbt_rh(points, connectors)

# Add a legend to chart
chart.plot_legend(markerscale=.7, frameon=False, fontsize=10, labelspacing=1.2)
#plot
chart.plot_points_dbt_rh(points, connectors)

plt.show()
