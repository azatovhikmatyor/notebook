import sys

from core import Notebook, JsonFile, Note

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    tabulate = None


class App:
    def __init__(self):
        storage = JsonFile(file_path="notes.json")
        self.__notebook = Notebook(storage=storage)

    def run(self):
        options = {
            "1": self.__show_notes,
            "2": self.__show_note,
            "3": self.__add_note,
            "4": self.__update_note,
            "5": self.__delete_note,
            "m": self.__show_menu,
            "q": sys.exit,
        }

        self.__show_menu()
        while True:
            option = input("Choose option: ").lower()
            cmd = options.get(option)
            if cmd:
                cmd()
            else:
                print('Invalid option')

    def __show_notes(self):
        if tabulate:
            print(
                tabulate(
                    [note.as_dict(shorten=True) for note in self.__notebook],
                    tablefmt="rounded_grid",
                    headers="keys",
                )
            )
        else:
            for note in self.__notebook:
                note.display()

    def __show_note(self):
        id = int(input('Enter note id: ')) # TODO: Implement input validation
        note = self.__notebook[id]
        if tabulate:
            print(tabulate([note.as_dict()], tablefmt='rounded_grid', headers='keys'))
        else:
            note.display()

    def __add_note(self):
        text = input('Note text: ')
        id = self.__notebook.last_note_id + 1
        new_note = Note(id=id, text=text)
        self.__notebook.add_note(new_note)
        # TODO: print some message

    def __update_note(self):
        id = int(input('Enter note id: ')) # TODO: Implement input validation
        text = input('Note text: ')
        note = Note(id=id, text=text)
        self.__notebook.update_note(note)
        # TODO: print some message

    def __delete_note(self):
        id = int(input('Enter note id: ')) # TODO: Implement input validation
        self.__notebook.delete_note(note_id=id)
        # TODO: print some message

    def __show_menu(self):
        menu = """CHOOSE OPTION
    1: SHOW ALL NOTES
    2: SHOW NOTE DETAILS
    3: CREATE NOTE
    4: UPDATE NOTE
    5: DELETE NOTE
    M: SHOW MENU AGAIN
    Q: QUIT THE APPLICATION
"""
        print(menu)



if __name__ == "__main__":
    app = App()
    app.run()
