#Ejercicio Calcular el factorial de un número

# Defino la función recursiva "factorial"
# Contemplo también, el caso n==0 y n==1, cuando el valor del factorial es 1.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=factorial(5)
print(n)    



