from gtts import gTTS
import os


class VoiceFileController():
    """class with the methods to generate and work with the voice files."""
    
    def generate_and_save(text, language='pt', file_name='voicefile.mp3'):
        print('Gerando arquivo de voz...')
        try:
            voice_file = gTTS(text, lang=language)
            voice_file.save(f'./assets/audios/{file_name}')
        except Exception as e:
            print('Erro ao gerar o arquivo de voz...')
            return e
        
        print('Arquivo de voz gerado e salvo em: '+ os.getcwd() + '/assets/audios')
        
        return file_name