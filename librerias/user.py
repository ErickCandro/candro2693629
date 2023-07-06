class User:
    def __init__(self,nombre,identificacion):
        self.__nombre=nombre
        self.__identificacion=identificacion

    def setNombre(self,nombre):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    def setIdentificacion(self,identificacion):
        self.__identificacion=identificacion
    def getIdentificacion(self):
        return  self.__identificacion

    def verificar(self):
        if self.__nombre =="Erick" and self.__identificacion == 1042851574:
            print ("las credenciales ingresadas son correctas")
        else:
            print ("las credenciales ingresadas no son correctas")
    def creacionCuenta(self):
        if self.__nombre =="Erick" and self.__identificacion == 1042851574:
            print ("la cuenta ya existe")
        else:
            print ("la cuenta aun no existe")
    def infoDelLibro(self):
        while True:
            print("1. informacion del libro\seleccione un libro")
            print("2. the world of cyberpunk 2077")
            print("3. metro 2033")
            print("4. the walking dead book")
            print("5. salir")
          
        
            eleccion= input("digite su eleccion:")  

            if eleccion == "1":
                print("El libro seleccionado es The world of cyberpunk 2077")
                print("el año de creacion fue 2022")
                print("Autor Mateusz Popławsk")
            elif eleccion =="2":
                print("El libro seleccionado es metro 2033")
                print("El año de creacion fue 2010")
                print("Autor del libro Dmitri Glujovski")
            elif eleccion =="3":
                print("")
                print("")
                print("")
            elif eleccion =="4":
                print("")
                print("")
                print("")
            elif eleccion =="5":
                print("Salir de el modo eleccion")
                break
            else:
                print ("la seleccion marcada no corresponde intentelo de nuevo")
                


