from __future__ import annotations

from typing import List
from Strategies.strategy import Strategy

class Sorting():
    """
    This defines interface for differnt sorting mechanisms.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Initialize the sorting strategy.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Return the sorting strategy.
        """
        return self._strategy
    
    @strategy.setter
    def set_strategy(self, strategy: Strategy) -> None:
        """
        Set the sorting strategy.
        """
        self._strategy = strategy
    
    def sort(self, array: List) -> List:
        """
        Sort the array.
        """
        return self._strategy.sort(array[:])