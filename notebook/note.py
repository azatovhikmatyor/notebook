from typing import Dict

class NoteCreate:
    pass


class NoteUpdate:
    pass


class Note:
    def __init__(self, id: int, text: str, created_date: str):
        self.id = id
        self.text = text
        self.created_date = created_date

    def as_dict(self) -> Dict:
        pass
