###############################################
# AULA11 - Estruturas de Controle
###############################################
def main():
    nome = str(input('Qual o seu nome? '))
    if nome == 'Fernando':
        print('Que nome bonito!')
    elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('Seu nome é bem comum no Brasil')
    elif nome in 'Ana Cláudia Jéssica Juliana Olivia':
        print('Belo nome de menina voce tem!')
    else:
        print('Seu nome é bem normal.')
    print('Tenha um bom dia, {}'.format(nome))


main()
