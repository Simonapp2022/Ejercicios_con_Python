# Defino la función determinante3 para el cálculo de un determinante de orden 3

def determinante3(a,b,c,d,e,f,g,h,i):
    detTres=a*(e*i-f*h)-b*(d*i-g*f)+c*(d*h-g*e)
    return detTres

a= float(input("Introduce el valor de a: "))
b= float(input("Introduce el valor de b: "))
c= float(input("Introduce el valor de c: "))
d= float(input("Introduce el valor de d: "))
e= float(input("Introduce el valor de e: "))
f= float(input("Introduce el valor de f: "))
g= float(input("Introduce el valor de g: "))
h= float(input("Introduce el valor de h: "))
i= float(input("Introduce el valor de i: "))

print("El valor del determinante de orden tres es: ", determinante3(a,b,c,d,e,f,g,h,i))
