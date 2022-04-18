####################################################################
# AULA 06 - Utilizando variaveis primitivas e usando mascaras dentro do print
####################################################################
def main():
    n1 = input('Digite um numero: ')
    print(n1)
    print('O valor digitado foi', n1)
    # funcao type() mostra o tipo da variavel
    print(type(n1))
    # convertendo a variavel n1 em um numero inteiro para poder somar
    n1_int = int(n1)
    n2 = int(input('Digite outro numero: '))
    print(n2)
    print('O valor digitado foi {}!'.format(n2))
    print(type(n2))
    soma = n1_int + n2
    subt = n1_int - n2
    mult = n1_int * n2
    divs = n1_int / n2
    pote = n1_int ** n2
    divint = n1_int // n2
    modulo = n1_int % n2
    prec1 = n1_int + n1_int * n2
    prec2 = n1_int * n2 + n2 ** n1_int
    # usando as mascaras na funcao print({}) e chamando o metodo format() passando as variaveis
    print('O valor da soma entre {} e {}, é: {}.'.format(n1_int, n2, soma))
    print('O valor da subtração entre {} e {}, é: {}.'.format(n1_int, n2, subt))
    print('O valor da multiplicação entre {} e {}, é: {}.'.format(n1_int, n2, mult))
    print('O valor da divisão entre {} e {}, é: {}.'.format(n1_int, n2, divs))
    print('O valor da potencia entre {} e {}, é: {}.'.format(n1_int, n2, pote))
    print('O valor da divisao inteira  entre {} e {}, é: {}.'.format(n1_int, n2, divint))
    print('O valor do módulo entre {} e {}, é: {}.'.format(n1_int, n2, modulo))
    print('O valor do precedente entre {} e {} + e x, é: {}.'.format(n1_int, n2, prec1))
    # é possivel ordenar a ordem das variaveis dentro das chaves:
    print('O valor do precedente entre {0} e {1}, * + **, é: {2}.'.format(n1_int, n2, prec2))


main()
