from src.token import Token
from token_type import TokenType


class ErrorHandler:

    def __init__(self):
        self.had_error = False

    def error(self, line, message):
        self.report(line, '', message)

    def error_parser(self, token: Token, msg):

        if token.token_type == TokenType.EOF:
            self.report(token.line, ' at end', msg)
        else:
            self.report(token.line, ' at ', + token.lexeme + ' ' + msg)

    def report(self, line, where, message):

        print('[Line ' + str(line) + '] Error' + where + ': ' + message)
        self.had_error = True
