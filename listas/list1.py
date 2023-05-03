import random
mediana=0
suma=0
max=0
min=1000
prom=0
lista= []
tam= int(random.randint (10,20))
print(tam)
for i in range (tam):
    num= int(random.randrange(100))
    lista.append(num)
    suma+=num
    prom=suma/tam
    if num>max:
        max=num
    if num<min and num!=0:
        min=num

print ("la lista de numeros es ", lista)
print ("la suma de los numeros es ",suma)
print("el promedio es",prom)
print ("el numero maximo es ",max)
print ("el numero minimo es",min)
print ("la media es:",mediana)