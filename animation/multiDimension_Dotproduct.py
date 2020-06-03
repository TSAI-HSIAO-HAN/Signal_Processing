from matplotlib.widgets import TextBox,Button
import matplotlib.pyplot as plt
import numpy as np

#define constants
PI = np.pi
TWOPI = 2 * np.pi

#set and adjust figure
fig, ax = plt.subplots(3, 1,
                       gridspec_kw={
                           'height_ratios':[1,1,1]},
                       figsize = (6,7))
plt.subplots_adjust(left = 0.1, bottom = 0.3, wspace = 0.2, hspace = 0.5)

#define variables
dimension = 4
v1 = [-1,2,-3,4]
v2 = [1,3,5,7]
base_v = np.arange(dimension)
bins = np.arange(dimension+1)
dot_value = np.dot(v1, v2)

#
axbox0 = plt.axes([0.15, 0.2, 0.13, 0.05])
axbox1 = plt.axes([0.15, 0.13, 0.13, 0.05])
axbox2 = plt.axes([0.15, 0.06, 0.13, 0.05])
axbutton = plt.axes([0.3 ,0.06, 0.13, 0.05])

dimension_text = plt.text(1.3,2.4,'dimension: ' + str(dimension))
v1_text = plt.text(1.3,1.8,'vertex 1: ' + str(v1))
v2_text = plt.text(1.3,1.2,'vertex 2: ' + str(v2))
dot_text = plt.text(1.3, 0.4, 'dot product value: ' + str(dot_value))
button = Button(axbutton, 'show')

textbox0 = TextBox(axbox0, 'dimension')
textbox1 = TextBox(axbox1, 'vertex 1')
textbox2 = TextBox(axbox2, 'vertex 2')

def draw():
    multi = np.multiply(v1,v2)
    arr0 = ax[0].hist(base_v, bins = bins,weights = v1,alpha=0.5,
                              edgecolor='#EFB28C',
                               color='#EED19C')

    arr1 = ax[1].hist(base_v, bins = bins,weights = v2,alpha=0.5,
                              edgecolor='#EFB28C',
                               color='#EED19C')

    arr2 = ax[2].hist(base_v, bins = bins,weights = multi,alpha=0.5,
                              edgecolor='#EFB28C',
                               color='#EED19C')
    for i in range(dimension):
        ax[0].text(base_v[i]+0.4,v1[i],str(v1[i]))
        ax[1].text(base_v[i]+0.4,v2[i],str(v2[i]))
        ax[2].text(base_v[i]+0.4,multi[i],str(multi[i]))

def resetData(text):
    ax[0].cla()
    ax[1].cla()
    ax[2].cla()
    draw()

def setDimension(text):
    global dimension, v1, v2, base_v, bins, dot_value

    try:
        dimension = int(text)
        temp1 = [0] * dimension
        temp2 = [0] * dimension
        for i in range(min(len(v1), dimension)):
            temp1[i] = v1[i]
        for i in range(min(len(v2), dimension)):
            temp2[i] = v2[i]

        v1 = temp1
        v2 = temp2

        dimension_text.set_text('dimension: ' + str(dimension))
        v1_text.set_text('vertex 1: ' + str(v1))
        v2_text.set_text('vertex 2: ' + str(v2))
        base_v = np.arange(dimension)
        bins = np.arange(dimension+1)
        dot_value = np.dot(v1, v2)
        dot_text.set_text('dot product value: ' + str(dot_value))
    except ValueError:
        return

def setV1(text):
    global dimension, v1, v2, dot_value
    try:
        tempstr = text.split(',')
        templst = list(map(int, tempstr))
        lst = [0] * dimension
        for i in range(min(len(templst), dimension)):
            lst[i] = templst[i]
        v1 = lst
        dot_value = np.dot(v1, v2)
        v1_text.set_text('vertex 1: ' + str(v1))
        dot_text.set_text('dot product value: ' + str(dot_value))
    except ValueError:
        return

def setV2(text):
    global dimension, v1, v2, dot_value
    try:
        tempstr = text.split(',')
        templst = list(map(int, tempstr))
        lst = [0] * dimension
        for i in range(min(len(templst), dimension)):
            lst[i] = templst[i]
        v2 = lst
        dot_value = np.dot(v1, v2)
        v2_text.set_text('vertex 2: ' + str(v2))
        dot_text.set_text('dot product value: ' + str(dot_value))
    except ValueError:
        return

textbox0.on_submit(setDimension)
textbox1.on_submit(setV1)
textbox2.on_submit(setV2)
button.on_clicked(resetData)

draw()
plt.show()
