##########################################################
# Desafios 16 - Truncando um numero
##########################################################
"""
from random import uniform
from math import trunc
def main():
    num = uniform(1.0, 50.0)
    inteiro = trunc(num)
    print('O numero flutuante é {:.2f} e seu truncado é {}'.format(num, inteiro))


main()
"""


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
    # sem usar a funcao math
    num = float(input('Digite um valor flutuante: '))
    print('{} O valor digitado foi: {} e a sua porção inteira é: {} {}'.format(form['invert'], num, int(num),
                                                                               form['limpa']))


main()
