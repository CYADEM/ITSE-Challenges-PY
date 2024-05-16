try:
    cantidad = int(input("Ingrese la cantidad de números a sumar: "))
    suma = 0
    for i in range(cantidad):
        numero = float(input("Ingrese el número {}: ".format(i + 1)))
        suma += numero
    
    print(f"La suma de los números ingresados es:", suma)
except ValueError:
    print(f"Por favor, ingrese un número válido.")