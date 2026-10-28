parentesco=input("Que eres mio? ")
if parentesco=="hermano" or parentesco=="hijo":
    print("Eres de mi familia")
else:
    print("No eres de mi familia")
print("--------------------")
edad=int(input("Ingresa tu edad: "))
permiso=input("Tienes permiso de tus padres? ")
if edad>=18 or permiso=="si":
    print("Puedes entrar el concierto")
else: 
    print("No puedes entrar al concierto")
acompañado=input("Vienes acompañado? ")
if edad>=18 or acompañado=="si":
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")