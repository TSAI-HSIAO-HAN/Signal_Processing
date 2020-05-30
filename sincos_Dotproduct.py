import matplotlib.pyplot as plt
import numpy as np

fig, (ax0, ax1, ax2) = plt.subplots(3, 1, 
                       gridspec_kw={
                        'height_ratios': [1, 1, 1]})

TWOPI = 2 * np.pi
x = np.arange(0,TWOPI,0.001)
x_plus = np.arange(-1/2 * np.pi,TWOPI - 1/2 * np.pi,0.001)
y_sin = np.sin(x_plus)
y_cos = np.cos(x)
y_dot = y_sin * y_cos

ax0.plot(x,np.sin(x))
ax0.plot(x,y_sin)
ax1.plot(x,y_cos)
ax2.plot(x,y_dot)
ax2.plot(x,y_cos * np.sin(x))
ax0.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
a = [1,2,3,4]
b = [4,3,2,1]
print(np.dot(a ,b))

plt.show()
