#########################################################
# Desafio 2 - print e input
#########################################################
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
            'azul': '\033[34m',
            'azulbold': '\033[1;34m'}

    dia = input('Qual o dia que você nasceu? ')
    mes = input('Qual o mês que você nasceu? ')
    ano = input('Qual o ano que você nasceu? ')
    print('Você nasceu no dia ', dia, ' de ', mes, ' de ', ano, '.', ' correto?')
    print('Você nasceu no dia {}{}{} de {}{}{} de {}{}{}'.format(form['vermbold'], dia, form['limpa'],
                                                                 form['verdebold'], mes, form['limpa'],
                                                                 form['azulbold'], ano, form['limpa']))


main()
