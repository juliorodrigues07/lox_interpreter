from token_type import *
from Expr import *
from visitor import Visitor


class Interpreter(Expr, Visitor):

    @staticmethod
    def is_truthy(expr):

        if expr is None:
            return False
        elif type(expr) is bool:
            return expr

        return True

    @staticmethod
    def is_equal(left, right):

        if left is None and right is None:
            return True
        if left is None:
            return False

        return left == right

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def visit_Literal_expr(self, expr: Literal):
        return expr.value

    def visit_Grouping_expr(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def visit_Unary_expr(self, expr: Unary):

        right = self.evaluate(expr.right)

        if expr.operator.token_type == TokenType.MINUS:
            return -float(right)
        if expr.operator.token_type == TokenType.BANG:
            return not self.is_truthy(right)
        else:
            return None

    def visit_Binary_expr(self, expr: Binary):

        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.token_type == TokenType.MINUS:
            return float(left) - float(right)
        elif expr.operator.token_type == TokenType.SLASH:
            return float(left) / float(right)
        elif expr.operator.token_type == TokenType.STAR:
            return float(left) * float(right)
        elif expr.operator.token_type == TokenType.PLUS:
            if type(left) is float and type(right) is float:
                return float(left) + float(right)
            if type(left) is str and type(right) is str:
                return str(left) + str(right)
        elif expr.operator.token_type == TokenType.GREATER:
            return float(left) > float(right)
        elif expr.operator.token_type == TokenType.GREATER_EQUAL:
            return float(left) >= float(right)
        elif expr.operator.token_type == TokenType.LESS:
            return float(left) < float(right)
        elif expr.operator.token_type == TokenType.LESS_EQUAL:
            return float(left) <= float(right)
        elif expr.operator.token_type == TokenType.BANG_EQUAL:
            return not self.is_equal(left, right)
        elif expr.operator.token_type == TokenType.EQUAL_EQUAL:
            return self.is_equal(left, right)

        return None

    def visit_Conditional_expr(self, expr: Conditional):
        pass
