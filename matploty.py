# #using matplotlib
# from matplotlib import pyplot as plt
# from matplotlib import style 
# #uncomment the following to see available styles
# #print(plt.style.available)
# #plt.style.use('fivethirtyeight')# a useful style , see full list in the above statement
# plt.xkcd()#nice style , looks like its handwritten
# xlist = [23,24,25,26,27,28,29]

# ylist = [2345, 2467 , 1900 , 3000 , 2780 ,3456 , 2000]

# ages_lstx = xlist

# pylist = [3400, 4500 ,5000 , 6700 , 4560 , 4780 , 6140]

# jslist = [2500 ,1900 , 3500 , 2750 , 4000 ,2800, 2600]

# plt.plot(xlist, ylist ,color= 'k',linestyle= '--' , marker=".",label= "All devs", linewidth=3)# length of both lists must be equal #label is used to identify the line in the legend
# #refer to markers and styles for plotted lines at its website# color can also be written in hexvalues

# plt.plot(ages_lstx, pylist,color='b',linestyle='-',marker='o', label="Python devs", linewidth=2)#new values

# plt.plot(ages_lstx,jslist, color='y', linestyle='-', marker= '.' ,label = "JS devs",linewidth=2)#linewidth is default as 




# plt.title("Median salary by age")

# plt.xlabel("Age" )
# plt.ylabel("Median Salary")

# plt.legend()

# plt.tight_layout()#removes any padding

# plt.grid(True, color= 'm')# makes a magenta grid ,default is black
#plt.savefig('Fig.png')# can add a directory , preceded by a comma else it is saved in current directory
#plt.show()# displays
#Economics tb 1.2
from matplotlib import pyplot as plt
from matplotlib import style
plt.style.use("seaborn")
plt.title("Production of pulses and wheat after the Green Revolution")
years = ["1965-66" , "70-71","80-81" , "90-91" , "2000-01" , "2010-11" , "12-13" , "14-15" , "17-18"]
pulses= [10, 12 ,11 ,14, 11 ,18,18, 17 , 24]
wheat = [10 ,24, 35 ,66 ,70 , 87 , 94 ,87 ,97]
plt.plot(years , pulses , label = "pulses" ,linestyle= "-" ,color= "m" , marker='*'  ,linewidth=2, )
plt.plot(years , wheat , label="wheat" , linestyle="-" , color='y' , marker = '.' , linewidth=2)
plt.xlabel("Years")
plt.ylabel("Crop Produced in Million Tons")
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()




