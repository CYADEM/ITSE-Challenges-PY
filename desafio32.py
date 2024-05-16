def potencia(base, exponente):
    # Caso base: si el exponente es 0, la potencia es 1
    if exponente == 0:
        return 1
    
    # Inicializar el resultado de la potencia
    resultado = 1

    # Si el exponente es negativo, invertimos la base y el exponente
    if exponente < 0:
        base = 1 / base
        exponente = -exponente

    # Algoritmo de exponenciación rápida
    while exponente > 0:
        # Si el exponente es impar, multiplicamos el resultado por la base
        if exponente % 2 == 1:
            resultado *= base
        # Elevamos la base al cuadrado y dividimos el exponente por 2
        base *= base
        exponente //= 2

    return resultado

# Ejemplo de uso
base = 2
exponente = 5
resultado = potencia(base, exponente)
print(f"El resultado de", base, "elevado a la", exponente, "es:", resultado)
