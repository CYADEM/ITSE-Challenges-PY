def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Solicitar al usuario que ingrese los años
try:
    inicio = int(input("Ingrese el año de inicio: "))
    fin = int(input("Ingrese el año de fin: "))
    
    print(f"Años bisiestos y múltiplos de 10 en el rango", inicio, "-", fin, ":")
    
    # Iterar sobre los años en el rango
    for year in range(inicio, fin + 1):
        if es_bisiesto(year) and year % 10 == 0:
            print(year)
except ValueError:
    print(f"Por favor, ingrese años válidos.")
