def factorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

try:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        print(f"El número ingresado no es positivo.")
    else:
        print(f"El factorial de", numero, "es:", factorial(numero))
except ValueError:
    print(f"Por favor, ingrese un número entero válido.")
