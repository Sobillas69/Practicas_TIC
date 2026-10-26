nombre=input("Ingrese su nombre: ")
pagoxhora=float(input("Ingrese su pago por hora: "))
horasxmes=int(input("Ingrese las horas trabajadas por mes: "))
sueldo= pagoxhora*horasxmes
print(f"Su sueldo es: {sueldo}")
if sueldo>=100 and sueldo<=300:
    print(f"Su sueldo con bono es: {sueldo+500}")
elif sueldo>300 and sueldo<=1500:
    print(f"Su sueldo con bono es: {sueldo+1700}")
elif sueldo>1500 and sueldo<=3000:
    print(f"Su sueldo con bono es: {sueldo+3500}")
elif sueldo>3000 and sueldo<=8000:
    print(f"Su sueldo con bono es: {sueldo+8500}")
elif sueldo>8000:
    print(f"Su sueldo con bono es: {sueldo+10000}")
else: 
    print("No valido")