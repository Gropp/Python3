##########################################################
# Desafios 15 - Aluguel de carros
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
    print('Bem vindo a locadora Seucarro.com.')
    print('Vamos fazer o fechamento do contrato!')
    diarias = float(input('Por favor informe a quantidade de dias que voce usou o veículo - Dias: '))
    km = float(input('Por favor informe a kilometragem rodada - KM: '))
    vlrd = diarias * 60.00
    vlrkm = km * 0.15
    vlrtot = vlrd + vlrkm
    print('{} Obrigado por utilizar nossos serviços {}'.format('\033[7;32;40m', '\033[m'))
    print('{}O valor das diarias é R${:.2f}, o valor do KM rodado é R${:.2f}{}'.format(form['ciano'], vlrd, vlrkm,
                                                                                       form['limpa']))
    print('O valor total devido é de {}R${:.2f}{}'.format(form['vermbold'], vlrtot, form['limpa']))


main()
