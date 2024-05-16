def cuadrado_perfecto(numero):
    cuadrados_perfectos = []
    # Iterar sobre los números enteros positivos hasta numero
    for i in range(1, numero + 1):
        cuadrado = i * i
        # Verificar si el cuadrado es perfecto y no es par
        if es_cuadrado_perfecto(cuadrado) and cuadrado % 2 != 0:
            cuadrados_perfectos.append(cuadrado)
    return cuadrados_perfectos

def es_cuadrado_perfecto(numero):
    # Verificar si un número es cuadrado perfecto
    raiz = int(numero ** 0.5)
    return raiz * raiz == numero

# Ejemplo de uso
numero = 20
resultado = cuadrado_perfecto(numero)
print(f"Números cuadrados perfectos que no son pares hasta", numero, ":", resultado)
