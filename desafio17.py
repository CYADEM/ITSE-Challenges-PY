frase = input("Ingrese una frase: ").lower()
cantidad_vocales = 0

for letra in frase:
    if letra in 'aeiou':
        cantidad_vocales += 1

print(f"La cantidad de vocales en la frase es:", cantidad_vocales)
