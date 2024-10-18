# Generated from Colecciones.g4 by ANTLR 4.13.2
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
        4,1,12,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,3,1,3,1,4,1,4,1,5,1,5,3,
        5,59,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,3,8,70,8,8,1,8,1,8,
        3,8,74,8,8,1,8,1,8,3,8,78,8,8,1,8,1,8,3,8,82,8,8,5,8,84,8,8,10,8,
        12,8,87,9,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,
        10,11,89,0,23,1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,43,1,0,0,0,8,54,
        1,0,0,0,10,58,1,0,0,0,12,60,1,0,0,0,14,64,1,0,0,0,16,69,1,0,0,0,
        18,88,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,
        0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,
        1,1,0,0,0,28,29,3,4,2,0,29,30,5,1,0,0,30,35,1,0,0,0,31,32,3,6,3,
        0,32,33,5,1,0,0,33,35,1,0,0,0,34,28,1,0,0,0,34,31,1,0,0,0,35,3,1,
        0,0,0,36,37,5,2,0,0,37,38,5,3,0,0,38,39,3,8,4,0,39,40,5,4,0,0,40,
        41,3,10,5,0,41,42,5,5,0,0,42,5,1,0,0,0,43,44,5,6,0,0,44,45,5,3,0,
        0,45,46,3,8,4,0,46,47,5,4,0,0,47,50,3,10,5,0,48,49,5,4,0,0,49,51,
        5,11,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,5,5,0,0,
        53,7,1,0,0,0,54,55,5,10,0,0,55,9,1,0,0,0,56,59,3,12,6,0,57,59,3,
        14,7,0,58,56,1,0,0,0,58,57,1,0,0,0,59,11,1,0,0,0,60,61,5,7,0,0,61,
        62,3,16,8,0,62,63,5,8,0,0,63,13,1,0,0,0,64,65,5,3,0,0,65,66,3,16,
        8,0,66,67,5,5,0,0,67,15,1,0,0,0,68,70,5,9,0,0,69,68,1,0,0,0,69,70,
        1,0,0,0,70,71,1,0,0,0,71,73,3,18,9,0,72,74,5,9,0,0,73,72,1,0,0,0,
        73,74,1,0,0,0,74,85,1,0,0,0,75,77,5,4,0,0,76,78,5,9,0,0,77,76,1,
        0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,81,3,18,9,0,80,82,5,9,0,0,81,
        80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,75,1,0,0,0,84,87,1,0,0,
        0,85,83,1,0,0,0,85,86,1,0,0,0,86,17,1,0,0,0,87,85,1,0,0,0,88,89,
        7,0,0,0,89,19,1,0,0,0,9,23,34,50,58,69,73,77,81,85
    ]

class ColeccionesParser ( Parser ):

    grammarFileName = "Colecciones.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'MAP'", "'('", "','", "')'", "'FILTER'", 
                     "'['", "']'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_mapFunction = 2
    RULE_filterFunction = 3
    RULE_functionCall = 4
    RULE_iterableObject = 5
    RULE_list = 6
    RULE_tuple = 7
    RULE_expressionList = 8
    RULE_expression = 9

    ruleNames =  [ "program", "statement", "mapFunction", "filterFunction", 
                   "functionCall", "iterableObject", "list", "tuple", "expressionList", 
                   "expression" ]

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
    ID=10
    INT=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ColeccionesParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ColeccionesParser.StatementContext)
            else:
                return self.getTypedRuleContext(ColeccionesParser.StatementContext,i)


        def getRuleIndex(self):
            return ColeccionesParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ColeccionesParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==6:
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(ColeccionesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapFunction(self):
            return self.getTypedRuleContext(ColeccionesParser.MapFunctionContext,0)


        def filterFunction(self):
            return self.getTypedRuleContext(ColeccionesParser.FilterFunctionContext,0)


        def getRuleIndex(self):
            return ColeccionesParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ColeccionesParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.mapFunction()
                self.state = 29
                self.match(ColeccionesParser.T__0)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.filterFunction()
                self.state = 32
                self.match(ColeccionesParser.T__0)
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


    class MapFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(ColeccionesParser.FunctionCallContext,0)


        def iterableObject(self):
            return self.getTypedRuleContext(ColeccionesParser.IterableObjectContext,0)


        def getRuleIndex(self):
            return ColeccionesParser.RULE_mapFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunction" ):
                listener.enterMapFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunction" ):
                listener.exitMapFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapFunction" ):
                return visitor.visitMapFunction(self)
            else:
                return visitor.visitChildren(self)




    def mapFunction(self):

        localctx = ColeccionesParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ColeccionesParser.T__1)
            self.state = 37
            self.match(ColeccionesParser.T__2)
            self.state = 38
            self.functionCall()
            self.state = 39
            self.match(ColeccionesParser.T__3)
            self.state = 40
            self.iterableObject()
            self.state = 41
            self.match(ColeccionesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(ColeccionesParser.FunctionCallContext,0)


        def iterableObject(self):
            return self.getTypedRuleContext(ColeccionesParser.IterableObjectContext,0)


        def INT(self):
            return self.getToken(ColeccionesParser.INT, 0)

        def getRuleIndex(self):
            return ColeccionesParser.RULE_filterFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterFunction" ):
                listener.enterFilterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterFunction" ):
                listener.exitFilterFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterFunction" ):
                return visitor.visitFilterFunction(self)
            else:
                return visitor.visitChildren(self)




    def filterFunction(self):

        localctx = ColeccionesParser.FilterFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ColeccionesParser.T__5)
            self.state = 44
            self.match(ColeccionesParser.T__2)
            self.state = 45
            self.functionCall()
            self.state = 46
            self.match(ColeccionesParser.T__3)
            self.state = 47
            self.iterableObject()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 48
                self.match(ColeccionesParser.T__3)
                self.state = 49
                self.match(ColeccionesParser.INT)


            self.state = 52
            self.match(ColeccionesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ColeccionesParser.ID, 0)

        def getRuleIndex(self):
            return ColeccionesParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ColeccionesParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ColeccionesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(ColeccionesParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(ColeccionesParser.TupleContext,0)


        def getRuleIndex(self):
            return ColeccionesParser.RULE_iterableObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterableObject" ):
                listener.enterIterableObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterableObject" ):
                listener.exitIterableObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterableObject" ):
                return visitor.visitIterableObject(self)
            else:
                return visitor.visitChildren(self)




    def iterableObject(self):

        localctx = ColeccionesParser.IterableObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iterableObject)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.list_()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.tuple_()
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(ColeccionesParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ColeccionesParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = ColeccionesParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ColeccionesParser.T__6)
            self.state = 61
            self.expressionList()
            self.state = 62
            self.match(ColeccionesParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(ColeccionesParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ColeccionesParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = ColeccionesParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tuple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ColeccionesParser.T__2)
            self.state = 65
            self.expressionList()
            self.state = 66
            self.match(ColeccionesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ColeccionesParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ColeccionesParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ColeccionesParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = ColeccionesParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 68
                self.match(ColeccionesParser.T__8)


            self.state = 71
            self.expression()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 72
                self.match(ColeccionesParser.T__8)


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 75
                self.match(ColeccionesParser.T__3)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 76
                    self.match(ColeccionesParser.T__8)


                self.state = 79
                self.expression()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 80
                    self.match(ColeccionesParser.T__8)


                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def INT(self):
            return self.getToken(ColeccionesParser.INT, 0)

        def ID(self):
            return self.getToken(ColeccionesParser.ID, 0)

        def getRuleIndex(self):
            return ColeccionesParser.RULE_expression

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

        localctx = ColeccionesParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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





