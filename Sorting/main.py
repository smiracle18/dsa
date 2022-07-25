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
    



class BubbleSort(Strategy):
    """
    This implements bubble sort.
    """
    def sort(self, array: List) -> List:
        """
        Sort the array.
        """
        for i in range(len(array)):
            for j in range(len(array)-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        print("Kudos, Based on your command we used Bubble Sort.")
        return array

class InsertionSort(Strategy):
    """
    This implements insertion sort.
    """
    def sort(self, array: List) -> List:
        """
        Sort the array.
        """
        for i in range(len(array)):
            j = i
            while j > 0 and array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1
        print("Kudos, Based on your command we used Insertion Sort.")
        return array

if __name__ == "__main__":

    # Create an array of integers.
    arr = [1, 9, 13, 4, 5, 6, 3, 7, 8, 2, 9, 10]

    sorting = Sorting(BubbleSort())
    print(sorting.sort(arr))
    print(arr)
    sorting = Sorting(InsertionSort())
    print(sorting.sort(arr))

    sorting.set_strategy = BubbleSort()
    print(sorting.sort(arr))

