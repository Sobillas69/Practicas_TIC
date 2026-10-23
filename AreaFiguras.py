#Programa para calcular áreas
#Área cuadrado; lado X lado
lado=float(input("Ingresa lado: "))
areaCuadrado=lado*lado
print("El área es: ", areaCuadrado)
print(f"El área es: {areaCuadrado}")
#Área de un triángulo
base=float(input("Ingresa base: "))
altura=float(input("Ingresa la altura: "))
areaTriangulo=base*altura/2
print(f"El área es: {areaTriangulo}")
#Área de un trapecio
baseMayor=float(input("Ingresa la base mayor: "))
BaseMenor=float(input("Ingresa la base menor: "))
altura=float(input("Ingresa la altura: "))
areaTrapecio=(baseMayor+BaseMenor)*altura/2
print(f"El área es: {areaTrapecio}")
#EXTRA-----------------
#Área de un circulo
radio=float(input("Ingresa el radio: "))
areaCirculo=3.1416*(radio*radio)
print(f"El área es: {areaCirculo}")
#Área de un pentagono
longitudLado=float(input("Ingresa la longitud de un lado: "))
perimetro=5*longitudLado
apotema=float(input("Ingresa el apotema: "))
areaPentagono=(perimetro*apotema)/2
print(f"El área es: {areaPentagono}")