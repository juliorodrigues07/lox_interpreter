from token_type import *
from token import Token


class Scanner:

    def __init__(self, source, tokens: Token):
        self.start = 0
        self.current = 0
        self.line = 1
        self.source = source
        self.tokens = tokens

    def scan_tokens(self):

        while self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.__init__(TokenType.EOF, '', None, self.line)
        return self.tokens

    def scan_token(self):

        c = self.advance()

        if c == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == '{':
            self.add_token(TokenType.LEFT_BRACE)
        elif c == '}':
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == ',':
            self.add_token(TokenType.COMMA)
        elif c == '.':
            self.add_token(TokenType.DOT)
        elif c == '-':
            self.add_token(TokenType.MINUS)
        elif c == '+':
            self.add_token(TokenType.PLUS)
        elif c == ';':
            self.add_token(TokenType.SEMICOLON)
        elif c == '*':
            self.add_token(TokenType.STAR)
        else:
            print(str(self.line) + 'Unexpected character!' + str(c))

    def is_at_end(self):

        if self.current >= len(self.source):
            return False

    def advance(self):

        self.current += 1
        return self.source[self.current + 1:]

    def add_token(self, token_type: TokenType):
        self.add_token(token_type, None)

    def add_token(self, token_type: TokenType, literal):

        text = self.source[self.start : self.current]
        self.tokens.__init__(TokenType.EOF, text, literal, self.line)
