#Programa que agrega peliculas a una lista
#Ponerle nombre a mi lista
peliculas=[]
#Preguntar cuantas peliculas
cantPeliculas=int(input("Ingresa la cantidad de peliculas que vas a agregar: "))
#Valor inicial para WHILE
i=0
#Mientras i sea menor a la cantidad ejecutar
while i<cantPeliculas:
    #Preguntar peliculas
    peli=input("Ingresa la pelicula: ")
    #Agregar pelicula a la lista
    peliculas.append(peli)
    #Muestra la lista
    print(peliculas)
    i=i+1
#Buscar una pelicula en la lista
#Preguntar la pelicula a buscar
peliBuscar=input("Ingresa la pelicula que estas buscando: ")
if peliBuscar in peliculas:
    print("Si esta")
else:
    print("No esta, pero dejame agregarla")
    peliculas.append(peliBuscar)
    print(peliculas)
#EXTRA...
#Solicitar una pelicula para borrar
#Borrar la pelicula
#Muestra la lista
peliBorrar=input("Ingresa la pelicula que quieres borrar: ")
peliculas.remove(peliBorrar)
print(peliculas)