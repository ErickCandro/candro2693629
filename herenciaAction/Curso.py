"""en esta archivo se procede a crear una clase con el nombre Curso y se procede a llenar con sus respectivos atributos """


class Curso:                                             #se definen los objetos que llevara la clase en su interior 
    def __init__(self,nombre,tipo):                      #se crea el constructor con sus respectivos objetos en este caso nombre y tipo
        self.__nombre=nombre                             #se define el objeto nombre 
        self.__tipo=tipo                                 #se define el objeto tipo

    def getNombre(self):                                 #se realiza el getter de el objeto nombre 
        return self.__nombre