nombre="Arath"
frase="El cielo es hermoso"
print(nombre)
print(frase)
#Mostrar en mayusculas
print(nombre.upper())
print(frase.upper())
#Mostrar en minusculas
print(frase.lower())
#Obtener un caracter en una posición
letra=frase[4]
print(letra)
#Separar frase
frase2="El-mundo-es-bonito"
print(frase2.split("-"))
nombreC="Arath Sebastian garcía Nieves"
print(nombreC.split(" "))
#Dos primeras letras del nombre
letras1=nombreC[0:2]
print(letras1)
#Reemplazar
nuevaFrase=frase.replace("hermoso", "maravilloso")
print(nuevaFrase)
#Numero de caracteres de la cadena: largo
largoCadena=len(nuevaFrase)
print(largoCadena)