#######################################################
# Desafio 35 - segmentos para formar um triangulo
#######################################################
def main():
    l1 = float(input('Primeiro Segmento: '))
    l2 = float(input('Segundo Segmento: '))
    l3 = float(input('Terceiro Segmento: '))
    # teste para ver se os segmentos formam um triangulo
    if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
        resp = 'NAO PODEM'
        print('\033[1;7m Os segmentos passados {} formar um triangulo \033[m '.format(resp))
    else:
        # caso formem um triangulo, qual tipo de triangulo é formado
        resp = 'PODEM'
        if l1 == l2 and l2 == l3:
            tipo = "TRIANGULO EQUILATERO"
        else:
            if l1 != l2 and l2 != l3:
                tipo = "TRIANGULO ESCALENO"
            else:
                tipo = "TRIANGULO ISOCELES"

        print('\033[1;7m Os segmentos passados {} formar um triangulo \033[m '.format(resp))
        print('\033[1;7m Os segmentos passados formam um {} \033[m '.format(tipo))

    """
    #solucao mais complicada
    ma = (l2 - l3) #reta1
    mb = (l1 - l3) #reta2
    mc = (l1 - l2) #reta3
    #garante que ninguem é negativo
    if ma < 0:
        ma = ma * (-1)
    if mb < 0:
        mb = mb * (-1)
    if mc < 0:
        mc = mc * (-1)
    sa = l2 + l3
    sb = l1 + l3
    sc = l1 + l2
    if (ma < l1 < sa) and (mb < l2 < sb) and (mc < l3 < sc):
        resp = 'PODEM'
    else:
        resp = 'NAO PODEM'
    """


main()
