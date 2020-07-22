# from matplotlib import pyplot as plt 
# from matplotlib import style
# plt.style.use('fivethirtyeight')

# plt.title("My pie chart" , color= 'r' , fontsize= 20)

# slices = [60, 40 , 30 , 20]
# labels= ["60" , "40" , "30" , "20"]
# colors = ['#008fd5' , '#fc4f30', '#e5ae37' , '#6d904f' ]


# plt.pie(slices,labels= labels ,colors= colors, wedgeprops={'edgecolor': 'black' } )

# plt.tight_layout()

# plt.show()
#MORE REAL WORLD APPLICATIONS
from matplotlib import pyplot as plt 
from matplotlib import style
plt.style.use('Solarize_Light2')
# plotting most popular programming languages
data_pop = [59219 , 55466 , 47544 ,36443 , 35917 ]
data_name = ["Javascript" , "HTML/CSS" , "SQL" , "Python" , "Java" ]
explode = [0,0,0,0.1,0]# the same argument in the plt.pie is used to offcenter that part. here the 4th value(python) is offcentered

plt.pie(data_pop , labels= data_name,  explode = explode,
 wedgeprops = {'edgecolor' : 'black' }, shadow = True , startangle = 90,
 autopct='%1.1f%%' , )#shadow gives 3d effect , start angle rotates the chart, autopct displays percent look at syntax in docs 

plt.show()