from notebook import Notebook
from notebook import JsonFile


class App:
    def __init__(self):
        storage = JsonFile(file_path='notes.json')
        self.__notebook = Notebook(storage=storage)
        

    def run(self):
        pass

