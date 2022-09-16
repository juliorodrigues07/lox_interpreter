from error_handler import ErrorHandler
from token_type import *
from token import Token


class Scanner:

    def __init__(self, error_handler: ErrorHandler, source):

        self.source = source
        self.error_handler = error_handler
        self.tokens = []

        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):

        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):

        char = self.advance()

        if char == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif char == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == '{':
            self.add_token(TokenType.LEFT_BRACE)
        elif char == '}':
            self.add_token(TokenType.RIGHT_BRACE)
        elif char == ',':
            self.add_token(TokenType.COMMA)
        elif char == '.':
            self.add_token(TokenType.DOT)
        elif char == '-':
            self.add_token(TokenType.MINUS)
        elif char == '+':
            self.add_token(TokenType.PLUS)
        elif char == ';':
            self.add_token(TokenType.SEMICOLON)
        elif char == '*':
            self.add_token(TokenType.STAR)
        elif char == '!':
            self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
        elif char == '=':
            self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
        elif char == '<':
            self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
        elif char == '>':
            self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
        elif char == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif char == ' ' or char == '\r' or char == '\t':
            pass
        elif char == '\n':
            self.line += 1
        elif char == '"':
            self.string()
        else:
            if self.is_digit(char):
                self.number()
            else:
                self.error_handler.error(self.line, 'Unexpected character.')

    def is_at_end(self):

        if self.current >= len(self.source):
            return True

    def advance(self):

        self.current += 1
        return self.source[self.current - 1]

    def match(self, expected):

        if self.is_at_end():
            return False

        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):

        if self.is_at_end():
            return '\0'

        return self.source[self.current]

    def string(self):

        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.is_at_end():
            self.error_handler.error(self.line, "Unterminated String.")
            return

        self.advance()
        string_value = self.source[self.start + 1: self.current - 1]
        self.add_token(TokenType.STRING, string_value)

    @staticmethod
    def is_digit(char):

        return '0' <= char <= '9'

    def number(self):

        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()

            while self.is_digit(self.peek()):
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.source[self.start: self.current]))

    def peek_next(self):

        if self.current + 1 >= len(self.source):
            return '\0'

        return self.source[self.current + 1]

    def add_token(self, token_type: TokenType, literal=None):

        text = self.source[self.start: self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))
