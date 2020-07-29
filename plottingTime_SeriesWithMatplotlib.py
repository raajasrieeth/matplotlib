# from matplotlib import pyplot as plt
# from matplotlib import dates as mpl_dates
# from datetime import timedelta , datetime
# import pandas as pd
# import numpy as np 



# plt.style.use('seaborn')
# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 5,6,7]
# #print(plt.style.available)
# # Available Styles:
# # ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
# # 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark',  'seaborn-dark-palette', 
# # 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper','seaborn-pastel',
# # 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

# data = pd.read_csv('D:\\python_envs\\All_other_codes\\read.csv')




# # plt.xlabel()
# # plt.xscale()

# # plt.ylabel()
# # plt.yscale()

# plt.plot_date(dates, y , linestyle="-")

# plt.gcf().autofmt_xdate()#gcf gets the current figure ,  autofmt_xdate tilts the dates to look neater
# date_format = mpl_dates.DateFormatter('%b , %d , %Y')#month , date , year(full)# check out for more: http://bit.ly/python-dt-fmt
# plt.gca().xaxis.set_major_formatter(date_format)

# #plt.grid()

# # plt.tight_layout()

# plt.show()



import matplotlib.pyplot as plt 
import matplotlib.dates as mpl_dates
import numpy as np
import pandas as pd

data = pd.read_csv("D:\\python_envs\\All_other_codes\\read.csv")

data['Date'] = pd.to_datetime(data['Date']) # check pandas guide , if unfamiliar
data.sort_values('Date' , inplace =True)#modifies data

price_date = data['Date']#but are read as strings  , not as dates



price_close = data['Close']

plt.plot_date(price_date , price_close , linestyle='-')
plt.gcf().autofmt_xdate()


plt.gca().xaxis.set_major_formatter(mpl_dates.DateFormatter("%b , %d , %Y"))

plt.tight_layout()

plt.show()




