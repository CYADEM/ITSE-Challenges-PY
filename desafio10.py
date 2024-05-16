def obtener_dia_semana_fecha(fecha):
    dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
    partes = fecha.split(', ')
    if len(partes) != 2:
        return None
    dia_semana = partes[0].lower()
    if dia_semana not in dias_semana:
        return None
    return dia_semana

def obtener_nivel_clases(dia_semana):
    niveles_clases = {
        'lunes': 'inicial',
        'martes': 'intermedio',
        'miércoles': 'avanzado',
        'jueves': 'práctica hablada',
        'viernes': 'inglés para viajeros'
    }
    return niveles_clases.get(dia_semana)

def obtener_numero_alumnos():
    while True:
        try:
            num_alumnos = int(input("Ingrese el número de alumnos: "))
            if num_alumnos <= 0:
                print(f"El número de alumnos debe ser mayor que cero.")
            else:
                return num_alumnos
        except ValueError:
            print(f"Por favor, ingrese un número válido.")

def obtener_arancel():
    while True:
        try:
            arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
            if arancel <= 0:
                print(f"El arancel debe ser mayor que cero.")
            else:
                return arancel
        except ValueError:
            print(f"Por favor, ingrese un número válido.")

def calcular_ingreso_total(num_alumnos, arancel):
    return num_alumnos * arancel

def main():
    fecha = input("Ingrese la fecha actual en formato 'día, DD/MM': ")
    dia_semana = obtener_dia_semana_fecha(fecha)
    if dia_semana is None:
        print(f"Se produjo un error, revise el formato ingresado.")
        return
    
    nivel_clases = obtener_nivel_clases(dia_semana)
    print(f"Hoy se dictan clases de", nivel_clases)
    1
    if nivel_clases in ['inicial', 'intermedio', 'avanzado']:
        tomaron_examenes = input("¿Hubo exámenes? (sí/no): ").lower() == 'sí'
        if tomaron_examenes:
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            total_alumnos = obtener_numero_alumnos()
            porcentaje_aprobados = (aprobados / total_alumnos) * 100
            print(f"Porcentaje de aprobados:", porcentaje_aprobados, "%")
    
    elif nivel_clases == 'práctica hablada':
        porcentaje_asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
        if porcentaje_asistencia > 50:
            print(f"Asistió la mayoría")
        else:
            print(f"No asistió la mayoría")
    
    elif nivel_clases == 'inglés para viajeros':
        if fecha.endswith('1/1') or fecha.endswith('1/7'):
            print(f"Comienzo de nuevo ciclo")
            num_alumnos = obtener_numero_alumnos()
            arancel = obtener_arancel()
            ingreso_total = calcular_ingreso_total(num_alumnos, arancel)
            print(f"Ingreso total en $:", ingreso_total)

if __name__ == "__main__":
    main()
