import sys
import os

os.chdir('..')

class GenerateAST:
    def __init__(self):
        if len(sys.argv) != 1:
            print('Usage: python tool.GenerateAst')
            sys.exit(64)

    def defineType(self, arquivo, basename, classname, fieldlist):
        arquivo.writelines(u'class ' + classname + '(Expr):\n')
        arquivo.writelines(u'\tdef __init__' + '(self')
        for nome in fieldlist:
            separado = nome.split(' ')
            arquivo.writelines(', ' + separado[1])
        arquivo.writelines(u')' + ':\n')
        for nome in fieldlist:
            separado = nome.split(' ')
            arquivo.writelines(u'\t\tself.' + separado[1] + ' = ' + separado[1] + '\n')
        arquivo.writelines(u'\n')

        arquivo.writelines("\tdef accept(self, visitor):\n")
        arquivo.writelines(f'\t\treturn visitor.visit_{classname}Expr(self)\n\n\n')


    def defineVisitor(self, arquivo, basename, types):
        arquivo.writelines('class Expr:\n')
        arquivo.writelines("\tpass\n\n\n")

    def defineAst(self, outputdir, basename, types):
        path = outputdir + '/' + basename + '.py'
        arquivo = open(path, 'w')
        self.defineVisitor(arquivo, basename, types)
        for elem in types:
            self.defineType(arquivo, basename, elem, types[elem])
        arquivo.writelines('\n')
        arquivo.close()


if __name__ == '__main__':
    GenerateAST()

    a = {"Binary": ['Expr left', 'Token operator', 'Expr right'], "Grouping": ['Expr expression'],
         "Literal": ["object value"],
         "Unary": ['Token operator', 'Expr right']}
    b = str(os.getcwd() + '/src')

    GenerateAST().defineAst(b, 'Expr', a)
