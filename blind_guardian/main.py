"""Main file of the project, call the other classes here."""
from controllers.text_file_controller import TextFileController
from controllers.voice_file_controller import VoiceFileController
from controllers.player_controller import PlayerController


#Gets the content of the text file
data_to_read = TextFileController.load_file()

#uses the text file to generate the voice file
voice_file = VoiceFileController.generate_and_save(data_to_read)

#play the voice file
if input('Deseja tocar o arquivo de voz gerado?\n'+'S/N\n').upper() == 'S':
    PlayerController.play(voice_file)


