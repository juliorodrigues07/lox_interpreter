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
        elif c == '!':
            if self.match('='):
                self.add_token(TokenType.BANG_EQUAL)
            else:
                self.add_token(TokenType.BANG)
        elif c == '=':
            if self.match('='):
                self.add_token(TokenType.EQUAL_EQUAL)
            else:
                self.add_token(TokenType.EQUAL)
        elif c == '<':
            if self.match('='):
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)
        elif c == '>':
            if self.match('='):
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)
        elif c == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif c == ' ' or c == '\r' or c == '\t':
            pass
        elif c == '\n':
            self.line += 1
        elif c == '"':
            self.string()
        else:
            if self.is_digit(c):
                self.number()
            else:
                print(str(self.line) + 'Unexpected character!' + str(c))

    def is_at_end(self):

        if self.current >= len(self.source):
            return False

    def advance(self):

        self.current += 1
        return self.source[self.current + 1:]

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
            print(str(self.line) + 'Unexpected character!' + self.peek())
            return

        self.advance()
        string_value = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, string_value)

    @static
    def is_digit(self, c):

        return '0' <= c <= '9'

    def number(self):

        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()

            while self.is_digit(self.peek()):
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.source[self.start, self.current]))

    def peek_next(self):

        if self.current + 1 >= len(self.source):
            return '\0'

        return self.source[self.current + 1]

    def add_token(self, token_type: TokenType):
        self.add_token(token_type, None)

    def add_token(self, token_type: TokenType, literal):

        text = self.source[self.start : self.current]
        self.tokens.__init__(TokenType.EOF, text, literal, self.line)
