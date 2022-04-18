#######################################
# Desafio 29 - radar eletronico
#######################################
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
    vel = float(input('Qual a sua velcidade atual? km/h '))
    if vel <= 80:
        print('Tenha um bom dia!')
    else:
        multa = (vel - 80) * 7.00
        print('{}MULTADO!{}'.format(form['vermbold'], form['limpa']))
        print('{}Voce excedeu a velocidade máxima de 80km/h{}'.format(form['vermelho'], form['limpa']))
        print('o valor da multa a ser paga é de: R$ {:.2f}'.format(multa))
    print('{}Dirija com SEGURANÇA!{}'.format(form['verdebold'], form['limpa']))


main()
