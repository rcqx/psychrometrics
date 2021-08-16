from psychrochart import PsychroChart
import matplotlib.pyplot as plt

PsychroChart('ashrae').plot(ax=plt.gca())

plt.show()