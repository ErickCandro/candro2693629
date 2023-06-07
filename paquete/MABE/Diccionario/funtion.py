def mostrar_menu():
    print("Bienvenido al programa")
    print("1. Alimentar diccionario español-inglés")
    print("2. Alimentar diccionario inglés-español")
    print("3. Usar diccionario español-inglés")
    print("4. Usar diccionario inglés-español")
    print("5. Ver diccionario español-inglés")
    print("6. Ver diccionario ingles-español")
    print("7. Salir")


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

def alimentar_diccionario_esp_ingles():
    palabra_esp = input("Ingrese una palabra en español: ")
    palabra_ing = input("Ingrese la traducción de la palabra en inglés: ")
    diccionarioI[palabra_ing] = palabra_esp


def alimentar_diccionario_ingles_esp():
    palabra_ing = input("Ingrese una palabra en inglés: ")
    palabra_esp = input("Ingrese la traducción de la palabra en español: ")
    diccionarioE[palabra_esp] = palabra_ing


def usar_diccionario_esp_ingles():
    palabra_esp = input("Ingrese una palabra en español para buscar su traducción: ")
    if palabra_esp in diccionarioI:
        print("La traducción al inglés es:", diccionarioI[palabra_esp])
    else:
        print("La palabra no se encuentra en el diccionario.")


def usar_diccionario_ingles_esp():
    palabra_ing = input("Ingrese una palabra en inglés para buscar su traducción: ")
    if palabra_ing in diccionarioE:
        print("La traducción al español es:", diccionarioE[palabra_ing])
    else:
        print("La palabra no se encuentra en el diccionario.")


def ver_diccionario_esp_ingles():
    print("Diccionario español-inglés:")
    for palabra_ing, palabra_esp in diccionarioI.items():
        print(palabra_ing, "---", palabra_esp)


def ver_diccionario_ingles_esp():
    print("Diccionario inglés-español:")
    for palabra_esp, palabra_ing in diccionarioE.items():
        print(palabra_esp, "---", palabra_ing)

continuar = True
while continuar:
     mostrar_menu()
     opcion = input("Ingrese el número de la opción deseada: ")

     if opcion == "1":
         alimentar_diccionario_esp_ingles()
     elif opcion == "2":
         alimentar_diccionario_ingles_esp()
     elif opcion == "3":
         usar_diccionario_esp_ingles()
     elif opcion == "4":
         usar_diccionario_ingles_esp()
     elif opcion == "5":
         ver_diccionario_ingles_esp()
     elif opcion == "6":
         ver_diccionario_esp_ingles()
     elif opcion == "7":
         print("¡Hasta luego!")
         continuar = False
     else:
         print("Opción inválida. Por favor, ingrese un número válido.")
