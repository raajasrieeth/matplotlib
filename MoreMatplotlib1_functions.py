
'''
Matplotlib requires the following dependencies:
• Python (>= 3.6)
• NumPy (>= 1.15)
• setuptools
• cycler (>= 0.10.0)
• dateutil (>= 2.1)
• kiwisolver (>= 1.0.0)
• Pillow (>= 6.2)
• pyparsing (>=2.0.3)
'''


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
start = -1
stop  = 1
X = np.linspace(int(start),int(stop),100)

fig , ax = plt.subplots()#create  a figure and axes
# print(np.linspace.__doc__)

plt.xlim((start,stop))#sets x limit
# xlim(​xmin, xmax​)

plt.ylim((start,stop))#sets y limit
#ylim(​ymin, ymax​)
# Get or set the y-limits of the current axes.
axis = plt.gca()#get current axis 
plt.plot(axis.get_xlim() , [0,0] , color="k" , linestyle="--" , linewidth = 1)#plots x axis#get_xlim:Get the x-axis range [left, right]
plt.plot([0,0] ,axis.get_ylim() , color="k" ,linestyle="--" ,linewidth = 1)#plots y axis #get_ylim:Get the y-axis range [bottom, top
ax.plot(X , X , label ="Linear")

ax.plot(X ,X**2 , label="Quadratic")


ax.plot(X, X**3 , label = "Cubic")


ax.set_ylabel("Y-axis")
plt.yscale("linear")
'''docs:yscale
SIGNATURE
value,
**kwargs
**KWARGSExpand
HOW OTHERS USED THIS
yscale(​value​)
yscale(​value, nonposy="'clip'"​)
DESCRIPTION
Set the scaling of the y-axis.

call signature:

yscale(scale, **kwargs)
The available scales are: u'linear' | u'log' | u'logit' | u'symlog'

Different keywords may be accepted, depending on the scale:

'linear'

'log'

basex/basey:
The base of the logarithm
nonposx/nonposy: ['mask' | 'clip' ]
non-positive values in x or y can be masked as invalid, or clipped to a very small positive number
subsx/subsy:
Where to place the subticks between each major tick. Should be a sequence of integers. For example, in a log10 scale: [2, 3, 4, 5, 6, 7, 8, 9]

will place 8 logarithmically spaced minor ticks between each major tick.

'logit'

nonpos: ['mask' | 'clip' ]
values beyond ]0, 1[ can be masked as invalid, or clipped to a number very close to 0 or 1
'symlog'

basex/basey:
The base of the logarithm
linthreshx/linthreshy:
The range (-x, x) within which the plot is linear (to avoid having the plot go to infinity around zero).
subsx/subsy:
Where to place the subticks between each major tick. Should be a sequence of integers. For example, in a log10 scale: [2, 3, 4, 5, 6, 7, 8, 9]

will place 8 logarithmically spaced minor ticks between each major tick.

linscalex/linscaley:
This allows the linear range (-linthresh to linthresh) to be stretched relative to the logarithmic range. Its value is the number
 of decades to use for each half of the linear range. For example, when linscale == 1.0 (the default), the space used for the
 positive and negative halves of the linear range will be equal to one decade in the logarithmic range.
'''

ax.set_title("A plot to show some math functions")
ax.set_xlabel("X-axis")
plt.xscale("linear")

ax.legend()

ax.grid(True)

if __name__ == '__main__':
	plt.show()

