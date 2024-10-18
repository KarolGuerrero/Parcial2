from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser
from LaplaceVisitor import LaplaceVisitor

class Visitor(LaplaceVisitor):

    def visitStart(self, ctx:LaplaceParser.StartContext):
        return self.visit(ctx.expr())

    def visitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        function = ctx.function().getText()

        if 'e^' in function:
            return "Transformada de Laplace de e^(-a*t) es 1 / (s + a)"
        elif 'u(t)' in function:
            return "Transformada de Laplace de u(t) es 1 / s"
        elif 'u(t-' in function:
            return "Transformada de Laplace de u(t-r) es e^(-r*s) / s"
        elif 'δ(t)' in function:
            return "Transformada de Laplace de δ(t) es 1"
        elif 'δ(t-' in function:
            return "Transformada de Laplace de δ(t-r) es e^(-r*s)"
        elif '^' in function:
            if 't^' in function:
                parts = function.split('^')
                exponent = parts[1].strip()  # Parte después de '^'
                if exponent == 'q':
                    return "Transformada de Laplace de t^q es Γ(q+1) / s^{q+1}"
                else:
                    n = int(exponent)
                    return f"Transformada de Laplace de t^{n} es {n}! / s^{n+1}"
        elif 'sin' in function:
            return "Transformada de Laplace de sin(ωt) es ω / (s^2 + ω^2)"
        elif 'cos' in function:
            return "Transformada de Laplace de cos(ωt) es s / (s^2 + ω^2)"
        elif 'sinh' in function:
            return "Transformada de Laplace de sinh(at) es a / (s^2 - a^2)"
        elif 'cosh' in function:
            return "Transformada de Laplace de cosh(at) es s / (s^2 - a^2)"
        elif 'log' in function:
            return "Transformada de Laplace de log(t/t0) es -log(t0)/s - 1/s^2"
        elif 'Jn' in function:
            return "Transformada de Laplace de Jn(ωt) es ω^n / (s^2 + ω^2)^(n+1/2)"
        elif 'I' in function:
            return "Transformada de Laplace de la función de Bessel modificada"
        return None

    def visitBaseFunction(self, ctx:LaplaceParser.BaseFunctionContext):
        return self.visit(ctx.function())
