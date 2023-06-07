from sys import path

path.append ("C:\pythonsandoval")#('..\\pythonsandoval')

import MABE.Listas.funcion
from MABE.Listas.funcion import lisAscendente, lisDescendente, llenarLista, mayor, mediana, menor, moda, promedioLista, sumaLista
lista1=llenarLista(3,10)
print(lista1)
print("la suma es: ")
print(sumaLista(lista1))
print("el promedio es: ")
print(round(promedioLista(lista1),2))
print("el numero mayor es: ")
print(mayor(lista1))
print("el numero menor es: ")
print(menor(lista1))
print("la lista organizada de forma ascendente es: ")
print(lisAscendente(lista1))
print("la lista organizada de forma descendente es: ")
print(lisDescendente(lista1))
print("la moda es: ")
print(moda(lista1))
print("la mediana es: ")
print(mediana(lista1))

import MABE.Diccionario.funtion
from MABE.Diccionario.funtion import alimentar_diccionario_esp_ingles, alimentar_diccionario_ingles_esp, mostrar_menu, usar_diccionario_ingles_esp, ver_diccionario_esp_ingles, ver_diccionario_ingles_esp  

diccionarioI = {
    'Bee': 'abeja',
    'Eagle': 'águila',
    'Spider': 'araña',
    'Squirrel': 'ardilla',
    'Whale': 'ballena',
    'Donkey': 'burro',
    'Hen': 'gallina',
    'Cock': 'gallo',
    'Seal': 'foca',
    'Elephant': 'elefante'
}

diccionarioE = {
    'abeja': 'Bee',
    'águila': 'Eagle',
    'araña': 'Spider',
    'ardilla': 'Squirrel',
    'ballena': 'Whale',
    'burro': 'Donkey',
    'gallina': 'Hen',
    'gallo': 'Cock',
    'foca': 'Seal',
    'elefante': 'Elephant'
}
while continuar:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        alimentar_diccionario_esp_ingles()
    elif opcion == "2":
        alimentar_diccionario_ingles_esp()
    elif opcion == "3":
        ver_diccionario_esp_ingles()
    elif opcion == "4":
        usar_diccionario_ingles_esp()
    elif opcion == "5":
        usar_diccionario_ingles_esp()
    elif opcion == "6":
        ver_diccionario_ingles_esp()
    elif opcion == "7":
        print("¡Hasta luego!")
        continuar = False
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
