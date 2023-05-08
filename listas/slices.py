"""llenar una lista con numeros aleatoreos (reales con un decimal)que representen calificaciones de un curso. se evalua de 0 a 5
el curso puede tener 2 y 30 aprendices. 
Hallar
1.genere listas nuevas por los aprobados y los reprobados (se aprueba con 3)
2.genere listas nuevas por cada unidad. es decir, los que sacan de 0 a 1 son una listas, los de 1 a 2 otro grupo y asi sucesivamente 
3. diga cuañ es eñ promedio que aprueban y de los que reprueban por separado """


import random
poscicion=[]
tam=random.randint (20,30)
list=[float(random.randrange(0,5))for i in range(tam)]
for i in range (tam):
    for j in range(i+1,tam):
        if list[i]>list[j]:
            aux=list[i]
            list[i]=list[j]
            list[j]=aux
for j in list:
    if j==3.0:
        poscicion=(list.index(j))
    if j==2.0:
        unidad1=(list.index(j))  
        
print("la unidad",unidad1)
print("el numero esta en la poscicion :",poscicion)
aprobados=list[poscicion:]
reprobados=list[:poscicion-1]
print("aprobados:",aprobados)
print("reprobados:",reprobados)

print(tam)
print(list)

