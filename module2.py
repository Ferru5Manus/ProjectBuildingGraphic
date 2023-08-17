import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

ax.plot([1,4],[1,4])

ax.add_patch(
     patches.Rectangle(
        (1, 1),
        0.5,
        0.5,
        edgecolor = 'blue',
        facecolor = 'red',
        fill=True
     ) )

plt.show()