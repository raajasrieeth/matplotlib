# import matplotlib.pyplot as plt 


# plt.ion()#turn on interactive mode , works in terminal
# # plt.ioff()
# plt.plot([1.07,2.17],[1.2,0.4])

# Live data of CPU usage
# Uses a lot of RAM, better algo needed.

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


