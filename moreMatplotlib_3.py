# import matplotlib.pyplot as plt 


# plt.ion()#turn on interactive mode , works in terminal
# # plt.ioff()
# plt.plot([1.07,2.17],[1.2,0.4])

# Live data of CPU usage
# Uses a lot of RAM, better algo needed.
'''
import matplotlib.pyplot as plt
import psutil
import time
import numpy as np 


# %matplotlib notebook for jupyter notebook
plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111) 
fig.show()
x, y = [] ,[]
arrx = np.array(x)#arrays are better
arry = np.array(y)
plt.xlabel("Time")
plt.ylabel("CPU use percent")

x, y = [], []
def a():
	num = psutil.cpu_percent()
	yield num
plt.ylim(0, 100)
def nums():

	while True:
		i = 0
		x.append(i)
		# y.append(a())
# 		 raise RuntimeError("matplotlib does not support generators "
# RuntimeError: matplotlib does not support generators as input
		y.append(psutil.cpu_percent())

		ax.plot(arrx, arry, color='b', linewidth=1)
	    
		fig.canvas.draw()
	    
		ax.set_xlim(left=max(0, i-50), right=i+50)
	    
		time.sleep(0.1)
		i += 1

	
nums()
plt.close()
'''
# from matplotlib import pyplot as plt 
# import numpy as np
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
# '''
from matplotlib import pyplot as plt 
import numpy as np 
data = {'a': np.arange(50),
'c': np.random.randint(0, 50, 50),
'd': np.random.randn(50)}
'''
numpy.arange
function
DESCRIPTION
arange([start,] stop[, step,], dtype=None)

Return evenly spaced values within a given interval.

Values are generated within the half-open interval [start, stop) (in other words, the interval including start but excluding stop). For integer arguments the function is equivalent to the Python built-in range function, but returns an ndarray rather than a list.

When using a non-integer step, such as 0.1, the results will often not be consistent. It is better to use linspace for these cases.

PARAMETERS
start : number, optional
Start of interval. The interval includes this value. The default start value is 0.
stop : number
End of interval. The interval does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of out.
step : number, optional
Spacing between values. For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. The default step size is 1. If step is specified, start must also be given.
dtype : dtype
The type of the output array. If dtype is not given, infer the data type from the other input arguments.
RETURNS
arange : ndarray
Array of evenly spaced values.

For floating point arguments, the length of the result is ceil((stop - start)/step). Because of floating point overflow, this rule may result in the last element of out being greater than stop.

SEE ALSO
linspace : Evenly spaced numbers with careful handling of endpoints. ogrid: Arrays of evenly spaced numbers in N-dimensions. mgrid: Grid-shaped arrays of evenly spaced numbers in N-dimensions.

EXAMPLES
>>> np.arange(3)
array([0, 1, 2])
>>> np.arange(3.0)
array([ 0.,  1.,  2.])
>>> np.arange(3,7)
array([3, 4, 5, 6])
>>> np.arange(3,7,2)
array([3, 5])
==========randn===========
randn(d0, d1, ..., dn)

Return a sample (or samples) from the "standard normal" distribution.

If positive, int_like or int-convertible arguments are provided,
`randn` generates an array of shape ``(d0, d1, ..., dn)``, filled
with random floats sampled from a univariate "normal" (Gaussian)
distribution of mean 0 and variance 1 (if any of the :math:`d_i` are
floats, they are first converted to integers by truncation). A single
float randomly sampled from the distribution is returned if no
argument is provided.


'''

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('something')
plt.ylabel('also Something')
plt.show()