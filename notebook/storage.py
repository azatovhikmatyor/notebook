from abc import ABC, abstractmethod
from typing import List

from .note import Note


class Storage(ABC):
    @abstractmethod
    def save(self, notes: List[Note]):
        pass


