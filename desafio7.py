print("Candidatos:")
print("A - Candidato por el partido rojo")
print("B - Candidato por el partido verde")
print("C - Candidato por el partido azul")

opcion = input("Ingrese la opción de su candidato (A, B, C): ").upper()

if opcion == 'A':
    print(f"Usted ha votado por el partido rojo.")
elif opcion == 'B':
    print(f"Usted ha votado por el partido verde.")
elif opcion == 'C':
    print(f"Usted ha votado por el partido azul.")
else:
    print(f"Opción errónea.")
