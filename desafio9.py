def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

try:
    year = int(input("Ingrese un año: "))
    
    if es_bisiesto(year):
        print(year, "es un año bisiesto.")
    else:
        print(year, "no es un año bisiesto.")
except ValueError:
    print(f"Por favor ingrese un año válido.")
