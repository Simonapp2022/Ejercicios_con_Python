# Se introducen los parámetros de un polinomio de grd 3 
# Se calcula el valor del polinomios para distintos valores de X
# Si el valor de un polinomio en un punto X1 es nulo, X=X1 es solución de la ec: P(X)=0
# Y si no, entonces no lo es.
# Forma del polinomio : P(X)=a*X^3+b*X^2+c*X+d

a=float(input("Introduce el valor de a: "))
b=float(input("Introduce el valor de b: "))
c=float(input("Introduce el valor de c: "))
d=float(input("Introduce el valor de d: "))

valPuntox=float(input("Introduce el valor de X: "))

def polinomioGrd3(a,b,c,d):
    valPolinomioenx=a*valPuntox*valPuntox*valPuntox+b*valPuntox*valPuntox+c*valPuntox+d
    print("El valor del polinomio dado, en el punto dado, tiene este valor: ", valPolinomioenx)
    
    if valPolinomioenx==0:
        print("El punto X dado es solución de la ecuación P(X)=0.")
    else:
        print(" El punto X dado NO es solución de la ecuación P(X)=0.")
polinomioGrd3(a,b,c,d)

