#Como usuario
#Quiero saber el coste diario, mensual y anual de un aparato, según su potencia en Wattios
#Para poder saber cuál sería, aproximadamente, el precio de tenerlo encendido.add()

# Datos de entrada:
# Potencia del aparato eléctrico
# Número de horas que estará funcionando
# El precio KWh

while True:
    PotenciaAparato=float(input("Introduce la potencia del aparato, en Wattios: "))
    if PotenciaAparato>0:
        break

NumerohorasFuncionando=float(input("Introduce el número de horas que estará funcionando: "))
PrecioKwh=float(input("Introduce al precio KWh, en €: "))

consumoDiario=(PotenciaAparato/1000)*NumerohorasFuncionando
costeDiario=consumoDiario*PrecioKwh
costeMensual=costeDiario*30

print("El consumo diario en Kwh es: ",round(consumoDiario,2) )
print("El coste diario en € es: ", round(costeDiario,2))
print("El coste mensual en € es: ", round(costeMensual,2))




