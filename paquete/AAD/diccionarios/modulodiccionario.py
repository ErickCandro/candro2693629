#diccionario de español a ingles
def FunDicciEsp_Ing(diccionario):
    diccionario = {}
    while True:
        clave = input("Digite la clave que desea agregar: ")
        if clave == "terminar":
            break
        valor = input("Digite el valor que desea agregar: ")
        diccionario[clave] = valor
        print("para finalizar el programa digite la palabra terminar")
    return print(diccionario)
diccionarioesp_ing = {}
FunDicciEsp_Ing(diccionarioesp_ing)


#diccionario de ingles a español
def FunDicciIng_Esp(diccionario):
    diccionario = {}
    while True:
        clave = input("Digite la clave que desea agregar: ")
        if clave == "terminar":
            break
        valor = input("Digite el valor que desea agregar: ")
        diccionario[clave] = valor
        print("para finalizar el programa digite la palabra terminar")
    return print(diccionario)
diccionarioing_esp = {}
FunDicciIng_Esp(diccionarioing_esp)