"""
Binary Search Module
"""
from multiprocessing.dummy import Array


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

