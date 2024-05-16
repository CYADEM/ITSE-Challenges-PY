def cifra_cesar(mensaje, corrimiento):
    mensaje_encriptado = ""
    for caracter in mensaje:
        if caracter.isalpha():  # Verificar si el caracter es una letra
            # Obtener el índice del caracter en el alfabeto
            indice = ord(caracter.lower()) - ord('a')
            # Calcular el nuevo índice después del corrimiento
            nuevo_indice = (indice + corrimiento) % 26
            # Obtener el nuevo caracter encriptado
            nuevo_caracter = chr(ord('a') + nuevo_indice)
            # Mantener mayúsculas si el caracter original es mayúscula
            if caracter.isupper():
                nuevo_caracter = nuevo_caracter.upper()
            mensaje_encriptado += nuevo_caracter
        else:
            # Mantener los caracteres que no son letras sin cambios
            mensaje_encriptado += caracter
    return mensaje_encriptado

# Ejemplo de uso
mensaje_original = str(input("Ingresar mensaje a cifrar: "))
corrimiento = int(input("Ingresar cantidad de corrimientos: "))
mensaje_encriptado = cifra_cesar(mensaje_original, corrimiento)
print(f"Mensaje encriptado:", mensaje_encriptado)
