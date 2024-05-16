def suma_digitos(numero):
    suma = 0
    while numero != 0:
        suma += numero % 10  # Obtener el último dígito y sumarlo a la suma total
        numero //= 10  # Eliminar el último dígito dividiendo el número por 10
    return suma

# Ejemplo de uso220
numero = int(input("Ingresa un número entero: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de", numero, "es:", resultado)
