try:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero <= 0:
        print(f"Por favor, ingrese un número entero positivo.")
    else:
        for i in range(numero, 2 * numero):
            print(i)
except ValueError:
    print(f"Por favor, ingrese un número entero válido.")
