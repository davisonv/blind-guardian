"""Main file of the project, call the other classes here."""
from controllers.file_controller import FileController

data_to_read = FileController.load_file()

print(data_to_read)