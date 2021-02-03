import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(1, 10)
s = 2 * t ^ 2
temp, ax = plt.subplots()
ax.plot(t, s, "r--")
ax.plot(t, s, "ko")

ax.set(xlabel='Days', ylabel='Stress Levels',
       title='My Brain')
plt.show()
