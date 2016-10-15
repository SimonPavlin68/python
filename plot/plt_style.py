import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 100)

plt.plot(x, x, label = 'linear', linewidth = 2)
plt.plot(x, x**2, '--', label = 'quadratic', linewidth = 2)
plt.plot(x, x**3/2, '.', label = 'cubic/2', linewidth = 2)
plt.plot(x, x**3, '.', label = 'cubic', linewidth = 2)

# b: blue g: green r: red
# c: cyan m: magenta y: yellow
# k: black  w: white

plt.xlabel('X label')
plt.ylabel('Y label')

# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
# plt.legend(loc='upper left', fancybox=True, shadow=True)
# plt.legend(loc = 'upper left', fancybox=True)
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True)
frame = legend.get_frame()
frame.set_facecolor('pink')
frame.set_edgecolor('lime')

# Shrink current axis by 20%
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.set_title('Simple Plot', color='blue')
# plt.title("Simple Plot")
ax.xaxis.label.set_color('red')
ax.tick_params(axis='x', colors='blue')
ax.yaxis.label.set_color('green')
ax.spines['bottom'].set_color('yellow')
ax.spines['left'].set_color('red')

# background color
ax.set_axis_bgcolor('silver')

plt.grid()

plt.show()