##########################################################
# AULA 09 - manipulando strings no Python com a funcao print
##########################################################
def main():
    frase = 'Curso em video Python'  # o python salva as strings como arrays inicia do ZERO
    print(len(frase))  # mostra o tamanho da string conta espacos
    print(frase.count('o'))  # mostra a contagem de quantos 'o's existem na frase
    print(frase.count('o', 0, 13))  # mostra quantos 'o's existem no intervalo ZERO a 12
    print(frase.upper().count('O'))  # mostra quantos 'O's maiusculos tem na frase apos o upper
    print(frase.find('deo'))  # mostra o resultado da busca onde comeca essa sequencia se achada
    # senao retorna -1
    print('curso' in frase)  # boolean - existe 'curso' no texto frase?
    print('Curso' in frase)  # diferencia maiusculas de minusculas!
    print(frase.lower().find('video'))  # garante que a busca ira comparar minuscula com minuscula
    print(frase)  # imprime toda a string
    print(frase.replace('Python', 'Android'))  # troca uma palavra pela outra - nao altera a variavel
    print(frase.upper())  # imprime tudo em maiusculo
    print(frase.lower())  # imprime tudo em minusculo
    print(frase.capitalize())  # somente o primeiro caractere em maiusculo
    print(frase.title())  # todos as palavras antes do espaco fica maiusculo
    print(frase.strip())  # remove todos os espaços INUTEIS DA STRING
    print(frase.rstrip())  # remove somente espacos a direita
    print(frase.lstrip())  # remove somente espacos a esquerda
    print(frase.split())  # divide onde tiver espacos - cria uma lista de strings
    separa = frase.split()  # variavel com a lista separada da string original
    print(separa)  # imprime a lista separa
    print(separa[0])  # imprime o item ZERO da lista separa
    print(separa[2][2])  # imprime somente o item dois da string na posicao 2 da lista separa
    junta = '-'.join(separa)  # uni uma lista de strings separando eles com '-', poderia ser espaco
    print(junta)
    print(frase[2])  # imprime a string na posicao 2 [0,1,2]
    print(frase[16])  # imprime a string na posicao 16 [0,1,2,3,...,15,16]
    print(frase[9:14])  # imprime a string no intervalo 9 - 13 (sempre um a menos na ultima posicao)
    print(frase[9:21:2])  # imprime o intervalo pulando de dois em dois
    print(frase[::2])  # imprime tudo pulando de dois em dois
    print(frase[:5])  # imprime da posicao ZERO ao 4
    print(frase[15:])  # imprime da posicao 15 ATE O FINAL DA STRING
    print(frase[4::3])  # imprime da posicao 4 ATE O FINAL DA STRING PULANDO DE 3 EM 3
    # imprimindo textos LONGOS - usa-se tres aspas duplas!
    print("""Esse módulo define um tipo de objeto que pode representar
    compactamente um vetor de valores básicos: caracteres, inteiros,
    números de ponto flutuante. Vetores são tipos de sequência e funcionam
    bem parecidamente com listas, porém o tipo dos objetos armazenados é
    restringido. O tipo é especificado na criação do objeto usando um código
    de tipo, que é um único caractere. São definidos os seguintes códigos de tipo:""")


main()
