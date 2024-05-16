def intercambiar_variables(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Ejemplo de uso
x = 5
y = 10
print(f"Valores originales: x =", x, ", y =", y)
x, y = intercambiar_variables(x, y)
print(f"Valores intercambiados: x =", x, ", y =", y)
