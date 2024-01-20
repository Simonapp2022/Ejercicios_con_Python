# Funciones recurrentes: factorial
# Defino la función que determina el valor del factorial de un nº natural

def factorial(n):
    if n==0 or n==1:
        resultado=1
    elif n>1:
        resultado=n*factorial(n-1)
    return resultado

x=int(input("Introduce el nº cuyo factorial quieres calcular: "))
print("El valor del factorial del número ", str(x), "es: ", factorial(x))










