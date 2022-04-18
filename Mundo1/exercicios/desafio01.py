###########################################################
# Desafio 01 - funcao input e print
###########################################################
def main():
    form = {'limpa': '\033[m',
            'bold': '\033[1m',
            'underline': '\033[4m',
            'invert': '\033[7m',
            'vermelho': '\033[31m',
            'vermbold': '\033[1;31m',
            'vermunder': '\033[4;31m',
            'vermbco': '\033[31;30m'}

    name = input('Qual seu nome? ')
    print('Ola!', name, 'Prazer em conhece-lo')
    print('Ola! {}{}{}. Prazer em conhecê-lo'.format(form['bold'], name, form['limpa']))
    print('Ola! {}{}{}. Prazer em conhecê-lo'.format(form['underline'], name, form['limpa']))
    print('Ola! {}{}{}. Prazer em conhecê-lo'.format(form['invert'], name, form['limpa']))
    print('Ola! {}{}{}{}. Prazer em conhecê-lo'.format(form['invert'], form['bold'], name, form['limpa']))
    print('Ola! {}{}{}{}. Prazer em conhecê-lo'.format(form['vermbco'], form['bold'], name, form['limpa']))


main()
