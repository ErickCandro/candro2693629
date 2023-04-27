i=1
sp=0
si=0
while i<=10:
    print(i)
    
    if i%2==0:
        sp=sp+i
else:
    si=si+i
i=i+1 #i+=1
print("la suma de los pares es",sp)
print("la suma de los impares es",si)