import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(3, 1, 
                       gridspec_kw={
                        'height_ratios': [1, 1, 1]})

TWOPI = 2 * np.pi
x = np.arange(0,TWOPI,0.5)
x_plus = np.arange(-1/2 * np.pi,TWOPI - 1/2 * np.pi,0.5)
y_sin = np.sin(x_plus)
y_cos = np.cos(x)
y_dot = y_sin * y_cos

ax[0].plot(x,np.sin(x))
ax[0].plot(x,y_sin)
ax[1].hist(x[:-1], bins = x,alpha=0.5,
                          edgecolor='#EFB28C',
                          color='#EED19C', weights = y_cos[:-1])
ax[1].stem(x,y_cos,markerfmt=',',use_line_collection=True)
ax[2].plot(x,y_dot)
ax[2].plot(x,y_cos * np.sin(x))


ax[0].axes.xaxis.set_ticklabels([])
ax[0].axes.yaxis.set_ticklabels([])

plt.show()
