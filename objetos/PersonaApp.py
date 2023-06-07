from persona import *
ob1=Persona("d  ",542187)
print (type(ob1))
print (ob1.getNombre())
ob1.setNombre("jose")
print (ob1.getNombre()) 
c=1

while c!=0:
    cso=input("ingrese un curso")
    if cso == "0":
        break
    ob1.ingresarCurso(cso)
    
ob1.consultarCurso()