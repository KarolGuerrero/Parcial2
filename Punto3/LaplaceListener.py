# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete listener for a parse tree produced by LaplaceParser.
class LaplaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceParser#start.
    def enterStart(self, ctx:LaplaceParser.StartContext):
        pass

    # Exit a parse tree produced by LaplaceParser#start.
    def exitStart(self, ctx:LaplaceParser.StartContext):
        pass


    # Enter a parse tree produced by LaplaceParser#laplaceTransform.
    def enterLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass

    # Exit a parse tree produced by LaplaceParser#laplaceTransform.
    def exitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass


    # Enter a parse tree produced by LaplaceParser#baseFunction.
    def enterBaseFunction(self, ctx:LaplaceParser.BaseFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#baseFunction.
    def exitBaseFunction(self, ctx:LaplaceParser.BaseFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#function.
    def enterFunction(self, ctx:LaplaceParser.FunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#function.
    def exitFunction(self, ctx:LaplaceParser.FunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#expFunction.
    def enterExpFunction(self, ctx:LaplaceParser.ExpFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#expFunction.
    def exitExpFunction(self, ctx:LaplaceParser.ExpFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#unitStepFunction.
    def enterUnitStepFunction(self, ctx:LaplaceParser.UnitStepFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#unitStepFunction.
    def exitUnitStepFunction(self, ctx:LaplaceParser.UnitStepFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#delayedUnitStepFunction.
    def enterDelayedUnitStepFunction(self, ctx:LaplaceParser.DelayedUnitStepFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#delayedUnitStepFunction.
    def exitDelayedUnitStepFunction(self, ctx:LaplaceParser.DelayedUnitStepFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#deltaFunction.
    def enterDeltaFunction(self, ctx:LaplaceParser.DeltaFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#deltaFunction.
    def exitDeltaFunction(self, ctx:LaplaceParser.DeltaFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#delayedDeltaFunction.
    def enterDelayedDeltaFunction(self, ctx:LaplaceParser.DelayedDeltaFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#delayedDeltaFunction.
    def exitDelayedDeltaFunction(self, ctx:LaplaceParser.DelayedDeltaFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#powFunction.
    def enterPowFunction(self, ctx:LaplaceParser.PowFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#powFunction.
    def exitPowFunction(self, ctx:LaplaceParser.PowFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#qPowFunction.
    def enterQPowFunction(self, ctx:LaplaceParser.QPowFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#qPowFunction.
    def exitQPowFunction(self, ctx:LaplaceParser.QPowFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#sineFunction.
    def enterSineFunction(self, ctx:LaplaceParser.SineFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#sineFunction.
    def exitSineFunction(self, ctx:LaplaceParser.SineFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#cosineFunction.
    def enterCosineFunction(self, ctx:LaplaceParser.CosineFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#cosineFunction.
    def exitCosineFunction(self, ctx:LaplaceParser.CosineFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#sinhFunction.
    def enterSinhFunction(self, ctx:LaplaceParser.SinhFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#sinhFunction.
    def exitSinhFunction(self, ctx:LaplaceParser.SinhFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#coshFunction.
    def enterCoshFunction(self, ctx:LaplaceParser.CoshFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#coshFunction.
    def exitCoshFunction(self, ctx:LaplaceParser.CoshFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#logFunction.
    def enterLogFunction(self, ctx:LaplaceParser.LogFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#logFunction.
    def exitLogFunction(self, ctx:LaplaceParser.LogFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#besselFunction.
    def enterBesselFunction(self, ctx:LaplaceParser.BesselFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#besselFunction.
    def exitBesselFunction(self, ctx:LaplaceParser.BesselFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#modifiedBesselFunction.
    def enterModifiedBesselFunction(self, ctx:LaplaceParser.ModifiedBesselFunctionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#modifiedBesselFunction.
    def exitModifiedBesselFunction(self, ctx:LaplaceParser.ModifiedBesselFunctionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#param.
    def enterParam(self, ctx:LaplaceParser.ParamContext):
        pass

    # Exit a parse tree produced by LaplaceParser#param.
    def exitParam(self, ctx:LaplaceParser.ParamContext):
        pass



del LaplaceParser