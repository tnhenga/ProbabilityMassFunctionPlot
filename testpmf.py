from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
from random import uniform

colors = ['b', 'g', 'r', 'y']

q = binom(20, 0.5)
q2 = binom(20, 0.7)
q3 = binom(40, 0.5)

obs = q.rvs(1000)

grid = np.linspace(0, 20, 21)
y = q.pmf(grid)

grid2 = np.linspace(0, 20, 21)
y2 = q2.pmf(grid2)

grid3 = np.linspace(0, 40, 41)
y3 = q3.pmf(grid3)



fig, ax = plt.subplots( figsize = (10, 6) )
ax.hist(obs, bins = 50, density = True)
ax.plot(grid, q.pmf(grid), 'k-', linewidth = 2, label = "n=20 & p=0.5")
plt.legend(loc="upper right")
fig.suptitle('Problem 2 Part 1', fontsize = 30)
ax.set_xlabel('n vals', fontsize = 20)
ax.set_ylabel('pmf of n vals', fontsize = 20)
#ax.scatter(grid, y)

fig, ax1 = plt.subplots( figsize = (10, 6) )
#ax1.hist(obs, bins = 40, density = True)
#ax1.plot(grid, q.pmf(grid), 'b.', label = "n=20 & p=0.5")
#ax1.plot(grid2, q2.pmf(grid2), 'g^', label = "n=20 & p=0.7")
#ax1.plot(grid3, q3.pmf(grid3), 'r*', label = "n=20 & p=0.7")
ax1.scatter(grid, y, marker='x', color=colors[3], label = "n=20 & p=0.5")
ax1.scatter(grid2, y2, marker='+', label = "n=20 & p=0.7")
ax1.scatter(grid3, y3, marker='*', label = "n=40 & p=0.5")
plt.legend(loc="upper right")
fig.suptitle('Problem 2 Part 2', fontsize = 30)
ax1.set_xlabel('n vals', fontsize = 20)
ax1.set_ylabel('pmf of n vals', fontsize = 20)


plt.show()

