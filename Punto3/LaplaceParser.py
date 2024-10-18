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
        4,1,28,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,3,1,30,8,1,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,94,8,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,8,9,1,0,10,
        11,103,0,10,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,52,1,0,0,0,8,93,
        1,0,0,0,10,11,5,1,0,0,11,12,5,2,0,0,12,13,3,2,1,0,13,14,5,3,0,0,
        14,15,5,4,0,0,15,16,5,5,0,0,16,17,5,6,0,0,17,18,5,25,0,0,18,19,5,
        7,0,0,19,1,1,0,0,0,20,30,3,8,4,0,21,26,3,4,2,0,22,23,7,0,0,0,23,
        25,3,4,2,0,24,22,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,
        0,27,30,1,0,0,0,28,26,1,0,0,0,29,20,1,0,0,0,29,21,1,0,0,0,30,3,1,
        0,0,0,31,36,3,6,3,0,32,33,7,1,0,0,33,35,3,6,3,0,34,32,1,0,0,0,35,
        38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,36,1,0,0,
        0,39,40,5,27,0,0,40,41,5,6,0,0,41,42,3,2,1,0,42,43,5,7,0,0,43,53,
        1,0,0,0,44,53,5,25,0,0,45,53,5,26,0,0,46,47,5,9,0,0,47,53,3,6,3,
        0,48,49,5,6,0,0,49,50,3,2,1,0,50,51,5,7,0,0,51,53,1,0,0,0,52,39,
        1,0,0,0,52,44,1,0,0,0,52,45,1,0,0,0,52,46,1,0,0,0,52,48,1,0,0,0,
        53,7,1,0,0,0,54,55,5,12,0,0,55,56,5,6,0,0,56,57,3,2,1,0,57,58,5,
        7,0,0,58,59,5,13,0,0,59,60,5,14,0,0,60,61,5,15,0,0,61,62,5,16,0,
        0,62,63,5,17,0,0,63,94,1,0,0,0,64,65,5,18,0,0,65,66,5,19,0,0,66,
        67,5,6,0,0,67,68,5,9,0,0,68,69,5,25,0,0,69,70,5,10,0,0,70,71,5,25,
        0,0,71,94,5,7,0,0,72,73,5,20,0,0,73,74,5,6,0,0,74,75,5,25,0,0,75,
        94,5,7,0,0,76,77,5,21,0,0,77,78,5,6,0,0,78,79,5,25,0,0,79,94,5,7,
        0,0,80,81,5,22,0,0,81,82,5,6,0,0,82,83,5,25,0,0,83,94,5,7,0,0,84,
        85,5,23,0,0,85,86,5,6,0,0,86,87,3,2,1,0,87,88,5,7,0,0,88,94,1,0,
        0,0,89,90,5,24,0,0,90,91,5,6,0,0,91,92,5,25,0,0,92,94,5,7,0,0,93,
        54,1,0,0,0,93,64,1,0,0,0,93,72,1,0,0,0,93,76,1,0,0,0,93,80,1,0,0,
        0,93,84,1,0,0,0,93,89,1,0,0,0,94,9,1,0,0,0,5,26,29,36,52,93
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'L'", "'{'", "'}'", "'->'", "'X'", "'('", 
                     "')'", "'+'", "'-'", "'*'", "'/'", "'integrate'", "'dt'", 
                     "'from'", "'0'", "'to'", "'infinity'", "'e'", "'^'", 
                     "'u'", "'cos'", "'cosh'", "'log'", "'Gamma'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VARIABLE", "NUMBER", "FUNCTION", "WS" ]

    RULE_laplaceTransform = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_function = 4

    ruleNames =  [ "laplaceTransform", "expression", "term", "factor", "function" ]

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
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    VARIABLE=25
    NUMBER=26
    FUNCTION=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LaplaceTransformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LaplaceParser.ExpressionContext,0)


        def VARIABLE(self):
            return self.getToken(LaplaceParser.VARIABLE, 0)

        def getRuleIndex(self):
            return LaplaceParser.RULE_laplaceTransform

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




    def laplaceTransform(self):

        localctx = LaplaceParser.LaplaceTransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_laplaceTransform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(LaplaceParser.T__0)
            self.state = 11
            self.match(LaplaceParser.T__1)
            self.state = 12
            self.expression()
            self.state = 13
            self.match(LaplaceParser.T__2)
            self.state = 14
            self.match(LaplaceParser.T__3)
            self.state = 15
            self.match(LaplaceParser.T__4)
            self.state = 16
            self.match(LaplaceParser.T__5)
            self.state = 17
            self.match(LaplaceParser.VARIABLE)
            self.state = 18
            self.match(LaplaceParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.TermContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.TermContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = LaplaceParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 18, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.function()
                pass
            elif token in [6, 9, 25, 26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.term()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8 or _la==9:
                    self.state = 22
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 23
                    self.term()
                    self.state = 28
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.FactorContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.FactorContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LaplaceParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.factor()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.factor()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LaplaceParser.FUNCTION, 0)

        def expression(self):
            return self.getTypedRuleContext(LaplaceParser.ExpressionContext,0)


        def VARIABLE(self):
            return self.getToken(LaplaceParser.VARIABLE, 0)

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def factor(self):
            return self.getTypedRuleContext(LaplaceParser.FactorContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = LaplaceParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(LaplaceParser.FUNCTION)
                self.state = 40
                self.match(LaplaceParser.T__5)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(LaplaceParser.T__6)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(LaplaceParser.VARIABLE)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(LaplaceParser.NUMBER)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(LaplaceParser.T__8)
                self.state = 47
                self.factor()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(LaplaceParser.T__5)
                self.state = 49
                self.expression()
                self.state = 50
                self.match(LaplaceParser.T__6)
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

        def expression(self):
            return self.getTypedRuleContext(LaplaceParser.ExpressionContext,0)


        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceParser.VARIABLE)
            else:
                return self.getToken(LaplaceParser.VARIABLE, i)

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
        self.enterRule(localctx, 8, self.RULE_function)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(LaplaceParser.T__11)
                self.state = 55
                self.match(LaplaceParser.T__5)
                self.state = 56
                self.expression()
                self.state = 57
                self.match(LaplaceParser.T__6)
                self.state = 58
                self.match(LaplaceParser.T__12)
                self.state = 59
                self.match(LaplaceParser.T__13)
                self.state = 60
                self.match(LaplaceParser.T__14)
                self.state = 61
                self.match(LaplaceParser.T__15)
                self.state = 62
                self.match(LaplaceParser.T__16)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(LaplaceParser.T__17)
                self.state = 65
                self.match(LaplaceParser.T__18)
                self.state = 66
                self.match(LaplaceParser.T__5)
                self.state = 67
                self.match(LaplaceParser.T__8)
                self.state = 68
                self.match(LaplaceParser.VARIABLE)
                self.state = 69
                self.match(LaplaceParser.T__9)
                self.state = 70
                self.match(LaplaceParser.VARIABLE)
                self.state = 71
                self.match(LaplaceParser.T__6)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(LaplaceParser.T__19)
                self.state = 73
                self.match(LaplaceParser.T__5)
                self.state = 74
                self.match(LaplaceParser.VARIABLE)
                self.state = 75
                self.match(LaplaceParser.T__6)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(LaplaceParser.T__20)
                self.state = 77
                self.match(LaplaceParser.T__5)
                self.state = 78
                self.match(LaplaceParser.VARIABLE)
                self.state = 79
                self.match(LaplaceParser.T__6)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(LaplaceParser.T__21)
                self.state = 81
                self.match(LaplaceParser.T__5)
                self.state = 82
                self.match(LaplaceParser.VARIABLE)
                self.state = 83
                self.match(LaplaceParser.T__6)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.match(LaplaceParser.T__22)
                self.state = 85
                self.match(LaplaceParser.T__5)
                self.state = 86
                self.expression()
                self.state = 87
                self.match(LaplaceParser.T__6)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.match(LaplaceParser.T__23)
                self.state = 90
                self.match(LaplaceParser.T__5)
                self.state = 91
                self.match(LaplaceParser.VARIABLE)
                self.state = 92
                self.match(LaplaceParser.T__6)
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





