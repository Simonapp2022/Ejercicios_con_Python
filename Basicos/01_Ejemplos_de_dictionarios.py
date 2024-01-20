#Ejemplos de dictionarios
#con claves números enteros

# Creando el diccionario

Dict={1: "Laura", 2: "Raluca"}
print("Diccionario con claves números enteros:")
print(Dict)

#Qué significa 1 usando el diccionario, dará el resultado "Laura"
print(Dict[1])

#Conseguir elementos usando get
# 0 no existe
# 1 significa Laura
# 2 significa Raluca
# 3 no existe

print(Dict.get(0))
print(Dict.get(1))
print(Dict.get(2))
print(Dict.get(3))


print(Dict.values())
print(Dict.keys())
print(Dict.items())

for i,j in Dict.items():
    print(f"El número {i} es {j}")




