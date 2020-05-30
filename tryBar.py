import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider


TWOPI = 2*np.pi

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2, left=0.3)

t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)
l = plt.plot(t, s)
redDot, = plt.plot([0], [np.sin(0)], 'ro')

ax = plt.axis([0,TWOPI,-1,1])

axcolor = 'lightgoldenrodyellow'
om1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor = axcolor)
som1 = Slider(om1, r'$\omega_1$', 0, TWOPI, valinit = 0)

def spv(i):
    return (i, np.sin(i))
def update(val):
    s1 = som1.val
    x,y = spv(s1)
    redDot.set_xdata(x)
    redDot.set_ydata(y)
    fig.canvas.draw_idle()

som1.on_changed(update)    

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

# create animation using the animate() function
#myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
 #                                     interval=10, blit=True, repeat=True)

plt.show()
