from typing import List

from .note import NoteCreate, NoteUpdate, Note
from .storage import Storage


class Notebook:
    def __init__(self, storage: Storage):
        self.__storage = storage
        self.__notes = self.__storage.load()

    @property
    def file_path(self):
        return self.__storage.location

    @property
    def notes(self):
        return self.__notes

    def add_note(self, note: NoteCreate) -> None:
        pass

    def update_note(self, note: NoteUpdate) -> None:
        pass

    def delete_note(self, note_id: int) -> None:
        pass

    def get_notes(self) -> List[Note]:
        pass

    def get_note(self, note_id: int) -> Note:
        pass

    def __iter__(self):
        pass

    # def __str__(self):
    #     pass
