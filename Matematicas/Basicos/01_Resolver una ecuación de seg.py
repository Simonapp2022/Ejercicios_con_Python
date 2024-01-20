#Ejercicio Resolver una ecuación de segundo grado
# a*X^2+b*X+c=0, soluciones: X1,2=(-b+/-(delta)^1/2)/(2*a)
import math

print("Resolución de ecuaciones de segundo grado")
print("Ecuación de segundo grado: a*X^2+b*X+c=0, soluciones: X1,2=(-b+/-(delta)^1/2)/(2*a)")

a=float(input("\n Introduce el valor de a:"))
b=float(input("\n Introduce el valor de b:"))
c=float(input("\n Introduce el valor de c:"))


if a==0 and b==0 and c==0:
    print("\n No es una ecuación, sino una identidad, ya que: 0=0.")
else:
    if a==0 and b==0 and c!= 0:
        print("¡Contradicción! Se ha introducido un valor de c distinto de cero.")
        print(" El valor", c, "no es igual a cero. La igualdad es falsa.")
    else:
        if a==0 and b!=0 and c==0:
            print(" La solución de la ecuación de primer grado es:", c/b)
        else:
            if a==0 and b!=0 and c!=0:
                print("La solución de la ecuación de primer grado es:", c/b)
            else:
                delta=b*b-4*a*c
                print("\n El valor del delta es:", delta)
                if delta<=0:
                    print("\n Las soluciones de la ecuación de segundo grado no son reales, ya que delta es negativo.")
                else:
                    print("\n Las soluciones de la ecuación de segundo grado son reales, ya que delta es positivo o cero.")

                if a!=0 and delta>=0:
                    print("Las soluciones de la ecuación de segundo grado son:")
                    print("x1:", (-b+(math.sqrt((b*b)-(4*a*c)))/(2*a)))
                    print("x2:", (-b-(math.sqrt((b*b)-(4*a*c)))/(2*a)))

                    

