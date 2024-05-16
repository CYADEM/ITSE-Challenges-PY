def repetir_nombre(nombre, veces):
    # Imprimir el nombre repetido 'veces' veces en la misma línea
    for _ in range(veces):
        print(nombre, end=' ')

# Solicitar al usuario que ingrese un nombre
nombre = input("Ingrese un nombre: ")

# Llamar a la función repetir_nombre para imprimir el nombre 30 veces en la misma línea
repetir_nombre(nombre, 30)
