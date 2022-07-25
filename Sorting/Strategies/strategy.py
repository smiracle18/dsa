from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    '''
    This defines interface for different sorting mechanisms.
    '''
    @abstractmethod
    def sort(self, array: List) -> List:
        """
        Sort the array.
        """
        pass