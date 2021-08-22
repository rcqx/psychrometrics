import matplotlib.pyplot as plt
from psychrochart import PsychroChart, load_config

#preconfig chart
chart = PsychroChart()

#append zones

#plot
chart.plot(ax=plt.gca())

# Add labelled points and conexions between points
points = {'exterior': {'label': 'Outside Air',
                       'style': {'color': [0.855, 0.004, 0.278, 0.8],
                                 'marker': 'X', 'markersize': 10},
                       'xy': (30.0, 50.0)},
          'interior': {'label': 'Supply Air',
                       'style': {'color': [0.592, 0.745, 0.051, 0.9],
                                 'marker': 'o', 'markersize': 15},
                       'xy': (10.0, 100.0)}}
connectors = [{'start': 'exterior',
               'end': 'interior',
               'label': 'Process 1',
               'style': {'color': [0.573, 0.106, 0.318, 0.7],
                         "linewidth": 2, "linestyle": "-."}}]

chart.plot_points_dbt_rh(points, connectors)

# Add a legend
chart.plot_legend(markerscale=.7, frameon=False, fontsize=10, labelspacing=1.2)

plt.show()
