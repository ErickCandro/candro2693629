import user

class Book():
    def __init__(self, nombre, ID, titulo, autor, ISBN, año):
        super().__init__(nombre, ID)
        self.__titulo = titulo
        self.__autor = autor
        self.__ISBN = ISBN
        self.__año = año

    def setTitulo(self,titulo):
        self.__titulo=titulo
    def getTitulo(self):
        return self.__titulo
    def setAutor(self,autor):
        self.__autor=autor 
    def getAutor(self):
        return self.__autor
    def setIsbn(self,ISBN):
        self.__ISBN=ISBN
    def getIsbn(self):
        return self.__ISBN
    def setAño(self,año):
        self.__año=año
    def getAño(self):
        return self.__año
    
    def estadoLibro(self, opcion):
        if self.__titulo == opcion:
            print("El libro esta disponible ")
        else:
            print("El libro no esta disponible ")

    def vencimiento(self):
        print ("vence el : 6 de junio de 2023")

    def informacion(self, opcion):
        if self.__titulo == opcion:
            print("Informacion sobre la renovacion")
        else:
            print("Este libro no se puede renovar mas")

    def estado(self, opcion):
        if self.__titulo == opcion:
            print("Estado del libro: Activo")
        else:
            print("Estado del libro: Inactivo")

    def detalles(self):
        while True:
            print("1. Mostrar fecha de vencimiento")
            print("2. Comprobar el estado de la reserva")
            print("3. Comprobar el estado de la solicitud")
            print("4. Obtener información de renovación")
            print("5. Salir")

            c = input("Ingrese el codigo: ")

            if c == "1":
                self.vencimiento()
            elif c == "2":
                opcion = input("ingrese el nombre del libro: ")
                self.estadoLibro(opcion)
            elif c == "3":
                opcion = input("ingrese el nombre del libro: ")
                self.informacion(opcion)
            elif c == "4":
                opcion = input("ingrese el nombre del libro ")
                self.estado(opcion)
            elif c == "5":
                print("salir del menu")
                break
            else:
                print("Codigo incorrecto por favor intentelo nuevamente.")