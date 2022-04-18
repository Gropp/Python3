#############################################################
# Desafio 30 - par ou impar
#############################################################
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
    n = int(input('{}Digite um numero inteiro qualquer: {}'.format(form['roxo'], form['limpa'])))
    pi = n % 2
    print('\033[1;4;7m Numero PAR! \033[m ' if pi == 0 else '\033[1;4;7m Numero Impar! \033[m ')


main()
