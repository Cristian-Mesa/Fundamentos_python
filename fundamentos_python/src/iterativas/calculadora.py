
# 1. Entrada de datos básicos
nombre = input("Ingrese su nombre: ")
proyectos = int(input("Ingrese la cantidad de proyectos asignados: "))

# Variables para acumular resultados y guardar el historial
horas_totales = 0
listar_horas = []

# 2. Ciclo para iterar y solicitar las horas por cada proyecto
for i in range(proyectos):
    print(f"\nProyecto {i+1}:")
    horas = int(input("Ingrese las horas trabajadas en este proyecto: "))
    
    # Acumulamos las horas al total general
    horas_totales += horas
    
    # Guardamos las horas específicas de este proyecto en nuestra lista
    listar_horas.append(horas)

# 3. Cálculos generales
promedio_horas = horas_totales / proyectos

# 4. Generación del reporte tabulado y ordenado (Uso avanzado de f-strings)
print("\n" + "="*50)
print(f"REPORTE DE MÉTRICAS: {nombre.upper()}")
print("="*50)

# Encabezado de la tabla: <12 significa alinear a la izquierda ocupando 12 espacios
print(f"{'Proyecto':<12} | {'Horas':<10} | {'Porcentaje':<15}")
print("-" * 50)

# Ciclo para calcular e imprimir los porcentajes en formato de tabla
for i in range(proyectos):
    # Extraemos las horas del proyecto actual desde la lista
    horas_proyecto = listar_horas[i]
    
    # Calculamos la regla de tres para el porcentaje
    porcentaje = (horas_proyecto / horas_totales) * 100

    # Imprimimos la fila tabulada asegurando 2 decimales para el porcentaje (.2f)
    print(f"Proyecto {i+1:<3} | {horas_proyecto:<10} | {porcentaje:.2f}%")

# Cierre de la tabla con los totales
print("-" * 50)
print(f"Total de horas trabajadas:      {horas_totales}")
print(f"Promedio de horas por proyecto: {promedio_horas:.2f}")
print("="*50)