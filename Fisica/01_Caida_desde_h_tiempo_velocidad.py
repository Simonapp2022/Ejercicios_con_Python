# Ejercicio Caida cuerpo con una v_inicial desde una altura h

#Se introducen la velocidad inicial y la altura de lanzamiento del móvil

from ast import Constant
from cmath import sqrt

v0=float(input("\n Introduce la velocidad inicial en mps:"))
h=float(input("\n Introduce la altura en m:"))

# Se calcula la velocidad que tiene el móvil al tocar el suelo
# Defino el valor de la constante gravitacional en m/s^2

constanteGravitacional=9.81 

velocidadSuelo=sqrt(v0*v0+2*constanteGravitacional*h)
print("\n La velocidad en el momento de tocar el suelo en m/s es:", velocidadSuelo)

# Se calcula el tiempo (en h, min y seg)que necesita el móvil para alcanzar el suelo

tiempoSuelo_h=(velocidadSuelo-v0)/9.81
tiempoSuelo_min=tiempoSuelo_h*60
tiempoSuelo_seg=tiempoSuelo_min*60
print("El tiempo para alcanzar el suelo en horas es:", tiempoSuelo_h)
print("El tiempo para alcanzar el suelo en minutos es:", tiempoSuelo_min)
print("El tiempo para alcanzar el suelo en segundos es:", tiempoSuelo_seg)


