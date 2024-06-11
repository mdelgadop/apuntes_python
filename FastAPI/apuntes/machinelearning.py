import numpy
import matplotlib.pyplot as plt #python -m pip install -U matplotlib
from scipy import stats #python -m pip install scipy

def mode(listOfElements):
    if type(listOfElements) != type([]):
        raise TypeError("The parameter is not a list")

    myListOfElements = listOfElements.copy()
    myListOfElements.sort()
    prev = None
    currSum = 0
    max = 0
    maxElement = None
    
    for n in myListOfElements:
        if prev is None:
            prev = n
            currSum = 1
            maxElement = n
        elif prev == n:
            currSum += 1
        else:
            if currSum > max:
                maxElement = n
                max = currSum
                currSum = 0
    
    return maxElement

def mean(listOfNumbers, decimals = -1):
    if type(listOfNumbers) != type([]):
        raise TypeError("The parameter is not a list (mean)")
    mySum=0
    for n in listOfNumbers:
        if (not isinstance(n, int)) and (not isinstance(n, float)):
            raise TypeError("The value is not a valid numeric: " + n)
        mySum += n
    return mySum/len(listOfNumbers) if decimals < 0 else round(mySum/len(listOfNumbers), decimals)

def var(listOfNumbers):
    if not isinstance(listOfNumbers, list):
        raise TypeError("The parameter is not a list (var)")
    media = mean(listOfNumbers)
    listaDeCuadrados = []
    for n in listOfNumbers:
        if (not isinstance(n, int)) and (not isinstance(n, float)):
            raise TypeError("The value is not a valid numeric: " + n)
        listaDeCuadrados.append((n - media)**2)

    return mean(listaDeCuadrados)

myListUniform = list(numpy.random.uniform(0.0, 100.0, 100000)) #genera un set de 100000 números aleatorios de 0 a 100
myList = list(numpy.random.normal(50.0, 10.0, 100000)) #genera un set de 100000 números aleatorios de 0 a 100, distribuidos de forma gaussiana. La media es 50 y la desviación estándar es 10

print("Hay ", len(myList), " números en el set")

print("Mínimo: ", min(myList)) # Mínimo
print("Máximo: ", max(myList)) # Máximo
print("Media: ", numpy.mean(myList), " vs ", mean(myList)) # Media
print("Mediana: ", numpy.median(myList)) # Mediana
print("Moda: ", mode(myList)) # El valor más repetido
print("Desviación estándar σ: ", numpy.std(myList)) # Mide la distancia media respecto a la media. Es el cuadrado de la varianza. Un valor más alto indica que los valores se distribuyen en un rango más amplio.
print("Varianza σ2: ", numpy.var(myList), " vs ", var(myList), " vs ", numpy.std(myList)**2) # Mide la distancia media al cuadrado respecto a la media. Es la media de los cuadrados de las diferencias de cada valor con la media normal. Un valor más alto indica que los valores se distribuyen en un rango más amplio.
print("Percentil (90): ", numpy.percentile(myList, 90)) # Percentil (90). indice = (percentil/100)*len;

plt.subplot(2, 2, 1)
plt.hist(myList, 100) #gráfico con 20 barras

plt.subplot(2, 2, 2)
plt.scatter(myListUniform, myList) #puntos

#Regresión lineal
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y) #Execute a method that returns some important key values of Linear Regression

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
print(mymodel)
plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.plot(x, mymodel)


plt.show()