#################################################################
# Desafio 23 - quebra um numero como string em digitos separados
# Soluçao matematica
#################################################################
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
    num = int(input('Informe um numero: '))
    print('Analisando o número {}{}{}'.format(form['vermbold'], num, form['limpa']))
    # divide o numero por 1 - 10 - 100 - 1000 e pega o modulo de 10 da divisao
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('{}'.format(form['invert']))
    print('unidade: {}'.format(u))
    print('dezena: {}'.format(d))
    print('centena: {}'.format(c))
    print('milhar: {}\n'.format(m))
    print('{}'.format(form['limpa']))


main()
