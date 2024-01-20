#Lista de la compra

# Crear 3 opciones: mostrar lista frutas_ dias semana_salir
# Declarar variable listaCompra

listaCompra=[]
opcion=0

while opcion!=3:
    # Mostrar las opciones del menú
    print("##### Opciones de menú #####")
    print(" 1.Lista de la compra")   
    print(" 2.Añadir a la lista de la compra")
    print(" 3.Salir del programa")

    # Recogemos la opción seleccionada por el usuario
    opcion=int(input("Introduce la opción deseada: "))

    # Validamos que la opción sea correcta
    if opcion >3 or opcion <1:
        print(" La opción no es correcta.")

    # Se ejecuta la opción seleccionada por el usuario
    if opcion==1:
        print("Lista de la compra")
        print(listaCompra)
        for prod in listaCompra:
            print(prod)
         
    if opcion==2:
        print("Añadir producto a la lista")
        nombreProducto=input("Introduce le nombre del producto deseado: ")
        listaCompra.append(nombreProducto)
        
    if opcion==3:
        print("¡Hasta la próxima!") 
pass      

