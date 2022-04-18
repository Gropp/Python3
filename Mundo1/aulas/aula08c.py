###################################################################################################
# AULA 08C - IMPORTANDO BIBLIOTECAS EXTERNAS
# IMPORTACAO DE BIBLIOTECAS PARA USO NO PYTHON
# PARA USAR BIBLIOTECAS NOVAS, VOCE COLOCA NO COMANDO DE IMPORT, AO APARECER A LAMPADA VERMELHA
# VOCE ESCOLHE A OPÇAO DE IMPORTAR A BIBLIOTE - ASSIM A IDE RESOLVE O PROBLEMA
###################################################################################################
import emoji


def main():
    # usando a bibliote de emojis
    print(emoji.emojize('Olá, Mundo :sunglasses:', use_aliases=True))
    print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))


main()
