from typing import List
from Strategies.strategy import Strategy

import heapq
class HeapSort(Strategy):
    """
    Heap sort implementation. O(nlog(n))
    """
    def sort(self, arr: List) -> List:
        heapq.heapify(arr)
        out = []
        while arr:
            out.append(heapq.heappop(arr))
        print("Kudos, Based on your command we used Heap Sort.")
        return out
        
