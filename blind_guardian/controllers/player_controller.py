from pygame import mixer
import os


class PlayerController():
    """class with the methods to play de voice file."""
    
    def play(file_name):
        try:
            mixer.init()
            mixer.music.load(os.getcwd() + '/' + file_name)
            mixer.music.play()
        except Exception as e:
            print('Erro ao executar arquivo de voz...')
            print(e)