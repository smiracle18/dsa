from typing import List
from Strategies.strategy import Strategy


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