#######################################
# Desafio 31 - preco da passagem
#######################################
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
    dist = float(input('Qual é a distancia a ser percorrida? Km/h '))
    # preco = dist * 0.50 if dist <=200 else dist * 0.45
    if dist <= 200:
        print('{}O valor da sua passagem é de R${:.2f}{}'.format(form['vermunder'], dist*0.50, form['limpa']))
    else:
        print('{}O valor da sua passagem é de R${:.2f}{}'.format(form['vermunder'], dist*0.45, form['limpa']))
    print('TENHA UMA BOA VIAGEM!')


main()
