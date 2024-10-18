from fractions import Fraction
from RacionalesParser import RacionalesParser
from RacionalesVisitor import RacionalesVisitor

class Visitor(RacionalesVisitor):

    def visitAddSub(self, ctx: RacionalesParser.AddSubContext):
        
        left = self.visit(ctx.getChild(0))  
        right = self.visit(ctx.getChild(2))        

        if ctx.getChild(1).getText() == '+':
            resultado = left + right
            return print(f"Resultado: {resultado}\n")
        else:
            resultado = left - right
            return print(f"Resultado: {resultado}\n")  


    def visitMulDiv(self, ctx: RacionalesParser.MulDivContext):
        left = self.visit(ctx.getChild(0)) 
        right = self.visit(ctx.getChild(2)) 

        if ctx.getChild(1).getText() == '*':
            resultado = left * right
            return print(f"Resultado: {resultado}\n")
        else:
            resultado = left / right 
            return print(f"Resultado: {resultado}\n")

    def visitFactor(self, ctx: RacionalesParser.FactorContext):
        if ctx.fraccion():
            return self.visit(ctx.fraccion())  
        return self.visit(ctx.expr())  

    def visitFractionExpr(self, ctx: RacionalesParser.FraccionContext):
        num = int(ctx.INT(0).getText())
        denom = int(ctx.INT(1).getText())  
        fraccion = Fraction(num, denom)                      
        return fraccion 
    
    def visitNegativeFraction(self, ctx: RacionalesParser.NegativeFractionContext):
        print("Entrando a visitNegativeFraction")
        num = int(ctx.fraccion().INT(0).getText())
        denom = int(ctx.fraccion().INT(1).getText())
        return Fraction(-num, denom) 
    
