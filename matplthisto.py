
# a real world example , forgot where i put the original code 
from matplotlib import pyplot as plt 
import pandas as pd 
from matplotlib import style
plt.style.use("fivethirtyeight")
data=  pd.read_csv("D:/1.csv")
ids = data['Responder_id']
ages = data['Age']
plt.title("My Histogram")
bins = [10,20 ,30 ,40 ,50 ,60 ,70, 80 , 90 ,100 ]
plt.ylabel("Total Respondents")
plt.xlabel("Ages")
meanAge = ages.mean()
print(meanAge)
plt.hist( ages ,bins=bins , edgecolor='k' , log=True)#log for a logarmithic scale
plt.axvline(meanAge , color='#fc4f30' , linestyle=':' , linewidth=2)# plots a straight line at the x-value specified 
plt.grid(True)
plt.show()