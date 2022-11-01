from abc import ABC
from abc import abstractmethod


class Visitor(ABC):

    @abstractmethod
    def visit_binary_expr(self, expr):
        pass

    @abstractmethod
    def visit_unary_expr(self, expr):
        pass

    @abstractmethod
    def visit_grouping_expr(self, expr):
        pass

    @abstractmethod
    def visit_literal_expr(self, expr):
        pass
