import random
import scipy
from matplotlib import pyplot
lista=[0]
n=10
lista=[0]*n
t=0
valores=[]
valores1=[]

while t<=5: 
    for i in range(n):
        lista.append(random.random())

    varianza=scipy.var(lista, ddof=1)
    print 'Para una muestra con ',n,'elementos'
    print "La Varianza es: ", varianza
    
#SI CALCULAMOS LA VARIANZA DE UNA FORMA DISTINTA
    suma = 0
#Primero se suman todos los elementos de una lista
    for j in lista:
        suma = suma + j
#Luego se calcula el Promedio Artimetico
    p=suma/len(lista)


    suma = scipy.sum(lista)


    sumatoria=0
#Se calculan las diferencias cuadraticas entre los elementos de la lista y el promedio
    for h in lista:
        sumatoria= sumatoria + (h-p)**2
#Se calcula la varianza dividiendo la operacion anterior por el numero de elementos de la lista
    varianza1 = sumatoria/(len(lista)-1)
    valores.append(varianza)
    valores1.append(varianza1)
    print "La varianza calculada de otra forma es: ",varianza1   
    print 'El error entre ambas es de: ', varianza1-varianza
    print ' ' 
    n=n*10
    t=t+1

#Se creara una lista con el valor teorico de la varianza de una distribucion uniforme que va de 0 a 1
teorico=[1.0/12,1.0/12,1.0/12,1.0/12,1.0/12,]

pyplot.plot(valores,'b')
pyplot.plot(valores,'r')
pyplot.plot(teorico,'c')
pyplot.show
