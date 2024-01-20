#Ejercicio Calcular nota final alumnos de una lista
# Si el alumno no está en la lista, aparece un mensaje
# Si el alumno está en mi lista, calculo la nota final del alumno así:
# respuestas correctas: 1 pct; respuestas incorrectas: -0,33 pct; sin contestar: 0 pct
# Al final, imprimo la lista con los nombres de los alumnos y las notas

listaAlumnos=["Cristina", "Costel", "Robert"]
listaNomisalumnos=[]

nombreAlumno=str(input("Introduce el nombre del alumno:"))

if nombreAlumno in listaAlumnos:
    print("El alumno está en la lista.")
    print("Introduce el nº de preguntas:")
    totalPreguntas=int(input())

    print("Introduce el número de respuestas correctas: ")
    respuestasCorrectas=int(input())

    print("Introduce el número de respuestas incorrectas: ")
    respuestasIncorrectas=int(input())

    print("Introduce el número de respuestas sin contestar: ")
    respuestasSincontestar=int(input())
    
   
    print("Total nº respuestas:", str(respuestasCorrectas+respuestasIncorrectas+respuestasSincontestar))

    if totalPreguntas!=(respuestasCorrectas+respuestasIncorrectas+respuestasSincontestar):
        print("Te has equivocado al introducir los datos, el nº de respuestas introducido es distinto del real.")
    else:
        print("Has puesto bien los datos")

    notaFinal=respuestasCorrectas*1+respuestasIncorrectas*0,33+respuestasSincontestar*0
    print("La nota final es:", str(notaFinal))
else:
    print("Este no es mi alumno, se añadirá a la otra lista de alumnos.")
    listaNomisalumnos.append(nombreAlumno)
    print("La otra lista, de alumnos que no son míos:", listaNomisalumnos)
    
