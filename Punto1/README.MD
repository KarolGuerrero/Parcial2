# Calculadora de Fracciones

Este proyecto es una calculadora de fracciones que permite realizar operaciones aritméticas básicas con fracciones. El programa está implementado en Python utilizando ANTLR para el análisis léxico y sintáctico.

**Operaciones soportadas:** El programa permite las siguientes operaciones, incluyendo las fracciones negativas.
- Suma: a/b + c/d
- Resta: a/b - c/d
- Multiplicación: a/b * c/d
- División: a/b / c/d


## Requisitos

- Python3
- ANTLR4

## Archivos del Proyecto

- `Racionales.g4`: Archivo de gramática ANTLR que define la sintaxis de las operaciones con fracciones.
- `Visitor.py`: Implementación del Visitor que evalúa las operaciones aritméticas.
- `Racionales.py`: Script ejecutable que inicia la calculadora y gestiona la entrada del usuario.
- `Archivos generados por ANTLR`: Racionales.interp, Racionales.tokens, RacionalesLexer.interp, RacionalesLexer.py, RacionalesLexer.tokens, RacionalesListener.py, RacionalesParser.py, RacionalesVisitor.py.

## Uso

1. **Generar archivos de ANTLR:**

   Antes de ejecutar la calculadora, debes generar los archivos de parser y lexer usando ANTLR. Ejecuta el siguiente comando en la terminal:

   ```bash
   antlr4 -Dlanguage=Python3 Racionales.g4
   ```

   Asegúrate de que el archivo RacionalesVisitor.py se genere. Si no se genera, ejecuta el siguiente comando:

   ```bash
    antlr4 -Dlanguage=Python3 -visitor Racionales.g4
   ```

2. **Ejecutar la calculadora:**
    Asegúrate de tener Python instalado y luego ejecuta el programa con el siguiente comando:
    ```bash
    python Racionales.py
    ```
3. **Ejemplos de entrada y salida del programa:**
    ```bash
    Ingrese operación: -5/3*2/1
    Resultado: -10/3

    Ingrese operación: -5/2-4/3
    Resultado: -23/6

    Ingrese operación: 7/4+3/2
    Resultado: 13/4

    Ingrese operación: 7/1/7/1
    Resultado: 1
    ```
4. **Salir del programa**: Para salir de la calculadora, presiona Ctrl + D 



