numero1 = int(input("Introduce un numero"))
numero2 = int(input("Introduce un segundo numero"))

if numero1 < numero2:
    numero1, numero2 = numero2, numero1
c = 0
r = numero1

while r >= numero2:
    r -= numero2
    c += 1

print("el cociente es:", c)
print("el residuo es:", r)

