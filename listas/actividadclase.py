import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def Ascendente(lista,tam):
    for i in range (tam-1):
        for j in range(i+1,tam):
            if list[i]>list[j]:
                aux=list[i]
                list[i]=list[j]
                list[j]=aux
        return lista

print(Ascendente(l1,4))

def numeroMayor(lista):
    max=0
    for i in lista:
        if i>max:
            max=i
    return max
l1=llenarLista(3,10)    
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2))
print(numeroMayor(l1))
