import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.widgets import Slider

TWOPI = 2*np.pi

fig,ax = plt.subplots(2, 2, gridspec_kw={
                                        'wspace':0.2,
                                        'hspace':0.2,
                                        'width_ratios':[1,2],
                                        'height_ratios':[1,2]})
circle_ax = ax[0][0]
sin_ax = ax[0][1]
cos_ax = ax[1][0]
ax[1][1].set_visible(False)

circle_ax.set_xlim((-1,1))
circle_ax.set_ylim((-1,1))
sin_ax.set_xlim((0,TWOPI))
sin_ax.set_ylim((-1,1))
cos_ax.set_xlim((-1,1))
cos_ax.set_ylim((TWOPI,0))

circle_ax.axhline(0, color='k',linewidth = 0.5)
circle_ax.axvline(0, color='k',linewidth = 0.5)
sin_ax.axhline(0, color='k',linewidth = 0.5)
sin_ax.axvline(np.pi, color='k',linewidth = 0.5)
cos_ax.axhline(np.pi, color='k',linewidth = 0.5)
cos_ax.axvline(0, color='k',linewidth = 0.5)

circle = plt.Circle((0,0), 1, fill = False)
circle_ax.add_artist(circle)
line_sin, = circle_ax.plot([1,1],[0,0],color = 'r',linewidth = 3)
line_cos, = circle_ax.plot([0,1],[-1,-1],color = 'r',linewidth = 3)
line_m, = circle_ax.plot([0,1],[0,0],color = 'b',linewidth = 2)
line_cos1, = circle_ax.plot([0,1],[0,0],color = 'k',linestyle = ':',linewidth = 1)
line_sin1, = circle_ax.plot([0,0],[0,-1],color = 'k',linestyle = ':',linewidth = 1)
line_cos2, = circle_ax.plot([0,1],[0,0],color = 'k',linestyle = ':',linewidth = 1)
line_sin2, = circle_ax.plot([0,0],[0,-1],color = 'k',linestyle = ':',linewidth = 1)
redDot, = circle_ax.plot([1], [0], 'ro')

cos_y = np.arange(0.0, TWOPI, 0.001)
cos_x = np.cos(cos_y)
cos_line = cos_ax.plot(cos_x, cos_y)
redDot_cos, = cos_ax.plot(1, 0,'ro')
redline_cos, = cos_ax.plot([1,0],[0,0],color = 'r',linewidth = 2)
dotline_cos1, = cos_ax.plot([0,0],[0,0],color = 'k',linestyle = ':',linewidth = 1)
dotline_cos2, = cos_ax.plot([1,0],[0,0],color = 'k',linestyle = ':',linewidth = 1)

sin_x = np.arange(0.0, TWOPI, 0.001)
sin_y = np.sin(sin_x)
sin_line = sin_ax.plot(sin_x, sin_y)
redDot_sin, = sin_ax.plot(0, 0,'ro')
redline_sin, = sin_ax.plot([0,0],[0,0],color = 'r',linewidth = 2)
dotline_sin1, = sin_ax.plot([0,0],[0,0],color = 'k',linestyle = ':',linewidth = 1)
dotline_sin2, = sin_ax.plot([0,0],[0,0],color = 'k',linestyle = ':',linewidth = 1)

plt.subplots_adjust(bottom=0.2, left=0.3)
axcolor = 'lightgoldenrodyellow'
om1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor = axcolor)
som1 = Slider(om1, r'$\omega_1$', 0, TWOPI, valinit = 0)


def update(val):
    s1 = som1.val
    cos = np.cos(s1)
    sin = np.sin(s1)
    line_m.set_data([0,cos],[0,sin])
    line_sin.set_data([1,1],[0,sin])
    line_cos.set_data([0,cos],[-1,-1])
    line_cos1.set_data([cos,cos],[sin,-1])
    line_sin1.set_data([cos,1],[sin,sin])
    redDot.set_data([cos],[sin])
    redDot_sin.set_data([s1],[sin])
    redDot_cos.set_data([cos],[s1])
    redline_sin.set_data([s1,s1],[0,sin])
    redline_cos.set_data([0,cos],[s1,s1])
    dotline_sin1.set_data([0,s1],[0,0])
    dotline_sin2.set_data([0,s1],[sin,sin])
    dotline_cos1.set_data([0,0],[0,s1])
    dotline_cos2.set_data([cos,cos],[0,s1])
    fig.canvas.draw_idle()

som1.on_changed(update)

plt.show()
