
# Lista predefinida de stock de equipos
equipos = [12, 0, 5, 23, 2, 0, 8]

# Listas independientes para almacenar índices y valores según requerimiento
productos_agotados = []  # Guardará los índices de los elementos con stock 0
productos_criticos = []  # Guardará los valores de stock entre 1 y 5

# Recorremos la lista usando los índices con range(len())
for i in range(len(equipos)):
    stock_actual = equipos[i]
    
    # Evaluamos el nivel de stock según la escala
    if stock_actual == 0:
        print(f"Equipo {i}: Agotado - Reorden Inmediata")
        # Guardamos el ÍNDICE (i) tal como lo pide la guía
        productos_agotados.append(i)
        
    elif 1 <= stock_actual <= 5: # Forma elegante y limpia de evaluar rangos en Python
        print(f"Equipo {i}: Crítico - Reposición Sugerida")
        # Guardamos el VALOR real del stock
        productos_criticos.append(stock_actual)
        
    else:
        print(f"Equipo {i}: Adecuado")

# Cálculo del porcentaje general de disponibilidad (productos con stock mayor a 0)
total_productos = len(equipos)
# Contamos cuántos productos NO están agotados
productos_disponibles = total_productos - len(productos_agotados)
porcentaje_disponibilidad = (productos_disponibles / total_productos) * 100

# Reporte final en consola
print("\n" + "="*40)
print("REPORTE DE INVENTARIO")
print("="*40)
print(f"Índices de productos agotados (0 stock): {productos_agotados}")
print(f"Valores de stock críticos (1 a 5):        {productos_criticos}")
print(f"Porcentaje general de disponibilidad:     {porcentaje_disponibilidad:.2f}%")
print("="*40)