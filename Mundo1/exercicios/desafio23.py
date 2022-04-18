#################################################################
# Desafio 23 - quebra um numero como string em digitos separados
# Soluçao string
#################################################################
def main():
    num = str(input('digite um numero entre 1 e 9999: ')).strip()  # tirar os espacos
    if len(num) > 4:
        print('Digite no maximo 4 digitos')
        exit()
    if len(num) == 4:
        print('unidades: ' + num[3])
        print('dezenas: ' + num[2])
        print('centenas: ' + num[1])
        print('milhares: ' + num[0])
    elif len(num) == 3:
        print('unidades: ' + num[2])
        print('dezenas: ' + num[1])
        print('centenas: ' + num[0])
    elif len(num) == 2:
        print('unidades: ' + num[1])
        print('dezenas: ' + num[0])
    elif len(num) == 1:
        print('unidades: ' + num[0])
    elif len(num) == 0:
        print('Digite um numero!')


main()
