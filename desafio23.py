def cifrado_cesar(mensaje, corrimiento):
    mensaje_encriptado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            indice = ord(caracter.lower()) - ord('a')
            nuevo_indice = (indice + corrimiento) % 26
            nuevo_caracter = chr(ord('a') + nuevo_indice)
            if caracter.isupper():
                nuevo_caracter = nuevo_caracter.upper()
            mensaje_encriptado += nuevo_caracter
        else:
            mensaje_encriptado += caracter
    return mensaje_encriptado

# Solicitar al usuario el corrimiento
corrimiento = int(input("Ingrese el corrimiento para el cifrado César: "))

# Mensajes del jefe a los oficiales
mensajes_oficiales = [
    "¡Preparen sus armas y manténganse alerta!",
    "Revisen el flanco derecho del campo de batalla.",
    "Avancen hacia el objetivo con cautela.",
    "Reporten cualquier movimiento del enemigo.",
    "Mantengan la formación y sigan mi liderazgo."
]

# Encriptar los mensajes del jefe a los oficiales
for i, mensaje in enumerate(mensajes_oficiales, start=1):
    mensaje_encriptado = cifrado_cesar(mensaje, corrimiento)
    print(f"Mensaje al oficial {i}:", mensaje_encriptado)
