####################################################################
# Desafios 19 - escolha entre 4 nomes
####################################################################
from random import choice


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
    name1 = input('Digite o nome do aluno 1: ')
    name2 = input('Digite o nome do aluno 2: ')
    name3 = input('Digite o nome do aluno 3: ')
    name4 = input('Digite o nome do aluno 4: ')
    # listas ficam entre colchetes
    escolhido = choice([name1, name2, name3, name4])
    print('{}{}{}{}'.format(form['roxobold'], form['underline'], escolhido, form['limpa']))

    """ 
    escolhido = choices([1, 2, 3, 4])
    print(escolhido)
    if (escolhido == [1]):
        print(name1)
    if (escolhido == [2]):
        print(name2)
    if (escolhido == [3]):
        print(name3)
    if (escolhido == [4]):
        print(name4)
    """


main()
