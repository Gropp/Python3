####################################################################
# Desafios 21 - TOCAR UM ARQUIVO MP3
####################################################################
# import pygame
# o modulo pygame tem varias bibliotecas para a criacao de jogos
# precisamos inicializar esse modulo para poder utiliza-lo
# from playsound import playsound
import os
from pydub import AudioSegment
from pydub.playback import play


def main():
    # pygame deu erro no audio
    """
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('crazy.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    """
    # playsound executou o audio
    # playsound('crazy.mp3')
    # mostra o diretorio atual do interpretador
    print('\033[7m', os.getcwd(), '\033[m')
    song = AudioSegment.from_mp3('crazy.mp3')
    play(song)


main()
