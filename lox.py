import sys


class Main:

    def __init__(self):
        self.had_error = False

    def open_file(self, file_name):
        print(True)

    def run_prompt(self):

        while True:

            print('>>> ', end='')
            line = input()
            self.run_code(line)

            if not line:
                break

    def run_code(self, line):
        print(True)

    def run_lox(self):

        if len(sys.argv) > 2:
            print('Error!')
        elif len(sys.argv) == 2:
            self.open_file(sys.argv[1])
        else:
            self.run_prompt()


if __name__ == '__main__':
    Main().run_lox()
