# Fundamentos de Python

Este repositorio tiene los ejercicios de la guía de Fundamentos de Python, con los temas de variables, operadores, manejo de cadenas, estructuras condicionales, estructuras iterativas y funciones.



## Estructura del proyecto

fundamentos_python/
└── src/
├── Seccion1/    -> ejercicios con la funcion print
├── seccion2/    -> literales de Python
├── seccion3/    -> operadores matematicos
├── seccion4/    -> variables y expresiones
├── condicionales/ -> Sistema de calificación e inventario
├── iterativas/    -> Calculadora de métricas del desarrollador
└── funciones/     -> Motor de análisis de frecuencia de texto

## Como ejecutar los scripts

Cada archivo se ejecuta por separado con Python 3, por ejemplo
```
python src/Seccion1/lab1.py
python src/iterativas/calculadora.py
python src/condicionales/inventario.py
python src/funciones/analisis_texto.py
```

## Seccion 1 - Hola mundo

Se trabaja con la funcion print y sus argumentos sep y end, que sirven para cambiar el separador entre los valores y lo que se imprime al final en vez del salto de linea normal.

## Seccion 2 - Literales de Python

Se practica con cadenas de texto, usando comillas dentro del texto con la barra invertida y el salto de linea con \n.

## Seccion 3 - Operadores matematicos

Aqui se resuelven los ejercicios de operadores aritmeticos:

- Potencia: se usa el operador **, por ejemplo 2 ** 3 da 8.
- Division: se usa el operador /, y siempre devuelve un numero decimal, por ejemplo 6 / 3 da 2.0.
- Division con numeros negativos: el signo del resultado depende del signo de los numeros que se dividen, por ejemplo -6 / 3 da -2.0.

La logica es sencilla, se prueban los mismos numeros pero unas veces como enteros y otras como decimales, para ver que el resultado siempre termina siendo decimal cuando se usa la division normal.

## Seccion 4 - Variables

Se declaran variables para guardar datos, se hacen sumas simples y tambien conversiones de unidades, como pasar de millas a kilometros. Por ultimo se resuelve una expresion matematica usando variables de tipo decimal.

## Estructuras de Control y Funciones (Retos de la Práctica Actual)

### 1. Iterativas - Calculadora de Métricas del Desarrollador
Script que solicita las horas de proyectos mediante un ciclo, calcula el total, el promedio y muestra un reporte tabulado y ordenado usando f-strings.

### 2. Condicionales - Sistema de Calificación e Inventario
Monitorea el stock predefinido de un almacén informático (`[12, 0, 5, 23, 2, 0, 8]`). Evalúa cada valor con condicionales para clasificarlos en agotados (guardando sus índices), críticos o adecuados, calculando la disponibilidad general.

### 3. Funciones - Motor de Análisis de Frecuencia de Texto
Encapsula la lógica en una función para procesar una frase o párrafo ingresado por el usuario. Limpia signos de puntuación, pasa el texto a minúsculas, usa diccionarios para contar la frecuencia de cada palabra y halla la más repetida.

## Requisitos

- Python 3.x
- Editor de codigo como VS Code
- Git o GitLab para versionar el proyecto

## Autor

Cristian, aprendiz SENA, programa ADSO.