#Ejercicio Frutería cesta
listaFrutas=["manzana", "melocotón", "mandarina", "pera", "ciruela", "coco", "plátano"]

producto=str(input("Introduce la fruta que quieres comprar: "))
if producto in listaFrutas:
    print("La fruta seleccionada se encuentra disponible en nuestro almacén. ¿Deseas algo más?")
    respuestaMasfruta=str(input("S/N"))
    if respuestaMasfruta=="S" or respuestaMasfruta=="s":
        otraFruta=str(input("También quiero comprar: "))
        if otraFruta==producto:
            print("Ya has encargado esta fruta, elíge otra, si quieres.")
        else:
            print("De acuerdo, estamos preparando su pedido.")
    else:
        print("De acuerdo, estamos preparando su pedido.")
    
else:
    print("La fruta elegida no está en nuestro almacén, ¿deseas encargarla?")
    respuesta=str(input("Si deseas encargar la fruta, pulsa la letra <S>: " ))

    if respuesta=="S" or respuesta=="s":
        print("De acuerdo, encargamos la fruta seleccionada.")
    else:
        print("Gracias por su visita.")


    
