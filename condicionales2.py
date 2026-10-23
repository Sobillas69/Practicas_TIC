calif=float(input("Ingresa tu calificación: "))
if calif==10:
    print("Excelente!")
elif calif==9:
    print("Muy bien!")
elif calif==8:
    print("Bien!")
elif calif==7:
    print("Puedes mejorar!")
elif calif==6:
    print("Ayy mijo!")
else:
    print("Chancletazo!!!")
    print("--------------------") 
#Solicitar temperatura
temp=int(input("Ingresa la temperatura: "))
if temp>=40:
    print("Hace mucho calor!")
elif temp>=30 and temp<40:
    print("Esta templado!")
elif temp>=20 and temp<30:
    print("Esta fresco!")
elif temp<20:
    print("Hace frio!") 
else:
    print("No valido")
    print("--------------------") 
#Solicitar sexo y edad
sexo=input("Ingresa tu sexo: ")
edad=int(input("Ingresa tu edad: "))
if sexo=="hombre" and edad>=18:
    print("Puedes sacer la cartilla militar")
else:
    print("No puedes sacer la cartilla militar")
