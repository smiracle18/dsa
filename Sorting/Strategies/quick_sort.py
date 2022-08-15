
from typing import List
from Strategies.strategy import Strategy


class Quicksort(Strategy):
    """
    Quick sort implementation. O(n2)
    """
    def sort(self, arr: List) -> List:
        def partition(l, r):
            m = l - 1
            pivot = arr[r]
            for i in range(l, r):
                if arr[i] < pivot:
                    m += 1
                    arr[i], arr[m] = arr[m], arr[i]
            m += 1
            arr[m], arr[r] = arr[r], arr[m]
            return m

        def quickSort(l, r):
            if l < r:
                p = partition(l, r)
                # print(arr, arr[p], p, arr[:p], arr[p + 1:])
                quickSort(l, p - 1)
                quickSort(p + 1, r)
        
        quickSort(0, len(arr) - 1)

        print("Kudos, Based on your command we used Quick Sort.")
        return arr
        
