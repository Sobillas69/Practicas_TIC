numeros=[]
i=0
while i<10:
    num=int(input("Ingresa un numero: "))
    numeros.append(num)
    i=i+1
print("Números pares:")
for num in numeros:
    if num %2==0:
        print(num)
#EXTRA
numPares=[]
for num in numeros:
    if num %2==0:
       numPares.append(num)
print(numPares)
