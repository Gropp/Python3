####################################################################
# Desafios 18 - cálculo do sen/cos/tan dado angulo
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
    ang = float(input('digite o angulo a ser calculado: '))
    # as funcoes trigonometricas calcula em  radianos, nao em graus!!!
    radianos = 2 * 3.141519 * (ang / 360)
    sen = math.sin(math.radians(ang))
    senr = math.sin(radianos)
    cos = math.cos(math.radians(ang))
    cosr = math.cos(radianos)
    tan = math.tan(math.radians(ang))
    tanr = math.tan(radianos)
    print(
        '{} Para o angulo {:.0f}° \n radiandos = {:.2f} \n sen = {:.2f} - senr = {:.2f} \n cos = {:.2f} - cosr = {:.2f}'
        ' \n tan = {:.2f} - tanr = {:.2f}{}'.format(
                                                    form['azulbold'], ang, radianos, sen, senr, cos, cosr, tan, tanr,
                                                    form['limpa']))


main()
