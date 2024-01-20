# Calculadora 3 opciones
# La calculadora se enciende y hasta que no tecleemos SaL, no se apaga
# Funciona de la siguiente manera:
# Recogemos los datos a y b y elegimos la opción 1, 2 o 3
# Si la Operación es 1, calcula la raíz cuadrada de la suma a y b
# Operación 2: calcula a/b, con la condición b distinto de 0
# Operación 3: calculamos la fórmula: (a*b)/2.5

import math
print("¡Bienvenido, la calculadora está funcionando!")
print(" Las opciones ofrecidas por la calculadora son:")
print(" Opción 1: Calcúla la raíz cuadrada de la suma a y b")
print(" Opción 2: Calcúla a/b")
print(" Opción 3: Calcúla (a*b)/2.5 ")


SeguirUsandolacalculadora=str(input("Quieres seguir usando la calculadora? Pulsa S si quieres seguir u otra letra, si no quieres seguir."))
print("Has pulsado: ", SeguirUsandolacalculadora)

while SeguirUsandolacalculadora=="S":
    a=float(input("Introduce el valor de a: "))
    print("El valor de a es:", a)
    b=float(input("Introduce el valor de b: "))
    print("El valor de b es:", b)

    opcion=int(input("Elige la opción de quieras ejecutar:"))
    print("Has elegido la opción: ", opcion)

    if opcion==1:
        resultadoOpcion1=math.sqrt(a+b)
        print("El resultado de la operación 1 es: ", resultadoOpcion1)
    else:
        if opcion==2:
            if b!=0:
                resultadoOpcion2=a/b
                print("El resultado de la operación 2 es: ", resultadoOpcion2)
            else:
                print("La opción 2 no se puede llevar a cabo, el valor de b es 0.")
        else:
            if opcion==3:
                resultadoOpcion3=(a*b)/2.5
                print("El resultado de la operación 3 es: ", resultadoOpcion3) 
            else:
                pass
                print("La opción elegida no es válida.")     


