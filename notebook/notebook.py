from typing import List, Optional

from .note import NoteCreate, NoteUpdate, Note
from .storage import Storage


class Notebook:
    def __init__(self, storage: Storage, notes: Optional[List[Note]] = None):
        pass

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
