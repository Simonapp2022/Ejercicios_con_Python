# Sirul lui Fibonacci
# a0=1; a1=1; a2=a0+a1; un numar e suma celor doua precedente
# 1,1,2,3,5,8,13,21,34,...
# a(n+1)=a(n)+a(n-1)
# Functia coresp sirului Fibonacci

def Fibonacci(número):
    if número==0 or número==1:
        return 1
    else: 
        return Fibonacci(número-1)+Fibonacci(número-2)
    
while True:
    n=int(input("Termenii sirului Fibonacci, de la primul pana inclusiv la nº: ", )) 
    if (n>=1):
        break

for i in range(n):
    print(Fibonacci(i))
    
        
