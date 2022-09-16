
class ErrorHandler:

    def __init__(self):
        self.had_error = False

    def error(self, line, message):

        self.report(line, '', message)

    def report(self, line, where, message):

        print('[Line ' + str(line) + '] Error' + where + ': ' + message)
        self.had_error = True
