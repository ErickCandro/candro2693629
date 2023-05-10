ma = 0
nu = 1

while nu > 0:
    nu = int(input("Introduce un numero:"))


    if nu > ma:
        ma = nu

print("El numero maximo introducido es:", nu)
