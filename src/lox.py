from error_handler import ErrorHandler
from scanner import Scanner
import sys
from parser import Parser
from astPrinter import ASTPrinter
from src.token_type import TokenType


class Main:

    def __init__(self):
        self.haderror = None
        self.error_handler = ErrorHandler()

    def run_file(self, file_name):

        with open(file_name, 'r') as file:
            file_string = file.read()

        self.run_code(file_string)

        if self.error_handler.had_error:
            sys.exit(65)

    def run_prompt(self):

        while True:

            print('>>> ', end='')
            line = input()

            if not line:
                break

            self.run_code(line)
            self.error_handler.had_error = False

    def run_code(self, source):

        scanner = Scanner(self.error_handler, source)
        tokens = scanner.scan_tokens()

        if self.error_handler.had_error:
            return

    def run_lox(self):

        if len(sys.argv) > 2:
            print('Usage: lox.py [file_name]')
            sys.exit(64)
        elif len(sys.argv) == 2:
            self.run_file(sys.argv[1])
        else:
            self.run_prompt()

    def report(self, line, where, message):
        print(f"Linha{line}: Error: {where} : {message}")
        self.haderror = True

    def error(self, token, message):
        if token.tokentype == TokenType.EOF:
            self.report(token.line, " at end", message)
        else:
            self.report(token.line, " at '" + token.lexeme + "'", message)

    def run(self, source):
        tokens = Scanner.scan_tokens(source)
        parser = Parser(tokens)
        expression = parser.parse()
        if self.haderror:
            return
        print(ASTPrinter.pprint_ast(expression))


if __name__ == '__main__':
    Main().run_lox()
