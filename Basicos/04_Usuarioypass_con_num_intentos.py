#Ejercicicio comprobar usuarios y pass con número de intentos
print("\n ¡Bienvenido al programa con nº de intentos!")

# Defino el usuario y pass correctos para hacer log in

usuarioCorrecto="agente_secreto"
passCorrecta="123"
numeroIntentosmax=3

# Se comprueba si el usuario y la pass introducidas son correctas y aparece el mensaje de confirmación/error

for intento in range(numeroIntentosmax):
    # Se piden por consola el usuario y la pass
    usuario=input("\Introduce tu usuario:")
    passUsuario=input("Introduce tu contraseña: ")

    if usuario==usuarioCorrecto and passUsuario==passCorrecta:
        print("\n ¡Bienvenido, usuario y contraseña correctos!")
        break
    elif intento==numeroIntentosmax-1:
        print("\n Tu usuario ha sido bloqueado, has agotado el nº de 3 intentos.")
    else:
        print("\n El usuario y/o la contraseña introducidos son incorrectos.Te quedan " , numeroIntentosmax-intento-1)

    