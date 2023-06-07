class Empresa:
    salario=1160000
    def __init__(self,nombre,cargo,salario,):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario

    def setNombre(self,nombre):
        self.__nombre=nombre 
    def getNombre(self):
        return self.__nombre
    
    def setCargo(self,cargo):
        self.__cargo=cargo 
    def getCargo(self):
        return self.__cargo
    
    def setSalario(self,salario):
        self.__salario=salario 
    def getSalario(self):
        return self.__salario
    
    def salarioHora(self):
        horas=float(input("ingrese el monto de horas trabajadas:"))
        t=self.salario/(30*horas)
        return t
salario=float(input("ingrese el monto de horas trabajadas:"))
empresa=Empresa (salario)

salarioHora=empresa.salarioHora()
print ("el empleado gana ",salarioHora,"por hora ")


