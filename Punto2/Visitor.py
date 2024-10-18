from ColeccionesParser import ColeccionesParser
from ColeccionesVisitor import ColeccionesVisitor

class Visitor(ColeccionesVisitor):
    def visitMapFunction(self, ctx: ColeccionesParser.MapFunctionContext):
        function_name = ctx.functionCall().getText() 
        iterable = self.visit(ctx.iterableObject())  

        results = [self.apply_function(function_name, item) for item in iterable]
        print(f"MAP({function_name}, {iterable}) --> {results}")
        return results

    def visitFilterFunction(self, ctx: ColeccionesParser.FilterFunctionContext):
        function_name = ctx.functionCall().getText()
        iterable = self.visit(ctx.iterableObject())
        
        if ctx.INT() is not None:
            comparison_number = int(ctx.INT().getText())
            results = [item for item in iterable if self.apply_filter(function_name, item, comparison_number)]
        else:
            results = [item for item in iterable if self.apply_function(function_name, item)]
        
        print(f"FILTER({function_name}, {iterable}) --> {results}")
        return results

    def visitList(self, ctx: ColeccionesParser.ListContext):
        return [self.visit(expr) for expr in ctx.expressionList().expression()]

    def visitTuple(self, ctx: ColeccionesParser.TupleContext):
        return tuple(self.visit(expr) for expr in ctx.expressionList().expression())

    def visitExpression(self, ctx: ColeccionesParser.ExpressionContext):
        if ctx.INT() is not None:
            return int(ctx.INT().getText())
        return ctx.ID().getText()

    def apply_function(self, function_name, value):
        """Aplica la función indicada a un valor."""
        if function_name == 'square':
            return value * value
        elif function_name == 'increment':
            return value + 1
        elif function_name == 'double':
            return 2 * value
        else:
            raise Exception(f"Function '{function_name}' not implemented.")

    def apply_filter(self, function_name, item, *args):
        if function_name == "is_greater_than":
            return item > args[0]
        elif function_name == "is_less_than":
            return item < args[0]
        elif function_name == "is_multiple_of":
            return item % args[0] == 0
        elif function_name == "is_divisible_by":
            return args[0] % item == 0
        elif function_name == "greater_than_length":
            return len(item) > args[0]
        else:
            raise Exception(f"Function '{function_name}' not implemented.")

          
