from visitor import Visitor
from token_type import TokenType
from runtime_error import Run_time_Error

class Interpreter(Visitor):
    def __init__(self, lox):
        self.lox = lox
        self.locals = {}

    def interpret(self, expression):
        try:
            value = self.evaluate(expression)
            print(self.stringify(value))
        except Run_time_Error as error:
            self.lox.runtime_error(error)

    def stringify(self, obj):
        if obj == None:
            return 'nil'
        if isinstance(obj, bool):
            if obj:
                return 'true'
            return 'false'
        return str(obj)

    def visit_Literal_expr(self, expr):
        return expr.value

    def visit_Grouping_expr(self, expr):
        return self.evaluate(expr.expression)

    def visit_Unary_expr(self, expr):
        right = self.evaluate(expr.right)
        if expr.operator.tokentype == TokenType.MINUS:
            self.check_number_operand(expr.operator, right)
            return -float(right)
        elif expr.operator.tokentype == TokenType.BANG:
            return not self.istruthy(right)
        return None

    def evaluate(self, expr):
        return expr.accept(self)

    def istruthy(self, object):
        if object is None:
            return False
        elif isinstance(object, bool):
            return object
        return True

    def visit_Binary_expr(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator.token_type == TokenType.MINUS:
            self.check_number_operand(left, right)
            return left - right
        elif expr.operator.token_type == TokenType.STAR:
            self.check_number_operand(left, right)
            return left * right
        elif expr.operator.token_type == TokenType.SLASH:
            self.check_number_operand(left, right)
            return left / right
        elif expr.operator.token_type == TokenType.PLUS:
            self.check_number_operand(left, right)
            print(type(left))
            if type(left) == str and type(right) == str:
                return left + right
            elif type(left) == float and type(right) == float:
                return left + right
        elif expr.operator.token_type == TokenType.GREATER:
            self.check_number_operand(left, right)
            return left > right
        elif expr.operator.token_type == TokenType.GREATER_EQUAL:
            self.check_number_operand(left, right)
            return left >= right
        elif expr.operator.token_type == TokenType.LESS:
            self.check_number_operand(left, right)
            return left < right
        elif expr.operator.token_type == TokenType.LESS_EQUAL:
            self.check_number_operand(left, right)
            return left <= right
        elif expr.operator.token_type == TokenType.BANG_EQUAL:
            self.check_number_operand(left, right)
            return self.isEqual(True, left, right)
        elif expr.operator.token_type == TokenType.EQUAL_EQUAL:
            self.check_number_operand(left, right)
            return self.isEqual(False, left, right)
        return None

    def isEqual(self,flag, left, right):
        pass
    def check_number_operand(self, operand,  *numbers):
        for num in numbers:
            if not isinstance(num, float):
                raise Run_time_Error(operand, 'Operand must be a number.')
