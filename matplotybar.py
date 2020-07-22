# # #using matplotlib
# # from matplotlib import pyplot as plt
# # from matplotlib import style 

# # import numpy as np 
# # plt.style.use('seaborn')

# # xlist = [23,24,25,26,27,28,29]#ages

# # ylist = [2345, 2467 , 1900 , 3000 , 2780 ,3456 , 2000]

# # ages_lstx = xlist
 
# # x_indexes = np.arange(len(xlist)) #it makes a clone of xlist , but in the form of an array of values  ,which are a numbered value of x values

# # pylist = [3400, 4500 ,5000 , 6700 , 4560 , 4780 , 6140]

# # jslist = [2500 ,1900 , 3500 , 2750 , 4000 ,2800, 2600]

# # width = 0.25

# # plt.bar(x_indexes, ylist ,color= 'k',label = 'All Devs' , width = width)# length of both lists must be equal #label is used to identify the line in the legend
# # #refer to markers and styles for plotted lines at its website# color can also be written in hexvalues

# # plt.bar(x_indexes-width, pylist,color='b', width =width , label ='Python Devs')#new values# subtracting the width of a bar to locate it next to the bar

# # plt.bar(x_indexes + width,jslist, color='y', label='JS Devs' , width = width )# barwidth is default around 0.85

# # plt.title("Median salary by age")

# # plt.xlabel("Age" )
# # plt.ylabel("Median Salary")

# # plt.legend()

# # plt.tight_layout()#removes any padding

# # plt.grid(True , color= 'm')# makes a magenta grid ,default is black
# # #plt.savefig('Fig.png')# can add a directory , preceded by a comma else it is saved in current directory
# # plt.show()# displays 
# # working with csv files
# from matplotlib import pyplot as plt
# from matplotlib import style 
# # using Standard library
# # import csv
# # plt.style.use('seaborn')
# # # with open ('data.csv') as csv_file:
# # # 	csv_reader = csv.DictReader(csv_file)#use dictionary read method in csv (SL) , which makes  a dick to be accessed with key  , not index
# # # # testing :
# # # 	row = next(csv_reader)
# # # 	#print(row)# see contents of row
# # # 	print(row['LanguagesWorkedWith'].split(';'))#what we need , as a list
# # # as we need to track trackhe languages , we can use Counter , a built in python class
# # #refer to counter docs
# # from collections import Counter
# # with open('data.csv') as csv_file:
# # 	csv_reader = csv.DictReader(csv_file)
# # 	language_counter  = Counter()
# # 	for row in csv_reader:
# # 		language_counter.update(row['LanguagesWorkedWith'].split(';'))#the list is sent to the counter method
# # 		#file is closed
# # #print(language_counter) # prints all instances , but we want 14 most common. So:
# # #print(language_counter.most_common(14))# tuple values
# # languages = []
# # popularity = []
# # for i in  language_counter.most_common(14):
# # 	languages.append(i[0])
# # 	popularity.append(i[1])
# # plt.barh(languages, popularity)#horizontal , expects y values first
# # plt.title('Most popular Programming Languages:', fontsize= 20 , color = 'R')
# # plt.ylabel('Languages')
# # plt.xlabel('Number of people who know it:')
# # plt.tight_layout()
# # plt.show()
# #with pandas:
# from collections import Counter
# plt.style.use('fivethirtyeight')
# import pandas as pd 
# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# lang_responses = data['LanguagesWorkedWith']
# language_counter = Counter()
# languages = []
# popularity = []
# for response in  lang_responses:
# 	language_counter.update(response.split(';'))
# for i in language_counter.most_common(15):
# 	languages.append(i[0])
# 	popularity.append(i[1])
# languages.reverse()
# popularity.reverse()# to make them look from highest to lowest
# plt.barh(languages, popularity)#horizontal , expects y values first
# plt.title('Most popular Programming Languages:', fontsize= 20 , color = 'r')
# plt.ylabel('Languages')
# plt.xlabel('Number of people who know it:')
# plt.tight_layout()
# plt.show()
#econ tb 1.2:
from matplotlib import pyplot as plt
from matplotlib import style
plt.style.use("ggplot")
years = ["1965-66" , "70-71","80-81" , "90-91" , "2000-01" , "2010-11" , "12-13" , "14-15" , "17-18"]
pulses= [10, 12 ,11 ,14, 11 ,18,18, 17 , 24]
plt.barh(years, pulses , color= 'y' ,label="Pulses"  , height=0.35 , edgecolor='k' ,)
plt.ylabel("Years")
plt.xlabel("Production of Pulses in Million Tonnes")
plt.title("Production of pulses after Green Revolution in India" , fontsize=20)
plt.tight_layout()
plt.show()
#wheat
years = ["1965-66" , "70-71","80-81" , "90-91" , "2000-01" , "2010-11" , "12-13" , "14-15" , "17-18"]
wheat = [10 ,24, 35 ,66 ,70 , 87 , 94 ,87 ,97]
plt.bar(years, wheat , color= 'm' ,label="Wheat"  , width=0.35 , edgecolor='b' ,)
plt.xlabel("Years" , fontweight='bold' , color='k')
plt.ylabel("Production of Wheat in Million Tonnes" ,fontweight='bold' , color='k')
plt.title("Production of Wheat after Green Revolution in India" , fontsize=20,fontweight='bold' , color='k')
plt.tight_layout()
plt.show()






