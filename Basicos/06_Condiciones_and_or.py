#Ejercicio and_or
# Si se cumple la condición and-or, tienes derecho a beca

# Se utiliza la función lower para escribir un título íntegramente en minúsculas
tituloEjerciciolower=str.lower("EsTe título SE ESCRIBIRÁ EN minÚSCULAS Íntegramente.")
print(tituloEjerciciolower)

# Se utiliza la función upper para escribir un título íntegramente en mayúsculas
tituloEjercicioupper=str.upper("esTe título se escribirá en mayúsculAs íntegramente.")
print(tituloEjercicioupper)

# Se definen las variables: salario anual, distancia hasta el colegio y el número de hermanos:
# Se introducen correctamente los valores de las variables(hasta que no sean nº positivos enteros, te lo sigue pidiendo por consola.)
salarioAnual=int(input("Introduce el salario anual familiar: "))
while salarioAnual<=0:
    salarioAnual=int(input("Introduce correctamente el salario anual familiar:"))

distanciaHastaelcolegio=float(input("Introduce la distancia en km desde tu casa hasta el colegio: "))
while distanciaHastaelcolegio<=0:
    distanciaHastaelcolegio=int(input("Introduce correctamente la distancia hasta el colegio en km:"))

numeroHermanos=int(input("Introduce el nº de hermanos/hermanas que tienes: "))
while numeroHermanos<=0:
    numeroHermanos=int(input("Introduce correctamente el número de hermanos:"))

# Se evalúa si se cumplen las condiciones and/or y se imprime por pantalla el resultado, en cada caso.
if distanciaHastaelcolegio>3 and numeroHermanos>3 or salarioAnual<18000:
    print("Tienes derecho a beca, sí reúnes las condiciones necesarios.")
else:
    print("No tienes derecho a beca, no reúnes los requisitos.")
    
        