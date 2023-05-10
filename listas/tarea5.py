import random
ind=0
def llenarLista(tam:10,rango:100):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def numeroMayor(lista):
    max=0
    for i in lista:
        if i>max:
            max=i
    return max

def numeroMenor(lista):
    mini=100000
    for max in lista:
        if max<mini:
            mini=max
    return mini

def menor(lista,tam):
    for i in range (len(lista)):
        for j in range(len(lista)-i-1):
            if lista[i]<lista[j+1]:
                lista[i], lista[j+1]=lista[j+1], lista[i]
        return tam 
    
def mayor(lista,tam):
    for i in range (len(lista)):
        for j in range(len (lista)-i+1):
 #           if lista[i]<lista[j+1]:
                lista[i], lista[j-1]=lista[j-1], lista[i]
        return tam   
def mediana(lista):
    if  (len(lista))%2==0:
        lista=(lista[(len(lista)//2)-1]+lista [len(lista)//2])/2
    else:
        lista=lista[(len(lista)//2)]
        
        return lista
def moda(lista):   
    ind=0
    for num in lista:
        cont=0
        for f in lista:
            if num == f:
                cont+=1
            if cont > ind:
                ind=cont
    moda=num
    return moda
l1=llenarLista(3,10)    
print(l1)
print("la suma de los numeros es",sumaLista(l1))
print("El promedio es ", round(promedioLista(l1),2))
print("el numero mayor es:",numeroMayor(l1))
print("el numero menor es:",numeroMenor(l1))
print("el numero ascendente es",mayor(l1,5))
print("el numero descendente es",menor(l1,5))
print("la mediana es:",mediana(l1))
print("la moda es:",moda(l1))