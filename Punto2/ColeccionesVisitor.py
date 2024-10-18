# Generated from Colecciones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ColeccionesParser import ColeccionesParser
else:
    from ColeccionesParser import ColeccionesParser

# This class defines a complete generic visitor for a parse tree produced by ColeccionesParser.

class ColeccionesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ColeccionesParser#program.
    def visitProgram(self, ctx:ColeccionesParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#statement.
    def visitStatement(self, ctx:ColeccionesParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#mapFunction.
    def visitMapFunction(self, ctx:ColeccionesParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#filterFunction.
    def visitFilterFunction(self, ctx:ColeccionesParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#functionCall.
    def visitFunctionCall(self, ctx:ColeccionesParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#iterableObject.
    def visitIterableObject(self, ctx:ColeccionesParser.IterableObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#list.
    def visitList(self, ctx:ColeccionesParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#tuple.
    def visitTuple(self, ctx:ColeccionesParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColeccionesParser#expressionList.
    def visitExpressionList(self, ctx:ColeccionesParser.ExpressionListContext):
        return self.visitChildren(ctx)

    def visitExpression(self, ctx:ColeccionesParser.ExpressionContext):
        return self.visitChildren(ctx)



del ColeccionesParser