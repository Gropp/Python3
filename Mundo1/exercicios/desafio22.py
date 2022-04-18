##################################################################
# Desafio 22 - crie um programa que peça o nome completo da pessoa
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
    nome = str(input('Digite seu nome completo: ')).strip()  # tira os espacos inuteis digitados pelo usuario
    print('Seu nome todo em maiusculas:', nome.upper())
    print('Seu nome todo em minusculas:', nome.lower())
    print('Numero de caracters com espacos do seu nome: {}{}{}'.format(form['amarelo'], len(nome), form['limpa']))
    print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))  # desconta os espacos
    separa = nome.split()
    junto = ''.join(separa)
    print('Numero de caracteres sem espacos do seu nome: ', len(junto))
    print('Numero de caracteres do seu primeiro nome: ', len(separa[0]))
    # outra forma de contar os caracteres do primeiro nome é achando a posicao do primeiro espaco
    print('numero de caracteres do primeiro nome: {}'.format(nome.find(' ')))


main()
