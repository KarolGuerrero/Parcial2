import sys
from antlr4 import *
from ColeccionesLexer import ColeccionesLexer
from ColeccionesParser import ColeccionesParser
from Visitor import Visitor

if __name__ == '__main__':

    input_stream = FileStream(sys.argv[1])
    lexer = ColeccionesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ColeccionesParser(token_stream)
    tree = parser.program()
    visitor = Visitor()
    visitor.visit(tree)

