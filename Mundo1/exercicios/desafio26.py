##################################################################
# Desafio 26 - em busca da letra A
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
    frase = str(input('Digite uma frase qualquer: ')).upper().strip()
    print('Sua frase contêm', frase.count('A'), ' letras A')
    print('A primeira letra A esta na posicao: ', frase.find('A')+1)
    print('{}A ultima letra A esta na posicao: {}{}'.format(form['roxobold'], frase.rfind('A')+1, form['limpa']))


main()
