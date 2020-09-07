# Plotting the sine and cosine functions


import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib.style 

plt.style.use('ggplot')

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # endpoint : bool, optional
        # If True, `stop` is the last sample. Otherwise, it is not included.
        # Default is True.
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(10,6), dpi=80)
    # dpi : integer, optional, default: None
    #     resolution of the figure. If not provided, defaults to
    #     :rc:`figure.dpi` = ``100``.

plt.xlim(-np.pi, np.pi)
plt.ylim(max(C) + .25, min(C) - .25)#set the maximum and minimum values for y axis , .25 is added to encompass it fully, with a gap
'''
builtins.max
function
SIGNATURE
iterable,
*,
default="obj",
key="func"
HOW OTHERS USED THIS
max(​iterable, *​)
max(​iterable, key​)
DESCRIPTION
Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, iterable must be a non-empty iterable
(such as a non-empty string, tuple or list). The largest item in the iterable is returned.
If two or more positional arguments are provided, the largest of the positional arguments is returned.

The optional key argument specifies a one-argument ordering function like that used for list.sort().
The key argument, if supplied, must be in keyword form (for example, max(a,b,c,key=func)).

Changed in version 2.5: Added support for the optional key argument.
'''
ax = plt.gca()
plt.plot(ax.get_xlim() , [0,0] , linestyle= ':' , linewidth=2, color='k')#plots x axis
plt.plot([0,0], ax.get_ylim() , linestyle=':' , linewidth=2, color='k')#plots y axis


plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="Cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-" , label="Sine")


plt.title("Trigonometric ratios" , fontsize=32)
plt.xlabel('-Pi to Pi', fontsize=30)
plt.ylabel("Values", fontsize=30)

plt.tight_layout()
plt.legend()

plt.show()
