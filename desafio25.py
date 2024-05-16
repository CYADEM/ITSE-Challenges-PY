def encontrar_numero_no_repetido(nums):
    resultado = 0
    for num in nums:
        resultado ^= num
    return resultado

# Ejemplo de uso
lista_numeros = [4, 3, 2, 1, 2, 3, 1]
numero_no_repetido = encontrar_numero_no_repetido(lista_numeros)
print(f"El número que no se repite es:", numero_no_repetido)
