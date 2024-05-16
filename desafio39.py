def contar_vocales(texto):
    # Inicializar contadores para cada vocal
    contador_a = contador_e = contador_i = contador_o = contador_u = 0

    # Convertir el texto a minúsculas para simplificar el conteo
    texto = texto.lower()

    # Iterar sobre cada carácter en el texto
    for caracter in texto:
        if caracter == 'a' or caracter == 'á':
            contador_a += 1
        elif caracter == 'e' or caracter == 'é':
            contador_e += 1
        elif caracter == 'i' or caracter == 'í':
            contador_i += 1
        elif caracter == 'o' or caracter == 'ó':
            contador_o += 1
        elif caracter == 'u' or caracter == 'ú':
            contador_u += 1

    # Calcular la cantidad total de vocales
    total_vocales = contador_a + contador_e + contador_i + contador_o + contador_u

    # Imprimir la cantidad de ocurrencias de cada vocal y el total de vocales
    print(f"Cantidad de ocurrencias de la vocal a:", contador_a)
    print(f"Cantidad de ocurrencias de la vocal e:", contador_e)
    print(f"Cantidad de ocurrencias de la vocal i:", contador_i)
    print(f"Cantidad de ocurrencias de la vocal o:", contador_o)
    print(f"Cantidad de ocurrencias de la vocal u:", contador_u)
    print(f"Cantidad total de vocales:", total_vocales)

# Solicitar al usuario que ingrese un texto largo
texto = input("Ingrese un texto largo: ")

# Llamar a la función contar_vocales para contar la cantidad de ocurrencias de cada vocal
contar_vocales(texto)
