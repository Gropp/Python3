########################################################################
# Desafio 33 - identificar entre tres numeros qual o maior e qual o menor
########################################################################
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
    n1 = int(input('\033[44m Digite o primeiro numero: \033[m '))
    n2 = int(input('\033[45m Digite o segundo numero: \033[m '))
    n3 = int(input('\033[46m Digite o terceiro numero: \033[m '))
    # testando o menor
    # elege um valor como menor
    menor = n1
    if n2 < n1 and n2 < n3:
        menor = n2
    if n3 < n1 and n3 < n2:
        menor = n3
    # testando o maior
    # elege um valor como maior
    maior = n1
    if n2 > n1 and n2 > n3:
        maior = n2
    if n3 > n1 and n3 > n2:
        maior = n3
    print('{}O maior valor é {} e o menor valor é {}{}'.format(form['cibold'], maior, menor, form['limpa']))


main()
