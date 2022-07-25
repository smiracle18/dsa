from typing import List
from Strategies.strategy import Strategy

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