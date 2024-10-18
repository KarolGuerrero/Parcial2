# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceParser.

class LaplaceVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceParser#start.
    def visitStart(self, ctx:LaplaceParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#laplaceTransform.
    def visitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#baseFunction.
    def visitBaseFunction(self, ctx:LaplaceParser.BaseFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#function.
    def visitFunction(self, ctx:LaplaceParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#expFunction.
    def visitExpFunction(self, ctx:LaplaceParser.ExpFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#unitStepFunction.
    def visitUnitStepFunction(self, ctx:LaplaceParser.UnitStepFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#delayedUnitStepFunction.
    def visitDelayedUnitStepFunction(self, ctx:LaplaceParser.DelayedUnitStepFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#deltaFunction.
    def visitDeltaFunction(self, ctx:LaplaceParser.DeltaFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#delayedDeltaFunction.
    def visitDelayedDeltaFunction(self, ctx:LaplaceParser.DelayedDeltaFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#powFunction.
    def visitPowFunction(self, ctx:LaplaceParser.PowFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#qPowFunction.
    def visitQPowFunction(self, ctx:LaplaceParser.QPowFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#sineFunction.
    def visitSineFunction(self, ctx:LaplaceParser.SineFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#cosineFunction.
    def visitCosineFunction(self, ctx:LaplaceParser.CosineFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#sinhFunction.
    def visitSinhFunction(self, ctx:LaplaceParser.SinhFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#coshFunction.
    def visitCoshFunction(self, ctx:LaplaceParser.CoshFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#logFunction.
    def visitLogFunction(self, ctx:LaplaceParser.LogFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#besselFunction.
    def visitBesselFunction(self, ctx:LaplaceParser.BesselFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#modifiedBesselFunction.
    def visitModifiedBesselFunction(self, ctx:LaplaceParser.ModifiedBesselFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#param.
    def visitParam(self, ctx:LaplaceParser.ParamContext):
        return self.visitChildren(ctx)



del LaplaceParser