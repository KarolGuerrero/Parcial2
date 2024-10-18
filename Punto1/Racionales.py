from antlr4 import *
from RacionalesLexer import RacionalesLexer
from RacionalesParser import RacionalesParser
from Visitor import Visitor

def main():
    visitor = Visitor()
    while True:
        try:
            input_stream = InputStream(input("Ingrese operación: "))
            lexer = RacionalesLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = RacionalesParser(token_stream)
            tree = parser.prog()  
            result = visitor.visit(tree)

        except EOFError:
            break  

if __name__ == '__main__':
    main()
