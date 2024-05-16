nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")

if nombre1[0].lower() == nombre2[0].lower() or nombre1[-1].lower() == nombre2[-1].lower():
    print(f"Coincidencia")
else:
    print(f"No hay coincidencia")