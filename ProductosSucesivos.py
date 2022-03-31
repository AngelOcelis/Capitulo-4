n=int(input("Digite Su Numero: "))
x=1
acumulador=1
for i in range(1,n+1):
    x1=(x*i)**2
    acumulador=acumulador*x1
print(acumulador)