from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import style
import pandas as pd 
import random
import bs4
plt.style.use('fivethirtyeight')
plt.title("My Scatter plot")



data = pd.read_csv('D:\\python_envs\\data.csv')

view_count = data['view_count']
likes  = data['likes']
ratio = data['ratio']



plt.scatter(view_count, likes , s= 75  , c = ratio , cmap = 'summer',  marker='.' , 
	edgecolors='g' , linewidths=0.5 , alpha=0.75 ,)
 


plt.xscale('log')#for a  logarthmic scale
plt.yscale('log')
cbar = plt.colorbar()# describes intensity with a gradient
cbar.set_label('Like / Dislike Ratio ')#label

plt.tight_layout()
plt.xlabel("Random Values")
plt.ylabel("Also random values")
plt.show()

# fig = plt.figure() #3d
# ax = plt.axes(projection="3d")
# plt.grid(True , color= 'b' , linewidth=4 , linestyle=':')
# plt.show()




# import matplotlib.pyplot as plt
# import matplotlib.style

# plt.style.use('Solarize_Light2')

# x = []
# y = []
# colors = []

# for i in range(20):
# 	x.append(random.randint(0 , 30)
# 		)
# 	y.append(random.randint(12 ,42))
# 	colors.append(i)

# plt.title('A Scatter Plot')

# plt.scatter(x , y , c = colors , cmap = 'Greens' , alpha =0.77 , edgecolors='k' , marker = 'X' , linewidths=2,)
# # #cmapvals = supported values are 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r',
# #  'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r',
# #  #'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 
# #  'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'

# plt.xscale('log')
# plt.yscale('log')
# cbar  =plt.colorbar()
# cbar.set_label("Bar of Randomness")



# plt.xlabel("Random Values")

# plt.ylabel("More Random Values")

# plt.tight_layout()
# plt.show()






