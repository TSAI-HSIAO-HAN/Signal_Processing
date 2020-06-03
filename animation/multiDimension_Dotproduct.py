from matplotlib.widgets import TextBox
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
n = 4
v1 = [1,2,3,4]
v2 = [1,3,5,7]
base_v = np.arange(n + 1)



plt.show()
