"""se creo una clase en este caso se llamo la clase como persona ya que esta sera la clase padre o super clase ."""

class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
"""se procede a crear los objetos de la clase persona en este caso son nombre y documento, no hay
que olvidar que en este ejemplo faltan los setters y los getters ya que el constructor si esta realizado"""