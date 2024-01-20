# Ejercicio listas
# En una lista vacía, almaceno las notas de un alumno
# Introduzco las notas hasta introducir la letra Q o q en un while
# Calcúlo el número de notas que hay en la lista
# Hago la suma y la divido entre el número de notas, 
# determinando así, la nota media del alumno
# Defino la lista de notas del alumno, vacía
listaNotasalumno=[]
# Pido las notas, una por una:
nota=(input("Introduce la nota: "))
# Introduzco notas hasta pulsar la tecla Q o q

while nota.upper()!="Q":
    listaNotasalumno.append(nota)
    nota=input("Introduce otra nota, hasta introducir <Q> o <q>: ") 

# Determino el nº de notas de 9 que ha sacado el alumno, la vb notasNueve está a cero
# cuando empieza el for
# De momento, funciona bien con notas int
# con notas tipo float, no calcula el nº de notas de 9
notasNueve=0
for i in listaNotasalumno:
    if i==str(9):
        notasNueve+=1
print("El alumno ha sacado: ", notasNueve, "notas de nueve." )
    
# El número de notas de la lista es:
print("El número de notas del alumno introducidas es: ", len(listaNotasalumno))
# La suma de las notas del alumno la determino con un for, recorriendo la lista
# La suma de las notas tiene previamente el valor cero

sumaNotas=0
for valor in listaNotasalumno:
    sumaNotas=sumaNotas+float(valor)
    print("La suma de las notas introducidas hasta ahora es: ", sumaNotas)

# Determino la media de las notas, efectuando el cociente: suma/num notas

mediaNotas=sumaNotas/(len(listaNotasalumno))
print("La nota media del alumno es: ", mediaNotas)
round(mediaNotas,2)
print("La nota media del alumno, redondeada a dos decimales es: ", round(mediaNotas,2))

# Determino si la mendia del alumno es superior o igual a 5, para ver si ha aprobado el curso.
if mediaNotas>=5:
    print("El alumno ha aprobado el curso. ¡Enhorabuena!")
else:
    print("El alumno ha suspendido, la nota es inferior a 5.")

# Imprimo por pantalla la lista de notas del alumno
print("La lista de las notas del alumno es: ")
print(listaNotasalumno)





  
