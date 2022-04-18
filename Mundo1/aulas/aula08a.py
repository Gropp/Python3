######################################################################
# AULA 08A - importar bibliotecas
# importacao de uma biblioteca de funcoes matematicas
# import math - importa tudo
# from math import sqrt - importa somente o metodo desejado, nao sendo
# necessario referenciar o objeto ao usar o metodo
######################################################################
from math import sqrt, ceil, floor  # traz as funcoes para o codigo


num = int(input('Digite um numero: '))  # raiz = math.sqrt(num)
raiz = sqrt(num)  # como eu importei somente a funcao nao preciso referenciar o objeto math
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))  # forma padrao
# print('A raiz quadrada de {} é {:.2f}'.format(num, math.ceil(raiz)))  # funcao arredonda para cima
print('A raiz quadrada de {} é {:.2f}'.format(num, ceil(raiz)))  # sem chamar o objeto - funcao arredonda para cima
# print('A raiz quadrada de {} é {:.2f}'.format(num, math.floor(raiz)))  # funcao arredonda para baixo
print('A raiz quadrada de {} é {:.2f}'.format(num, floor(raiz)))  # sem chamar o objeto - funcao
# arredonda para baixo
