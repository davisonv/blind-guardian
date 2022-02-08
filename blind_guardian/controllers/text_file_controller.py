import os

class TextFileController():
    """Class that has the methods to deal with the file that will be converted do voice."""
    
    DEFAULT_PATH = os.getcwd() + '/assets/manual.txt'
    
    PROVIDED_PATH = input('Digite o diretório do arquivo de texto a ser lido...\n')
    
    def load_file(path=PROVIDED_PATH, default_path=DEFAULT_PATH):
        
        print('O arquivo está sendo processado...')
        
        if os.path.isfile(path):
            file = open(path)
            file_data = file.read()
            return file_data
        else:
            file = open(default_path)
            file_data = file.read()
            return file_data