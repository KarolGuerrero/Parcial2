import sys
from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser
from Visitor import Visitor

def main():
    if len(sys.argv) < 2:
        print("Uso: python LaplaceEvalVisitor.py <archivo_entrada.txt>")
        sys.exit(1)

    file_name = sys.argv[1]

    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    for line in lines:
        lexer = LaplaceLexer(InputStream(line))
        stream = CommonTokenStream(lexer)
        parser = LaplaceParser(stream)
        tree = parser.start()

        visitor = Visitor()
        result = visitor.visit(tree)

        if result is not None:
            print(result)
        else:
            print(f"No se pudo calcular la transformada de Laplace para: {line}")

if __name__ == '__main__':
    main()
