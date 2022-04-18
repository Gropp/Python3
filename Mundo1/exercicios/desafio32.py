##################################################
# Desafio 32 - Ano bissexto
##################################################
from datetime import date


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
    ano = int(input('digite o ano de interesse (0 para ano atual): '))
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('{}O ano {} é Bissexto{}'.format(form['azulbold'], ano, form['limpa']))
    else:
        print('{}O ano {} não é Bissexto{}'.format(form['vermbold'], ano, form['limpa']))
    # errado - faltam mais testes para ver se é bissexto!
    # bissexto = ano % 4
    # print('O ano {} é bissexto'.format(ano) if bissexto == 0 else 'O ano {} não é bisexto'.format(ano))


main()
