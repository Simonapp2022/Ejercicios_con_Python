# Cálculo hipotenusa, dados los catetos opuesto y adyacente
# Se define la función con 2 parámetros

from cmath import sqrt
import math

def hipotenusa(a,b):
    if a>0 and b>0:
        c=sqrt(a*a+b*b)
        return c
 
catOpuesto=float(input("Introduce la medida del cateto opuesto: "))
catAdyacente=float(input("Introduce la medida del cateto adyacente: "))

hipotenusa=hipotenusa(catOpuesto,catAdyacente)

print("La medida de la hipotenusa con 2 decimales es: ", round(hipotenusa.real,2))
# Se determina si el triangulo es isoscel:

if catOpuesto==catAdyacente:
    print("El triángulo es un triángulo isósceles.")
else:
    print("El triángulo NO es un triángulo isósceles.")







