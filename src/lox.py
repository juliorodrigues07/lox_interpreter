from error_handler import ErrorHandler
from astPrinter import ASTPrinter
from scanner import Scanner
from parser import Parser
import sys


class Main:

    def __init__(self):
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

        parser = Parser(tokens, self.error_handler)
        expression = parser.parse()

        if self.error_handler.had_error:
            return

        print(ASTPrinter().pprint_ast(expression))

    def run_lox(self):

        if len(sys.argv) > 2:
            print('Usage: lox.py [file_name]')
            sys.exit(64)
        elif len(sys.argv) == 2:
            self.run_file(sys.argv[1])
        else:
            self.run_prompt()


if __name__ == '__main__':
    Main().run_lox()
