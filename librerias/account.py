from user import User
class Cuenta(User):
    def __init__ (self, nombre,ID):
        super().__init__(nombre,ID)
        self.__nolibros =0
        self.__noreservados =0
        self.__sinlibrosdevueltos =0
        self.__sinperdidos =0
        self.__multa =0

    def despliegueMenu(self):
        print("------------ Menu de la libreria ------------")
        print("| 1. libros prestados                       |")
        print("---------------------------------------------")
        print("| 2. libros reservados                      |")
        print("---------------------------------------------")
        print("| 3. devolucion de libros                   |")
        print("---------------------------------------------")
        print("| 4. libros perdidos                        |")
        print("---------------------------------------------")
        print("| 5. multa por libros perdidos              |")
        print("---------------------------------------------") 
        print("| 6. salir                                  |")
        print("---------------------------------------------")
    def prestamos(self):
        libro= input(" Ingrese el libro que desea tomar en prestamo:")
        print("El libro que escogio es:",libro)
    def reservados(self):
        libro1= input ("Ingrese el nombre del libro que desea reservar:")
        print("el libro que desea reservar es:",libro1)
    def devolucion(self):
        libro3= input("Escriba el nombre del libro que desea devolver:")
        print("el libro que desea devolver es:",libro3)
    def perdidos(self):
        libro4= input ("Escriba el nombre del libro que perdio:")
        print("El nombre del libro perdido es:",libro4)
    def multa (self):
        libro5= input ("Digite elk valor de la multa a pagar:")
        print ("la multa que debe pagar es de:",libro5)


    def menu(self):
        while True:
            self.despliegueMenu(self)
            codigo = input("Ingrese el codigo: ")
            
            if codigo == "1":
                self.prestamos()
            elif codigo == "2":
                self.reservados()
            elif codigo == "3":
                self.devolucion()
            elif codigo == "4":
                self.perdidos()
            elif codigo == "5":
                self.multa()
            elif codigo == "6":
                print("salir del menu.")
                break
            else:
                print("el codigo ingresado es invalido.")


    
