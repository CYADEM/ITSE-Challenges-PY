def suma_sin_sumar(a, b):
    while b != 0:
        suma_sin_carry = a ^ b
        carry = (a & b) << 1
        a = suma_sin_carry
        b = carry
    return a

# Ejemplo de uso
numero1 = 5
numero2 = 7
resultado = suma_sin_sumar(numero1, numero2)
print(f"La suma de", numero1, "+", numero2, "es igual a:", resultado)
