import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
from matplotlib import gridspec
from matplotlib.patches import Arrow

TWOPI = 2*np.pi

fig = plt.figure(figsize = (10, 4))
gs = gridspec.GridSpec(1, 2, width_ratios=[1,2])
plt.subplots_adjust(bottom=0.3)
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])

ax1.set_xlim((0, TWOPI))
ax1.set_ylim((-1.3, 1.3))
t = np.arange(0.0, TWOPI, 0.001)
s = np.cos(t)
l = ax1.plot(t, s)
redDot, = ax1.plot([0], [np.cos(0)], 'ro')

circle = plt.Circle((0,0), 1, fill = False)

ax0.set_xlim((-1.3, 1.3))
ax0.set_ylim((-1.3, 1.3))
ax0.add_artist(circle)
line0, = ax0.plot([0,1],[0,0],color = 'k', linewidth = 2)
line1, = ax0.plot([0,1],[0,0],color = 'b', linewidth = 2)
line2, = ax0.plot([1,1],[1,1],color = 'k',linestyle = ':', linewidth = 1)
line3, = ax0.plot([0,1],[0,0],color = 'r', linewidth = 1.5)


axcolor = 'lightgoldenrodyellow'
om1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor = axcolor)
som1 = Slider(om1, r'$\omega_1$', 0, TWOPI, valinit = 0)

def spv(i):
    return (i, np.cos(i))
def update(val):
    s1 = som1.val
    x,y = spv(s1)
    sin = np.sin(x)
    cos = y
    redDot.set_xdata(x)
    redDot.set_ydata(y)
    line1.set_data([0,cos],[0,sin])
    line2.set_data([cos,cos],[0,sin])
    line3.set_data([0,cos],[0,0])
    fig.canvas.draw_idle()

som1.on_changed(update)    


plt.show()
