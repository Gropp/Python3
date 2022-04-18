##################################################################
# Desafio 27 - mostra o primeiro e o ultimo nome digitado
##################################################################
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
    nome = str(input('Digite seu nome completo: ')).strip()
    separa = nome.split()
    print('{}Primeiro nome: {}{}'.format(form['azul'], separa[0], form['limpa']))
    print('{}ultimo nome: {}{}'.format(form['ciano'], separa[len(separa)-1], form['limpa']))


main()
