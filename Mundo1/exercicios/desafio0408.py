##########################################################
# Desafios 4 a 8 - OPERADORES
##########################################################
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

    num = int(input('Digite um número: '))
    # desafio 5
    print('{}O antecessor do numero é: {} e o sucessor: {}{}'.format(form['roxobold'], num - 1, num + 1, form['limpa']))
    # desafio 6
    print('{}O dobro: {}, o triplo: {} e a raiz quadrada: {:.2f}{}'.format(form['vermbold'], num * 2, num * 3,
                                                                           num ** (1 / 2), form['limpa']))
    # desafio 7
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    print('{}A média entre {} e {} é: {:.2f}{}'.format(form['amabold'], nota1, nota2, media, form['limpa']))
    # desafio 8
    # pondo com no input
    distancia = int(input('\033[1;36m Digite a distancia em metros: \033[m'))
    # km hm dam m dm cm mm
    print(
        '{}São: \n {} quilometros \n {} hectometros \n {} decametros \n {} metros  \n {} decimetros \n'
        ' {} centimetros \n {} milimetros{}'.format(
            form['cibold'], distancia / 1000, distancia / 100, distancia / 10, distancia, distancia * 10,
            distancia * 100, distancia * 1000, form['limpa']))


main()
