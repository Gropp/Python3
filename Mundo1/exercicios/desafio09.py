##########################################################
# Desafios 9 - Utilizando operadores - tabuada
##########################################################
def main():
    form = {'limpa': '\033[m',
            'bold': '\033[1m',
            'underline': '\033[4m',
            'invert': '\033[7m',
            'vermelho': '\033[31m',
            'vermbold': '\033[1;31m',
            'vermunder': '\033[4;31m',
            'vermbco': '\033[31;30m',
            'verde': '\033[32m',
            'verdebold': '\033[1;32m',
            'amarelo': '\033[33m',
            'amabold': '\033[1;33m',
            'azul': '\033[34m',
            'azulbold': '\033[1;34m',
            'roxo': '\033[35m',
            'roxobold': '\033[1;35m',
            'ciano': '\033[36m',
            'cibold': '\033[1;36m'}

    fator = int(input('\033[37m Digite um fator para tabuada: \033[m'))
    c = 1
    print('\n')
    while c <= 10:
        print(' {}{:2} x {:<2} = {:2} {}'.format(form['invert'], fator, c, fator * c, form['limpa']))
        c = c + 1
    print(form['cibold'], '-' * 13, form['limpa'])


main()
