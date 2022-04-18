############################################################
# AULA 08B - IMPORTACAO DE BIBLIOTECAS PARA USO NO PYTHON
############################################################
import random


def main():
    # digita import (crtl+espaco) - abre uma lista de bibliotecas
    num = random.random()  # nativamente traz um numero real entre 0 e 1
    num1 = random.randint(1, 10)  # gera um numero inteiro entre 1 e 10
    print('{:>.5f}\n{:<7}'.format(num, num1))  # formatado com casas decimais e alinhamento


main()
