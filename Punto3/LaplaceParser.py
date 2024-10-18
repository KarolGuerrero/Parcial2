# Generated from Laplace.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,62,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,
        0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,1,1,0,
        19,20,152,0,36,1,0,0,0,2,45,1,0,0,0,4,61,1,0,0,0,6,63,1,0,0,0,8,
        72,1,0,0,0,10,77,1,0,0,0,12,84,1,0,0,0,14,89,1,0,0,0,16,96,1,0,0,
        0,18,100,1,0,0,0,20,104,1,0,0,0,22,111,1,0,0,0,24,118,1,0,0,0,26,
        125,1,0,0,0,28,132,1,0,0,0,30,139,1,0,0,0,32,146,1,0,0,0,34,154,
        1,0,0,0,36,37,3,2,1,0,37,38,5,0,0,1,38,1,1,0,0,0,39,40,5,18,0,0,
        40,41,5,1,0,0,41,42,3,4,2,0,42,43,5,2,0,0,43,46,1,0,0,0,44,46,3,
        4,2,0,45,39,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,62,3,6,3,0,48,
        62,3,8,4,0,49,62,3,10,5,0,50,62,3,12,6,0,51,62,3,14,7,0,52,62,3,
        16,8,0,53,62,3,18,9,0,54,62,3,20,10,0,55,62,3,22,11,0,56,62,3,24,
        12,0,57,62,3,26,13,0,58,62,3,28,14,0,59,62,3,30,15,0,60,62,3,32,
        16,0,61,47,1,0,0,0,61,48,1,0,0,0,61,49,1,0,0,0,61,50,1,0,0,0,61,
        51,1,0,0,0,61,52,1,0,0,0,61,53,1,0,0,0,61,54,1,0,0,0,61,55,1,0,0,
        0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,
        1,0,0,0,62,5,1,0,0,0,63,64,5,3,0,0,64,65,5,4,0,0,65,66,5,1,0,0,66,
        67,5,5,0,0,67,68,3,34,17,0,68,69,5,6,0,0,69,70,5,7,0,0,70,71,5,2,
        0,0,71,7,1,0,0,0,72,73,5,8,0,0,73,74,5,1,0,0,74,75,5,7,0,0,75,76,
        5,2,0,0,76,9,1,0,0,0,77,78,5,8,0,0,78,79,5,1,0,0,79,80,5,7,0,0,80,
        81,5,5,0,0,81,82,3,34,17,0,82,83,5,2,0,0,83,11,1,0,0,0,84,85,5,9,
        0,0,85,86,5,1,0,0,86,87,5,7,0,0,87,88,5,2,0,0,88,13,1,0,0,0,89,90,
        5,9,0,0,90,91,5,1,0,0,91,92,5,7,0,0,92,93,5,5,0,0,93,94,3,34,17,
        0,94,95,5,2,0,0,95,15,1,0,0,0,96,97,5,7,0,0,97,98,5,4,0,0,98,99,
        5,19,0,0,99,17,1,0,0,0,100,101,5,7,0,0,101,102,5,4,0,0,102,103,3,
        34,17,0,103,19,1,0,0,0,104,105,5,10,0,0,105,106,5,1,0,0,106,107,
        3,34,17,0,107,108,5,6,0,0,108,109,5,7,0,0,109,110,5,2,0,0,110,21,
        1,0,0,0,111,112,5,11,0,0,112,113,5,1,0,0,113,114,3,34,17,0,114,115,
        5,6,0,0,115,116,5,7,0,0,116,117,5,2,0,0,117,23,1,0,0,0,118,119,5,
        12,0,0,119,120,5,1,0,0,120,121,3,34,17,0,121,122,5,6,0,0,122,123,
        5,7,0,0,123,124,5,2,0,0,124,25,1,0,0,0,125,126,5,13,0,0,126,127,
        5,1,0,0,127,128,3,34,17,0,128,129,5,6,0,0,129,130,5,7,0,0,130,131,
        5,2,0,0,131,27,1,0,0,0,132,133,5,14,0,0,133,134,5,1,0,0,134,135,
        5,7,0,0,135,136,5,15,0,0,136,137,3,34,17,0,137,138,5,2,0,0,138,29,
        1,0,0,0,139,140,5,16,0,0,140,141,5,1,0,0,141,142,3,34,17,0,142,143,
        5,6,0,0,143,144,5,7,0,0,144,145,5,2,0,0,145,31,1,0,0,0,146,147,5,
        17,0,0,147,148,3,34,17,0,148,149,5,1,0,0,149,150,3,34,17,0,150,151,
        5,6,0,0,151,152,5,7,0,0,152,153,5,2,0,0,153,33,1,0,0,0,154,155,7,
        0,0,0,155,35,1,0,0,0,2,45,61
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'e'", "'^'", "'-'", "'*'", 
                     "'t'", "'u'", "'\\u03B4'", "'sin'", "'cos'", "'sinh'", 
                     "'cosh'", "'log'", "'/'", "'Jn'", "'I'", "'L'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LAPLACE", "INT", "FLOAT", 
                      "WS" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_function = 2
    RULE_expFunction = 3
    RULE_unitStepFunction = 4
    RULE_delayedUnitStepFunction = 5
    RULE_deltaFunction = 6
    RULE_delayedDeltaFunction = 7
    RULE_powFunction = 8
    RULE_qPowFunction = 9
    RULE_sineFunction = 10
    RULE_cosineFunction = 11
    RULE_sinhFunction = 12
    RULE_coshFunction = 13
    RULE_logFunction = 14
    RULE_besselFunction = 15
    RULE_modifiedBesselFunction = 16
    RULE_param = 17

    ruleNames =  [ "start", "expr", "function", "expFunction", "unitStepFunction", 
                   "delayedUnitStepFunction", "deltaFunction", "delayedDeltaFunction", 
                   "powFunction", "qPowFunction", "sineFunction", "cosineFunction", 
                   "sinhFunction", "coshFunction", "logFunction", "besselFunction", 
                   "modifiedBesselFunction", "param" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    LAPLACE=18
    INT=19
    FLOAT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaplaceParser.ExprContext,0)


        def EOF(self):
            return self.getToken(LaplaceParser.EOF, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = LaplaceParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.expr()
            self.state = 37
            self.match(LaplaceParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LaplaceParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BaseFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseFunction" ):
                listener.enterBaseFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseFunction" ):
                listener.exitBaseFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseFunction" ):
                return visitor.visitBaseFunction(self)
            else:
                return visitor.visitChildren(self)


    class LaplaceTransformContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAPLACE(self):
            return self.getToken(LaplaceParser.LAPLACE, 0)
        def function(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaplaceTransform" ):
                listener.enterLaplaceTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaplaceTransform" ):
                listener.exitLaplaceTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLaplaceTransform" ):
                return visitor.visitLaplaceTransform(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = LaplaceParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = LaplaceParser.LaplaceTransformContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(LaplaceParser.LAPLACE)
                self.state = 40
                self.match(LaplaceParser.T__0)
                self.state = 41
                self.function()
                self.state = 42
                self.match(LaplaceParser.T__1)
                pass
            elif token in [3, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17]:
                localctx = LaplaceParser.BaseFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expFunction(self):
            return self.getTypedRuleContext(LaplaceParser.ExpFunctionContext,0)


        def unitStepFunction(self):
            return self.getTypedRuleContext(LaplaceParser.UnitStepFunctionContext,0)


        def delayedUnitStepFunction(self):
            return self.getTypedRuleContext(LaplaceParser.DelayedUnitStepFunctionContext,0)


        def deltaFunction(self):
            return self.getTypedRuleContext(LaplaceParser.DeltaFunctionContext,0)


        def delayedDeltaFunction(self):
            return self.getTypedRuleContext(LaplaceParser.DelayedDeltaFunctionContext,0)


        def powFunction(self):
            return self.getTypedRuleContext(LaplaceParser.PowFunctionContext,0)


        def qPowFunction(self):
            return self.getTypedRuleContext(LaplaceParser.QPowFunctionContext,0)


        def sineFunction(self):
            return self.getTypedRuleContext(LaplaceParser.SineFunctionContext,0)


        def cosineFunction(self):
            return self.getTypedRuleContext(LaplaceParser.CosineFunctionContext,0)


        def sinhFunction(self):
            return self.getTypedRuleContext(LaplaceParser.SinhFunctionContext,0)


        def coshFunction(self):
            return self.getTypedRuleContext(LaplaceParser.CoshFunctionContext,0)


        def logFunction(self):
            return self.getTypedRuleContext(LaplaceParser.LogFunctionContext,0)


        def besselFunction(self):
            return self.getTypedRuleContext(LaplaceParser.BesselFunctionContext,0)


        def modifiedBesselFunction(self):
            return self.getTypedRuleContext(LaplaceParser.ModifiedBesselFunctionContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = LaplaceParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.expFunction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.unitStepFunction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.delayedUnitStepFunction()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.deltaFunction()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.delayedDeltaFunction()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.powFunction()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 53
                self.qPowFunction()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 54
                self.sineFunction()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 55
                self.cosineFunction()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 56
                self.sinhFunction()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 57
                self.coshFunction()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 58
                self.logFunction()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 59
                self.besselFunction()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 60
                self.modifiedBesselFunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_expFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpFunction" ):
                listener.enterExpFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpFunction" ):
                listener.exitExpFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpFunction" ):
                return visitor.visitExpFunction(self)
            else:
                return visitor.visitChildren(self)




    def expFunction(self):

        localctx = LaplaceParser.ExpFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(LaplaceParser.T__2)
            self.state = 64
            self.match(LaplaceParser.T__3)
            self.state = 65
            self.match(LaplaceParser.T__0)
            self.state = 66
            self.match(LaplaceParser.T__4)
            self.state = 67
            self.param()
            self.state = 68
            self.match(LaplaceParser.T__5)
            self.state = 69
            self.match(LaplaceParser.T__6)
            self.state = 70
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitStepFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LaplaceParser.RULE_unitStepFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnitStepFunction" ):
                listener.enterUnitStepFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnitStepFunction" ):
                listener.exitUnitStepFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitStepFunction" ):
                return visitor.visitUnitStepFunction(self)
            else:
                return visitor.visitChildren(self)




    def unitStepFunction(self):

        localctx = LaplaceParser.UnitStepFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unitStepFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(LaplaceParser.T__7)
            self.state = 73
            self.match(LaplaceParser.T__0)
            self.state = 74
            self.match(LaplaceParser.T__6)
            self.state = 75
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DelayedUnitStepFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_delayedUnitStepFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelayedUnitStepFunction" ):
                listener.enterDelayedUnitStepFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelayedUnitStepFunction" ):
                listener.exitDelayedUnitStepFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelayedUnitStepFunction" ):
                return visitor.visitDelayedUnitStepFunction(self)
            else:
                return visitor.visitChildren(self)




    def delayedUnitStepFunction(self):

        localctx = LaplaceParser.DelayedUnitStepFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_delayedUnitStepFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(LaplaceParser.T__7)
            self.state = 78
            self.match(LaplaceParser.T__0)
            self.state = 79
            self.match(LaplaceParser.T__6)
            self.state = 80
            self.match(LaplaceParser.T__4)
            self.state = 81
            self.param()
            self.state = 82
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeltaFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LaplaceParser.RULE_deltaFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeltaFunction" ):
                listener.enterDeltaFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeltaFunction" ):
                listener.exitDeltaFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeltaFunction" ):
                return visitor.visitDeltaFunction(self)
            else:
                return visitor.visitChildren(self)




    def deltaFunction(self):

        localctx = LaplaceParser.DeltaFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_deltaFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(LaplaceParser.T__8)
            self.state = 85
            self.match(LaplaceParser.T__0)
            self.state = 86
            self.match(LaplaceParser.T__6)
            self.state = 87
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DelayedDeltaFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_delayedDeltaFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelayedDeltaFunction" ):
                listener.enterDelayedDeltaFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelayedDeltaFunction" ):
                listener.exitDelayedDeltaFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelayedDeltaFunction" ):
                return visitor.visitDelayedDeltaFunction(self)
            else:
                return visitor.visitChildren(self)




    def delayedDeltaFunction(self):

        localctx = LaplaceParser.DelayedDeltaFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_delayedDeltaFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(LaplaceParser.T__8)
            self.state = 90
            self.match(LaplaceParser.T__0)
            self.state = 91
            self.match(LaplaceParser.T__6)
            self.state = 92
            self.match(LaplaceParser.T__4)
            self.state = 93
            self.param()
            self.state = 94
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LaplaceParser.INT, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_powFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowFunction" ):
                listener.enterPowFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowFunction" ):
                listener.exitPowFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowFunction" ):
                return visitor.visitPowFunction(self)
            else:
                return visitor.visitChildren(self)




    def powFunction(self):

        localctx = LaplaceParser.PowFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_powFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(LaplaceParser.T__6)
            self.state = 97
            self.match(LaplaceParser.T__3)
            self.state = 98
            self.match(LaplaceParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QPowFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_qPowFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQPowFunction" ):
                listener.enterQPowFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQPowFunction" ):
                listener.exitQPowFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQPowFunction" ):
                return visitor.visitQPowFunction(self)
            else:
                return visitor.visitChildren(self)




    def qPowFunction(self):

        localctx = LaplaceParser.QPowFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_qPowFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LaplaceParser.T__6)
            self.state = 101
            self.match(LaplaceParser.T__3)
            self.state = 102
            self.param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SineFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_sineFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSineFunction" ):
                listener.enterSineFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSineFunction" ):
                listener.exitSineFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSineFunction" ):
                return visitor.visitSineFunction(self)
            else:
                return visitor.visitChildren(self)




    def sineFunction(self):

        localctx = LaplaceParser.SineFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sineFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(LaplaceParser.T__9)
            self.state = 105
            self.match(LaplaceParser.T__0)
            self.state = 106
            self.param()
            self.state = 107
            self.match(LaplaceParser.T__5)
            self.state = 108
            self.match(LaplaceParser.T__6)
            self.state = 109
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CosineFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_cosineFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosineFunction" ):
                listener.enterCosineFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosineFunction" ):
                listener.exitCosineFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosineFunction" ):
                return visitor.visitCosineFunction(self)
            else:
                return visitor.visitChildren(self)




    def cosineFunction(self):

        localctx = LaplaceParser.CosineFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cosineFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(LaplaceParser.T__10)
            self.state = 112
            self.match(LaplaceParser.T__0)
            self.state = 113
            self.param()
            self.state = 114
            self.match(LaplaceParser.T__5)
            self.state = 115
            self.match(LaplaceParser.T__6)
            self.state = 116
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinhFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_sinhFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinhFunction" ):
                listener.enterSinhFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinhFunction" ):
                listener.exitSinhFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinhFunction" ):
                return visitor.visitSinhFunction(self)
            else:
                return visitor.visitChildren(self)




    def sinhFunction(self):

        localctx = LaplaceParser.SinhFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sinhFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(LaplaceParser.T__11)
            self.state = 119
            self.match(LaplaceParser.T__0)
            self.state = 120
            self.param()
            self.state = 121
            self.match(LaplaceParser.T__5)
            self.state = 122
            self.match(LaplaceParser.T__6)
            self.state = 123
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoshFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_coshFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoshFunction" ):
                listener.enterCoshFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoshFunction" ):
                listener.exitCoshFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoshFunction" ):
                return visitor.visitCoshFunction(self)
            else:
                return visitor.visitChildren(self)




    def coshFunction(self):

        localctx = LaplaceParser.CoshFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_coshFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(LaplaceParser.T__12)
            self.state = 126
            self.match(LaplaceParser.T__0)
            self.state = 127
            self.param()
            self.state = 128
            self.match(LaplaceParser.T__5)
            self.state = 129
            self.match(LaplaceParser.T__6)
            self.state = 130
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_logFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogFunction" ):
                listener.enterLogFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogFunction" ):
                listener.exitLogFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogFunction" ):
                return visitor.visitLogFunction(self)
            else:
                return visitor.visitChildren(self)




    def logFunction(self):

        localctx = LaplaceParser.LogFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_logFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(LaplaceParser.T__13)
            self.state = 133
            self.match(LaplaceParser.T__0)
            self.state = 134
            self.match(LaplaceParser.T__6)
            self.state = 135
            self.match(LaplaceParser.T__14)
            self.state = 136
            self.param()
            self.state = 137
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BesselFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LaplaceParser.ParamContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_besselFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBesselFunction" ):
                listener.enterBesselFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBesselFunction" ):
                listener.exitBesselFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBesselFunction" ):
                return visitor.visitBesselFunction(self)
            else:
                return visitor.visitChildren(self)




    def besselFunction(self):

        localctx = LaplaceParser.BesselFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_besselFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(LaplaceParser.T__15)
            self.state = 140
            self.match(LaplaceParser.T__0)
            self.state = 141
            self.param()
            self.state = 142
            self.match(LaplaceParser.T__5)
            self.state = 143
            self.match(LaplaceParser.T__6)
            self.state = 144
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifiedBesselFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.ParamContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.ParamContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_modifiedBesselFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifiedBesselFunction" ):
                listener.enterModifiedBesselFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifiedBesselFunction" ):
                listener.exitModifiedBesselFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifiedBesselFunction" ):
                return visitor.visitModifiedBesselFunction(self)
            else:
                return visitor.visitChildren(self)




    def modifiedBesselFunction(self):

        localctx = LaplaceParser.ModifiedBesselFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_modifiedBesselFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(LaplaceParser.T__16)
            self.state = 147
            self.param()
            self.state = 148
            self.match(LaplaceParser.T__0)
            self.state = 149
            self.param()
            self.state = 150
            self.match(LaplaceParser.T__5)
            self.state = 151
            self.match(LaplaceParser.T__6)
            self.state = 152
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LaplaceParser.INT, 0)

        def FLOAT(self):
            return self.getToken(LaplaceParser.FLOAT, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = LaplaceParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





