# Ejercicio El programa multiplica 2 polinomios de tercer grado
# La forma del primer polinómio es: a*X^3+b*X^2+c*X+d
# La forma del segundo polinómio es: e*X^3+f*X^2+g*X+h
# El resultado de la multiplicación es un polinómio de sexto grado, de forma:
# a*e*X^6+(a*f+b)*X^5+(a*g+b*f+c*e)*X^4+
#(a*h+b*g+c*f+d*e)*X^3+(b*h+c*g+d*f)*X^2+(c*h+d*g)*X+dh

print("Programa de cálculo producto de dos polinómios")

# Se piden los valores de: a, b, c, d, e, f, g y h
# Y se imprimen por pantalla

a=float(input("Introduce el valor de a: "))
b=float(input("Introduce el valor de b: "))
c=float(input("Introduce el valor de c: "))
d=float(input("Introduce el valor de d: "))
e=float(input("Introduce el valor de e: "))
f=float(input("Introduce el valor de f: "))
g=float(input("Introduce el valor de g: "))
h=float(input("Introduce el valor de h: "))

print("El polinómio P(X) es: ", str(a)+"*"+"X^3+"+str(b)+"*"+"X^2+"+str(c)+"*"+"X+"+str(d))
print("El polinómio Q(X) es: ", str(e)+"*"+"X^3+"+str(f)+"*"+"X^2+"+str(g)+"*"+"X+"+str(h))

print("El resultado de la multiplicación: P(X)*Q(X) es R(X). ")

print("R(X)= ")
print("Se efectúa el cálculo de los coeficientes.")

coefGrd6=a*e
coefGrd5=a*f+b
coefGrd4=a*g+b*f+c*e
coefGrd3=a*h+b*g+c*f+d*e
coefGrd2=b*h+c*g+d*f
coefGrd1=c*h+d*g
termIndep=d*h

print("El coeficiente de grado 6 es: ", coefGrd6)
print("El coeficiente de grado 5 es: ", coefGrd5)
print("El coeficiente de grado 4 es: ", coefGrd4)
print("El coeficiente de grado 3 es: ", coefGrd3)
print("El coeficiente de grado 2 es: ", coefGrd2)
print("El coeficiente de grado 1 es: ", coefGrd1)
print("El término independiente es: ", termIndep)

print("Coeficiente grd6 e incógnita: ", "("+str(coefGrd6)+")*X^6")
print("Coeficiente grd5 e incógnita: ", "("+str(coefGrd5)+")*X^5")
print("Coeficiente grd4 e incógnita: ", "("+str(coefGrd4)+")*X^4")
print("Coeficiente grd3 e incógnita: ", "("+str(coefGrd3)+")*X^3")
print("Coeficiente grd2 e incógnita: ", "("+str(coefGrd2)+")*X^2")
print("Coeficiente grd1 e incógnita: ", "("+str(coefGrd1)+")*X")
print("Término independiente: ", "("+str(termIndep)+")")

print("R(X)= ",  "("+str(coefGrd6)+")*X^6"+" +"+"("+str(coefGrd5)+")*X^5"+" +"+"("+str(coefGrd4)+")*X^4"+" +"+"("+str(coefGrd3)+")*X^3"+" +"+"("+str(coefGrd2)+")*X^2"+" +"+"("+str(coefGrd1)+")*X"+" +"+"("+str(termIndep)+")")





