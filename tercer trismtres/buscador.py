

from os import strerror

# Inicializa un diccionario para todos los caracteres que deseas contar, incluyendo letras latinas, símbolos y dígitos.
counters = {chr(ch): 0 for ch in range(32, 127)}
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Solo aumenta el contador si el carácter está presente en el diccionario.
            if char in counters:
                counters[char] += 1

    # Demos salida a los contadores.
    for char, count in counters.items():
        if count > 0:
            print(char, '->', count)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))