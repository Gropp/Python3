####################################################################
# AULA 06A - Tipos de variaveis
####################################################################
def main():
    n1 = input('Digite um numero: ')
    # n1 sempre sera string (str) neste formato
    print(n1)
    print(type(n1))
    # convertendo n1 para float
    n1_float = float(n1)
    print(n1_float)
    print(type(n1_float))
    # forcando a entrada ser um boolen (se teclar algo True, senao False)
    t1 = bool(input('Digite um numero: '))
    print(t1)
    t2 = input('Digite algo: ')
    # metodos de teste de tipos de strings (se converter o resultado pode mudar
    print(t2.isnumeric())  # testa se é numerico
    print(t2.isalpha())  # testa se é alfabetico
    print(t2.isalnum())  # testa se é alfanumerico
    print(t2.isupper())  # testa se é maiusculo
    
    
main()
