class Visitor:
    def visit(self, expr_or_stmt):
        return expr_or_stmt.accept(self)

    def visit_AssignExpr(self, expr_or_stmt):
        return expr_or_stmt.accept(self)

    def visit_BinaryExpr(self, expr_or_stmt):
        return expr_or_stmt.accept(self)

    def visit_GroupingExpr(self, expr_or_stmt):
        return expr_or_stmt.accept(self)

    def visit_LiteralExpr(self, expr_or_stmt):
        return expr_or_stmt.accept(self)