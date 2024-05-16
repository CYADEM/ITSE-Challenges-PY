import math

def calcular_volumen_rectangular():
    largo = float(input("Ingrese el largo del contenedor en metros: "))
    ancho = float(input("Ingrese el ancho del contenedor en metros: "))
    alto = float(input("Ingrese la altura del contenedor en metros: "))
    volumen = largo * ancho * alto
    print(f"El volumen del contenedor rectangular es:", volumen, "metros cúbicos")

def calcular_volumen_redondo():
    radio = float(input("Ingrese el radio de la base del contenedor en metros: "))
    altura = float(input("Ingrese la altura del contenedor en metros: "))
    volumen = math.pi * radio ** 2 * altura
    print(f"El volumen del contenedor redondo es:", volumen, "metros cúbicos")

def calcular_volumen_cilindrico():
    radio = float(input("Ingrese el radio del contenedor en metros: "))
    altura = float(input("Ingrese la altura del contenedor en metros: "))
    volumen = math.pi * radio ** 2 * altura
    print(f"El volumen del contenedor cilíndrico es:", volumen, "metros cúbicos")

# Función principal
def main():
    while True:
        # Mostrar el menú de opciones
        print(f"Menú de Opciones")
        print(f"-----------------------------------------------------------")
        print(f"1 - Calcular volumen contenedor rectangular")
        print(f"2 - Calcular volumen contenedor redondo")
        print(f"3 - Calcular volumen contenedor cilíndrico")
        print(f"s - Salir")

        # Solicitar al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")

        # Realizar acciones según la opción seleccionada
        if opcion == '1':
            calcular_volumen_rectangular()
        elif opcion == '2':
            calcular_volumen_redondo()
        elif opcion == '3':
            calcular_volumen_cilindrico()
        elif opcion == 's':
            print(f"¡Hasta luego!")
            break
        else:
            print(f"Opción inválida. Por favor, seleccione una opción válida.")

# Llamar a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
