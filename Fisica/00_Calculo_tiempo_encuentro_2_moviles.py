# Ejercicio Cálculo tiempo de encuentro de 2 móviles

# Se introducen los datos

velocidad1=float(input("\n Introduce la velocidad del primer móvil en km/h:"))
velocidad2=float(input("\n Introduce la velocidad del segundo móvil en km/h:"))
distanciaMomentopartida=float(input("\n Introduce la distancia entre los dos móviles en el momento de partida, en km:"))

# Cálculo tiempo trascurrido en el momento de encuentro
# Condición de encuentro: d1+d2=D

tiempoEncuentro_h=distanciaMomentopartida/(velocidad1+velocidad2)
tiempoEncuentro_min=tiempoEncuentro_h*60
tiempoEncuentro_segundos=tiempoEncuentro_min*60
distanciaRecorridamov1=velocidad1*tiempoEncuentro_h
distanciaRecorridamov2=velocidad2*tiempoEncuentro_h
acceleracionMov1=velocidad1/tiempoEncuentro_h
acceleracionMov2=velocidad2/tiempoEncuentro_h
sumaDistanciarecorrida=distanciaRecorridamov2+distanciaRecorridamov1

#Se determina cuál de los móviles tiene la mayor velocidad

if velocidad1>=velocidad2:
    print("\n El primer móvil tiene mayor velocidad")
    difVelocidad12=velocidad1-velocidad2
    print("\n La diferencia de velocidad entre 1 y 2 en km/h es de:", difVelocidad12)
else:
    print("\n El segundo móvil tiene mayor velocidad")
    difVelocidad21=velocidad2-velocidad1
    print("\n La diferencia de velocidad entre 2 y 1 en km/h es de:", difVelocidad21)

#Se comprueba que el resultado es correcto
if sumaDistanciarecorrida==distanciaMomentopartida:
    print("\n El resultado está OK")
else:
    print("\ Está mal calculado...")

#Salida por pantalla tiempo encuentro

print("\n El tiempo de encuentro en horas es:", tiempoEncuentro_h)
print("\n El tiempo de encuentro en minutos es:", tiempoEncuentro_min)
print("\n El tiempo de encuentro en segundos es:", tiempoEncuentro_segundos)
print("\n La distancia recorrida por el móvil1 en km es:", distanciaRecorridamov1)
print("\n La distancia recorrida por el móvil2 en km es:", distanciaRecorridamov2)
print("\n La acceleración del Mov1 en km/h^2 es:", acceleracionMov1)
print("\n La acceleración del Mov2 en km/s^2 es:", acceleracionMov2)
print("\n El resultado es correcto")        








