import matplotlib.pyplot as plt
import numpy as np

# fig,ax = plt.subplots(2,2)


# plt.show()


def my_plotter(ax, data1, data2, param_dict):

# A helper function to make a graph
# Parameters
# ----------
# ax : Axes
# The axes to draw to
# data1 : array
# The x data
# data2 : array
# The y data
# param_dict : dict
# Dictionary of kwargs to pass to ax.plot
# Returns
# -------
# out : list
# list of artists added

    out = ax.plot(data1, data2, **param_dict)
    return out
data_1, data_2 , data_3 , data_4 = np.random.randn(4,100)

fig,(ax1,ax2) = plt.subplots(1,2)

my_plotter(ax1, data_1,data_2, {'marker':'x'})#the kwargs can be used just as with a normal ax.plot function
my_plotter(ax2, data_3, data_4, {'marker':'o'})
plt.show()
'''
======================
        Backends
======================
What is a backend?
A lot of documentation on the website and in the mailing lists refers to the ”backend” and
many new users are confused by this term. matplotlib targets many different use cases and
output formats. Some people use matplotlib interactively from the python shell and have
plotting windows pop up when they type commands. Some people run Jupyter notebooks
and draw inline plots for quick data analysis. Others embed matplotlib into graphical user
interfaces like wxpython or pygtk to build rich applications. Some people use matplotlib in
batch scripts to generate postscript images from numerical simulations, and still others run
web application servers to dynamically serve up graphs.
To support all of these use cases, matplotlib can target different outputs, and each of these
capabilities is called a backend; the ”frontend” is the user facing code, i.e., the plotting code,
whereas the ”backend” does all the hard work behind-the-scenes to make the figure. There
are two types of backends: user interface backends (for use in pygtk, wxpython, tkinter, qt4,
or macosx; also referred to as ”interactive backends”) and hardcopy backends to make image
files (PNG, SVG, PDF, PS; also referred to as ”non-interactive backends.
'''
