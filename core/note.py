from __future__ import annotations

from typing import Dict
from reprlib import repr



class NoteUpdate:
    pass


class Note:
    def __init__(self, id: int, text: str, created_date = None):
        self.__id = id
        self.text = text
        self.__created_date = created_date or '2020-12-12'  # TODO: created_date must be datetime.datetime, NOT str

    @property
    def id(self):
        return self.__id

    @property
    def created_date(self):
        return self.__created_date

    def as_dict(self, shorten: bool = False) -> Dict:
        return {
            'id': self.id,
            'text': repr(self.text) if shorten else self.text,
            'created_date': self.created_date
        }
    
    def update(self, note: Note):
        if self.id != note.id:
            raise ValueError('Can not update') # TODO: write better message
        self.text = note.text

    def __str__(self):
        return f"Note(id={self.id}, text={repr(self.text)}, created_date={self.created_date!r})"

    def display(self, shorten: bool = False):
        text = repr(self.text) if shorten else self.text
        print(
            f"| ID: {self.id:<4} | Text: {text:<30} | Datetime: {self.created_date} |"
        )
