##################################################################
# Desafio 24 - diz se a cidade digitada comeca com a palavra santo
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
    cidade = str(input('Digite o nome da cidade onde vc mora: ')).strip()
    separa = cidade.split()
    bol = separa[0].lower() in 'santo'
    # bol = 'santo' in separa[0].lower()
    if bol:
        print('{}A sua cidade começa com Santo!{}'.format(form['verdebold'], form['limpa']))
    else:
        print('{}A sua cidade nao começa com a palavra Santo!{}'.format(form['vermbold'], form['limpa']))


main()
