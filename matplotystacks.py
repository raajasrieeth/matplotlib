#stack plots are much simple.
from matplotlib import pyplot as plt 
from matplotlib import style
plt.style.use('bmh')

plt.title('My Awesome Stack chart')
# in a sports game

minutes = [1,2,3,4,5,6,7,8,9]

player1= [1 , 2, 3 ,3 ,4, 4 , 4 , 4 ,5]
player2 = [1 ,1 ,1 ,1 , 2 ,2, 2, 3 ,4]
player3 = [1, 1,1 , 2,2 ,2 , 3, 3, 3]
labels= [ 'player1' ,'player2' ,'player3' ]
colors = ['#008fd5' , '#fc4f30', '#e5ae37' ]# look up hex values , here- blue, red , yellow

plt.stackplot(minutes , player1 , player2 , player3 , labels= labels , colors = colors)# x ,y  ,others
# plt.legend(loc= 'upper left')
plt.legend(loc=(0.07 , 0.05))# the bottom left of the legend is 7% and 5% far from origin		

plt.tight_layout()

plt.show()
