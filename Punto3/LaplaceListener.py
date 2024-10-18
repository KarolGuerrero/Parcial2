# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete listener for a parse tree produced by LaplaceParser.
class LaplaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceParser#laplaceTransform.
    def enterLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass

    # Exit a parse tree produced by LaplaceParser#laplaceTransform.
    def exitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass


    # Enter a parse tree produced by LaplaceParser#expression.
    def enterExpression(self, ctx:LaplaceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#expression.
    def exitExpression(self, ctx:LaplaceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#term.
    def enterTerm(self, ctx:LaplaceParser.TermContext):
        pass

    # Exit a parse tree produced by LaplaceParser#term.
    def exitTerm(self, ctx:LaplaceParser.TermContext):
        pass


    # Enter a parse tree produced by LaplaceParser#factor.
    def enterFactor(self, ctx:LaplaceParser.FactorContext):
        pass

    # Exit a parse tree produced by LaplaceParser#factor.
    def exitFactor(self, ctx:LaplaceParser.FactorContext):
        pass


    # Enter a parse tree produced by LaplaceParser#function.
    def enterFunction(self, ctx:LaplaceParser.FunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#function.
    def exitFunction(self, ctx:LaplaceParser.FunctionContext):
        pass



del LaplaceParser