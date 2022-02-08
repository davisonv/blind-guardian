from utils import bcolors
from playsound import playsound


class PlayerController():
    """class with the methods to play de voice file."""
    
    def play(file_name):
        try:
            playsound(f'./assets/audios/{file_name}')
        except Exception as e:
            print(bcolors.FAIL + 'Erro ao executar arquivo de voz...')
            print(e)