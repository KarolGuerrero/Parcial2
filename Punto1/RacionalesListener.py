# Generated from Racionales.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RacionalesParser import RacionalesParser
else:
    from RacionalesParser import RacionalesParser

# This class defines a complete listener for a parse tree produced by RacionalesParser.
class RacionalesListener(ParseTreeListener):

    # Enter a parse tree produced by RacionalesParser#prog.
    def enterProg(self, ctx:RacionalesParser.ProgContext):
        pass

    # Exit a parse tree produced by RacionalesParser#prog.
    def exitProg(self, ctx:RacionalesParser.ProgContext):
        pass


    # Enter a parse tree produced by RacionalesParser#SingleTerm.
    def enterSingleTerm(self, ctx:RacionalesParser.SingleTermContext):
        pass

    # Exit a parse tree produced by RacionalesParser#SingleTerm.
    def exitSingleTerm(self, ctx:RacionalesParser.SingleTermContext):
        pass


    # Enter a parse tree produced by RacionalesParser#AddSub.
    def enterAddSub(self, ctx:RacionalesParser.AddSubContext):
        pass

    # Exit a parse tree produced by RacionalesParser#AddSub.
    def exitAddSub(self, ctx:RacionalesParser.AddSubContext):
        pass


    # Enter a parse tree produced by RacionalesParser#MulDiv.
    def enterMulDiv(self, ctx:RacionalesParser.MulDivContext):
        pass

    # Exit a parse tree produced by RacionalesParser#MulDiv.
    def exitMulDiv(self, ctx:RacionalesParser.MulDivContext):
        pass


    # Enter a parse tree produced by RacionalesParser#SingleFactor.
    def enterSingleFactor(self, ctx:RacionalesParser.SingleFactorContext):
        pass

    # Exit a parse tree produced by RacionalesParser#SingleFactor.
    def exitSingleFactor(self, ctx:RacionalesParser.SingleFactorContext):
        pass


    # Enter a parse tree produced by RacionalesParser#ParensExpr.
    def enterParensExpr(self, ctx:RacionalesParser.ParensExprContext):
        pass

    # Exit a parse tree produced by RacionalesParser#ParensExpr.
    def exitParensExpr(self, ctx:RacionalesParser.ParensExprContext):
        pass


    # Enter a parse tree produced by RacionalesParser#FractionFactor.
    def enterFractionFactor(self, ctx:RacionalesParser.FractionFactorContext):
        pass

    # Exit a parse tree produced by RacionalesParser#FractionFactor.
    def exitFractionFactor(self, ctx:RacionalesParser.FractionFactorContext):
        pass


    # Enter a parse tree produced by RacionalesParser#NegativeFraction.
    def enterNegativeFraction(self, ctx:RacionalesParser.NegativeFractionContext):
        pass

    # Exit a parse tree produced by RacionalesParser#NegativeFraction.
    def exitNegativeFraction(self, ctx:RacionalesParser.NegativeFractionContext):
        pass


    # Enter a parse tree produced by RacionalesParser#FractionExpr.
    def enterFractionExpr(self, ctx:RacionalesParser.FractionExprContext):
        pass

    # Exit a parse tree produced by RacionalesParser#FractionExpr.
    def exitFractionExpr(self, ctx:RacionalesParser.FractionExprContext):
        pass



del RacionalesParser