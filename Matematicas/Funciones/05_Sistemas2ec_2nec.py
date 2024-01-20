# Método para resolver un sistema de 2 ecuaciones con 2 incógnitas
# La forma del sistema es:
# a*X+b*Y=c
# d*x+e*Y=f
# Las variables a, b, c, d, e y f las introduce el usuario
# el programa determina los valores de X e Y, siendo la condición: a*e != de b*d
# Es decir que el determinante sea distinto de cero

def sistDosecdosinc(a, b, c, d, e, f):
    determinante=a*e-b*d

    if determinante!=0:
        X=(c*e-b*f)/determinante
        Y=(a*f-c*d)/determinante
        return X,Y
    else:
        return None, None   

a= float(input("Introduce el valor de a: "))
b= float(input("Introduce el valor de b: "))
c= float(input("Introduce el valor de c: "))
d= float(input("Introduce el valor de d: "))
e= float(input("Introduce el valor de e: "))
f= float(input("Introduce el valor de f: "))

print("Las soluciones del sistema son: ")
print(sistDosecdosinc(a,b,c,d,e,f))


      





