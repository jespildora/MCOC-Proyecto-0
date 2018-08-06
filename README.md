# MCOC-Proyecto-0
En este proyecto se espera apreciar el problema de "loss of significance".
"Loss of significance, es un efecto indeseable de los calculos aritméticos usando precisión finita, tales como puntos flotantes".

El programa calcula la varianza de una muestra con distribución uniforme, de dos formas, una es usando la función scipy.var(), y la otra es usando operaciones aritméticas.
La varianza teórica de una distribución uniforme, es 1/12 para numeros entre 0 y 1, por lo que se trata de comparar en el código como se va perdiendo información en los ultimos digitos de significancia, debido a que cuanto se compara el error entre ambas operaciones, scipy y la forma aritmética, es un numero extremadamente pequeño, siendo que debería ser cero ya que se ocupa la misma lista como entrada de datos, pero como se aproximan los ultimos decimales, ya que se esta trabajando con 32 bit, terminan siendo valores parecidos pero no idénticos. 
Al final del código se puede apreciar que a mayor tamaño de la lista de datos, más preciso es el resultado disminuyendo el error de este.
