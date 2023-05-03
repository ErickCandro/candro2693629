m = int (input("introduce un primer numero:"))
n = int (input("introduce un segundo numero:"))

while n !=0:
    r = m % n 
    m = n 
    n = r 

print ("El maximo como un divisor es el numero:", m)