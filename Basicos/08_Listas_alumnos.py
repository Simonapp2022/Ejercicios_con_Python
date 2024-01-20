# Lista alumnos
# Determino si el alumno pertenece a mi clase, y,
# en ese caso, calculo la media de 2 asignaturas
# También determino si ha aprobado, dependiendo de si ha sacado 5 o más

# Si no pertenece a mi clase, simplemente aparece un mensaje, pero no calculo nada

listaAlumnos=("Alina", "Raluca", "Aurelian", "Marian")
determinarAlumno=str(input("Introduce el nombre del alumno: "))

if determinarAlumno in listaAlumnos:
    print("Sí, el alumno", determinarAlumno, "es mi alumno.")
    notaMatem=float(input("Introduce la nota de Matemáticas de "+ determinarAlumno+" : "))                      
    print(notaMatem)

    notaFísica=float(input("Introduce la nota de Física de "+ determinarAlumno+" : "))
    print(notaFísica)
    
    notaMedia=(notaMatem+notaFísica)/2
    print("La media de las 2 notas del alumno: ", determinarAlumno, "es: ", notaMedia)
        
    if notaMedia>=5:
        print("El alumno: ", determinarAlumno, "ha aprobado.")
    else:
        print("El alumno: ",determinarAlumno, "NO ha sacado notas para aprobar.")
else:
    print("El alumno:", determinarAlumno, "no pertenece a mi clase.")
        

