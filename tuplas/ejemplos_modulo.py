import random as vip
tam=vip.randint (5,10)
lista=[vip.randrange(100)for i in range(tam)]
rebanada=lista[len(lista)//2:len(lista)]
print(lista)
print(rebanada)




"""from random import randint,randrange      
tam=randint (5,10)
lista=[randrange(100)for i in range(tam)]
rebanada=lista[len(lista)//2:len(lista)]
print(lista)
print(rebanada)"""


"""from random import *

tam=randint(1,20)
tup=()
for i in range (tam):
    tupla=randrange(0,100)
    tup=tup+(tupla,)
print(tup)"""
