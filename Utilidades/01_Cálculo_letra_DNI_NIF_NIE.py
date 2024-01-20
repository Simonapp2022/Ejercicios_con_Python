# Cálculo letra DNI/NIE/NIF

# Se introduce el número formado por 8 dígitos y se determina:
# El resto de la división de un número por 23

#Guardo en una tupla las letras 

listaDigitos=("T","R","W","A","G","M","Y","F","P", "D","X","B","N","J","Z","S","Q","V","H","L","C","K","E")

#Pido por consola los 8 dígitos y los imprimo por pantalla
#Si es NIF:
# en lugar de X se pone un 0; 
# en lugar de Y se pone un 1 y 
# en lugar de Z se pone un 2

digitos=int(input("Introduce los 8 digitos de tu DNI/NIF: "))
print(digitos)

# Comprobamos que la longitud del DNI/NIE es de 8 dígitos; 
# Si son 8 dígitos, determino la letra
# Y si no, entonces aparece el mensaje de que has introducido +/- dígitos

longitud=len(str(digitos))

if longitud<=8:
    restoDivision=digitos%23
    print("El resto al dividir " + str(digitos) + " por el 23 es: ", restoDivision)
    print("La letra de tu DNI/NIF es: ",(listaDigitos[restoDivision]))
    print("Tu DNI/NIE completo es: ", str(digitos) + (listaDigitos[restoDivision]))
else: 
    print("Has introducido más de 8 o menos de 8 dígitos.")








