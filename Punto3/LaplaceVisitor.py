# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceParser.

class LaplaceVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceParser#laplaceTransform.
    def visitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#expression.
    def visitExpression(self, ctx:LaplaceParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#term.
    def visitTerm(self, ctx:LaplaceParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#factor.
    def visitFactor(self, ctx:LaplaceParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#function.
    def visitFunction(self, ctx:LaplaceParser.FunctionContext):
        return self.visitChildren(ctx)



del LaplaceParser