class Expr:
	pass


class Binary(Expr):
	def __init__(self, left, operator, right, ):
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return visitor.visit_BinaryExpr(self)


class Grouping(Expr):
	def __init__(self, expression, ):
		self.expression = expression

	def accept(self, visitor):
		return visitor.visit_GroupingExpr(self)


class Literal(Expr):
	def __init__(self, value, ):
		self.value = value

	def accept(self, visitor):
		return visitor.visit_LiteralExpr(self)


class Unary(Expr):
	def __init__(self, operator, right, ):
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return visitor.visit_UnaryExpr(self)



