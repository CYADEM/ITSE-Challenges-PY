def mediana(lista):
    if len(lista) == 0:
        raise ValueError("La lista está vacía")

    # Ordenar la lista
    lista_ordenada = sorted(lista)

    # Calcular la mediana
    n = len(lista_ordenada)
    if n % 2 == 1:
        # Longitud impar: devolver el valor mediano
        return lista_ordenada[n // 2]
    else:
        # Longitud par: devolver el promedio de los dos valores medianos
        mediana_izquierda = lista_ordenada[n // 2 - 1]
        mediana_derecha = lista_ordenada[n // 2]
        return (mediana_izquierda + mediana_derecha) / 2

# Ejemplo de uso
try:
    lista = [5, 2, 9, 1, 7]
    resultado = mediana(lista)
    print(f"La mediana de la lista", lista, "es:", resultado)
except ValueError as error:
    print(f"Error:", error)
