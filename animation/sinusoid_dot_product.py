import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox

#define constants
TWOPI = 2 * np.pi
PI = np.pi

#set and adjust figure
fig, ax = plt.subplots(3, 1, 
                       gridspec_kw={
                        'height_ratios': [1, 1, 1]},
                       figsize=(8, 7))
plt.subplots_adjust(left = 0.1, bottom = 0.2, wspace = 0.2,hspace = 0.5)
tick_pos= [0, 0.25*PI, 0.5*PI, 0.75*PI, PI, 1.25*PI, 1.5*PI, 1.75*PI, 2*np.pi]
labels = ['0', '$1/4\pi$','$1/2\pi$', '$3/4\pi$','$\pi$','$5/4\pi$','$3/2\pi$','$7/4\pi$','$2\pi$']
plt.setp(ax, xticks=tick_pos, xticklabels=labels)

#initiate continuous function variables
sample_space = 0.25
phase = 0
x = np.arange(0,TWOPI,0.0001)
x_plus = np.arange(phase * PI,TWOPI + phase * PI,0.0001)
y_sin = np.sin(x_plus)
y_sin_fixed = np.sin(x)
y_dot = y_sin * y_sin_fixed
dot_value = np.dot(y_sin, y_sin_fixed)
dot_value_str = 'Dot Product Sum: %0.2f\n'% dot_value

#initiate discrete function variables
x_sample = np.arange(0,TWOPI,sample_space)
x_plus_sample = np.arange(phase * PI,TWOPI + phase * PI,sample_space)
y_sin_sample = np.sin(x_plus_sample)
y_sin_fixed_sample = np.sin(x_sample)
y_dot_sample = y_sin_sample * y_sin_fixed_sample
dot_sample_value = np.dot(y_sin_sample, y_sin_fixed_sample)
dot_value_sample_str = 'Sample Dot Product Sum: %0.2f\n'% dot_sample_value

#draw sinusoid(fixed) line
line_fix, = ax[0].plot(x,y_sin_fixed)
markerline_fix, stemlines_fix, baseline_fix = ax[0].stem(x_sample,
                                                         y_sin_fixed_sample,
                                                         markerfmt=',',
                                                         use_line_collection=True)
count_fix, bins_fix, bars_fix = ax[0].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                          edgecolor='#EFB28C',
                          color='#EED19C',weights = y_sin_fixed_sample[:-1])

#draw sinusoid(changable) line
line_change, = ax[1].plot(x,y_sin)
count, bins, bars = ax[1].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                          edgecolor='#EFB28C',
                          color='#EED19C', weights = y_sin_sample[:-1])
markerline, stemlines, baseline = ax[1].stem(x_sample,
                                            y_sin_sample,
                                            markerfmt=',',
                                            use_line_collection=True)
#draw two sinusoid dot product line
line_dot, = ax[2].plot(x,y_dot)
count_dot, bins_dot, bars_dot = ax[2].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                              edgecolor='#EFB28C',
                              color='#EED19C', weights = y_dot_sample[:-1])
markerline_dot, stemlines_dot, baseline_dot = ax[2].stem(x_sample,
                                            y_dot_sample,
                                            markerfmt=',',
                                            use_line_collection=True)

#ax[0].axes.xaxis.set_ticklabels([])
#ax[0].axes.yaxis.set_ticklabels([])

#textbox edit function
def setPhase(text):
    
    #declare global var
    global line_change, count, bins, bars, markerline, stemlines, baseline
    global line_dot, count_dot, bins_dot, bars_dot, markerline_dot, stemlines_dot, baseline_dot
    global x_plus, y_sin, y_dot, dot_value, dot_value_str
    global x_plus_sample, y_sin_sample, dot_sample_value, dot_value_sample_str, phase

    #convert input to number
    textval = 0
    try:
        textval = float(text)
    except ValueError:
        try:
            num, denom = text.split('/')
            textval = float(num) / float(denom)
        except ValueError:
            return
    phase = textval

    #remove old graph
    line_change.remove()
    markerline.remove()
    stemlines.remove()
    baseline.remove()

    line_dot.remove()
    markerline_dot.remove()
    stemlines_dot.remove()
    baseline_dot.remove()
    
    for b in bars:
        b.remove()
        
    for b in bars_dot:
        b.remove()

    #draw ner graph
    x_plus = np.arange(phase * PI,TWOPI + phase * PI,0.0001)
    y_sin = np.sin(x_plus)
    y_dot = y_sin * y_sin_fixed
    dot_value = np.dot(y_sin, y_sin_fixed)
    dot_value_str = 'Dot Product Sum: %0.2f\n'% dot_value

    x_plus_sample = np.arange(phase * PI,TWOPI + phase * PI,sample_space)
    y_sin_sample = np.sin(x_plus_sample)
    y_dot_sample = y_sin_sample * y_sin_fixed_sample
    dot_sample_value = np.dot(y_sin_sample, y_sin_fixed_sample)
    dot_value_sample_str = 'Sample Dot Product Sum: %0.2f\n'% dot_sample_value

    line_change, = ax[1].plot(x,y_sin)
    count, bins, bars = ax[1].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                          edgecolor='#EFB28C',
                          color='#EED19C', weights = y_sin_sample[:-1])
    markerline, stemlines, baseline = ax[1].stem(x_sample,
                                            y_sin_sample,
                                            markerfmt=',',
                                            use_line_collection=True)
    line_dot, = ax[2].plot(x,y_dot)
    count_dot, bins_dot, bars_dot = ax[2].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                              edgecolor='#EFB28C',
                              color='#EED19C', weights = y_dot_sample[:-1])
    markerline_dot, stemlines_dot, baseline_dot = ax[2].stem(x_sample,
                                            y_dot_sample,
                                            markerfmt=',',
                                            use_line_collection=True)

    dot_text.set_text(dot_value_str+dot_value_sample_str)

    plt.draw()


#textbox edit function
def setSample(text):
    
    #declare global var
    global count, bins, bars, markerline, stemlines, baseline
    global count_dot, bins_dot, bars_dot, markerline_dot, stemlines_dot, baseline_dot
    global markerline_fix, stemlines_fix, baseline_fix, count_fix, bins_fix, bars_fix
    global x_sample, y_sin_fixed_sample
    global x_plus_sample, y_sin_sample, dot_sample_value, dot_value_sample_str, sample_space

    #convert input to number
    textval = 0
    try:
        textval = float(text)
    except ValueError:
        try:
            num, denom = text.split('/')
            textval = float(num) / float(denom)
        except ValueError:
            return
    sample_space = textval

    #remove old graph
    markerline.remove()
    stemlines.remove()
    baseline.remove()

    markerline_dot.remove()
    stemlines_dot.remove()
    baseline_dot.remove()

    markerline_fix.remove()
    stemlines_fix.remove()
    baseline_fix.remove()
    
    for b in bars:
        b.remove()
        
    for b in bars_dot:
        b.remove()

    for b in bars_fix:
        b.remove()

    #draw ner graph
    x_sample = np.arange(0,TWOPI,sample_space)
    x_plus_sample = np.arange(phase * PI,TWOPI + phase * PI,sample_space)
    y_sin_sample = np.sin(x_plus_sample)
    y_sin_fixed_sample = np.sin(x_sample)
    y_dot_sample = y_sin_sample * y_sin_fixed_sample
    dot_sample_value = np.dot(y_sin_sample, y_sin_fixed_sample)
    dot_value_sample_str = 'Sample Dot Product Sum: %0.2f\n'% dot_sample_value

    count, bins, bars = ax[1].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                          edgecolor='#EFB28C',
                          color='#EED19C', weights = y_sin_sample[:-1])
    markerline, stemlines, baseline = ax[1].stem(x_sample,
                                            y_sin_sample,
                                            markerfmt=',',
                                            use_line_collection=True)
    
    count_dot, bins_dot, bars_dot = ax[2].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                              edgecolor='#EFB28C',
                              color='#EED19C', weights = y_dot_sample[:-1])
    markerline_dot, stemlines_dot, baseline_dot = ax[2].stem(x_sample,
                                            y_dot_sample,
                                            markerfmt=',',
                                            use_line_collection=True)

    markerline_fix, stemlines_fix, baseline_fix = ax[0].stem(x_sample,
                                                         y_sin_fixed_sample,
                                                         markerfmt=',',
                                                         use_line_collection=True)
    count_fix, bins_fix, bars_fix = ax[0].hist(x_sample[:-1], bins = x_sample,alpha=0.5,
                          edgecolor='#EFB28C',
                          color='#EED19C',weights = y_sin_fixed_sample[:-1])

    dot_text.set_text(dot_value_str+dot_value_sample_str)

    plt.draw()

#set textbox
axbox1 = plt.axes([0.15, 0.05, 0.13, 0.05])
text_box1 = TextBox(axbox1, r'$Phase Shift(\pi)$', initial='0')
text_box1.on_submit(setPhase)

axbox2 = plt.axes([0.45, 0.05, 0.13, 0.05])
text_box2 = TextBox(axbox2, r'$TrapeziumWidth$', initial='0.25')
text_box2.on_submit(setSample)

dot_text = plt.text(1.3, 0, dot_value_str+dot_value_sample_str)


plt.show()
