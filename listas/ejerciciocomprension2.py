
import random

x= int(input("digite el numero a buscar en los datos"))
q= int(random.randint(15,20))
cont=0
posc=[]
lista=[ random.randrange(0,9) for i in range(q) ]  

for i in lista:
    if i == x:
        cont=cont+1
if x in lista:
    print("el numero digitado si esta")
    
else:
    print("el numero digitado no esta")
    
if cont>1:
    print("el numero se repite", cont,"veces")    

for i in range (len(lista)):
    if x == lista[i]:
        posc.append (i)
print("el numero esta en la poscicion:", posc)
print(lista)


