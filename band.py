#!/usr/bin/env python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['axes.linewidth'] = 1.5

bands = np.loadtxt('kband.dat')
EnergyWeight = np.loadtxt('bclr.dat')

fig, ax = plt.subplots()
fig.set_size_inches(3, 4)
ax.tick_params(which='both', labelsize='x-small')

norm = mpl.colors.Normalize(vmin=EnergyWeight.min(),
                            vmax=EnergyWeight.max())
c_m = mpl.cm.seismic_r
# create a ScalarMappable and initialize a data structure
s_m = mpl.cm.ScalarMappable(cmap=c_m, norm=norm)
s_m.set_array([EnergyWeight])

LW = 2.0
DELTA = 0.3

for ii in range(32):
    x = bands[:,0]
    y = bands[:,ii+1]
    z = EnergyWeight[:,ii]

    ax.plot(bands[:,0], bands[:,ii+1],
            lw=LW + 2 * DELTA,
            color='gray', zorder=1)

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap='seismic_r', # alpha=0.7,
                        norm=plt.Normalize(0, 1))
    lc.set_array((z[1:] + z[:-1]) / 2)
    lc.set_linewidth(LW)

    ax.add_collection(lc)

cbar = plt.colorbar(s_m)
cbar.ax.tick_params(which='both', labelsize='x-small')

ax.set_ylim(-4, 4)

# plt.show()
plt.savefig('kaka.png', dpi=300)
