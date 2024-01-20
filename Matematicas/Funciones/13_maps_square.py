# Función map en Python
# Devuelve un objeto map  de los resultados
# después de aplicar la función dada a cada item de la lista o tupla
# El valor devuelto por map() se puede pasar a funciones como:
# list() para crear una lista o set() para crear un set

# 1.Se define la función que eleva al cuadrado los números
def square(n):
    return n**2

# 2.Se pasa la lista de los números cuyos cuadrados quiero determinar
numbers=[10,20,30,40,50]

# 3.El resultado se almacena en la variable <result>
result=map(square, numbers)

print("La lista con los cuadrados de los números mencionados en la lista <numbers> es: ")
# 4.Imprime la lista de los cuadrados de los números que aparecen el la lista nombrada como <number>
# Es lo mismo que arrastrar la fórmula en Excel
print(list(result))
    