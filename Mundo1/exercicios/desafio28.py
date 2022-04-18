##################################################################
# Desafio 28 - joguinho de advinhacao
##################################################################
from random import randint
from time import sleep


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
    print('-=-' * 20)
    print('{}Vou pensar em um numero entre 0 e 5. Tente advinhar...{}'.format(form['azul'], form['limpa']))
    print('-=-' * 20)
    n = randint(0, 5)
    a = int(input('{}Digite o numero que vc acha que eu pensei: {}'.format(form['vermelho'], form['limpa'])))
    print('{}Processando...{}'.format(form['invert'], form['limpa']))
    sleep(3)  # funcao da biblioteca time - da uma pausa de 3 segundos
    print('Acertou!' if a == n else 'Vc perdeu!')
    print('Eu pensei no numero: {} e vc apostou no numero: {}'.format(n, a))


main()
