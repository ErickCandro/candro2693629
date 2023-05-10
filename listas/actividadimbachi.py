def nummat(x):
    s=0
    n=1
    while s<maximo:
        s=s+n
        n=n+1
        return n-1
maximo = int(input("introduce un numero maximo"))
lista=nummat(-1)

print("El numero natural mas pequeño necesario para superar el maximo es:",lista)              