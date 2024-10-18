# Generated from Racionales.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RacionalesParser import RacionalesParser
else:
    from RacionalesParser import RacionalesParser

# This class defines a complete generic visitor for a parse tree produced by RacionalesParser.

class RacionalesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RacionalesParser#prog.
    def visitProg(self, ctx:RacionalesParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#SingleTerm.
    def visitSingleTerm(self, ctx:RacionalesParser.SingleTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#AddSub.
    def visitAddSub(self, ctx:RacionalesParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#MulDiv.
    def visitMulDiv(self, ctx:RacionalesParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#SingleFactor.
    def visitSingleFactor(self, ctx:RacionalesParser.SingleFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#ParensExpr.
    def visitParensExpr(self, ctx:RacionalesParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#FractionFactor.
    def visitFractionFactor(self, ctx:RacionalesParser.FractionFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#NegativeFraction.
    def visitNegativeFraction(self, ctx:RacionalesParser.NegativeFractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RacionalesParser#FractionExpr.
    def visitFractionExpr(self, ctx:RacionalesParser.FractionExprContext):
        return self.visitChildren(ctx)



del RacionalesParser