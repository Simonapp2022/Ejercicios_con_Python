#Ejercicio Valor del polinomio de grado 3 en un punto X=...
#p(x)=a*X^3+b*X^2+c*X+d, a distinto de cero
a=float(input("\n Introduce el valor de a:"))
b=float(input("\n Introduce el valor de b:"))
c=float(input("\n Introduce el valor de c:"))
d=float(input("\n Introduce el valor de d:"))

# Se determina el grado del polinomio, evaluando el valor de a

if a==0:
    print("\n El polinomio es de grado 2 o inferior, ya que a=0")
else:
    print("\n El polinomio es de grado 3.")

X=int(input(" Introduce el valor de X donde quieres que se calcule el polinomio:"))
valorDex=a*X*X*X+b*X*X+c*X+d

print("\n El valor del polinomio en el punto X dado es:", valorDex)

if valorDex==0:
    print("\n El valor de X es una solución de la ecuación P(X)=0 y se puede factorizar por X-", X)
    print("\n El polinomio se puede escribir así: ( X-", X, ")*( m*X^2 + n*X + p)") 
else:
    print("\n El valor de X dado no es una solución de la ecuación P(X)=0.")

