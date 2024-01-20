# Sumar los elementos de 3 listas
# Se define la función de sumar los elementos de las 3 listas

def Suma_elementos_lista(n1, n2, n3):
    return n1+n2+n3

# Se pasan las 3 listas que contienen los elementos a sumar
n1=[1,2,3,4,5]
n2=[54,34,23,12,34]
n3=[12,34,56,45,23]

# El resultado de sumar los elementos correspondientes de la lista se almacena en <resultado>
# Es lo mismo que arrastrar la fórmula en Excel, de una casilla a las demás
resultado=map(Suma_elementos_lista, n1, n2, n3)

# Se imprime por pantalla la lista que contiene los elementos- resultado de sumar
print(list(resultado))
