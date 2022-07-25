"""
BinarySearch Module
"""
from multiprocessing.dummy import Array


class BinarySearch:
    
    def binary_search(arr: Array, target: int) -> int:
        ''' 
        input: sorted arr and returns the occurance of target in it.
        output: index of target in arr starting from 0.
        '''
        low, high = 0, len(arr) - 1
        while low <= high:       
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            
            if arr[mid] < target:
                low= mid + 1
            else:
                high = mid - 1
        return -1

    def binary_search_left(arr: Array, target: int) -> int:
        ''' 
        input: sorted arr and returns the first occurance of target in it.
        output: index of target in arr starting from 0.
        '''
        low, high = 0, len(arr) - 1
        found_at = -1
        while low <= high:       
            mid = (low + high) // 2
            if arr[mid] == target:
                found_at = mid
                high = mid - 1

            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return found_at
