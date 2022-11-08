from src.visitor import Visitor
from src.token_type import TokenType


class Interpreter(Visitor):
    def __init__(self, lox):
        self.lox = lox
        self.locals = {}

    def visit_Literal_expr(self, expr):
        return expr.value

    def visit_Grouping_expr(self, expr):
        return self.evaluate(expr.expression)

    def visit_Unary_expr(self, expr):
        right = self.evaluate(expr.right)
        if expr.operator.tokentype == TokenType.MINUS:
            return -float(right)
        elif expr.operator.tokentype == TokenType.BANG:
            return not self.istruthy(right)
        return None

    def evaluate(self, expr):
        return self.visit(expr)

    def istruthy(self, object):
        if object is None:
            return False
        elif isinstance(object, bool):
            return object
        return True

    def visit_Binary_expr(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.tokentype == TokenType.MINUS:
            return left - right
        elif expr.operator.tokentype == TokenType.STAR:
            return left * right
        elif expr.operator.tokentype == TokenType.SLASH:
            return left / right
        elif expr.operator.tokentype == TokenType.PLUS:
            if type(left) == str and type(right) == str:
                return left + right
            elif type(left) == int and type(right) == int:
                return left + right
        elif expr.operator.tokentype == TokenType.GREATER:
            return left > right
        elif expr.operator.tokentype == TokenType.GREATER_EQUAL:
            return left >= right
        elif expr.operator.tokentype == TokenType.LESS:
            return left < right
        elif expr.operator.tokentype == TokenType.LESS_EQUAL:
            return left <= right
        elif expr.operator.tokentype == TokenType.BANG_EQUAL:
            return self.isEqual(True, left, right)
        elif expr.operator.tokentype == TokenType.EQUAL_EQUAL:
            return self.isEqual(False, left, right)
        return None

    def isEqual(self,flag, left, right):
        pass
