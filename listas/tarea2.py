num_digitos = int(input("Ingrese la cantidad de dígitos que desea en la serie de Fibonacci: "))
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
while len(str(fibonacci[-1])) < num_digitos:
    siguiente_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_num)

print(fibonacci)