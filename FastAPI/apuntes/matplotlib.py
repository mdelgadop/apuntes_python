import matplotlib.pyplot as plt #python -m pip install -U matplotlib
import numpy as np

#PUNTOS
xpoints = np.array([1, 3, 5, 7, 9])
ypoints = np.array([3, 4, 7, 8.5, 10])


plt.subplot(3, 2, 1) #the figure has 3 row, 2 columns, and this plot is the first plot. QUITAR PARA PONERLO TODO EN UN ÚNICO GRÁFICO
#plt.plot(xpoints, ypoints) #SERIE
plt.plot(xpoints, ypoints, marker='o', color="red") #PUNTOS
plt.grid(axis = 'y')
plt.title("Test")
plt.ylabel('Y')
plt.xlabel('X')

##########################################################################

#SERIE
plt.subplot(3, 2, 2) #the figure has 3 row, 2 columns, and this plot is the second plot. QUITAR PARA PONERLO TODO EN UN ÚNICO GRÁFICO
plt.plot([1, 2, 4, 3, 6, 5, 7, 6, 9, 10], marker='o', color="green", linestyle = 'dotted') #linestyle = 'dashed', linewidth = '20.5'
#GRID
#plt.grid()
plt.grid(axis = 'x', color = 'blue', linestyle = '--', linewidth = 0.5)
#LABELS
plt.title("Mario Bolsa", fontdict = {'family':'serif','color':'blue','size':20}, loc = 'center')
plt.ylabel('Ganancias')
plt.xlabel('Días')

##########################################################################

#PUNTOS
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.subplot(3, 2, 3)
plt.scatter(x, y, color = 'hotpink')

plt.subplot(3, 2, 4)
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
sizes = np.array([2,5,10,20,250, 100,6,9,10,30,60,80,7, 2, 2])
plt.scatter(x, y, color = '#88c999', s=sizes)

##########################################################################

#BARRAS
plt.subplot(3, 2, 5)
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y, color = "magenta", width = 0.5)
#plt.barh(x,y, height = 0.5) #horizontal

##########################################################################

#PIE
plt.subplot(3, 2, 6)
y = np.array([35, 25, 25, 15])
plt.pie(y, labels = ["Apples", "Bananas", "Cherries", "Dates"], colors = ["green", "yellow", "pink", "brown"], explode = [0.1, 0, 0, 0], startangle = 90, shadow = True)
plt.legend(title = "Four Fruits:")

##########################################################################

#MOSTRAR GRÁFICA
plt.show()

