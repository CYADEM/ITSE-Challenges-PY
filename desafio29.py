def distancia_mas_corta(texto, x):
    # Encontrar la posición de la primera ocurrencia de x en el texto
    primera_ocurrencia = texto.find(x)
    if primera_ocurrencia == -1:  # Si x no está presente en el texto
        return [len(texto)] * len(texto)

    # Calcular la distancia más corta desde cada caracter hasta la primera ocurrencia de x
    distancias = []
    for i, caracter in enumerate(texto):
        if caracter == x:
            distancias.append(0)
        else:
            distancias.append(abs(i - primera_ocurrencia))
    return distancias

# Ejemplo de uso
texto = "abcdefgahijklmnoa"
x = 'a'
resultado = distancia_mas_corta(texto, x)
print(f"Distancias más cortas desde cada caracter hasta la primer ocurrencia de", x, ":", resultado)
