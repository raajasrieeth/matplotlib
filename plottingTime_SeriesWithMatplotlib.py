# # from matplotlib import pyplot as plt
# # from matplotlib import dates as mpl_dates
# # from datetime import timedelta , datetime
# # import pandas as pd
# # import numpy as np 



# # plt.style.use('seaborn')
# # dates = [
# #     datetime(2019, 5, 24),
# #     datetime(2019, 5, 25),
# #     datetime(2019, 5, 26),
# #     datetime(2019, 5, 27),
# #     datetime(2019, 5, 28),
# #     datetime(2019, 5, 29),
# #     datetime(2019, 5, 30)
# # ]

# # y = [0, 1, 3, 4, 5,6,7]
# # #print(plt.style.available)
# # # Available Styles:
# # # ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
# # # 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark',  'seaborn-dark-palette', 
# # # 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper','seaborn-pastel',
# # # 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

# # data = pd.read_csv('D:\\python_envs\\All_other_codes\\read.csv')




# # # plt.xlabel()
# # # plt.xscale()

# # # plt.ylabel()
# # # plt.yscale()

# # plt.plot_date(dates, y , linestyle="-")

# # plt.gcf().autofmt_xdate()#gcf gets the current figure ,  autofmt_xdate tilts the dates to look neater
# # date_format = mpl_dates.DateFormatter('%b , %d , %Y')#month , date , year(full)# check out for more: http://bit.ly/python-dt-fmt
# # plt.gca().xaxis.set_major_formatter(date_format)

# # #plt.grid()

# # # plt.tight_layout()

# # plt.show()



import matplotlib.pyplot as plt 
import matplotlib.dates as mpl_dates
import matplotlib.style as mpl_style
import numpy as np
import pandas as pd
mpl_style.use(['dark_background', 'seaborn', 'fast'])
'''
The fast style can be used to automatically set simplification and chunking parameters to
reasonable settings to speed up plotting large amounts of data. It can be used simply by
running:
import matplotlib.style as mplstyle
mplstyle.use('fast')
It is very light weight, so it plays nicely with other styles, just make sure the fast style is
applied last so that other styles do not overwrite the settings:
mplstyle.use(['dark_background', 'ggplot', 'fast'])
'''

data = pd.read_csv("D:\\python_envs\\All_other_codes\\read.csv")

data['Date'] = pd.to_datetime(data['Date']) # check pandas guide , if unfamiliar
data.sort_values('Date' , inplace =True)#modifies data

price_date = data['Date']#but are read as strings  , not as dates

price_close = data['Close']#these are the indexes through which pandas reads.

plt.plot_date(price_date , price_close , linestyle='-')#plots line
plt.gcf().autofmt_xdate()#gets current figure , formats the dates on x-axis


plt.gca().xaxis.set_major_formatter(mpl_dates.DateFormatter("%b , %d , %Y"))#formats to bettter layout

plt.tight_layout()

plt.show()
