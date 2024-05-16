def puede_armar_entrega(cantidad_pedida):
    # Lista de cantidades de bombones en cajas
    cajas = [5, 8, 13]

    # Realizar una búsqueda exhaustiva para ver si es posible armar la entrega
    for caja in cajas:
        if cantidad_pedida % caja == 0:
            # Si la cantidad pedida es divisible por alguna de las cantidades de cajas,
            # entonces es posible armar la entrega
            return True
        else:
            # Si no, intentar con las otras cantidades de cajas
            continue
    
    # Si no se puede armar la entrega con ninguna cantidad de cajas, retornar False
    return False

# Ejemplo de uso
cantidad_pedida = 10
if puede_armar_entrega(cantidad_pedida):
    print(f"Es posible armar una entrega con", cantidad_pedida, "bombones.")
else:
    print(f"No es posible armar una entrega con", cantidad_pedida, "bombones.")
