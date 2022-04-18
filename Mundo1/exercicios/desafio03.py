##########################################################
# Desafio 3 - funcao para receber dois numeros e soma-los
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
            'azul': '\033[34m',
            'azulbold': '\033[1;34m'}
    num1 = input('Digite um numero: ')
    # uma forma mais pratica de conversao de string para inteiro:
    # num1 = int(input('Digite um numero: '))
    num2 = input('Digite outro número: ')
    # input - funcao que le o teclado
    # converte string em inteiro para somar, senao ele concatena as duas strings
    n1_int = int(num1)
    n2_int = int(num2)
    soma = n1_int + n2_int
    print(form['bold'], soma, form['limpa'])
    print(form['azulbold'], n1_int + n2_int, form['limpa'])
    # print - funcao que joga para tela uma string ou variavel


main()
