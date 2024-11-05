import os
import json

from abc import ABC, abstractmethod
from typing import List

from .note import Note


class Storage(ABC):
    @abstractmethod
    def save(self, notes: List[Note]) -> None:
        pass

    @abstractmethod
    def load(self) -> List[Note]:
        pass

    @property
    @abstractmethod
    def location(self) -> str:
        pass


class JsonFile(Storage):
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def save(self, notes: List[Note]) -> None:
        notes = [note.as_dict() for note in notes]
        with open(self.file_path, "wt") as f:
            json.dump(notes, f)

    def load(self) -> List[Note]:
        with open(self.file_path, "rt") as f:
            raw_notes = json.load(f)
        return [Note(**note) for note in raw_notes]

    @property
    def location(self):
        return self.file_path


class CsvFile(Storage):
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                pass

    def save(self, notes: List[Note]) -> None:
        notes = [note.as_dict() for note in notes]
        pass

    def load(self) -> List[Note]:
        pass

    @property
    def location(self):
        return self.file_path
