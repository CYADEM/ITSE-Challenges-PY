def obtener_nombres_estudiantes():
    nombres = set()
    while True:
        nombre = input("Ingrese el nombre del estudiante ('S' para finalizar): ")
        if nombre == 'S':
            break
        nombres.add(nombre)
    return nombres

# Solicitar los nombres de los estudiantes de primer año
print(f"Ingrese los nombres de los estudiantes de primer año:")
nombres_primer_anio = obtener_nombres_estudiantes()

# Solicitar los nombres de los estudiantes de segundo año
print(f"\nIngrese los nombres de los estudiantes de segundo año:")
nombres_segundo_anio = obtener_nombres_estudiantes()

# Lista de todos los nombres de los estudiantes de primer año y segundo año, sin repeticiones
todos_los_nombres = nombres_primer_anio.union(nombres_segundo_anio)

# Lista de los nombres de los estudiantes que se repiten en ambos años
nombres_repetidos = nombres_primer_anio.intersection(nombres_segundo_anio)

# Lista de los nombres de los estudiantes de primer año que no se repiten en segundo año
nombres_no_repetidos_primer_anio = nombres_primer_anio.difference(nombres_segundo_anio)

# Imprimir los resultados
print(f"\nLista de todos los nombres de los estudiantes:")
print(todos_los_nombres)

print(f"\nLista de los nombres de los estudiantes que se repiten en ambos años:")
print(nombres_repetidos)

print(f"\nLista de los nombres de los estudiantes de primer año que no se repiten en segundo año:")
print(nombres_no_repetidos_primer_anio)
