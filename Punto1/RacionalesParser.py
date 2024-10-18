# Generated from Racionales.g4 by ANTLR 4.13.2
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
        4,1,8,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,46,8,3,1,4,1,4,1,4,1,4,1,4,0,1,2,5,0,2,4,6,8,0,0,52,0,
        10,1,0,0,0,2,13,1,0,0,0,4,36,1,0,0,0,6,45,1,0,0,0,8,47,1,0,0,0,10,
        11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,6,1,-1,0,14,15,3,4,2,
        0,15,24,1,0,0,0,16,17,10,3,0,0,17,18,5,1,0,0,18,23,3,4,2,0,19,20,
        10,2,0,0,20,21,5,2,0,0,21,23,3,4,2,0,22,16,1,0,0,0,22,19,1,0,0,0,
        23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,24,1,0,
        0,0,27,28,3,6,3,0,28,29,5,3,0,0,29,30,3,6,3,0,30,37,1,0,0,0,31,32,
        3,6,3,0,32,33,5,4,0,0,33,34,3,6,3,0,34,37,1,0,0,0,35,37,3,6,3,0,
        36,27,1,0,0,0,36,31,1,0,0,0,36,35,1,0,0,0,37,5,1,0,0,0,38,39,5,5,
        0,0,39,40,3,2,1,0,40,41,5,6,0,0,41,46,1,0,0,0,42,46,3,8,4,0,43,44,
        5,2,0,0,44,46,3,8,4,0,45,38,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,
        46,7,1,0,0,0,47,48,5,7,0,0,48,49,5,4,0,0,49,50,5,7,0,0,50,9,1,0,
        0,0,4,22,24,36,45
    ]

class RacionalesParser ( Parser ):

    grammarFileName = "Racionales.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_fraccion = 4

    ruleNames =  [ "prog", "expr", "term", "factor", "fraccion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(RacionalesParser.ExprContext,0)


        def EOF(self):
            return self.getToken(RacionalesParser.EOF, 0)

        def getRuleIndex(self):
            return RacionalesParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RacionalesParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(RacionalesParser.EOF)
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
            return RacionalesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RacionalesParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTerm" ):
                listener.enterSingleTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTerm" ):
                listener.exitSingleTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTerm" ):
                return visitor.visitSingleTerm(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RacionalesParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(RacionalesParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RacionalesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RacionalesParser.SingleTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = RacionalesParser.AddSubContext(self, RacionalesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 17
                        self.match(RacionalesParser.T__0)
                        self.state = 18
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = RacionalesParser.AddSubContext(self, RacionalesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 20
                        self.match(RacionalesParser.T__1)
                        self.state = 21
                        self.term()
                        pass

             
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RacionalesParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RacionalesParser.FactorContext)
            else:
                return self.getTypedRuleContext(RacionalesParser.FactorContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class SingleFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(RacionalesParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleFactor" ):
                listener.enterSingleFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleFactor" ):
                listener.exitSingleFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleFactor" ):
                return visitor.visitSingleFactor(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = RacionalesParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = RacionalesParser.MulDivContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.factor()
                self.state = 28
                self.match(RacionalesParser.T__2)
                self.state = 29
                self.factor()
                pass

            elif la_ == 2:
                localctx = RacionalesParser.MulDivContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.factor()
                self.state = 32
                self.match(RacionalesParser.T__3)
                self.state = 33
                self.factor()
                pass

            elif la_ == 3:
                localctx = RacionalesParser.SingleFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.factor()
                pass


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


        def getRuleIndex(self):
            return RacionalesParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FractionFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fraccion(self):
            return self.getTypedRuleContext(RacionalesParser.FraccionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFractionFactor" ):
                listener.enterFractionFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFractionFactor" ):
                listener.exitFractionFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFractionFactor" ):
                return visitor.visitFractionFactor(self)
            else:
                return visitor.visitChildren(self)


    class NegativeFractionContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fraccion(self):
            return self.getTypedRuleContext(RacionalesParser.FraccionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativeFraction" ):
                listener.enterNegativeFraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativeFraction" ):
                listener.exitNegativeFraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegativeFraction" ):
                return visitor.visitNegativeFraction(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RacionalesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = RacionalesParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = RacionalesParser.ParensExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(RacionalesParser.T__4)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(RacionalesParser.T__5)
                pass
            elif token in [7]:
                localctx = RacionalesParser.FractionFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.fraccion()
                pass
            elif token in [2]:
                localctx = RacionalesParser.NegativeFractionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(RacionalesParser.T__1)
                self.state = 44
                self.fraccion()
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


    class FraccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RacionalesParser.RULE_fraccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FractionExprContext(FraccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RacionalesParser.FraccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(RacionalesParser.INT)
            else:
                return self.getToken(RacionalesParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFractionExpr" ):
                listener.enterFractionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFractionExpr" ):
                listener.exitFractionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFractionExpr" ):
                return visitor.visitFractionExpr(self)
            else:
                return visitor.visitChildren(self)



    def fraccion(self):

        localctx = RacionalesParser.FraccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fraccion)
        try:
            localctx = RacionalesParser.FractionExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(RacionalesParser.INT)
            self.state = 48
            self.match(RacionalesParser.T__3)
            self.state = 49
            self.match(RacionalesParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




