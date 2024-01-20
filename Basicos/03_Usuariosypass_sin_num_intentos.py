# Ejercicio comprobar usuario y pass sin num intentos

# Defino el usuario y pass correctos para hacer log in

usuarioCorrecto="agente_secreto"
passCorrecta="123"

# Se piden por consola el usuario y la pass

usuario=input("\Introduce tu usuario:")
passUsuario=input("Introduce tu contraseña: ")

# Se comprueba si el usuario y la pass introducidas son correctas y aparece el mensaje de confirmación/error


if usuario==usuarioCorrecto and passUsuario==passCorrecta:
    print("\n ¡Bienvenido, usuario y contraseña correctos!")
else:
    print("\n El usuario y/o la contraseña introducidos son incorrectos.")



        
     