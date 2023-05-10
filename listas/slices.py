"""llenar una lista con numeros aleatoreos (reales con un decimal)que representen calificaciones de un curso. se evalua de 0 a 5
el curso puede tener 2 y 30 aprendices. 
Hallar
1.genere listas nuevas por los aprobados y los reprobados (se aprueba con 3)
2.genere listas nuevas por cada unidad. es decir, los que sacan de 0 a 1 son una listas, los de 1 a 2 otro grupo y asi sucesivamente 
3. diga cuañ es eñ promedio que aprueban y de los que reprueban por separado """
import random

lista=[]
elevado=[]
resta=[]
suma=0
sum=1
promedio=0
max=0
min=100000

tam=int(random.randint (10,20))
print("el tamaño de esta lisa es de:",tam)
for i in range (tam):
    num=int(random.randrage(100))
    lista.append(num)
    suma+=num
    promedio=suma/tam
    if num > max:
        max=num
    if max<min and num!=0:
        min=num
ind=0
for num in lista:
    cont=0
    for f in lista:
        if num == f:
            cont+=1
    if cont > ind:
        ind=cont
        moda=num
for i in range (tam):
    for j in range(i+1,tam):
        if list[i]>list[j]:
            aux=list[i]
            list[i]=list[j]
            list[j]=aux
if len (list)%2==0:
    mediana=(list[(len(list)//2)-1]+list [len(list)//2])/2
else:
    mediana=list[(len(list)//2)]
for i in lista:
    y=((i-promedio))
    resta.append(y)
    for j in resta:
        y=((j**2))
        elevado.append(y)
    for y in elevado:
        sum+=y
    divi=(sum/tam-1)
    ds=divi**0.5


print("Lalista es:",lista)
print("la suma de los datos es:",suma)
print("el promedio de los datos es:",promedio)
print("El numero maximo es:",max)    
print("el numero menor es:",min)
print("La moda es:",moda)
print("la mediana es:",mediana)
print("la desviacion estandar es:",ds)

