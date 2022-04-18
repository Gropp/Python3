##########################################################
# Desafios 11 - calculo de area
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
    alt = float(input('\033[31m Digite a altura da parede: \033[m'))
    lar = float(input('\033[32m Digite a largura da parede: \033[m'))
    rend = float(input('\033[36m Digite o rendimento da tinta: \033[m'))
    area = alt * lar
    qtd = area / rend
    print(
        '{}A área a ser pintada é de {:.2f}, para isso serão necessarios {:.2f} litros{}'.format(form['amarelo'], area,
                                                                                                 qtd, form['limpa']))


main()
