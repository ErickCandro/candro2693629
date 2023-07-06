from user import User
class clase(User):
    def __init__(self, nombre, id, nombreclase):
        super().__init__(nombre, id)
        self.__nombreclase = nombreclase
        self.__clases = []

    def adicionarClase(self, claseObj):
        self.__clases.append(claseObj)

    def setClass(self):
        claseNombre = input("Ingrese el nombre de la clase: ")
        objClase = clase(claseNombre)
        self.__clases.append(objClase)
