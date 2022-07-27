
from typing import List
from Strategies.strategy import Strategy


class SelectionSort(Strategy):
    """
    Selection sort implementation. O(n2)
    """
    def sort(self, arr: List) -> List:
        l = len(arr)
        for i in range(l):
            arr[i] = min(arr[i:])
        print("Kudos, Based on your command we used Selection Sort.")
        return arr
