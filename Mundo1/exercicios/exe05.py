#####################################################
# exercicio 05 - Utilizando os formatadores do print
#####################################################
def main():
    n1 = int(input('um valor: '))
    n2 = int(input('outro valor: '))
    print('A soma vale {}'.format(n1+n2))
    s = n1 + n2
    m = n1 * n2
    d = n1 / n2
    di = n1 // n2
    e = n1 ** n2
    r2 = n1 ** (1/2)
    r3 = n2 ** (1/3)

    print('A soma é {}, \no produto é {} \ne a divisao é {:.3f} '. format(s, m, d), end='')
    # end - retira a quebra de linha
    # \n quebra linha
    print('Divisão Inteira {}, '
          '\npotencia {}, '
          '\nraiz quadrada {},'
          '\nraiz cubica {}'. format(di, e, r2, r3))

    nome = input('Digite o seu nome: ')
    print('prazer em te conhecer {:20}!'.format(nome))
    # reserva 20 caracteres
    print('prazer em te conhecer {:>20}!'.format(nome))
    # ajusta a direita
    print('prazer em te conhecer {:<20}!'.format(nome))
    # ajusta a esquerda
    print('prazer em te conhecer {:^20}!'.format(nome))
    # ajusta ao centro
    print('prazer em te conhecer {:-^20}!'.format(nome))
    # ajusta ao centro e completa com -


main()
