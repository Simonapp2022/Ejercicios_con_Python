# Se calcula el valor del determinante de orden 2, en base a los datos que se introducen
# Se define la función con el nombre de determinante( el determinante es un número, no una función)
# Pero no hay que confundir la función de cálculo con lo que es un determinante

def determinante2(a,b,c,d):
    detDos=a*d-b*c
    return detDos


a=float(input("Introduce el valor de a: "))
b=float(input("Introduce el valor de b: "))
c=float(input("Introduce el valor de c: "))
d=float(input("Introduce el valor de d: "))

print("El valor del determinante de orden dos es: ", determinante2(a,b,c,d))


    



