
from typing import List
from Strategies.strategy import Strategy


class MergeSort(Strategy):
    """
    Merge sort implementation. O(nlog(n))
    """

    
    def sort(self, arr: List) -> List:
        n = len(arr)

        def merge(L, R):
            i, j = 0, 0
            out = []
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    out.append(L[i])
                    i += 1
                else:
                    out.append(R[j])
                    j += 1
            out += R[j:]
            out += L[i:]
            return out

        def mergeSort(l, r):

            if l > r: return []
            if l == r: return [arr[l]]

            m = (l + r) // 2
            Left = mergeSort(l, m)
            Right = mergeSort(m + 1, r)

            return merge(Left, Right)

        print("Kudos, Based on your command we used Merge Sort.")
        return mergeSort(0, n - 1)
