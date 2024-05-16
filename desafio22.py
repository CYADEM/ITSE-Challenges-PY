sumatoria_negativos = 0
contador_positivos = 0
sumatoria_positivos = 0

for _ in range(6):
    numero = int(input("Ingrese un número entero: "))
    if numero < 0:
        sumatoria_negativos += numero
    elif numero > 0:
        contador_positivos += 1
        sumatoria_positivos += numero

if contador_positivos > 0:
    promedio_positivos = sumatoria_positivos / contador_positivos
else:
    promedio_positivos = 0

print(f"La sumatoria de los números negativos es:", sumatoria_negativos)
print(f"El promedio de los números positivos es:", promedio_positivos)
