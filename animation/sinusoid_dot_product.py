import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox

fig, ax = plt.subplots(3, 1, 
                       gridspec_kw={
                        'height_ratios': [1, 1, 1]},
                       figsize=(6, 7))
plt.subplots_adjust(left = 0.1, bottom = 0.2, wspace = 0.2,hspace = 0.5)

TWOPI = 2 * np.pi
x = np.arange(0,TWOPI,0.5)
x_plus = np.arange(-1/2 * np.pi,TWOPI - 1/2 * np.pi,0.5)
y_sin = np.sin(x_plus)
y_cos = np.cos(x)
y_dot = y_sin * y_cos

ax[0].plot(x,np.sin(x))
line1, = ax[0].plot(x,y_sin)
ax[1].hist(x[:-1], bins = x,alpha=0.5,
                          edgecolor='#EFB28C',
                          color='#EED19C', weights = y_cos[:-1])
ax[1].stem(x,y_cos,markerfmt=',',use_line_collection=True)
ax[2].plot(x,y_dot)
ax[2].plot(x,y_cos * np.sin(x))


ax[0].axes.xaxis.set_ticklabels([])
ax[0].axes.yaxis.set_ticklabels([])

def submit(text):
    global line1
    try:
        float(text)
    except ValueError:
        return
    line1.remove()
    x_plus = np.arange(float(text),TWOPI + float(text),0.5)
    y_sin = np.sin(x_plus)
    line1, = ax[0].plot(x,y_sin)
    plt.draw()

axbox = plt.axes([0.2, 0.05, 0.5, 0.07])
text_box = TextBox(axbox, 'Evaluate', initial='hellp')
text_box.on_submit(submit)

plt.show()
