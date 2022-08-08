
from typing import List
from Strategies.strategy import Strategy


class SelectionSort(Strategy):
    """
    Selection sort implementation. O(n2)
    """

    
    def sort(self, arr: List) -> List:
        n = len(arr)
        def find_min_ix(l):
            min_ix = l
            for i in range(l, n):
                if arr[i] < arr[min_ix]:
                    min_ix = i
            return min_ix
        
        l = len(arr)
        for i in range(l):
            mix = find_min_ix(i)
            arr[i], arr[mix] = arr[mix], arr[i]
        print("Kudos, Based on your command we used Selection Sort.")
        return arr
