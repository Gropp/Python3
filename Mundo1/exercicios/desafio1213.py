##########################################################
# Desafios 12/13 - percentual
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
    preco = float(input('Digite o valor do produto: R$ '))
    desc = float(input('Digite o % desconto: '))
    juros = float(input('Digite o % juros: '))
    comdes = preco - (preco * (desc / 100))
    comjur = preco + (preco * (juros / 100))
    print('{}O valor com desconto será: {:.2f}{}'.format(form['amabold'], comdes, form['limpa']))
    print('{}O valor com juros será: {:.2f}{}'.format(form['vermbold'], comjur, form['limpa']))


main()
