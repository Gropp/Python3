######################################
# exercicio 04 - tipos de variaveis
######################################
def main():
    a = input('Digite algo: ')
    print('Tipo da variavel', type(a))
    print('É um numero? ', a.isnumeric())
    # retorna True se for um caracter numerico
    print('É um decimal? ', a.isdecimal())
    # retorna True se for um caracter decimal
    print('É um digito? ', a.isdigit())
    # retorna True se for um caracter digito (inclui decimais)
    print('É um alfanumerico? ', a.isalnum())
    # retorna True se for um caracter alfanumerico
    print('É um alfabeto? ', a.isalpha())
    # retorna True se for um caracter alfabeto
    print('É maiusculo? ', a.isupper())
    # retorna True se for um caracter MAIUSCULO
    print('É minusculo? ', a.islower())
    # retorna True se for um caracter minusculo
    print('É um Titulo? ', a.istitle())
    # retorna True se for um caracter Titulado/Capitalizada
    print('É um espaço? {}'.format(a.isspace()))
    # retorna True se for um caracter espaço
    print('É printavel? {}'.format(a.isprintable()))
    # retorna True se for um caracter printavel (nao de controle p.ex /n)
    print('É um identificador? {}'.format(a.isidentifier()))
    # retorna True se for um caracter se for um identificador valido (nao sendo palavras reservadas
    # p.ex def)


main()
