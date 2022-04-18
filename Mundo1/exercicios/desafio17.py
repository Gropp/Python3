####################################################################
# Desafios 17 - cálculo da hipotenusa, dados os catetos a² = b² + c²
####################################################################
import math


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
    catetob = float(input('\033[44m Digite o valor do cateto oposto:\033[m '))
    catetoc = float(input('\033[44m Digite o valor do cateto adjacente:\033[m '))
    # hipotenusa = ((catetob**2 + catetoc**2)**(1/2))
    # print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))
    # usando a biblioteca math para fazer o mesmo calculo acima
    hi = math.hypot(catetob, catetoc)
    print('O valor da hipotenusa é: {}{:.2f}{}'.format(form['azulbold'], hi, form['limpa']))


main()
