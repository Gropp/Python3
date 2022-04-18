####################################################
# AULA 11 - EXTRA - CORES NO TERMINAL
####################################################
# \033[estilo;cortexto(30-37);corback(40-47)m
# \033[m -> padrao do terminal
# \033[7;30m -> inverte o padrao letra preta e fundo branco
def main():
    print('\033[31mTESTE')  # sem padrao, sem fundo
    print('\033[31;40mTESTE1')  # sem estilo
    print('\033[1;31;43mTESTE1\033[m')  # negrito com final de formatacao
    print('\033[4;30;45mTESTE1\033[m')  # sublinhado
    print('\033[7;37;40mTESTE1\033[m')  # inverte
    a = 5
    b = 6
    print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))
    print('Os valores são \033[32;41m{}\033[m e \033[31;46m{}\033[m!'.format(a, b))
    nome = 'FERNANDO'
    # formata no format da funcao print
    print('Oi, bem vindo, {}{}{}, volte sempre'.format('\033[1m', nome, '\033[m'))
    # variaveis - lista - array - dicionario
    texto = 'CORES NO PYTHON'
    cores = {'limpa': '\033[m',
             'azul': '\033[34m',
             'amarelo': '\033[33m',
             'pretoebranco': '\033[7;40m',
             'negrita': '\033[1m'}
    print('{}{}{}'.format(cores['azul'], texto, cores['limpa']))
    print('{}{}{}'.format(cores['amarelo'], texto, cores['limpa']))
    print('{}{}{}'.format(cores['negrita'], texto, cores['limpa']))
    print('{}{}{}'.format(cores['pretoebranco'], texto, cores['limpa']))


main()
