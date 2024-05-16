frase = input("Ingrese una frase: ").lower()
vocales = []

for letra in frase:
    if letra in 'aeiou' and letra not in vocales:
        vocales.append(letra)

print(f"Vocales en la frase:", vocales)
