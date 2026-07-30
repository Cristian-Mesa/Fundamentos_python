

def analizar_frecuencia_texto():
    # 1. Solicitar el texto al usuario
    texto = input("Ingresa una frase o un párrafo largo: ")
    
    # 2. Limpieza básica del texto
    # Convertimos todo a minúsculas
    texto_limpio = texto.lower()
    
    # Reemplazamos los signos de puntuación básicos por espacios o los borramos
    for signo in [",", ".", ";", "!", "?", "¿", "¡"]:
        texto_limpio = texto_limpio.replace(signo, "")
        
    # 3. Separar el texto en una lista de palabras usando .split()
    palabras = texto_limpio.split()
    
    # 4. Crear un diccionario de frecuencias
    frecuencias = {}
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, sumamos 1; si no, empieza en 0 + 1
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    # 5. Encontrar la palabra con mayor frecuencia
    palabra_mas_frecuente = ""
    max_conteo = 0
    
    for palabra, conteo in frecuencias.items():
        if conteo > max_conteo:
            max_conteo = conteo
            palabra_mas_frecuente = palabra
            
    # 6. Mostrar los resultados en consola
    print("\n" + "="*40)
    print("RESULTADOS DEL ANÁLISIS DE TEXTO")
    print("="*40)
    print(f"Diccionario de frecuencias: {frecuencias}")
    print(f"La palabra más frecuente es '{palabra_mas_frecuente}' con {max_conteo} apariciones.")
    print("="*40)

# Bloque para ejecutar la función
if __name__ == "__main__":
    analizar_frecuencia_texto()