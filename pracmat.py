from matplotlib import pyplot as plt 
from matplotlib import style
plt.xkcd()
months = [ "December" , "January" , "February" , "March " , "April" , "May" , "June"]
cases_ind = [3, 200,2000, 7500, 11600, 40000, 96000]
cases_Us = [4500 , 20000 , 60000 , 80000 , 150000 , 200000 ,300000]
cases_italy=[3000, 10000 , 70000 , 350000 ,22000 ,15000 , 75000]

plt.plot(months , cases_ind , linestyle = '-' , marker= "*" , color ='g' , linewidth= 4, label='India' , markersize = 10)
plt.plot(months, cases_Us ,linestyle= '-' , marker ='.' ,color= 'b' , linewidth = 3 , label = "USA" , markersize = 11) 
plt.plot(months , cases_italy , linestyle ='--' , marker ='*',  color='k' , linewidth= 3 ,label = 'Italy' , markersize =12)

plt.title(" Graphing Covid-19 Cases in Countries ")
plt.ylabel("Number of cases")
plt.xlabel("Months" , fontsize = 15)

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

