letra = input("Ingrese una letra: ")

if len(letra) != 1:
    print(f"No se puede procesar el dato. Por favor ingrese solo una letra.")
else:
    letra = letra.lower()
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print(f"Es vocal")
    else:
        print(f"No es vocal")
