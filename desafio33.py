def sumar_uno(lista):
    # Crear una nueva lista para almacenar los números sumados más uno
    lista_sumada = []
    
    # Iterar sobre los números en la lista de entrada
    for numero in lista:
        # Sumar uno al número y agregarlo a la nueva lista
        lista_sumada.append(numero + 1)
    
    return lista_sumada

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
numeros_sumados = sumar_uno(numeros)
print(f"Lista original:", numeros)
print(f"Lista con los números sumados más uno:", numeros_sumados)
