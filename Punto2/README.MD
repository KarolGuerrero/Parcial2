# Colecciones

Este programa es un intérprete de colecciones que permite realizar operaciones de mapeo y filtrado utilizando listas y tuplas. El programa está implementado en Python utilizando ANTLR para el análisis léxico y sintáctico.

## Funciones soportadas

El programa permite las siguientes operaciones:

### 1. MAP

  - `square`: Devuelve el cuadrado del número.
  - `increment`: Aumenta el número en uno.
  - `double`: Multiplica el número por dos.

### 2. FILTER

  - `is_greater_than`: Filtra elementos que son mayores que un número dado.
  - `is_less_than`: Filtra elementos que son menores que un número dado.
  - `is_multiple_of`: Filtra elementos que son múltiplos de un número dado.
  - `is_divisible_by`: Filtra elementos que son divisores de un número dado.
  - `greater_than_length`: Filtra cadenas cuya longitud es mayor que un número dado.

## Requisitos

- Python3
- ANTLR4

## Archivos del Proyecto

- `Colecciones.g4`: Archivo de gramática ANTLR que define la sintaxis para las operaciones de `MAP` y `FILTER`.
- `Visitor.py`: Implementación del Visitor que evalúa las operaciones de mapeo y filtrado.
- `Colecciones.py`: Script ejecutable que inicia el intérprete y gestiona la entrada del usuario.
- Archivos generados por ANTLR: `ColeccionesLexer.py`, `ColeccionesParser.py`, `ColeccionesVisitor.py`, `ColeccionesLexer.interp`, `ColeccionesParser.interp`, `Colecciones.tokens`, `ColeccionesLexer.tokens`, `ColeccionesListener.py`.

## Uso

1. **Generar archivos de ANTLR:**

   Antes de ejecutar el programa, debes generar los archivos de parser y lexer usando ANTLR. Ejecuta el siguiente comando en la terminal:

   ```bash
   antlr4 -Dlanguage=Python3 -visitor Colecciones.g4
   ```
   Asegurate de poner **-visitor** para que se genere el visitor que antlr da junto con los otros archivos.


2. **Ejecutar el intérprete:**

   Asegúrate de tener Python instalado y luego ejecuta el programa con el siguiente comando:

   ```bash
   python Colecciones.py
   ```

3. **Archivo de pruebas:**

   Para realizar pruebas, necesitas crear un archivo de texto donde se especifiquen las operaciones de `MAP` y `FILTER`. La salida de estas operaciones se mostrará en la consola.

   **Estructura del archivo de prueba:**
   - Cada línea debe contener una declaración de operación, terminada con un punto y coma (`;`).
   - Las operaciones se pueden escribir usando listas `[...]` o tuplas `(...)`.

   **Ejemplo de archivo de pruebas (`test.txt`):**

   ```plaintext
   MAP(square, [1, 2, 3, 4]);
   FILTER(is_greater_than, [10, 20, 30], 15);
   MAP(increment, (5, 10, 15));
   FILTER(is_multiple_of, [10, 15, 20, 25, 30], 5);
   ```

4. **Salida:**

   Al ejecutar el programa con el archivo de prueba, la salida se mostrará en la consola en el siguiente formato:

   ```plaintext
   MAP(square, [1, 2, 3, 4]) --> [1, 4, 9, 16]
   FILTER(is_greater_than, [10, 20, 30], 15) --> [20, 30]
   MAP(increment, (5, 10, 15)): [6, 11, 16]
   FILTER(is_multiple_of, [10, 15, 20, 25, 30], 5) --> [10, 15, 20, 25, 30]
   ```