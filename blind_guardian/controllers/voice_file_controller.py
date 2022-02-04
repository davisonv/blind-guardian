from gtts import gTTS
import os


class VoiceFileController():
    """class with the methods to generate and work with the voice files."""
    
    def generate_and_save(text, language='pt', file_name='voice_file.mp3'):
        print('Gerando arquivo de voz...')
        try:
            voice_file = gTTS(text, lang=language)
            voice_file.save(file_name)
        except:
            print('Erro ao gerar o arquivo de voz...')
            return
        
        print('Arquivo de voz gerado e salvo em: '+ os.getcwd())
        
        return file_name