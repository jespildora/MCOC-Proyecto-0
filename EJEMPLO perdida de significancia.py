import random
import scipy
lista=[0]
n=100
lista=[0]*n

for i in range(n):
    lista[i]=random.random()

varianza=scipy.var(lista)
print "La Varianza es: ", varianza

#SI CALCULAMOS LA VARIANZA DE UNA FORMA DISTINTA
suma = 0
for j in lista:
        suma = suma + j
p=suma/len(lista)
sumatoria=0
for h in lista:
        sumatoria= sumatoria + (h-p)**2
varianza1 = sumatoria/(len(lista)-1)
print "La varianza calculada de otra forma es: ",varianza1   
print ''
print 'El error entre ambas es de: ', varianza1-varianza
     