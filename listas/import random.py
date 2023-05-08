import random
#se crea la primera lista con numeros random
lista=[]
tam= int(random.randint (10,15))
for x in range (tam):
    num= int(random.randrange(100))
    lista.append(num)

#se crea la segunda lista con numeros random
list=[]
tamaño= int(random.randint (10,15))
for i in range (tamaño):
    num= int(random.randrange(100))
    list.append(num)

print("los numeros son ",lista)
print("los numeros son ",list)

#se suman los numeros de las listas para saber cual tiene la suma mas alta 
if sum(lista) > sum (list):
    print("la lista 1 es la suma mas alta")
elif sum(lista) < sum(list):
    print("la suma mayor es la lista 2 ")
#se establecen las variables para almacenar los datos de que lista tiene el numero mayor y menor 
max_lista= max(list)
max_lista2= max(lista) 

if max_lista > max_lista2:
    print("la lista 1 tiene el numero mayor",max_lista)
elif max_lista < max_lista2:
    print("la lista 2 tiene el numero mayor",max_lista2)
#se crea la variable en la cual se almacenara la informacion de los promedios de cada lista 
prom_conjunto = (sum(list) + sum(lista)) / (num * 2)
prom1 = sum(list) / num
prom2 = sum(lista) / num
if prom1 > prom_conjunto:
    print("La primera lista tiene un promedio por encima del conjunto")
else:
    print("La primera lista tiene un promedio por debajo del conjunto")
if prom2 > prom_conjunto:
    print("La segunda lista tiene un promedio por encima del conjunto")
else:
    print("La segunda lista tiene un promedio por debajo del conjunto")

par1 = sum(1 for num in list if num % 2 == 0)
par2 = sum(1 for num in lista if num % 2 == 0)
if par1 > par2:
    print("La primera lista tiene mayor cantidad de pares")
else:
    print("La segunda lista tiene mayor cantidad de pares")

# Cuál de los dos tiene mayor cantidad de impares
impar1 = sum(1 for num in list if num % 2 == 1)
impar2 = sum(1 for num in lista if num % 2 == 1)
if impar1 > impar2:
    print("La primera lista tiene mayor cantidad de impares",impar1)
else:
    print("La segunda lista tiene mayor cantidad de impares")















