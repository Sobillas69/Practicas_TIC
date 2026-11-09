deportes=["Futbol"]
dep=input("Ingresa un deporte: ")
deportes.append(dep)
print(deportes)
dep2=input("Ingresa otro deporte: ")
deportes.append(dep2)
print(deportes)
depBorrar=input("Cuál quieres borrar? ")
deportes.remove(depBorrar)
print(deportes)
dep3=input("Ingresa otro deporte: ")
pos=int(input("En que posición? "))
deportes.insert(pos,dep3)
print(deportes)
#TAREA
#Solcitar cadena o string
palabra=input("Escribe algo")
#Comprobar si una palabra contiene una letra
letra=input("a")
if letra in palabra:
    print("La letra si esta en la palabra")
else:
    print("La letra no esta")
#Comprobar cuantas veces aparece una letra
cantidad=palabra.lower().count(letra)
print(f"La letra aparece{cantidad} veces")
#Reemplazar una letra
PalabraNueva=palabra.replace(letra, "x")
#Contar cantidad de caracteres de una palabra
cantidadLetras=len(palabra)
#Verificar si una palabra tiene mas de 5 letras
if len(palabra)>5:
    print("Tiene mas de 5")
else:
    print("Tiene 5 o menos")
#Comprobar si una palabra termina en S
if palabra.lower().endswith("s"):
    print("Termina con S")
else:
    print("No termina con S")