####################################################################
# Desafios 20 - embaralhar a ordem de nomes
####################################################################
from random import shuffle


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
    n1 = str(input('digite o primeiro nome: '))
    n2 = str(input('digite o segundo nome: '))
    n3 = str(input('digite o terceiro nome: '))
    n4 = str(input('digite o quarto nome: '))
    # crio um array com as variaveis
    lista = [n1, n2, n3, n4]
    # a funcao shuffle embaralha o array ja existente
    shuffle(lista)
    print('{}{}{}'.format(form['amabold'], lista, form['limpa']))


main()
