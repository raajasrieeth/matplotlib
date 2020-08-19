import matplotlib.pyplot as plt 
import matplotlib.style
import numpy as np


'''plotting functions expect numpy.array or numpy.ma.masked_array as input. Classes that are
’array-like’ such as pandas data objects and numpy.matrix may or may not work as intended. It
is best to convert these to numpy.array objects prior to plotting.'''

# fig = plt.figure() # an empty figure with no Axe
# fig, ax = plt.subplots() # a figure with a single Axes ; usually used
# fig, axs = plt.subplots(2, 2) # a figure with a 2x2 grid of Axes


'''There are essentially two ways to use Matplotlib:
• Explicitly create figures and axes, and call methods on them (the ”object-oriented (OO)
style”).
• Rely on pyplot to automatically create and manage the figures and axes, and use pyplot
functions for plotting.'''

#OO style:

X = np.linspace(-1,1,100)

fig , ax = plt.subplots()#create  a figure and axes
# print(np.linspace.__doc__)
ax.plot(X , X , label ="Linear")

ax.plot(X ,X**2 , label="Quadratic")


ax.plot(X, X**3 , label = "Cubic")


ax.set_xlabel("X axis")

ax.set_ylabel("Y-axis")

ax.set_title("A plot to show some math functions")

ax.legend()

ax.grid(True)

plt.show()

