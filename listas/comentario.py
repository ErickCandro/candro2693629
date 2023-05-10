#lo primero que se debe hacer es importar la biblioteca random para llenar las listas con numeros aleatorios segun el rango que se escoja 
import random
#se declara el def que sirve para definir la funcion en este caso llenarListas
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista
#podemos ver como dentro de la funcion llenarLista hay parametros los cuales fueron nombrados como tam y rango
#Esta funcion nos sirve para retornar los datos de la lista que se lleno anteriormente con la biblioteca random
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum
#esta funcion hace la suma de la lista anterior mente llena haciendo uso del return

def promedioLista(lista):
    return sumaLista(lista)/len(lista)
    
l1=llenarLista(3,10)
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2))