# Generated from Colecciones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ColeccionesParser import ColeccionesParser
else:
    from ColeccionesParser import ColeccionesParser

# This class defines a complete listener for a parse tree produced by ColeccionesParser.
class ColeccionesListener(ParseTreeListener):

    # Enter a parse tree produced by ColeccionesParser#program.
    def enterProgram(self, ctx:ColeccionesParser.ProgramContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#program.
    def exitProgram(self, ctx:ColeccionesParser.ProgramContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#statement.
    def enterStatement(self, ctx:ColeccionesParser.StatementContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#statement.
    def exitStatement(self, ctx:ColeccionesParser.StatementContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#mapFunction.
    def enterMapFunction(self, ctx:ColeccionesParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#mapFunction.
    def exitMapFunction(self, ctx:ColeccionesParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#filterFunction.
    def enterFilterFunction(self, ctx:ColeccionesParser.FilterFunctionContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#filterFunction.
    def exitFilterFunction(self, ctx:ColeccionesParser.FilterFunctionContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#functionCall.
    def enterFunctionCall(self, ctx:ColeccionesParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#functionCall.
    def exitFunctionCall(self, ctx:ColeccionesParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#iterableObject.
    def enterIterableObject(self, ctx:ColeccionesParser.IterableObjectContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#iterableObject.
    def exitIterableObject(self, ctx:ColeccionesParser.IterableObjectContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#list.
    def enterList(self, ctx:ColeccionesParser.ListContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#list.
    def exitList(self, ctx:ColeccionesParser.ListContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#tuple.
    def enterTuple(self, ctx:ColeccionesParser.TupleContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#tuple.
    def exitTuple(self, ctx:ColeccionesParser.TupleContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#expressionList.
    def enterExpressionList(self, ctx:ColeccionesParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#expressionList.
    def exitExpressionList(self, ctx:ColeccionesParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by ColeccionesParser#expression.
    def enterExpression(self, ctx:ColeccionesParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ColeccionesParser#expression.
    def exitExpression(self, ctx:ColeccionesParser.ExpressionContext):
        pass



del ColeccionesParser