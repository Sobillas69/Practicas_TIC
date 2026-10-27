sexo=input("Ingresa tu sexo: ")
edad=int(input("Ingresa tu edad: "))
estadocivil=input("Ingresa tu estado civil: ")
hijos=int(input("Ingresa tu numero de hijos: "))
if sexo=="mujer" and hijos==1 and edad<18:
    print("Eres mujer, tienes un hijo y eres menor de edad, entonces el apoyo es de: $800")
elif sexo=="mujer" and hijos==1 and edad>=18:
    print("Eres mujer, tienes un hijo y eres meyor de edad, entonces el apoyo es de: $300")
elif sexo=="mujer" and hijos>1 and edad<18:
    print("Eres mujer, tienes mas de un hijo y eres menor de edad, entonces el apoyo es de: $1,500 ")
elif sexo=="mujer" and hijos>1 and edad>=18:
    print("Eres mujer, tienes mas de un hijo y eres mayor de edad, entonces el apoyo es de: $500")
elif sexo=="hombre" and hijos>=1 and estadocivil=="soltero":
    print("Eres hombre y tienes hijos, entonces el apoyo es de: $780")
else: 
    print("No valido")