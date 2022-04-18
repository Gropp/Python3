##########################################################
# AULA 10 - condicoes
##########################################################
def main():
    tempo = int(input('Quantos anos tem seu carro: '))
    # if composto
    if tempo <= 3:
        print('carro novo')
    else:
        print('carro velho')
    # if simplificado
    print('carro novo' if tempo <= 3 else 'carro velho')
    print('FIM')

    nome = str(input('Digite seu nome: ')).strip().capitalize()
    if nome == 'Fernando':
        print('Lindo nome!')
    else:
        print('Que nome bosta!')
    print('Bye')


main()
