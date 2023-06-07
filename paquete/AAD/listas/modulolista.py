import random

#funcion para llena una lista
def LlenarArreglo(tam):
    lista=[random.randrange(100) for i in range(tam)]    
    return lista

#funcion para sumar los elementos de la lista
def SumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return print(f"la suma de los elementos de la lista es {sum}")

#ordenar una lista de fora ascendente 
def OrdenarListaAscendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return print(f'La lista ordenada de forma ascendente es {lista}')

#ordenar lista descendente
def OrdenarListaDescendente(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return print(f'La lista ordenada de forma descendente es {lista}')

#hallar la moda de la lista
def Moda(lista):
    OrdenarListaAscendente(lista)
    contador = 0
    mayor = 0
    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                contador += 1
        if contador > mayor:
            mayor = contador
            moda = lista[i]
        elif mayor<=1:
            moda = 0
    if moda != 0:
        print('la moda es ', moda)
    else:
        print('no hay moda en esta lista ya que ningun numero se repite')

