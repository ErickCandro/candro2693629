diccionario_español_ingles = {}
diccionario_ingles_español = {}

def agregar_animal():
    nombre_español = input("Ingrese el nombre del animal en español: ")
    nombre_ingles = input("Ingrese el nombre del animal en inglés: ")

    diccionario_español_ingles[nombre_español] = nombre_ingles
    diccionario_ingles_español[nombre_ingles] = nombre_español
    return 
español=agregar_animal