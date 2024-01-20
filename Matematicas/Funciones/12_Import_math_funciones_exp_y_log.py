# Funciones exponenciales y logarítmicas
#1. math.cbrt(x) Retorna la raíz cúbica de x.

#2. math.exp(x) Retorna e elevado a la x potencia, dónde e = 2.718281… es la base de los logaritmos naturales. 
# Esto generalmente es más preciso que math.e ** x o pow(math.e, x).

#3. math.exp2(x) Retorna 2 elevado a la potencia x.

#4. math.expm1(x) Retorna e elevado a la x potencia, menos 1. Aquí e es la base de los logaritmos naturales. 
# Para flotantes x pequeños, la resta en exp(x) - 1 puede resultar en una pérdida significativa de precisión; 
# la función expm1() proporciona una forma de calcular este valor con una precisión total:

#5.  math.log1p(x)
# Retorna el logaritmo natural de 1+x (base e). 
# El resultado se calcula de forma precisa para x cercano a cero.

# 6. math.log2(x)
# Retorna el logaritmo en base 2 de x. Esto suele ser más preciso que log(x, 2).

# 7. math.log10(x)
# Retorna el logaritmo en base 10 de x. Esto suele ser más preciso que log(x, 10).

# 8. math.sqrt(x)
# Retorna la raíz cuadrada de x.

# 9. math.pow(x, y)
# Retorna x elevado a la potencia y. 
# Los casos excepcionales siguen el estándar IEEE 754 en la medida de lo posible. 
# En particular, pow(1.0, x) y pow(x, 0.0) siempre retornan 1.0, incluso cuando x es cero o NaN. 
# Si tanto x como y son finitos, x es negativo e y no es un número entero, entonces pow(x, y) no está definido y se lanza una excepción ValueError.
# No la incluyo en la calculadora, porque es la única que necesita 2 param



import math

print("Calculadora funciones exponenciales y logarítmicas")
print("___________________________________________________")
print("Las operaciones que ofrece la calculadora son los siguientes:")
print("Operación1-Calcula la raíz cúbica de x")
print("Operación2- Calcula e elevado a la x potencia ")
print("Operación3- Calcula 2 elevado a la potencia x")
print("Operación4- Calcula e elevado a la x potencia, menos 1")
print("Operación5- Calcula el logaritmo natural de 1+x (base e) ")
print("Operación6- Calcula el logaritmo en base 2 de x")
print("Operación7- Calcula el logaritmo en base 10 de x")
print("Operación8- Calcula la raíz cuadrada de x")

# Se tiene que introducir un número del 1 al 10 inclusive
# correspondiente a la operación que se quiere realizar

variable1=float(input("Introduzca el valor de la variable:"))


opcion=0
while opcion !=9:
    print("""Indica la opción a realizar:
    1.Calcula la raíz cúbica de x")
    2.Calcula e elevado a la x potencia ")
    3.Calcula 2 elevado a la potencia x")
    4.Calcula e elevado a la x potencia, menos 1")
    5.Calcula el logaritmo natural de 1+x (base e) ")
    6.Calcula el logaritmo en base 2 de x")
    7.Calcula el logaritmo en base 10 de x")
    8.Calcula la raíz cuadrada de x")
    9.Salir
    """)
    opcion=int(input("Introduce la opción:"))

    if opcion==1:
        print("El resultado de la operación 1 es: ", math.cbrt(variable1))

    if opcion==2:
        print("El resultado de la operación 2 es: ", math.exp(variable1))

    if opcion==3:
        print("El resultado de la operación 3 es: ", math.exp2(variable1))

    if opcion==4:
        print("El resultado de la operación 4 es: ", math.expm1(variable1))

    if opcion==5:
        print("El resultado de la operación 5 es: ", math.log1p(variable1))

    if opcion==6:
        print("El resultado de la operación 6 es: ", math.log2(variable1))

    if opcion==7:
        print("El resultado de la operación 7 es: ", math.log10(variable1))

    if opcion==8:
        print("El resultado de la operación 8 es: ", math.sqrt(variable1))

    if opcion==9:
        print("Gracias por utilizar la calculadora.")





