# A
def crear_matrices():
    matrices = []
    while True:
        adicionar_matriz = str(input('¿Crear matriz? (s/n):\n'))
        if adicionar_matriz.upper() == 'S':
            lineas = int(input('Indique el numero de lineas:\n'))
            columnas = int(input('Indique el numero de columnas:\n'))

            matriz = crear_matriz(lineas=lineas, columnas=columnas)
            matrices.append(matriz)
        else:
            break

    return matrices


def crear_matriz(lineas=0, columnas=0):
    matriz = []
    for linea in range(lineas):
        matriz.append([])
        for columna in range(columnas):
            valor = int(input(f'Introduzaca el valor de a{linea + 1}{columna + 1}: '))
            matriz[linea].append(valor)

    return matriz


# B
def determinante_existe(matriz):
    lineas, columnas = len(matriz), len(matriz[0])
    if lineas == columnas:
        return True
    else:
        return False


# C
def calcular_cofator(determinante, linea=1, columna=1):
    cofator = ((-1) ** (linea + columna)) * determinante
    return cofator


# D
def calcular_determinantes(matriz):
    orden = len(matriz)

    if orden == 1:
        determinante = matriz[0][0]

    elif orden == 2:
        determinante = calcular_orden_2(matriz)

    elif orden == 3:
        determinante = calcular_sarrus(matriz)

    elif orden > 3:
        determinante = calcular_laplace(matriz)

    return determinante


def calcular_orden_2(matriz):
    orden = 2
    diagonal_principal = 1
    diagonal_secundaria = 1
    for linea in range(orden):
        for columna in range(orden):
            if linea == columna:
                diagonal_principal *= matriz[linea][columna]
            else:
                diagonal_secundaria *= matriz[linea][columna]

    determinante = diagonal_principal - diagonal_secundaria
    return determinante


def calcular_sarrus(matriz):
    orden = 3
    diagonales_principales = []
    diagonales_secundarias = []
    for y in range(orden):
        diagonales_principales.append(1)
        diagonales_secundarias.append(1)

    for linea in range(orden):
        for columna in range(orden):
            # PRINCIPALES
            if linea == columna:
                diagonales_principales[0] *= matriz[linea][columna]
            elif (linea + 1) == columna or (linea - 2) == columna:
                diagonales_principales[1] *= matriz[linea][columna]
            elif (linea + 2) == columna or (linea - columna) == 1:
                diagonales_principales[2] *= matriz[linea][columna]

            # SECUNDARIAS
            if (linea + columna) == 2:
                diagonales_secundarias[0] *= matriz[linea][columna]
            elif (linea + columna) == 0 or (linea + columna) == 3:
                diagonales_secundarias[1] *= matriz[linea][columna]
            elif (linea + columna) == 4 or (linea + columna) == 1:
                diagonales_secundarias[2] *= matriz[linea][columna]

    diagonales_principales = sum(diagonales_principales)
    diagonales_secundarias = sum(diagonales_secundarias)

    determinante = diagonales_principales - diagonales_secundarias

    return determinante


def calcular_laplace(matriz):
    orden = len(matriz)

    if orden > 4:
        x = 0
        for elemento in matriz[0]:
            sub_matriz = crear_sub_matriz(matriz, elemento_linea=0, elemento_columna=x)
            x += 1
            calcular_laplace(sub_matriz)

    n = 0
    elementos_multiplicados_por_cofatores = []
    for elemento in matriz[0]:
        sub_matriz = crear_sub_matriz(matriz, elemento_linea=0, elemento_columna=n)
        n += 1
        determinante_sub_matriz = calcular_determinantes(sub_matriz)
        cofator_elemento = calcular_cofator(determinante_sub_matriz, linea=1, columna=n)

        elementos_multiplicados_por_cofatores.append(elemento * cofator_elemento)

    return sum(elementos_multiplicados_por_cofatores)


def crear_sub_matriz(matriz, elemento_linea=0, elemento_columna=0):
    sub_matriz = []
    for x in range(len(matriz) - 1):
        sub_matriz.append([])

    i = 0
    linea_atual = 0
    for linea in matriz:
        if linea_atual != elemento_linea:
            columna_atual = 0
            for columna in linea:
                if columna_atual != elemento_columna:
                    sub_matriz[i].append(columna)
                columna_atual += 1
            i += 1
        linea_atual += 1

    return sub_matriz


# E
def resolver_matrices_y_determinantes(matrices):
    x = 1
    for matriz in matrices:
        print(f'\nMatriz {x}')
        x += 1
        for linea in matriz:
            print(linea)

        if determinante_existe(matriz):
            determinante = calcular_determinantes(matriz)
            print(f'Determinante: {determinante}')
        else:
            print('No se puede calcular el determinante de esta matriz.')


matrices = crear_matrices()
resolver_matrices_y_determinantes(matrices)
