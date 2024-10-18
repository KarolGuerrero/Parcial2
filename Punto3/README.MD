# Transformadas de Laplace

Este programa es un intérprete de transformadas de Laplace que permite calcular la transformada de funciones matemáticas utilizando ANTLR para el análisis léxico y sintáctico. Está implementado en Python.

## Funciones soportadas

### 1. Transformadas Básicas

- `L(e^(-a*t))`: Transformada de Laplace de \( e^{-at} \) es \( \frac{1}{s + a} \).
- `L(u(t))`: Transformada de Laplace de \( u(t) \) es \( \frac{1}{s} \).
- `L(u(t-r))`: Transformada de Laplace de \( u(t-r) \) es \( \frac{e^{-r*s}}{s} \).
- `L(δ(t))`: Transformada de Laplace de \( δ(t) \) es \( 1 \).
- `L(δ(t-r))`: Transformada de Laplace de \( δ(t-r) \) es \( e^{-r*s} \).

### 2. Funciones Potenciales

- `L(t^n)`: Transformada de Laplace de \( t^n \) es \( \frac{n!}{s^{n+1}} \).
- `L(sin(ωt))`: Transformada de Laplace de \( sin(ωt) \) es \( \frac{ω}{s^2 + ω^2} \).
- `L(cos(ωt))`: Transformada de Laplace de \( cos(ωt) \) es \( \frac{s}{s^2 + ω^2} \).
- `L(sinh(at))`: Transformada de Laplace de \( sinh(at) \) es \( \frac{a}{s^2 - a^2} \).
- `L(cosh(at))`: Transformada de Laplace de \( cosh(at) \) es \( \frac{s}{s^2 - a^2} \).
- `L(log(t/t0))`: Transformada de Laplace de \( log(t/t0) \) es \( -\frac{log(t0)}{s} - \frac{1}{s^2} \).
- `L(Jn(ωt))`: Transformada de Laplace de \( J_n(ωt) \) es \( \frac{ω^n}{(s^2 + ω^2)^{(n+1/2)}} \).
- `L(I(at))`: Transformada de Laplace de la función de Bessel modificada.

## Requisitos

- Python 3
- ANTLR 4

## Archivos del Proyecto

- `Laplace.g4`: Archivo de gramática ANTLR que define la sintaxis para las transformadas de Laplace.
- `LaplaceEvalVisitor.py`: Implementación del Visitor que evalúa las transformadas de Laplace.
- `Laplace.py`: Script ejecutable que inicia el intérprete y gestiona la entrada del usuario.
- Archivos generados por ANTLR: `LaplaceLexer.py`, `LaplaceParser.py`, `LaplaceVisitor.py`, `LaplaceLexer.interp`, `LaplaceParser.interp`, `LaplaceLexer.tokens`, `LaplaceParser.tokens`, `LaplaceListener.py`.

## Uso

1. **Generar archivos de ANTLR:**

   Antes de ejecutar el programa, debes generar los archivos de parser y lexer usando ANTLR. Ejecuta el siguiente comando en la terminal:

   ```bash
   antlr4 -Dlanguage=Python3 --visitor Laplace.g4
   ```

   Asegúrate de incluir **--visitor** para que se genere el visitor que ANTLR proporciona junto con los otros archivos.

2. **Ejecutar el intérprete:**

   Asegúrate de tener Python instalado y luego ejecuta el programa con el siguiente comando:

   ```bash
   python Laplace.py Input.txt
   ```

3. **Archivo de pruebas:**

   Para realizar pruebas, necesitas crear un archivo de texto donde se especifiquen las transformadas de Laplace. La salida de estas transformadas se mostrará en la consola.

   **Estructura del archivo de prueba:**
   - Cada línea debe contener una declaración de transformada, comenzando con `L(` y terminando con `)`.
   - Las funciones se pueden escribir usando variables y constantes.

   **Ejemplo de archivo de pruebas (`Input.txt`):**

   ```plaintext
   L(e^(-2*t));
   L(u(t));
   L(u(t-3));
   L(δ(t));
   L(δ(t-4));
   L(t^3);
   L(sin(2*t));
   L(cos(3*t));
   L(cosh(7*t));
   L(Jn(2*t));
   ```

4. **Salida:**

   Al ejecutar el programa con el archivo de prueba, la salida se mostrará en la consola en el siguiente formato:

   ```plaintext
   Transformada de Laplace de e^(-2*t) es 1 / (s + 2)
   Transformada de Laplace de u(t) es 1 / s
   Transformada de Laplace de u(t-3) es e^(-3*s) / s
   Transformada de Laplace de δ(t) es 1
   Transformada de Laplace de δ(t-4) es e^(-4*s)
   Transformada de Laplace de t^3 es 6 / s^4
   Transformada de Laplace de sin(2*t) es 2 / (s^2 + 4)
   Transformada de Laplace de cos(3*t) es s / (s^2 + 9)
   Transformada de Laplace de cosh(7*t) es s / (s^2 - 49)
   Transformada de Laplace de Jn(2*t) es 2^n / (s^2 + 4)^(n+1/2)
   ```
